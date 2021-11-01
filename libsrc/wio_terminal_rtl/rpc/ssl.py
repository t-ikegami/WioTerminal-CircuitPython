from . import MTYPE_INVOKE, perform_request
from ..Codec import Codec
 
# rpc_wifi_ssl_client_create() -> uint32
def client_create() :
    codec = Codec(17, 1, MTYPE_INVOKE, "", "I")
    return perform_request(codec)

# rpc_wifi_ssl_client_destroy(uint32 ssl_client) -> void
def client_destroy(ssl_client) :
    codec = Codec(17, 2, MTYPE_INVOKE, "I", "")
    return perform_request(codec, ssl_client)

# rpc_wifi_ssl_init(uint32 ssl_client) -> void
def init(ssl_client) :
    codec = Codec(17, 3, MTYPE_INVOKE, "I", "")
    return perform_request(codec, ssl_client)

# rpc_wifi_ssl_set_socket(uint32 ssl_client, int32 socket) -> void
def set_socket(ssl_client, socket) :
    codec = Codec(17, 4, MTYPE_INVOKE, "Ii", "")
    return perform_request(codec, ssl_client, socket)

# rpc_wifi_ssl_set_timeout(uint32 ssl_client, uint32 timeout) -> void
def set_timeout(ssl_client, timeout) :
    codec = Codec(17, 5, MTYPE_INVOKE, "II", "")
    return perform_request(codec, ssl_client, timeout)

# rpc_wifi_ssl_get_socket(uint32 ssl_client) -> int32
def get_socket(ssl_client) :
    codec = Codec(17, 6, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, ssl_client)

# rpc_wifi_ssl_get_timeout(uint32 ssl_client) -> uint32
def get_timeout(ssl_client) :
    codec = Codec(17, 7, MTYPE_INVOKE, "I", "I")
    return perform_request(codec, ssl_client)

# rpc_wifi_ssl_set_rootCA(uint32 ssl_client, string rootCABuff @retain) -> uint32
def set_rootCA(ssl_client, rootCABuff) :
    codec = Codec(17, 8, MTYPE_INVOKE, "II{}", "I")
    return perform_request(codec, ssl_client, rootCABuff)

# rpc_wifi_ssl_get_rootCA(uint32 ssl_client, out string rootCABuff @nullable @max_length(3092)) -> uint32
def get_rootCA(ssl_client) :
    # codec = Codec(17, 9, MTYPE_INVOKE, "I", "b{}I")
    codec = Codec(17, 9, MTYPE_INVOKE, "Ix", "I{}I")
    return perform_request(codec, ssl_client)

# rpc_wifi_ssl_set_cliCert(uint32 ssl_client, string cli_cert @retain) ->uint32
def set_cliCert(ssl_client, cli_cert) :
    codec = Codec(17, 10, MTYPE_INVOKE, "II{}", "I")
    return perform_request(codec, ssl_client, cli_cert)

# rpc_wifi_ssl_get_cliCert(uint32 ssl_client, string cli_cert @nullable @max_length(2048)) -> uint32
def get_cliCert(ssl_client, cli_cert) :
    codec = Codec(17, 11, MTYPE_INVOKE, "Ib{}", "I")
    return perform_request(codec, ssl_client, cli_cert)

# rpc_wifi_ssl_set_cliKey(uint32 ssl_client, string cli_key @retain) -> uint32
def set_cliKey(ssl_client, cli_key) :
    codec = Codec(17, 12, MTYPE_INVOKE, "II{}", "I")
    return perform_request(codec, ssl_client, cli_key)

# rpc_wifi_ssl_get_cliKey(uint32 ssl_client, string cli_key @nullable @max_length(2048)) -> uint32
def get_cliKey(ssl_client, cli_key) :
    codec = Codec(17, 13, MTYPE_INVOKE, "Ib{}", "I")
    return perform_request(codec, ssl_client, cli_key)

# rpc_wifi_ssl_set_pskIdent(uint32 ssl_client, string pskIdent @retain) -> uint32
def set_pskIdent(ssl_client, pskIdent) :
    codec = Codec(17, 14, MTYPE_INVOKE, "II{}", "I")
    return perform_request(codec, ssl_client, pskIdent)

# rpc_wifi_ssl_get_pskIdent(uint32 ssl_client, string pskIdent @nullable @max_length(256)) -> uint32
def get_pskIdent(ssl_client, pskIdent) :
    codec = Codec(17, 15, MTYPE_INVOKE, "Ib{}", "I")
    return perform_request(codec, ssl_client, pskIdent)

# rpc_wifi_ssl_set_psKey(uint32 ssl_client, string psKey @retain) -> uint32
def set_psKey(ssl_client, psKey) :
    codec = Codec(17, 16, MTYPE_INVOKE, "II{}", "I")
    return perform_request(codec, ssl_client, psKey)

# rpc_wifi_ssl_get_psKey(uint32 ssl_client, string psKey @nullable @max_length(256)) -> uint32
def get_psKey(ssl_client, psKey) :
    codec = Codec(17, 17, MTYPE_INVOKE, "Ib{}", "I")
    return perform_request(codec, ssl_client, psKey)

# rpc_wifi_start_ssl_client(uint32 ssl_client, string host @nullable, uint32 port, int32 timeout) -> int32
def start_client(ssl_client, host, port, timeout) :
    codec = Codec(17, 18, MTYPE_INVOKE, "Ib{}Ii", "i")
    return perform_request(codec, ssl_client, host, port, timeout)

# rpc_wifi_stop_ssl_socket(uint32 ssl_client) -> void
def stop_socket(ssl_client) :
    codec = Codec(17, 19, MTYPE_INVOKE, "I", "")
    return perform_request(codec, ssl_client)

# rpc_wifi_data_to_read(uint32 ssl_client) -> int32
def data_to_read(ssl_client) :
    codec = Codec(17, 20, MTYPE_INVOKE, "I", "i")
    return perform_request(codec, ssl_client)

# rpc_wifi_send_ssl_data(uint32 ssl_client, in binary data, uint16 len) -> int32
def send_data(ssl_client, data, len) :
    codec = Codec(17, 21, MTYPE_INVOKE, "II{}H", "i")
    return perform_request(codec, ssl_client, data, len)

# rpc_wifi_get_ssl_receive(uint32 ssl_client, out binary data, int32 length) -> int32
def get_receive(ssl_client, length) :
    codec = Codec(17, 22, MTYPE_INVOKE, "Ii", "I{}i")
    return perform_request(codec, ssl_client, length)

# rpc_wifi_verify_ssl_fingerprint(uint32 ssl_client, string fp, string domain_name) -> bool
def verify_fingerprint(ssl_client, fp, domain_name) :
    codec = Codec(17, 23, MTYPE_INVOKE, "II{}I{}", "b")
    return perform_request(codec, ssl_client, fp, domain_name)

# rpc_wifi_verify_ssl_dn(uint32 ssl_client, string domain_name) -> bool
def verify_dn(ssl_client, domain_name) :
    codec = Codec(17, 24, MTYPE_INVOKE, "II{}", "b")
    return perform_request(codec, ssl_client, domain_name)

# rpc_wifi_strerror(int32 errnum, out binary buffer, uint32 buflen) -> void
def strerror(errnum, buflen) :
    codec = Codec(17, 25, MTYPE_INVOKE, "iI", "I{}")
    return perform_request(codec, errnum, buflen)

