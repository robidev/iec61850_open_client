import logging

logger = logging.getLogger(__name__)

def scheme():
    return "abstract"

# this is an abstract class for a client. it can be used to ensure all functions are instantiated for a specific client, by using it as the base class
class abstract_client():
    def __init__(self,readvaluecallback = None, loggerRef = None, cmd_cb = None, event_cb = None):
        raise Exception("abstract function should be overwritten")

    @staticmethod
    def ErrorCodes(value):
        raise Exception("abstract function should be overwritten")

    def registerWriteValue(self, id, value):
        raise Exception("abstract function should be overwritten")

    def registerReadValue(self, id):
        raise Exception("abstract function should be overwritten")
    
    def ReadValue(self, id):
        raise Exception("abstract function should be overwritten")
    
    def operate(id, value):
        raise Exception("abstract function should be overwritten")

    def select(id, value):
        raise Exception("abstract function should be overwritten")

    def cancel(id, value):
        raise Exception("abstract function should be overwritten")

    def poll():
        raise Exception("abstract function should be overwritten")
    