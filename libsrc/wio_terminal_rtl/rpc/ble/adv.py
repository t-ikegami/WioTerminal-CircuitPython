from .. import MTYPE_INVOKE, perform_request
from ...Codec import Codec

# rpc_le_adv_set_param(RPC_T_LE_ADV_PARAM_TYPE param, in binary value) -> RPC_T_GAP_CAUSE
def set_param(param, value) :
    codec = Codec(7, 1, MTYPE_INVOKE, "II{}", "I")
    return perform_request(codec, param, value)

# rpc_le_adv_get_param(RPC_T_LE_ADV_PARAM_TYPE param, out binary value) -> RPC_T_GAP_CAUSE
def get_param(param) :
    codec = Codec(7, 2, MTYPE_INVOKE, "I", "I{}I")
    return perform_request(codec, param)

# rpc_le_adv_start() -> RPC_T_GAP_CAUSE
def start() :
    codec = Codec(7, 3, MTYPE_INVOKE, "", "I")
    return perform_request(codec)

# rpc_le_adv_stop() -> RPC_T_GAP_CAUSE
def stop() :
    codec = Codec(7, 4, MTYPE_INVOKE, "", "I")
    return perform_request(codec)

# rpc_le_adv_update_param() -> RPC_T_GAP_CAUSE
def update_param() :
    codec = Codec(7, 5, MTYPE_INVOKE, "", "I")
    return perform_request(codec)

