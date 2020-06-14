#!/usr/bin/env python3
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
from werkzeug.utils import secure_filename

import socket
import json
import subprocess
import time
import logging
import yaml
import os
import logging

import libiec61850client


thread = None
tick = 0.001
focus = ''
hosts_info = {}
reset_log = False
async_mode = None

#webserver
app = Flask(__name__, template_folder='templates', static_folder='static')
socketio = SocketIO(app, async_mode=async_mode)

#logging handler, for sending logs to the client
class socketHandler(logging.StreamHandler):
  def __init__(self, socket):
    logging.StreamHandler.__init__(self)
    self.socket = socket

  def emit(self, record):
    msg = self.format(record)
    self.socket.emit('log_event', {'host':'localhost','data':msg,'clear':0})


#http calls
@app.route('/', methods = ['GET'])
def index():
  global reset_log
  reset_log = True
  return render_template('index.html', async_mode=socketio.async_mode)


# Socket events
@socketio.on('get_page_data', namespace='')
def get_page_data(data):
  emit('page_reload', {'data': ""})


@socketio.on('register_datapoint', namespace='')
def register_datapoint(data):
  global client
  logger.debug("register datapoint:" + str(data) )
  client.registerReadValue(str(data['id']))


@socketio.on('write_value', namespace='')
def write_value(data):
  global client
  logger.debug("write value:" + str(data['value']) + ", element:" + str(data['id']) )
  return client.registerWriteValue(str(data['id']),str(data['value']))

@socketio.on('write_position', namespace='')
def write_position(data):
  logger.debug("operate:" + str(data['id'])  )
  return client.operate(str(data['id']),str(data['value']))


#synchronous call
@socketio.on('read_value', namespace='')
def read_value(data):
  logger.debug("read value:" + str(data['id'])  )
  return client.ReadValue(data['id'])



  
@socketio.on('set_focus', namespace='')
def set_focus(data):
  global focus
  global hosts_info
  focus = data
  #print("focus:" + str(focus))
  if focus in hosts_info and 'data' in hosts_info[focus]:
    socketio.emit('info_event', hosts_info[focus]['data'] )
  else:
    socketio.emit('info_event', "" )
  emit('select_tab_event', {'host_name': focus})
  

@socketio.on('connect', namespace='')
def test_connect():
  global thread
  if thread is None:
    thread = socketio.start_background_task(target=worker)


@socketio.on('register_datapoint_finished', namespace='')
def register_datapoint_finished(data):
  #return #there is a bug here, so disable for now
  global client
  ieds = client.getRegisteredIEDs()
  for key in ieds:
    tupl = key.split(':')
    hostname = tupl[0]

    emit('log_event', {'host':key,'data':'[+] adding IED info','clear':1})

    port = None
    if len(tupl) > 1 and tupl[1] != "":
      port = int(tupl[1])
    model = client.getDatamodel(hostname=hostname, port=port)

    loaded_json = {}
    loaded_json['host'] = key
    loaded_json['data'] = model
    process_info_event(loaded_json)



#worker subroutines
def process_info_event(loaded_json): #add info to the ied datamodel tab
  global focus
  global hosts_info
  ihost = loaded_json['host']
  
  # store data
  if not ihost in hosts_info:
    hosts_info[ihost] = {}

  lastupdate =  time.time()
  loaded_json['last'] = lastupdate
  idata = printItems(loaded_json)

  hosts_info[ihost]['last'] = lastupdate
  hosts_info[ihost]['data'] = idata
  # send data also to webclient
  if ihost==focus:
    socketio.emit('info_event', idata)


def printItems(dictObjs):
  dictObj = dictObjs['data']
  el = 'Last update: '+str(time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime(dictObjs['last'])))+'<br><br>'
  el += '<table id="CurrentIEDModel" style="width:100%; border: 1px solid white; border-collapse: collapse;"><tr>'
  el += '<th>Reference</th><th>Value</th></tr>\n'

  def printrefs(model, ref="", depth=0):
    _ref = ""
    row = ""
    for element in model:
      if depth == 0:
        _ref = element
      elif depth == 1:
        _ref = ref + "/" + element
      elif depth > 1:
        _ref = ref + "." + element
        
      if 'value' in model[element] and 'FC' in model[element]:
        id = "iec61850://" + dictObjs['host'] + "/" + _ref
        row += ('<tr id="'+id+'"><td style="border: 1px solid white; border-collapse: collapse;">['+ model[element]['FC'] + '] ' + _ref + '</td><td style="border: 1px solid white; border-collapse: collapse;">'+ model[element]['value']+ '</td></tr>')
      else:
        row += printrefs(model[element],_ref, depth + 1)
    return row

  el += printrefs(dictObj)
  el += ('</table>\n')
  return el


#background thread
def worker():
  global focus
  global hosts_info
  global reset_log
  global client
  socketio.sleep(tick)

  sh = socketHandler(socketio)
  sh.setLevel(logging.DEBUG)
  fm = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
  sh.setFormatter(fm)
  logger.addHandler(sh)

  logger.info("worker treat started")

  while True:
    socketio.sleep(tick)
    #reset the client
    if reset_log == True:
      socketio.sleep(0.5)
      focus = ''
      reset_log = False
      socketio.sleep(0.5)

    socketio.sleep(1)
    client.poll()
    logger.info("values polled")

    # updating datamodel values
    ieds = client.getRegisteredIEDs()
    for key in ieds:
      tupl = key.split(':')
      hostname = tupl[0]

      #socketio.emit('log_event', {'host':key,'data':'[+] updating IED info','clear':0})

      port = None
      if len(tupl) > 1 and tupl[1] != "":
        port = int(tupl[1])
      model = client.getDatamodel(hostname=hostname, port=port)

      loaded_json = {}
      loaded_json['host'] = key
      loaded_json['data'] = model
      process_info_event(loaded_json)


# callback from libiec61850client
# called by client.poll
def readvaluecallback(key,data):
  logger.debug("callback: %s - %s" % (key,data))
  socketio.emit("svg_value_update_event",{ 'element' : key, 'data' : data })


if __name__ == '__main__':
  logger = logging.getLogger('webserver')
  logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    level=logging.INFO)
	# note the `logger` from above is now properly configured
  logger.debug("started")
  client = libiec61850client.iec61850client(readvaluecallback, logger)
  socketio.run(app)

"""

simulation... not sure.. special handling?

"""
