from . import MTYPE_INVOKE, perform_request
from ..Codec import Codec

# rpc_mdns_init() -> int32
def init() :
    codec = Codec(18, 1, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_mdns_free() -> int32
def free() :
    codec = Codec(18, 2, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_mdns_service_add(in string instance_name,in string service_type,in string proto,uint16 port) -> int32
def service_add(instance_name, service_type, proto, port) :
    codec = Codec(18, 3, MTYPE_INVOKE, "I{}I{}I{}H", "i")
    return perform_request(codec, instance_name, service_type, proto, port)

# rpc_mdns_service_remove(in string service_type,in string proto) -> int32
def service_remove(service_type, proto) :
    codec = Codec(18, 4, MTYPE_INVOKE, "I{}I{}", "i")
    return perform_request(codec, service_type, proto)

# rpc_mdns_service_txt_item_set(in string service_type,in string proto,in string key,in string value) -> int32
def service_txt_item_set(service_type, proto, key, value) :
    codec = Codec(18, 5, MTYPE_INVOKE, "I{}I{}I{}I{}", "i")
    return perform_request(codec, service_type, proto, key, value)

# rpc_mdns_service_instance_name_set(in string service,in string proto,in string instance) -> int32
def service_instance_name_set(service, proto, instance) :
    codec = Codec(18, 6, MTYPE_INVOKE, "I{}I{}I{}", "i")
    return perform_request(codec, service, proto, instance)

# rpc_mdns_instance_name_set(in string instance_name) -> int32
def instance_name_set(instance_name) :
    codec = Codec(18, 7, MTYPE_INVOKE, "I{}", "i")
    return perform_request(codec, instance_name)

# rpc_mdns_hostname_set(in string hostname) -> int32
def hostname_set(hostname) :
    codec = Codec(18, 8, MTYPE_INVOKE, "I{}", "i")
    return perform_request(codec, hostname)

# rpc_mdns_query_a(in string host_name, uint32 timeout,out binary addr) -> int32
def query_a(host_name, timeout) :
    codec = Codec(18, 9, MTYPE_INVOKE, "I{}I", "I{}i")
    return perform_request(codec, host_name, timeout)

# rpc_mdns_query_ptr(in string service_type,in string proto, uint32 timeout,int32 max_results,out int32 result_total) -> int32
def query_ptr(service_type, proto, timeout, max_results) :
    codec = Codec(18, 10, MTYPE_INVOKE, "I{}I{}Ii", "ii")
    return perform_request(codec, service_type, proto, timeout, max_results)

# rpc_mdns_query_ptr_result_basic(int32 result_target,out binary scan_result) -> int32
def query_ptr_result_basic(result_target) :
    codec = Codec(18, 11, MTYPE_INVOKE, "i", "I{}i")
    return perform_request(codec, result_target)

# rpc_mdns_query_ptr_result_txt(int32 result_target,int32 txt_target,out binary txt) -> int32
def query_ptr_result_txt(result_target, txt_target) :
    codec = Codec(18, 12, MTYPE_INVOKE, "ii", "I{}i")
    return perform_request(codec, result_target, txt_target)

# rpc_mdns_query_ptr_result_addr(int32 result_target,int32 addr_target,out binary addr) -> int32
def query_ptr_result_addr(result_target, addr_target) :
    codec = Codec(18, 13, MTYPE_INVOKE, "ii", "I{}i")
    return perform_request(codec, result_target, addr_target)

# rpc_mdns_query_results_free() -> int32
def query_results_free() :
    codec = Codec(18, 14, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

