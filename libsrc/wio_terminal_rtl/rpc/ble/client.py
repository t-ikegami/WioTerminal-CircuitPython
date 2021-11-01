from .. import MTYPE_INVOKE, perform_request
from ...Codec import Codec

# rpc_client_init(uint8 client_num)->void
def init(client_num) :
    codec = Codec(11, 3, MTYPE_INVOKE, "B", "")
    return perform_request(codec, client_num)

# rpc_client_all_primary_srv_discovery(uint8 conn_id, uint8 client_id) -> RPC_T_GAP_CAUSE
def all_primary_srv_discovery(conn_id, client_id) :
    codec = Codec(11, 4, MTYPE_INVOKE, "BB", "I")
    return perform_request(codec, conn_id, client_id)

# rpc_client_by_uuid_srv_discovery(uint8 conn_id, uint8 client_id, uint16 uuid16) -> RPC_T_GAP_CAUSE
def by_uuid_srv_discovery(conn_id, client_id, uuid16) :
    codec = Codec(11, 5, MTYPE_INVOKE, "BBH", "I")
    return perform_request(codec, conn_id, client_id, uuid16)

# rpc_client_by_uuid128_srv_discovery(uint8 conn_id, uint8 client_id,in uint8[16] p_uuid128) -> RPC_T_GAP_CAUSE
def by_uuid128_srv_discovery(conn_id, client_id, p_uuid128) :
    codec = Codec(11, 6, MTYPE_INVOKE, "BB16s", "I")
    return perform_request(codec, conn_id, client_id, p_uuid128)

# rpc_client_relationship_discovery(uint8 conn_id, uint8 client_id,uint16 start_handle, uint16 end_handle) -> RPC_T_GAP_CAUSE
def relationship_discovery(conn_id, client_id, start_handle, end_handle) :
    codec = Codec(11, 7, MTYPE_INVOKE, "BBHH", "I")
    return perform_request(codec, conn_id, client_id, start_handle, end_handle)

# rpc_client_all_char_discovery(uint8 conn_id, uint8 client_id, uint16 start_handle, uint16 end_handle) -> RPC_T_GAP_CAUSE
def all_char_discovery(conn_id, client_id, start_handle, end_handle) :
    codec = Codec(11, 8, MTYPE_INVOKE, "BBHH", "I")
    return perform_request(codec, conn_id, client_id, start_handle, end_handle)

# rpc_client_by_uuid_char_discovery(uint8 conn_id, uint8 client_id, uint16 start_handle,uint16 end_handle, uint16 uuid16) -> RPC_T_GAP_CAUSE
def by_uuid_char_discovery(conn_id, client_id, start_handle, end_handle, uuid16) :
    codec = Codec(11, 9, MTYPE_INVOKE, "BBHHH", "I")
    return perform_request(codec, conn_id, client_id, start_handle, end_handle, uuid16)

# rpc_client_by_uuid128_char_discovery(uint8 conn_id, uint8 client_id, uint16 start_handle, uint16 end_handle, uint8[16] p_uuid128) -> RPC_T_GAP_CAUSE
def by_uuid128_char_discovery(conn_id, client_id, start_handle, end_handle, p_uuid128) :
    codec = Codec(11, 10, MTYPE_INVOKE, "BBHH16s", "I")
    return perform_request(codec, conn_id, client_id, start_handle, end_handle, p_uuid128)

# rpc_client_all_char_descriptor_discovery(uint8 conn_id, uint8 client_id, uint16 start_handle, uint16 end_handle) -> RPC_T_GAP_CAUSE
def all_char_descriptor_discovery(conn_id, client_id, start_handle, end_handle) :
    codec = Codec(11, 11, MTYPE_INVOKE, "BBHH", "I")
    return perform_request(codec, conn_id, client_id, start_handle, end_handle)

# rpc_client_attr_read(uint8 conn_id, uint8 client_id, uint16 handle) -> RPC_T_GAP_CAUSE
def attr_read(conn_id, client_id, handle) :
    codec = Codec(11, 12, MTYPE_INVOKE, "BBH", "I")
    return perform_request(codec, conn_id, client_id, handle)

# rpc_client_attr_read_using_uuid(uint8 conn_id, uint8 client_id, uint16 start_handle, uint16 end_handle, uint16 uuid16, uint8[16] p_uuid128) -> RPC_T_GAP_CAUSE
def attr_read_using_uuid(conn_id, client_id, start_handle, end_handle, uuid16, p_uuid128) :
    codec = Codec(11, 13, MTYPE_INVOKE, "BBHHH16s", "I")
    return perform_request(codec, conn_id, client_id, start_handle, end_handle, uuid16, p_uuid128)

# rpc_client_attr_write(uint8 conn_id, uint8 client_id, RPC_T_GATT_WRITE_TYPE write_type, uint16 handle, in binary data) -> RPC_T_GAP_CAUSE
def attr_write(conn_id, client_id, write_type, handle, data) :
    codec = Codec(11, 14, MTYPE_INVOKE, "BBIHI{}", "I")
    return perform_request(codec, conn_id, client_id, write_type, handle, data)

# rpc_client_attr_ind_confirm(uint8 conn_id) -> RPC_T_GAP_CAUSE
def attr_ind_confirm(conn_id) :
    codec = Codec(11, 15, MTYPE_INVOKE, "B", "I")
    return perform_request(codec, conn_id)


