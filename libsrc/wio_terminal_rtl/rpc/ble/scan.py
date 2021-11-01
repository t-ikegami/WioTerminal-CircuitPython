from .. import MTYPE_INVOKE, perform_request
from ...Codec import Codec

# rpc_le_scan_set_param(RPC_T_LE_SCAN_PARAM_TYPE param, in binary value) -> RPC_T_GAP_CAUSE
def set_param(param, value) :
    codec = Codec(8, 1, MTYPE_INVOKE, "II{}", "I")
    return perform_request(codec, param, value)

# rpc_le_scan_get_param(RPC_T_LE_SCAN_PARAM_TYPE param, out binary value) -> RPC_T_GAP_CAUSE
def get_param(param) :
    codec = Codec(8, 2, MTYPE_INVOKE, "I", "I{}I")
    return perform_request(codec, param)

# rpc_le_scan_start() -> RPC_T_GAP_CAUSE
def start() :
    codec = Codec(8, 3, MTYPE_INVOKE, "", "I")
    return perform_request(codec)

# rpc_le_scan_timer_start(uint32 tick) -> RPC_T_GAP_CAUSE
def timer_start(tick) :
    codec = Codec(8, 4, MTYPE_INVOKE, "I", "I")
    return perform_request(codec, tick)

# rpc_le_scan_stop() -> RPC_T_GAP_CAUSE
def stop() :
    codec = Codec(8, 5, MTYPE_INVOKE, "", "I")
    return perform_request(codec)

# rpc_le_scan_info_filter(bool enable, uint8 offset, uint8 len, in uint8[31] p_filter) -> bool
def info_filter(enable, offset, len, p_filter) :
    codec = Codec(8, 6, MTYPE_INVOKE, "bBB31s", "b")
    return perform_request(codec, enable, offset, len, p_filter)

