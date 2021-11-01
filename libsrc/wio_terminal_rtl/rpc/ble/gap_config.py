from .. import MTYPE_INVOKE, perform_request
from ...Codec import Codec

# rpc_gap_config_cccd_not_check(RPC_T_GAP_CONFIG_GATT_CCCD_NOT_CHECK cccd_not_check_flag) -> void
def cccd_not_check(cccd_not_check_flag) :
    codec = Codec(6, 1, MTYPE_INVOKE, "I", "")
    return perform_request(codec, cccd_not_check_flag)

# rpc_gap_config_ccc_bits_count(uint8 gatt_server_ccc_bits_count, uint8 gatt_storage_ccc_bits_count) -> void
def ccc_bits_count(gatt_server_ccc_bits_count, gatt_storage_ccc_bits_count) :
    codec = Codec(6, 2, MTYPE_INVOKE, "BB", "")
    return perform_request(codec, gatt_server_ccc_bits_count, gatt_storage_ccc_bits_count)

# rpc_gap_config_max_attribute_table_count(uint8 gatt_max_attribute_table_count) -> void
def max_attribute_table_count(gatt_max_attribute_table_count) :
    codec = Codec(6, 3, MTYPE_INVOKE, "B", "")
    return perform_request(codec, gatt_max_attribute_table_count)

# rpc_gap_config_max_mtu_size(uint16 att_max_mtu_size) -> void
def max_mtu_size(att_max_mtu_size) :
    codec = Codec(6, 4, MTYPE_INVOKE, "H", "")
    return perform_request(codec, att_max_mtu_size)

# rpc_gap_config_bte_pool_size(uint8 bte_pool_size) -> void
def bte_pool_size(bte_pool_size) :
    codec = Codec(6, 5, MTYPE_INVOKE, "B", "")
    return perform_request(codec, bte_pool_size)

# rpc_gap_config_bt_report_buf_num(uint8 bt_report_buf_num) -> void
def bt_report_buf_num(bt_report_buf_num) :
    codec = Codec(6, 6, MTYPE_INVOKE, "B", "")
    return perform_request(codec, bt_report_buf_num)

# rpc_gap_config_le_key_storage_flag(uint16 le_key_storage_flag) -> void
def le_key_storage_flag(le_key_storage_flag) :
    codec = Codec(6, 7, MTYPE_INVOKE, "H", "")
    return perform_request(codec, le_key_storage_flag)

# rpc_gap_config_max_le_paired_device(uint8 max_le_paired_device) -> void
def max_le_paired_device(max_le_paired_device) :
    codec = Codec(6, 8, MTYPE_INVOKE, "B", "")
    return perform_request(codec, max_le_paired_device)

# rpc_gap_config_max_le_link_num(uint8 le_link_num) -> void
def max_le_link_num(le_link_num) :
    codec = Codec(6, 9, MTYPE_INVOKE, "B", "")
    return perform_request(codec, le_link_num)

