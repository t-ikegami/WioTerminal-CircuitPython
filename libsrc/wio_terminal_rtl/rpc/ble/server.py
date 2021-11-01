from .. import MTYPE_INVOKE, perform_request
from ...Codec import Codec

# rpc_server_send_data(uint8 conn_id, uint8 service_id, uint16 attrib_index, in binary data, RPC_T_GATT_PDU_TYPE pdu_type) -> bool
def send_data(conn_id, service_id, attrib_index, data, pdu_type) :
    codec = Codec(12, 8, MTYPE_INVOKE, "BBHI{}I", "b")
    return perform_request(codec, conn_id, service_id, attrib_index, data, pdu_type)

# rpc_server_exec_write_confirm(uint8 conn_id, uint16 cause, uint16 handle) -> bool
def exec_write_confirm(conn_id, cause, handle) :
    codec = Codec(12, 10, MTYPE_INVOKE, "BHH", "b")
    return perform_request(codec, conn_id, cause, handle)

# rpc_server_attr_write_confirm(uint8 conn_id, uint8 service_id, uint16 attrib_index, RPC_T_APP_RESULT cause) -> bool
def attr_write_confirm(conn_id, service_id, attrib_index, cause) :
    codec = Codec(12, 11, MTYPE_INVOKE, "BBHI", "b")
    return perform_request(codec, conn_id, service_id, attrib_index, cause)

# rpc_server_attr_read_confirm(uint8 conn_id, uint8 service_id, uint16 attrib_index, in binary data, RPC_T_APP_RESULT cause) -> bool
def attr_read_confirm(conn_id, service_id, attrib_index, data, cause) :
    codec = Codec(12, 12, MTYPE_INVOKE, "BBHI{}I", "b")
    return perform_request(codec, conn_id, service_id, attrib_index, data, cause)

