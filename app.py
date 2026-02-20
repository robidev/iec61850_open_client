#!/usr/bin/env -S python3 -u
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
from werkzeug.utils import secure_filename

import socket
import json
import subprocess
import time
import sys
import os
import logging

import libiec61850client
import libiec60870client
from urllib.parse import urlparse

import threading

thread = None
thread_lock = threading.Lock()

tick = 0.001
focus = ''
hosts_info = {}
reset_log = False
async_mode = None
local_svg = True
async_msg = []
async_rpt = {}

# Locks for thread safety
clients_lock = {}
async_lock = threading.Lock()
hosts_info_lock = threading.Lock()

#webserver
app = Flask(__name__, template_folder='templates', static_folder='static')
#socketio = SocketIO(app, async_mode=async_mode, logger=True, engineio_logger=True)
socketio = SocketIO(app, 
    async_mode="gevent", 
    cors_allowed_origins="*",   
    allow_upgrades=False,       # no upgrade dance needed
    transports=["websocket"],    # server side: websocket only, no polling
    ping_timeout=30,
    ping_interval=60
    )


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
  global local_svg
  reset_log = True
  return render_template('index.html', local_svg=local_svg, async_mode=socketio.async_mode)


@socketio.on('connect', namespace='')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(worker)

# web UI: refresh page
@socketio.on('get_page_data', namespace='')
def get_page_data(data):
  emit('page_reload', {'data': ""})


# web UI: set focus
@socketio.on('set_focus', namespace='')
def set_focus(data):
  global focus
  global hosts_info
  focus = data
  #print("focus:" + str(focus))
  with hosts_info_lock:
      if focus in hosts_info and 'data' in hosts_info[focus]:
        socketio.emit('info_event', hosts_info[focus]['data'] )
      else:
        socketio.emit('info_event', "" )
  emit('select_tab_event', {'host_name': focus})
  

# Simulation interface
# Retrieve available simulation parameters and values
# type: IFL a,b,c - phase, freq, vss
# type: LOAD a,b,c - r
# type: FAULT a,b,c - r-ok, r-fault, start-time, end-time

# write simulation parameters
#elem, val

# start/stop simulation

# read global simulation parameters->load .trans section
# write global simulation parameters->write .trans section

# FEATURE: load comtrade (need mapping to CTR/VTR elements)



# IEC61850 client interface


#synchronous read call, returns dict with sub-elements
@socketio.on('read_value', namespace='')
def read_value(data):
  logger.debug("read value:" + str(data['id'])  )
  uri = urlparse(data['id'])
  if uri.scheme in clients:
      with clients_lock[uri.scheme]:
          return clients[uri.scheme].ReadValue(data['id'])
  return {}, -1


# write call, only supports DA elements
@socketio.on('write_value', namespace='')
def write_value(data):
  logger.debug("write value:" + str(data['value']) + ", element:" + str(data['id']) )
  uri = urlparse(data['id'])
  if uri.scheme in clients:
      with clients_lock[uri.scheme]:
          retValue = clients[uri.scheme].registerWriteValue(str(data['id']),str(data['value']))
      if uri.scheme == 'iec61850':
          if retValue > 0:
              return retValue, libiec61850client.IedClientError(retValue).name
          if retValue == 0:
              return retValue, "no error"
          return retValue, "general error"
      else:
          return retValue, "no error" if retValue == 0 else "general error"
  return -1, "unsupported scheme"



# control model, only supports control object ref. e.g. LogicalDevice/CSWI.Pos
@socketio.on('operate', namespace='')
def operate(data):
  logger.debug("operate:" + str(data['id']) + " v:" + str(data['value'])  )
  uri = urlparse(data['id'])
  if uri.scheme == 'iec61850':
      with clients_lock['iec61850']:
          return clients['iec61850'].operate(str(data['id']),str(data['value']))
  if uri.scheme == 'iec60870':
      with clients_lock['iec60870']:
          return clients['iec60870'].operate(str(data['id']),str(data['value'])) # 1 on success
  return -1, "Operation not supported for this protocol"

