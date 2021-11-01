from .. import MTYPE_INVOKE, perform_request
from ...Codec import Codec

# rpc_flash_save_local_name(in RPC_T_LOCAL_NAME p_data) -> uint32
def save_local_name(p_data) :
    codec = Codec(10, 1, MTYPE_INVOKE, "40s", "I")
    return perform_request(codec, p_data)

# rpc_flash_load_local_name(out RPC_T_LOCAL_NAME p_data) -> uint32
def load_local_name() :
    codec = Codec(10, 2, MTYPE_INVOKE, "", "40sI")
    return perform_request(codec)

# rpc_flash_save_local_appearance(in RPC_T_LOCAL_APPEARANCE p_data) -> uint32
def save_local_appearance(p_data) :
    codec = Codec(10, 3, MTYPE_INVOKE, "04s", "I")
    return perform_request(codec, p_data)

# rpc_flash_load_local_appearance(out RPC_T_LOCAL_APPEARANCE p_data) -> uint32
def load_local_appearance() :
    codec = Codec(10, 4, MTYPE_INVOKE, "", "04sI")
    return perform_request(codec)

