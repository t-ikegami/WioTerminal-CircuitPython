from .. import MTYPE_INVOKE, perform_request
from ...Codec import Codec

# rpc_ble_init() -> bool
def init() :
    codec = Codec(2, 1, MTYPE_INVOKE, "", "b")
    return perform_request(codec)

# rpc_ble_start() -> void
def start() :
    codec = Codec(2, 2, MTYPE_INVOKE, "", "")
    return perform_request(codec)

# rpc_ble_deinit() -> void
def deinit() :
    codec = Codec(2, 3, MTYPE_INVOKE, "", "")
    return perform_request(codec)

# rpc_le_get_max_link_num() -> uint8
def get_max_link_num() :
    codec = Codec(5, 3, MTYPE_INVOKE, "", "B")
    return perform_request(codec)

# rpc_le_set_gap_param(RPC_T_GAP_LE_PARAM_TYPE param, in binary value) -> RPC_T_GAP_CAUSE
def set_gap_param(param, value) :
    codec = Codec(5, 4, MTYPE_INVOKE, "II{}", "I")
    return perform_request(codec, param, value)

# rpc_le_get_gap_param(RPC_T_GAP_LE_PARAM_TYPE param, out binary value) -> RPC_T_GAP_CAUSE
def get_gap_param(param) :
    codec = Codec(5, 5, MTYPE_INVOKE, "I", "I{}I")
    return perform_request(codec, param)

# rpc_le_modify_white_list(RPC_T_GAP_WHITE_LIST_OP operation, in uint8[6] bd_addr, RPC_T_GAP_REMOTE_ADDR_TYPE bd_type) -> RPC_T_GAP_CAUSE
def modify_white_list(operation, bd_addr, bd_type) :
    codec = Codec(5, 6, MTYPE_INVOKE, "I6sI", "I")
    return perform_request(codec, operation, bd_addr, bd_type)

# rpc_le_gen_rand_addr(RPC_T_GAP_RAND_ADDR_TYPE rand_addr_type, out uint8[6] random_bd) -> RPC_T_GAP_CAUSE
def gen_rand_addr(rand_addr_type) :
    codec = Codec(5, 7, MTYPE_INVOKE, "I", "6sI")
    return perform_request(codec, rand_addr_type)

# rpc_le_set_rand_addr(in uint8[6] random_bd) -> RPC_T_GAP_CAUSE
def set_rand_addr(random_bd) :
    codec = Codec(5, 8, MTYPE_INVOKE, "6s", "I")
    return perform_request(codec, random_bd)

# rpc_le_cfg_local_identity_address(in uint8[6] addr, RPC_T_GAP_IDENT_ADDR_TYPE ident_addr_type) -> RPC_T_GAP_CAUSE
def cfg_local_identity_address(addr, ident_addr_type) :
    codec = Codec(5, 9, MTYPE_INVOKE, "6sI", "I")
    return perform_request(codec, addr, ident_addr_type)

# rpc_le_set_host_chann_classif(in uint8 p_channel_map) -> RPC_T_GAP_CAUSE
def set_host_chann_classif(p_channel_map) :
    codec = Codec(5, 10, MTYPE_INVOKE, "B", "I")
    return perform_request(codec, p_channel_map)

# rpc_le_write_default_data_len(uint16 tx_octets, uint16 tx_time) -> RPC_T_GAP_CAUSE
def write_default_data_len(tx_octets, tx_time) :
    codec = Codec(5, 11, MTYPE_INVOKE, "HH", "I")
    return perform_request(codec, tx_octets, tx_time)

# rpc_le_get_conn_param(RPC_T_LE_CONN_PARAM_TYPE param, out binary value, uint8 conn_id) -> RPC_T_GAP_CAUSE
def get_conn_param(param, conn_id) :
    codec = Codec(9, 1, MTYPE_INVOKE, "IB", "I{}I")
    return perform_request(codec, param, conn_id)

# rpc_le_get_conn_info(uint8 conn_id, out RPC_T_GAP_CONN_INFO p_conn_info) -> bool
def get_conn_info(conn_id) :
    codec = Codec(9, 2, MTYPE_INVOKE, "B", "15sb")
    return perform_request(codec, conn_id)

# rpc_le_get_conn_addr(uint8 conn_id, out uint8[6] bd_addr, out uint8 bd_type) -> bool
def get_conn_addr(conn_id) :
    codec = Codec(9, 3, MTYPE_INVOKE, "B", "6sBb")
    return perform_request(codec, conn_id)

# rpc_le_get_conn_id(in uint8[6] bd_addr, uint8 bd_type, out uint8 p_conn_id) -> bool
def get_conn_id(bd_addr, bd_type) :
    codec = Codec(9, 4, MTYPE_INVOKE, "6sB", "Bb")
    return perform_request(codec, bd_addr, bd_type)

# rpc_le_get_active_link_num() -> uint8
def get_active_link_num() :
    codec = Codec(9, 5, MTYPE_INVOKE, "", "B")
    return perform_request(codec)

# rpc_le_get_idle_link_num() -> uint8
def get_idle_link_num() :
    codec = Codec(9, 6, MTYPE_INVOKE, "", "B")
    return perform_request(codec)

