from .. import MTYPE_INVOKE, perform_request
from ...Codec import Codec

# rpc_le_bond_set_param(RPC_T_LE_BOND_PARAM_TYPE param, in binary value) -> RPC_T_GAP_CAUSE
def set_param(param, value) :
    codec = Codec(4, 1, MTYPE_INVOKE, "II{}", "I")
    return perform_request(codec, param, value)

# rpc_le_bond_get_param(RPC_T_LE_BOND_PARAM_TYPE param, out binary value) -> RPC_T_GAP_CAUSE
def get_param(param) :
    codec = Codec(4, 2, MTYPE_INVOKE, "I", "I{}I")
    return perform_request(codec, param)

# rpc_le_bond_pair(uint8 conn_id) -> RPC_T_GAP_CAUSE
def pair(conn_id) :
    codec = Codec(4, 3, MTYPE_INVOKE, "B", "I")
    return perform_request(codec, conn_id)

# rpc_le_bond_get_display_key(uint8 conn_id, out uint32 key) -> RPC_T_GAP_CAUSE
def get_display_key(conn_id) :
    codec = Codec(4, 4, MTYPE_INVOKE, "B", "II")
    return perform_request(codec, conn_id)

# rpc_le_bond_passkey_input_confirm(uint8 conn_id, uint32 passcode, RPC_T_GAP_CFM_CAUSE cause) -> RPC_T_GAP_CAUSE
def passkey_input_confirm(conn_id, passcode, cause) :
    codec = Codec(4, 5, MTYPE_INVOKE, "BII", "I")
    return perform_request(codec, conn_id, passcode, cause)

# rpc_le_bond_oob_input_confirm(uint8 conn_id, RPC_T_GAP_CFM_CAUSE cause) -> RPC_T_GAP_CAUSE
def oob_input_confirm(conn_id, cause) :
    codec = Codec(4, 6, MTYPE_INVOKE, "BI", "I")
    return perform_request(codec, conn_id, cause)

# rpc_le_bond_just_work_confirm(uint8 conn_id, RPC_T_GAP_CFM_CAUSE cause) -> RPC_T_GAP_CAUSE
def just_work_confirm(conn_id, cause) :
    codec = Codec(4, 7, MTYPE_INVOKE, "BI", "I")
    return perform_request(codec, conn_id, cause)

# rpc_le_bond_passkey_display_confirm(uint8 conn_id, RPC_T_GAP_CFM_CAUSE cause) -> RPC_T_GAP_CAUSE
def passkey_display_confirm(conn_id, cause) :
    codec = Codec(4, 8, MTYPE_INVOKE, "BI", "I")
    return perform_request(codec, conn_id, cause)

# rpc_le_bond_user_confirm(uint8 conn_id, RPC_T_GAP_CFM_CAUSE cause) -> RPC_T_GAP_CAUSE
def user_confirm(conn_id, cause) :
    codec = Codec(4, 9, MTYPE_INVOKE, "BI", "I")
    return perform_request(codec, conn_id, cause)

# rpc_le_bond_cfg_local_key_distribute(uint8 init_dist, uint8 rsp_dist) -> RPC_T_GAP_CAUSE
def cfg_local_key_distribute(init_dist, rsp_dist) :
    codec = Codec(4, 10, MTYPE_INVOKE, "BB", "I")
    return perform_request(codec, init_dist, rsp_dist)

# rpc_le_bond_clear_all_keys() -> void
def clear_all_keys() :
    codec = Codec(4, 11, MTYPE_INVOKE, "", "")
    return perform_request(codec)

# rpc_le_bond_delete_by_idx(uint8 idx) -> RPC_T_GAP_CAUSE
def delete_by_idx(idx) :
    codec = Codec(4, 12, MTYPE_INVOKE, "B", "I")
    return perform_request(codec, idx)

# rpc_le_bond_delete_by_bd(in uint8[6] bd_addr, RPC_T_GAP_REMOTE_ADDR_TYPE bd_type) -> RPC_T_GAP_CAUSE
def delete_by_bd(bd_addr, bd_type) :
    codec = Codec(4, 13, MTYPE_INVOKE, "6sI", "I")
    return perform_request(codec, bd_addr, bd_type)

# rpc_le_bond_get_sec_level(uint8 conn_id, out RPC_T_GAP_SEC_LEVEL sec_type) -> RPC_T_GAP_CAUSE
def get_sec_level(conn_id) :
    codec = Codec(4, 14, MTYPE_INVOKE, "B", "II")
    return perform_request(codec, conn_id)

