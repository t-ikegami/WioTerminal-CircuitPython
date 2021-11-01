from . import MTYPE_INVOKE, perform_request
from ..Codec import Codec

# rpc_system_version() -> string
def version() :
    codec = Codec(1, 1, MTYPE_INVOKE, "", "I{}")
    return perform_request(codec)

# rpc_system_ack(uint8 c) -> uint8
def ack(c) :
    codec = Codec(1, 2, MTYPE_INVOKE, "B", "B")
    return perform_request(codec, c)
