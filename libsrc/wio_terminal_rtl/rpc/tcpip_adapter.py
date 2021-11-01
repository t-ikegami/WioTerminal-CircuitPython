from . import MTYPE_INVOKE, perform_request
from ..Codec import Codec

# rpc_tcpip_adapter_init() -> int32
def init() :
    codec = Codec(15, 1, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_tcpip_adapter_sta_start(in binary mac, in binary ip_info) -> int32
def sta_start(mac, ip_info) :
    codec = Codec(15, 2, MTYPE_INVOKE, "I{}I{}", "i")
    return perform_request(codec, mac, ip_info)

# rpc_tcpip_adapter_ap_start(in binary mac, in binary ip_info) -> int32
def ap_start(mac, ip_info) :
    codec = Codec(15, 3, MTYPE_INVOKE, "I{}I{}", "i")
    return perform_request(codec, mac, ip_info)

# rpc_tcpip_adapter_stop(uint32 tcpip_if) -> int32
def stop(tcpip_if) :
    codec = Codec(15, 4, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, tcpip_if)

# rpc_tcpip_adapter_up(uint32 tcpip_if) -> int32
def up(tcpip_if) :
    codec = Codec(15, 5, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, tcpip_if)

# rpc_tcpip_adapter_down(uint32 tcpip_if) -> int32
def down(tcpip_if) :
    codec = Codec(15, 6, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, tcpip_if)

# rpc_tcpip_adapter_get_ip_info(uint32 tcpip_if, out binary ip_info) -> int32
def get_ip_info(tcpip_if) :
    codec = Codec(15, 7, MTYPE_INVOKE, "I", "I{}i")
    return perform_request(codec, tcpip_if)

# rpc_tcpip_adapter_set_ip_info(uint32 tcpip_if, in binary ip_info) -> int32
def set_ip_info(tcpip_if, ip_info) :
    codec = Codec(15, 8, MTYPE_INVOKE, "II{}", "i")
    return perform_request(codec, tcpip_if, ip_info)

# rpc_tcpip_adapter_set_dns_info(uint32 tcpip_if, uint32 dns_type, in binary dns) -> int32
def set_dns_info(tcpip_if, dns_type, dns) :
    codec = Codec(15, 9, MTYPE_INVOKE, "III{}", "i")
    return perform_request(codec, tcpip_if, dns_type, dns)

# rpc_tcpip_adapter_get_dns_info(uint32 tcpip_if, uint32 dns_type, out binary dns) -> int32
def get_dns_info(tcpip_if, dns_type) :
    codec = Codec(15, 10, MTYPE_INVOKE, "II", "I{}i")
    return perform_request(codec, tcpip_if, dns_type)

# rpc_tcpip_adapter_dhcps_start(uint32 tcpip_if) -> int32
def dhcps_start(tcpip_if) :
    codec = Codec(15, 11, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, tcpip_if)

# rpc_tcpip_adapter_dhcps_stop(uint32 tcpip_if) -> int32
def dhcps_stop(tcpip_if) :
    codec = Codec(15, 12, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, tcpip_if)

# rpc_tcpip_adapter_dhcpc_start(uint32 tcpip_if) -> int32
def dhcpc_start(tcpip_if) :
    codec = Codec(15, 13, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, tcpip_if)

# rpc_tcpip_adapter_dhcpc_stop(uint32 tcpip_if) -> int32
def dhcpc_stop(tcpip_if) :
    codec = Codec(15, 14, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, tcpip_if)

# rpc_tcpip_adapter_set_hostname(uint32 tcpip_if, in string hostname) -> int32
def set_hostname(tcpip_if, hostname) :
    codec = Codec(15, 15, MTYPE_INVOKE, "II{}", "i")
    return perform_request(codec, tcpip_if, hostname)

# rpc_tcpip_adapter_get_hostname(uint32 tcpip_if, out string hostname @max_length(32)) -> int32
def get_hostname(tcpip_if) :
    codec = Codec(15, 16, MTYPE_INVOKE, "I", "I{}i")
    return perform_request(codec, tcpip_if)

# rpc_tcpip_adapter_get_mac(uint32 tcpip_if, out binary mac) -> int32
def get_mac(tcpip_if) :
    codec = Codec(15, 17, MTYPE_INVOKE, "I", "I{}i")
    return perform_request(codec, tcpip_if)

# rpc_tcpip_adapter_set_mac(uint32 tcpip_if, in binary mac) -> int32
def set_mac(tcpip_if, mac) :
    codec = Codec(15, 18, MTYPE_INVOKE, "II{}", "i")
    return perform_request(codec, tcpip_if, mac)

# rpc_tcpip_api_call(in binary func,in binary call) -> int32
def rpc_tcpip_api_call(func, call) :
    codec = Codec(15, 19, MTYPE_INVOKE, "I{}I{}", "i")
    return perform_request(codec, func, call)

