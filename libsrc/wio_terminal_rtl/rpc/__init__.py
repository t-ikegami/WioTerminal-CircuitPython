import board
import time
from micropython import const
from ..Transport import Transport
from .. import pwr

MTYPE_INVOKE = const(0)
MTYPE_ONEWAY = const(1)
MTYPE_REPLY  = const(2)
MTYPE_NOTIFY = const(3)

_RTLTransport = None

def reset() :
    pwr.value = False
    time.sleep(0.1)
    pwr.value = True
    time.sleep(0.2)
    if _RTLTransport is not None : _RTLTransport.reset()

def init() :
    global _RTLTransport
    if _RTLTransport is not None: raise RuntimeError("Transport is already active.")
    _RTLTransport = Transport()
    reset()

def deinit() :
    global _RTLTransport
    if _RTLTransport is None : raise RuntimeError("Transport is not active.")
    _RTLTransport.deinit()
    _RTLTransport = None
    pwr.value = False

def perform_request(codec, *param) :
    send = codec.pack(*param)
    _RTLTransport.send(send)
    while True :
        recv = _RTLTransport.receive()
        if recv[0] == MTYPE_REPLY  :
            break
        elif recv[0] == MTYPE_ONEWAY or recv[0] == MTYPE_NOTIFY :
            # These are callbacks from RTL to notify STA_START and etc;
            # simply ignore them for now.
            continue
        else :
            raise RuntimeError("Unexpected message type: {}".format(recv[0]))
    if recv[4:8] != send[4:8] : raise RuntimeError("Unexpected sequence number in reply")
    return codec.unpack(recv)

# Suppress automatic import of modules

# from . import system
# from . import wifi
# from . import tcpip_adapter
# from . import tcp
# from . import lwip
# from . import ssl
# from . import mdns
# from . import ble
# from . import constants

init()