#supports both SBO and SBOw
@socketio.on('select', namespace='')
def select(data):
  logger.debug("select:" + str(data['id'])  )
  uri = urlparse(data['id'])
  if uri.scheme == 'iec61850':
      with clients_lock['iec61850']:
          return clients['iec61850'].select(str(data['id']),str(data['value']))
  if uri.scheme == 'iec60870':
      with clients_lock['iec60870']:
          return clients['iec60870'].select(str(data['id']),str(data['value'])) # 1 on success
  return -1, "Operation not supported for this protocol"

#cancel selection
@socketio.on('cancel', namespace='')
def cancel(data):
  logger.debug("cancel:" + str(data['id'])  )
  uri = urlparse(data['id'])
  if uri.scheme == 'iec61850':
      with clients_lock['iec61850']:
          return clients['iec61850'].cancel(str(data['id']))
  return -1, "Operation not supported for this protocol"


# register datapoint for polling/reporting
@socketio.on('register_datapoint', namespace='')
def register_datapoint(data):
  logger.debug("register datapoint:" + str(data) )
  uri = urlparse(data['id'])
  if uri.scheme in clients:
      with clients_lock[uri.scheme]:
          clients[uri.scheme].registerReadValue(str(data['id']))


# web UI: load datamodels for registered IED's
@socketio.on('register_datapoint_finished', namespace='')
def register_datapoint_finished(data):
  #return #there is a bug here, so disable for now
  with clients_lock['iec61850']:
      ieds = clients['iec61850'].getRegisteredIEDs()
  for key in ieds:
    tupl = key.split(':')
    hostname = tupl[0]

    emit('log_event', {'host':key,'data':'[+] adding IED info','clear':1})

    port = None
    if len(tupl) > 1 and tupl[1] != "":
      port = int(tupl[1])
    with clients_lock['iec61850']:
        model = clients['iec61850'].getDatamodel(hostname=hostname, port=port)

    loaded_json = {}
    loaded_json['host'] = key
    loaded_json['data'] = model
    lastupdate =  time.time()
    loaded_json['last'] = lastupdate

    process_info_event(loaded_json,printItemsIEC61850(loaded_json))
  
  with clients_lock['iec60870']:
      rtus = clients['iec60870'].getRegisteredRTUs()
  for key in rtus:
    tupl = key.split(':')
    hostname = tupl[0]
    emit('log_event', {'host':key,'data':'[+] adding RTU info','clear':1})
    port = None
    if len(tupl) > 1 and tupl[1] != "":
      port = int(tupl[1])
    with clients_lock['iec60870']:
        model = clients['iec60870'].getIOA_list(hostname=hostname, port=port)

    loaded_json = {}
    loaded_json['host'] = key
    loaded_json['data'] = model
    lastupdate =  time.time()
    loaded_json['last'] = lastupdate

    process_info_event(loaded_json, printItemsIEC60870(loaded_json))


# callbacks from libiec61850client
# also called by client.poll
def readvaluecallback61850(key,data):
  logger.debug("iec61850 callback: %s - %s" % (key,data))
  socketio.emit("svg_value_update_event",{ 'element' : key, 'data' : data })

def readvaluecallback104(key,data):
  logger.debug("104 callback: %s - %s" % (key,data))
  socketio.emit("svg_value_update_event",{ 'element' : key, 'data' : data })


def cmdTerm_cb(msg):
  with async_lock:
      async_msg.append(msg)

def Rpt_cb(key, value):
  #print("key:" + str(key) + " val:" + str(value))
  with async_lock:
      async_rpt[key] = value

#add info to the ied datamodel tab
def process_info_event(loaded_json, prnitems): 
  global focus
  global hosts_info
  ihost = loaded_json['host']
  
  # store data
  with hosts_info_lock:
      if not ihost in hosts_info:
        hosts_info[ihost] = {}

      hosts_info[ihost]['last'] = loaded_json['last']
      hosts_info[ihost]['data'] = prnitems
  # send data also to webclient
  if ihost==focus:
    socketio.emit('info_event', prnitems)


