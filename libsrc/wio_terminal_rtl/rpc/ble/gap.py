from .. import MTYPE_INVOKE, perform_request
from ...Codec import Codec

# rpc_gap_set_param(RPC_T_GAP_PARAM_TYPE param, in binary value) -> RPC_T_GAP_CAUSE
def set_param(param, value) :
    codec = Codec(3, 1, MTYPE_INVOKE, "II{}", "I")
    return perform_request(codec, param, value)

# rpc_gap_get_param(RPC_T_GAP_PARAM_TYPE param, out binary value) -> RPC_T_GAP_CAUSE
def get_param(param) :
    codec = Codec(3, 2, MTYPE_INVOKE, "I", "I{}I")
    return perform_request(codec, param)

# rpc_gap_set_pairable_mode() -> RPC_T_GAP_CAUSE
def set_pairable_mode() :
    codec = Codec(3, 3, MTYPE_INVOKE, "", "I")
    return perform_request(codec)


# rpc_le_gap_init(uint8 link_num) -> bool
def init(link_num) :
    codec = Codec(5, 1, MTYPE_INVOKE, "B", "b")
    return perform_request(codec, link_num)

# rpc_le_gap_msg_info_way(bool use_msg) -> void
def msg_info_way(use_msg) :
    codec = Codec(5, 2, MTYPE_INVOKE, "b", "")
    return perform_request(codec, use_msg)