# rpc_le_disconnect(uint8 conn_id) -> RPC_T_GAP_CAUSE
def disconnect(conn_id) :
    codec = Codec(9, 7, MTYPE_INVOKE, "B", "I")
    return perform_request(codec, conn_id)

# rpc_le_read_rssi(uint8 conn_id) -> RPC_T_GAP_CAUSE
def read_rssi(conn_id) :
    codec = Codec(9, 8, MTYPE_INVOKE, "B", "I")
    return perform_request(codec, conn_id)

# rpc_le_set_data_len(uint8 conn_id, uint16 tx_octets, uint16 tx_time) -> RPC_T_GAP_CAUSE
def set_data_len(conn_id, tx_octets, tx_time) :
    codec = Codec(9, 9, MTYPE_INVOKE, "BHH", "I")
    return perform_request(codec, conn_id, tx_octets, tx_time)

# rpc_le_set_phy(uint8 conn_id, uint8 all_phys, uint8 tx_phys, uint8 rx_phys, RPC_T_GAP_PHYS_OPTIONS phy_options) -> RPC_T_GAP_CAUSE
def set_phy(conn_id, all_phys, tx_phys, rx_phys, phy_options) :
    codec = Codec(9, 10, MTYPE_INVOKE, "BBBBI", "I")
    return perform_request(codec, conn_id, all_phys, tx_phys, rx_phys, phy_options)

# rpc_le_set_conn_param(RPC_T_GAP_CONN_PARAM_TYPE conn_type, in RPC_T_GAP_LE_CONN_REQ_PARAM p_conn_param) -> RPC_T_GAP_CAUSE
def set_conn_param(conn_type, p_conn_param) :
    codec = Codec(9, 11, MTYPE_INVOKE, "I16s", "I")
    return perform_request(codec, conn_type, p_conn_param)

# rpc_le_connect(uint8 init_phys, in uint8[6] remote_bd, RPC_T_GAP_REMOTE_ADDR_TYPE remote_bd_type, RPC_T_GAP_LOCAL_ADDR_TYPE local_bd_type, uint16 scan_timeout) -> RPC_T_GAP_CAUSE
def connect(init_phys, remote_bd, remote_bd_type, local_bd_type, scan_timeout) :
    codec = Codec(9, 12, MTYPE_INVOKE, "B6sIIH", "I")
    return perform_request(codec, init_phys, remote_bd, remote_bd_type, local_bd_type, scan_timeout)

# rpc_le_update_conn_param(uint8 conn_id, uint16 conn_interval_min, uint16 conn_interval_max, uint16 conn_latency, uint16 supervision_timeout, uint16 ce_length_min, uint16 ce_length_max) -> RPC_T_GAP_CAUSE
def update_conn_param(conn_id, conn_interval_min, conn_interval_max, conn_latency, supervision_timeout, ce_length_min, ce_length_max) :
    codec = Codec(9, 13, MTYPE_INVOKE, "BHHHHHH", "I")
    return perform_request(codec, conn_id, conn_interval_min, conn_interval_max, conn_latency, supervision_timeout, ce_length_min, ce_length_max)

# rpc_le_find_key_entry(in uint8[6] bd_addr, RPC_T_GAP_REMOTE_ADDR_TYPE bd_type) -> @nullable RPC_T_LE_KEY_ENTRY
def find_key_entry(bd_addr, bd_type) :
    codec = Codec(10, 5, MTYPE_INVOKE, "6sI", "b24s")
    return perform_request(codec, bd_addr, bd_type)

# rpc_le_find_key_entry_by_idx(uint8 idx) -> @nullable RPC_T_LE_KEY_ENTRY
def find_key_entry_by_idx(idx) :
    codec = Codec(10, 6, MTYPE_INVOKE, "B", "b24s")
    return perform_request(codec, idx)

# rpc_le_get_bond_dev_num() -> uint8
def get_bond_dev_num() :
    codec = Codec(10, 7, MTYPE_INVOKE, "", "B")
    return perform_request(codec)

# rpc_le_get_low_priority_bond() -> @nullable RPC_T_LE_KEY_ENTRY
def get_low_priority_bond() :
    codec = Codec(10, 8, MTYPE_INVOKE, "", "b24s")
    return perform_request(codec)

# rpc_le_get_high_priority_bond() -> @nullable RPC_T_LE_KEY_ENTRY
def get_high_priority_bond() :
    codec = Codec(10, 9, MTYPE_INVOKE, "", "b24s")
    return perform_request(codec)

# rpc_le_set_high_priority_bond(in uint8[6] bd_addr, RPC_T_GAP_REMOTE_ADDR_TYPE bd_type) -> bool
def set_high_priority_bond(bd_addr, bd_type) :
    codec = Codec(10, 10, MTYPE_INVOKE, "6sI", "b")
    return perform_request(codec, bd_addr, bd_type)

