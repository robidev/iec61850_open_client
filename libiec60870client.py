#!/usr/bin/env python3
from lib60870 import *
from urllib.parse import urlparse
import time
import logging
from threading import Lock, Thread, Event
from collections import defaultdict

logger = logging.getLogger(__name__)

class IEC60870_5_104_client:
    # Connection event handler 
    def connectionHandler (self, parameter, connection, event):
        tupl = ctypes.cast(parameter, ctypes.py_object).value
        if event == CS104_CONNECTION_OPENED:
            logger.info("104 Connection established: %s" % str(tupl))
            self.connections[tupl]['state'] = 2
        elif event == CS104_CONNECTION_CLOSED:
            logger.info("104 Connection closed: %s" % str(tupl))
            self.connections[tupl]['state'] = 0
            CS104_Connection_destroy(self.connections[tupl]["con"])
            self.connections[tupl]["con"] = None
        elif event == CS104_CONNECTION_STARTDT_CON_RECEIVED:
            logger.debug("Received STARTDT_CON")
            self.connections[tupl]['state'] = 3
        elif event == CS104_CONNECTION_STOPDT_CON_RECEIVED:
            logger.debug("Received STOPDT_CON")
            self.connections[tupl]['state'] = 1


    #CS101_ASDUReceivedHandler implementation
    #For CS104 the address parameter has to be ignored
    def asduReceivedHandler (self, parameter, address, asdu):
        data = {}
        tupl = ctypes.cast(parameter, ctypes.py_object).value
        if not tupl in self.connections:
            logger.error("error: cannot find %s in connections" % str(tupl))
            return False

        logger.debug("RECVD ASDU type: %s(%i) elements: %i" % (
            TypeID_toString(CS101_ASDU_getTypeID(asdu)),
            CS101_ASDU_getTypeID(asdu),
            CS101_ASDU_getNumberOfElements(asdu)
        ))

        if CS101_ASDU_getTypeID(asdu) == C_IC_NA_1:
            self.connections[tupl]['GI'] = True

        if (CS101_ASDU_getTypeID(asdu) == M_ME_TE_1):

            logger.debug("  measured scaled values with CP56Time2a timestamp:")

            for i in range(CS101_ASDU_getNumberOfElements(asdu)):

                io = cast(CS101_ASDU_getElement(asdu, i), MeasuredValueScaledWithCP56Time2a) 
                ioa = InformationObject_getObjectAddress(cast(io, InformationObject) )
                value = MeasuredValueScaled_getValue(cast(io, MeasuredValueScaled) )
                logger.debug("    IOA: %i value: %i" % (ioa,value ))
                self.connections[tupl]['data'][ioa] = {'value': value, 'ASDU': M_ME_TE_1, 'type': 'int'}
                data[ioa] = {'value': value, 'ASDU': M_ME_TE_1, 'type': 'int'}
                MeasuredValueScaledWithCP56Time2a_destroy(io)

        elif (CS101_ASDU_getTypeID(asdu) == M_SP_NA_1):
            logger.debug("  single point information:")

            for i in range(CS101_ASDU_getNumberOfElements(asdu)):

                io = cast(CS101_ASDU_getElement(asdu, i), SinglePointInformation) 
                ioa = InformationObject_getObjectAddress(cast(io,InformationObject) )
                value = SinglePointInformation_getValue(cast(io,SinglePointInformation) )
                logger.debug("    IOA: %i value: %i" % (ioa,value ))
                self.connections[tupl]['data'][ioa] = {'value': value, 'ASDU': M_SP_NA_1, 'type': 'boolean'}
                data[ioa] = {'value': value, 'ASDU': M_SP_NA_1, 'type': 'boolean'}
                SinglePointInformation_destroy(io)
        elif (CS101_ASDU_getTypeID(asdu) == M_DP_NA_1):
            logger.debug("  double point information:")

            for i in range(CS101_ASDU_getNumberOfElements(asdu)):

                io = cast(CS101_ASDU_getElement(asdu, i), DoublePointInformation)
                ioa = InformationObject_getObjectAddress(cast(io,InformationObject) ) 
                value = DoublePointInformation_getValue(cast(io,DoublePointInformation) )
                logger.debug("    IOA: %i value: %i" % (ioa,value ))
                self.connections[tupl]['data'][ioa] = {'value': value, 'ASDU': M_DP_NA_1, 'type': 'bit-string'}
                data[ioa] = {'value': value, 'ASDU': M_DP_NA_1, 'type': 'bit-string'}
                DoublePointInformation_destroy(io)
        elif (CS101_ASDU_getTypeID(asdu) == M_ME_NB_1):
            logger.debug("  measured value scaled:")

            for i in range(CS101_ASDU_getNumberOfElements(asdu)):

                io = cast(CS101_ASDU_getElement(asdu, i), MeasuredValueScaled) 
                ioa = InformationObject_getObjectAddress(cast(io,InformationObject) )
                value = MeasuredValueScaled_getValue(cast(io,MeasuredValueScaled) )
                logger.debug("    IOA: %i value: %i" % (ioa,value ))
                self.connections[tupl]['data'][ioa] = {'value': value, 'ASDU': M_ME_NB_1, 'type': 'int'}
                data[ioa] = {'value': value, 'ASDU': M_ME_NB_1, 'type': 'int'}
                MeasuredValueScaled_destroy(io)     
        elif (CS101_ASDU_getTypeID(asdu) == C_SC_NA_1):
            logger.debug("received single command response")
            for i in range(CS101_ASDU_getNumberOfElements(asdu)):

                io = cast(CS101_ASDU_getElement(asdu, i), SinglePointInformation) 
                ioa = InformationObject_getObjectAddress(cast(io,InformationObject) )
                value = SinglePointInformation_getValue(cast(io,SinglePointInformation) )
                logger.debug("    IOA: %i value: %i" % (ioa,value ))
                self.connections[tupl]['data'][ioa] = {'value': value, 'ASDU': C_SC_NA_1, 'type': 'boolean'}
                data[ioa] = {'value': value, 'ASDU': C_SC_NA_1, 'type': 'boolean'}
                SinglePointInformation_destroy(io)

        elif (CS101_ASDU_getTypeID(asdu) == C_DC_NA_1):
            logger.debug("received double command response")
            for i in range(CS101_ASDU_getNumberOfElements(asdu)):

                io = cast(CS101_ASDU_getElement(asdu, i), DoublePointInformation) 
                ioa = InformationObject_getObjectAddress(cast(io,InformationObject) )
                value = DoublePointInformation_getValue(cast(io,DoublePointInformation) )
                logger.debug("    IOA: %i value: %i" % (ioa,value ))
                self.connections[tupl]['data'][ioa] = {'value': value, 'ASDU': C_DC_NA_1, 'type': 'bit-string'}
                data[ioa] = {'value': value, 'ASDU': C_DC_NA_1, 'type': 'bit-string'}
                DoublePointInformation_destroy(io)

        elif (CS101_ASDU_getTypeID(asdu) == C_TS_TA_1):
            self.connections[tupl]['testfr_received'] += 1
            logger.debug("  received test command with timestamp. send: %i, received: %i" % (self.connections[tupl]['testfr_send'],self.connections[tupl]['testfr_received']))
            return True

        if self.callback != None and len(data) > 0:
            for ioa in data:
                ref = "iec60870://" + tupl + "/" + str(data[ioa]['ASDU']) + "/" + str(ioa)
                self.callback(ref, data[ioa])
        return True


    def __init__(self, callback,loggerRef = None):
        global logger
        if loggerRef != None:
            logger = loggerRef
        self.connections = {}
        self.timeout = 2
        self.callback = callback
        self.next_poll = 0
        self.p_connectionHandler = CS104_ConnectionHandler(self.connectionHandler)
        self.p_asduReceivedHandler = CS101_ASDUReceivedHandler(self.asduReceivedHandler)
        self.connection_locks = {}
        self.stop_event = Event()
        self.connection_worker =  Thread(target=self.connection_worker_thread)
        self.connection_worker.start()


    def stop_worker(self):
        self.stop_event.set()
        if self.connection_worker is not None:
            self.connection_worker.join(timeout=3)


    def getRegisteredRTUs(self):
        return self.connections


    def getIOA_list(self, hostname, port):
        if self.getRTU(hostname, port) != 0: # check for active connection
            return {}
        
        if port == "" or port == None:
            port = 2404

        tupl = hostname + ":" + str(port)
        return self.connections[tupl]['data']

    def connection_worker_thread(self):
        while not self.stop_event.is_set():
			# iterate over self.connections
            for tupl in self.connections.keys():
                if tupl not in self.connection_locks:
                    continue

                with self.connection_locks[tupl]:
                    if self.connections[tupl]["con"] != None:
                        if self.connections[tupl]["GI"] is True:
                            continue
                        else:
                            # Perform GI
                            if not CS104_Connection_sendInterrogationCommand( self.connections[tupl]["con"], CS101_COT_ACTIVATION, 1, IEC60870_QOI_STATION):
                                self.connections[tupl]["state"] = 0
                                CS104_Connection_destroy(self.connections[tupl]["con"])
                                self.connections[tupl]["con"] = None
                            continue
                    # else no con
                    host, port = tupl.split(":")
                    con = CS104_Connection_create(host, int(port))
                    CS104_Connection_setConnectionHandler(con, self.p_connectionHandler, id(self.connections[tupl]["self"]) )
                    CS104_Connection_setASDUReceivedHandler( con, self.p_asduReceivedHandler, id(self.connections[tupl]["self"]))

                                       
                    if CS104_Connection_connect(con) == False:
                        logger.debug("error: could not connect to %s" % str(tupl))
                        self.connections[tupl]["state"] = 0
                        CS104_Connection_destroy(con)
                        continue

                    logger.info("connected:" + str(tupl)) 
                    if CS104_Connection_sendStartDT(con) == False:
                        logger.error("error: could not send startDT")
                        self.connections[tupl]["state"] = 0
                        CS104_Connection_destroy(con)
                        continue

                    self.connections[tupl]["con"] = con
                    #with
                #for
            time.sleep(1.0)

    

    # retrieve an active connection to an RTU, and up to date datamodel, stored in 'connections'
    def getRTU(self, host, port):
        if not port:
            port = 2404
        if not host:
            logger.error("missing hostname")
            return -1

        tupl = host + ":" + str(port)
        if tupl not in self.connection_locks:
            self.connection_locks[tupl] = Lock()

        with self.connection_locks[tupl]:
            # Fast path: already connected and ready
            if tupl in self.connections:
                if self.connections[tupl]["con"] is not None and self.connections[tupl]["GI"] is True:
                    return 0
                else:
                    return -1
    
            # Initialize structure if needed
            self.connections[tupl] = {
                "con": None,
                "GI": False,
                "data": {},
                "state": 0,
                "testfr_received": 0,
                "testfr_send": 0,
                "self": tupl
            }
            return -1


    def parseref(self,ref):
        uri_ref = urlparse(ref)
        port = uri_ref.port
        if port == "" or port == None:
            port = 2404

        if uri_ref.scheme != "iec60870":
            logger.error("incorrect scheme, only iec60870 is supported, not %s" % uri_ref.scheme)
            return None

        if uri_ref.hostname == None:
            logger.error("missing hostname: %s" % ref)
            return None

        tupl = uri_ref.hostname + ":" + str(port)

        #check if connection is active, or reconnect
        err = self.getRTU(uri_ref.hostname, port)
        if err == 0:
            con = self.connections[tupl]['con']
            if not con:
                logger.error("no valid connection")
                return None		

            model = self.connections[tupl]['data']
            if not model:
                logger.error("no valid model")
                return None
			
            _ref = uri_ref.path[1:].split("/")
            type = _ref[0]
            ioa = _ref[1]
            return {"RTU":self.connections[tupl], "type":type, "ioa":int(ioa) }
        else:
            return None


    def select(self,ref, value):
        obj = self.parseref(ref) 
        if obj != None:
            ca = 1 # common address
            if obj['type'] == "45":
                dc = cast(SingleCommand_create(None, obj['ioa'], int(value), True, 0), InformationObject)
                logger.info("Send select command C_SC_NA_1")
            elif obj['type'] == "46":
                dc = cast(DoubleCommand_create(None, obj['ioa'], int(value), True, 0), InformationObject)
                logger.info("Send select command C_DC_NA_1")
            else:
                return 0

            CS104_Connection_sendProcessCommandEx(obj["RTU"]["con"], CS101_COT_ACTIVATION, ca, dc)
            InformationObject_destroy(dc)
            return 1
        return 0


    def operate(self,ref, value):
        obj = self.parseref(ref) 
        if obj != None:
            ca = 1 # common address
            if obj['type'] == "45":
                dc = cast(SingleCommand_create(None, obj['ioa'], int(value), False, 0), InformationObject)
                logger.info("Send operate command C_SC_NA_1 with value:" + str(value))
            elif obj['type'] == "46":
                dc = cast(DoubleCommand_create(None, obj['ioa'], int(value), False, 0), InformationObject)
                logger.info("Send operate command C_DC_NA_1 with value:" + str(value))
            else:
                return 0

            CS104_Connection_sendProcessCommandEx(obj["RTU"]["con"], CS101_COT_ACTIVATION, ca, dc)
            InformationObject_destroy(dc)
            return 1
        return 0

    def testframe(self, host, port):
        if port == "" or port == None:
            port = 2404

        if host == None:
            logger.error("missing hostname")
            return -1

        err = self.getRTU(host, port)
        if err == 0:
            tupl = host + ":" + str(port)
            con = self.connections[tupl]['con']
            if not con:
                logger.error("no valid connection")
                return -1
            if self.connections[tupl]['testfr_send'] > self.connections[tupl]['testfr_received'] + 5:
                logger.error("too many missed testframes, closing connection")
                CS104_Connection_sendStopDT(self.connections[tupl]["con"])
                CS104_Connection_destroy(self.connections[tupl]["con"])
                self.connections[tupl]["con"] = None
                self.connections[tupl]["state"] = 0
                return -1

            newTime = sCP56Time2a() 
            CP56Time2a_createFromMsTimestamp(CP56Time2a(newTime), Hal_getTimeInMs())
            if CS104_Connection_sendTestCommandWithTimestamp(con, 1, 0x4938, newTime) == False:
                logger.error("could not send testframe, closing connection")
                CS104_Connection_sendStopDT(con)
                CS104_Connection_destroy(con)
                self.connections[tupl]["con"] = None
                self.connections[tupl]["state"] = 0              
                return -1

            self.connections[tupl]['testfr_send'] += 1
            return 0


    def removeRTU(self,host,port):
        if port == "" or port == None:
            port = 2404

        tupl = host + ":" + str(port)
        if tupl in self.connections and self.connections[tupl]["con"] != None:
            CS104_Connection_sendStopDT(self.connections[tupl]["con"])
            CS104_Connection_destroy(self.connections[tupl]["con"])
            self.connections[tupl]["con"] = None

        self.connections[tupl]["state"] = 0


    def ReadValue(self,ref):
        logger.info("ReadValue not implemented, called with:" + str(ref))
        return 0

    def registerWriteValue(self,ref,val):
        logger.info("registerWriteValue not implemented, called with:" + str(ref) + ", with val:" + str(val))
        return 0

    def registerReadValue(self,ref):
        logger.debug("registerReadValue called" )
        retval = self.parseref(ref)
        return

    def poll(self):
        now = time.monotonic()
        if now < self.next_poll:
            return
        self.next_poll = now + 1.0 # interval in seconds

        for tupl in self.connections:
            if self.connections[tupl]["state"] == 3:
                # send a GI
                con = self.connections[tupl]['con']
                if CS104_Connection_sendInterrogationCommand(con, CS101_COT_ACTIVATION, 1, IEC60870_QOI_STATION) == False:
                    logger.error("error: could not send GI")
                    CS104_Connection_sendStopDT(con)
                    CS104_Connection_destroy(con)
                    self.connections[tupl]["state"] = 0
                    return
                else:
                    logger.debug("GI send!")
        return

def testcallb(tupl, data):
    logger.info("RTU:" + tupl + " - update:" + str(data))

#test the class
if __name__== "__main__":
    client = IEC60870_5_104_client(testcallb)
    if client.getRTU("localhost", 2404) == 0:
        tupl = "localhost:2404"
        # perform read of latest data
        logger.info(client.connections[tupl]["data"])
        #perform operate
        if client.select("iec60870://localhost:2404/46/6000", 1) == 1: # doublepoint command ASDU = 46
            if client.operate("iec60870://localhost:2404/46/6000", 1) == 1: # doublepoint command ASDU = 46
                logger.info("oper success")
            else:
                logger.error("oper failed")
        else:
            logger.error("select failed")