def printItemsIEC60870(dictObjs):
  dictObj = dictObjs['data']
  el = 'Last update: '+str(time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime(dictObjs['last'])))+'<br><br>'
  el += '<table id="CurrentRTUModel" style="width:100%; border: 1px solid white; border-collapse: collapse;"><tr>'
  el += '<th>ASDU</th><th>IOA</th><th>Value</th></tr>\n'

  for element in dictObj:      
      if 'value' in dictObj[element]:
        id = "iec60870://" + dictObjs['host'] + "/" + str(dictObj[element]['value']) + "/" + str(element)
        el += ('<tr id="'+id+'"><td style="border: 1px solid white; border-collapse: collapse;"> ' + str(dictObj[element]['ASDU']) + '</td><td style="border: 1px solid white; border-collapse: collapse;"> ' + str(element) + '</td><td style="border: 1px solid white; border-collapse: collapse;">'+ str(dictObj[element]['value']) + '</td></tr>')
  el += ('</table>\n')
  return el

# print datamodel in table
def printItemsIEC61850(dictObjs):
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
  socketio.sleep(0.1)

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
    for scheme, c in clients.items():
        with clients_lock[scheme]:
            c.poll()
    logger.debug("values polled")

    # updating datamodel values
    with clients_lock['iec61850']:
        ieds = clients['iec61850'].getRegisteredIEDs()
    for key in ieds:
      tupl = key.split(':')
      hostname = tupl[0]
      port = None
      if len(tupl) > 1 and tupl[1] != "":
        port = int(tupl[1])
      with clients_lock['iec61850']:
          model = clients['iec61850'].getDatamodel(hostname=hostname, port=port)

      loaded_json = {}
      loaded_json['host'] = key
      loaded_json['data'] = model
      lastupdate =  time.time()
      loaded_json['last'] = lastupdate
      process_info_event(loaded_json,printItemsIEC61850(loaded_json))

    with clients_lock['iec60870']:
        rtus = clients['iec60870'].getRegisteredRTUs()
    for key in rtus:
      tupl = key.split(':')
      hostname = tupl[0]

      port = None
      if len(tupl) > 1 and tupl[1] != "":
        port = int(tupl[1])
      with clients_lock['iec60870']:
          model = clients['iec60870'].getIOA_list(hostname=hostname, port=port)

      loaded_json = {}
      loaded_json['host'] = key
      loaded_json['data'] = model
      lastupdate =  time.time()
      loaded_json['last'] = lastupdate
      process_info_event(loaded_json, printItemsIEC60870(loaded_json))


    while True:
      with async_lock:
          if len(async_msg) == 0:
              break
          msg = async_msg.pop(0)
      logger.info(msg)
    
    with async_lock:
        rpt_keys = list(async_rpt.keys())
    for key in rpt_keys:
      with async_lock:
          if key in async_rpt:
              val = async_rpt.pop(key)
          else:
              continue
      socketio.emit("svg_value_update_event",{ 'element' : key, 'data' : val })
      logger.debug("%s updated via report" % key)
        


if __name__ == '__main__':
  logger = logging.getLogger('webserver')
  logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    level=logging.INFO)

  shm = socketHandler(socketio)
  shm.setLevel(logging.INFO)
  fmm = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
  shm.setFormatter(fmm)
  logger.addHandler(shm)

	# note the `logger` from above is now properly configured

  if len(sys.argv) > 1 and sys.argv[1] == "-nD": #use different svg for debug
  	local_svg = False

  logger.info("started")
  clients = {
      'iec61850': libiec61850client.iec61850client(readvaluecallback61850, logger, cmdTerm_cb, Rpt_cb),
      'iec60870': libiec60870client.IEC60870_5_104_client(readvaluecallback104,logger)
  }
  clients_lock = {
      'iec61850': threading.Lock(),
      'iec60870': threading.Lock()
  }
  socketio.run(app,host="0.0.0.0", use_reloader=False, allow_unsafe_werkzeug=True)