# rpc_le_resolve_random_address(in uint8[6] unresolved_addr, inout uint8[6] resolved_addr, inout RPC_T_GAP_IDENT_ADDR_TYPE resolved_addr_type) -> bool
def resolve_random_address(unresolved_addr, resolved_addr, resolved_addr_type) :
    codec = Codec(10, 11, MTYPE_INVOKE, "6s6sI", "6sIb")
    return perform_request(codec, unresolved_addr, resolved_addr, resolved_addr_type)

# rpc_le_get_cccd_data(in RPC_T_LE_KEY_ENTRY p_entry, out RPC_T_LE_CCCD p_data) -> bool
def get_cccd_data(p_entry) :
    codec = Codec(10, 12, MTYPE_INVOKE, "24s", "05sb")
    return perform_request(codec, p_entry)

# rpc_le_gen_bond_dev(in uint8[6] bd_addr, RPC_T_GAP_REMOTE_ADDR_TYPE bd_type, RPC_T_GAP_LOCAL_ADDR_TYPE local_bd_type, in binary local_ltk, RPC_T_LE_KEY_TYPE key_type, RPC_T_LE_CCCD p_cccd) -> bool
def gen_bond_dev(bd_addr, bd_type, local_bd_type, local_ltk, key_type, p_cccd) :
    codec = Codec(10, 13, MTYPE_INVOKE, "6sIII{}I05s", "b")
    return perform_request(codec, bd_addr, bd_type, local_bd_type, local_ltk, key_type, p_cccd)

# rpc_le_get_dev_bond_info_len() -> uint16
def get_dev_bond_info_len() :
    codec = Codec(10, 14, MTYPE_INVOKE, "", "H")
    return perform_request(codec)

# rpc_le_set_dev_bond_info(in binary p_data, out bool exist) -> @nullable RPC_T_LE_KEY_ENTRY
def set_dev_bond_info(p_data) :
    codec = Codec(10, 15, MTYPE_INVOKE, "I{}", "bb24s")
    return perform_request(codec, p_data)

# rpc_le_get_dev_bond_info(RPC_T_LE_KEY_ENTRY p_entry, out binary p_data) -> bool
def get_dev_bond_info(p_entry) :
    codec = Codec(10, 16, MTYPE_INVOKE, "24s", "I{}b")
    return perform_request(codec, p_entry)

# rpc_ble_client_init(uint8 num) -> bool
def client_init(num) :
    codec = Codec(11, 1, MTYPE_INVOKE, "B", "b")
    return perform_request(codec, num)

# rpc_ble_add_client(uint8 app_id, uint8 link_num) -> uint8
def add_client(app_id, link_num) :
    codec = Codec(11, 2, MTYPE_INVOKE, "BB", "B")
    return perform_request(codec, app_id, link_num)

# rpc_ble_server_init(uint8 num) -> bool
def server_init(num) :
    codec = Codec(12, 1, MTYPE_INVOKE, "B", "b")
    return perform_request(codec, num)

# rpc_ble_create_service(uint8[16] uuid, uint8 uuid_length, bool is_primary) -> uint8
def create_service(uuid, uuid_length, is_primary) :
    codec = Codec(12, 2, MTYPE_INVOKE, "16sBb", "B")
    return perform_request(codec, uuid, uuid_length, is_primary)

# rpc_ble_delete_service(uint8 app_id) -> bool
def delete_service(app_id) :
    codec = Codec(12, 3, MTYPE_INVOKE, "B", "b")
    return perform_request(codec, app_id)

# rpc_ble_service_start(uint8 app_id) -> uint8
def service_start(app_id) :
    codec = Codec(12, 4, MTYPE_INVOKE, "B", "B")
    return perform_request(codec, app_id)

# rpc_ble_get_servie_handle(uint8 app_id) -> uint8
def get_servie_handle(app_id) :
    codec = Codec(12, 5, MTYPE_INVOKE, "B", "B")
    return perform_request(codec, app_id)

# rpc_ble_create_char(uint8 app_id, uint8[16] uuid, uint8 uuid_length, uint8 properties, uint32 permissions) -> uint16
def create_char(app_id, uuid, uuid_length, properties, permissions) :
    codec = Codec(12, 6, MTYPE_INVOKE, "B16sBBI", "H")
    return perform_request(codec, app_id, uuid, uuid_length, properties, permissions)

# rpc_ble_create_desc(uint8 app_id, uint16 char_handle, uint8[16] uuid, uint8 uuid_length, uint8 flags, uint32 permissions, uint16 value_length, in binary p_value @retain @nullable) -> uint16
def create_desc(app_id, char_handle, uuid, uuid_length, flags, permissions, value_length, p_value) :
    codec = Codec(12, 7, MTYPE_INVOKE, "BH16sBBIHb{}", "H")
    return perform_request(codec, app_id, char_handle, uuid, uuid_length, flags, permissions, value_length, p_value)

# rpc_ble_server_get_attr_value(uint8 app_id, uint16 attr_handle) -> @nullable binary
def server_get_attr_value(app_id, attr_handle) :
    codec = Codec(12, 9, MTYPE_INVOKE, "BH", "b{}")
    return perform_request(codec, app_id, attr_handle)

from . import gap
from . import bond
from . import gap_config
from . import adv
from . import scan
from . import flash
from . import client
from . import server

