from . import MTYPE_INVOKE, perform_request
from ..Codec import Codec

# rpc_lwip_accept(int32 s, in binary addr, inout uint32 addrlen) -> int32
def accept(s, addr, addrlen) :
    codec = Codec(16, 1, MTYPE_INVOKE, "iI{}I", "Ii")
    return perform_request(codec, s, addr, addrlen)

# rpc_lwip_bind(int32 s, in binary name, uint32 namelen) -> int32
def bind(s, name, namelen) :
    codec = Codec(16, 2, MTYPE_INVOKE, "iI{}I", "i")
    return perform_request(codec, s, name, namelen)

# rpc_lwip_shutdown(int32 s, int32 how) -> int32
def shutdown(s, how) :
    codec = Codec(16, 3, MTYPE_INVOKE, "ii", "i")
    return perform_request(codec, s, how)

# rpc_lwip_getpeername (int32 s, out binary name, inout uint32 namelen) -> int32
def getpeername(s, namelen) :
    codec = Codec(16, 4, MTYPE_INVOKE, "iI", "I{}Ii")
    return perform_request(codec, s, namelen)

# rpc_lwip_getsockname (int32 s, out binary name, inout uint32 namelen) -> int32
def getsockname(s, namelen) :
    codec = Codec(16, 5, MTYPE_INVOKE, "iI", "I{}Ii")
    return perform_request(codec, s, namelen)

# rpc_lwip_getsockopt (int32 s, int32 level, int32 optname, in binary in_optval, out binary out_optval, inout uint32 optlen) -> int32
def getsockopt(s, level, optname, in_optval, optlen) :
    codec = Codec(16, 6, MTYPE_INVOKE, "iiiI{}I", "I{}Ii")
    return perform_request(codec, s, level, optname, in_optval, optlen)

# rpc_lwip_setsockopt (int32 s, int32 level, int32 optname, in binary optval, uint32 optlen) -> int32
def setsockopt(s, level, optname, optval, optlen) :
    codec = Codec(16, 7, MTYPE_INVOKE, "iiiI{}I", "i")
    return perform_request(codec, s, level, optname, optval, optlen)

# rpc_lwip_close(int32 s) -> int32
def close(s) :
    codec = Codec(16, 8, MTYPE_INVOKE, "i", "i")
    return perform_request(codec, s)

# rpc_lwip_connect(int32 s, in binary name, uint32 namelen) -> int32
def connect(s, name, namelen) :
    codec = Codec(16, 9, MTYPE_INVOKE, "iI{}I", "i")
    return perform_request(codec, s, name, namelen)

# rpc_lwip_listen(int32 s, int32 backlog) -> int32
def listen(s, backlog) :
    codec = Codec(16, 10, MTYPE_INVOKE, "ii", "i")
    return perform_request(codec, s, backlog)

# rpc_lwip_available(int32 s) -> int32
def available(s) :
    codec = Codec(16, 11, MTYPE_INVOKE, "i", "i")
    return perform_request(codec, s)

# rpc_lwip_recv(int32 s, out binary mem, uint32 len, int32 flags, uint32 timeout) -> int32
def recv(s, len, flags, timeout) :
    codec = Codec(16, 12, MTYPE_INVOKE, "iIiI", "I{}i")
    return perform_request(codec, s, len, flags, timeout)

# rpc_lwip_read(int32 s, out binary mem, uint32 len, uint32 timeout) -> int32
def read(s, len, timeout) :
    codec = Codec(16, 13, MTYPE_INVOKE, "iII", "I{}i")
    return perform_request(codec, s, len, timeout)

# rpc_lwip_recvfrom(int32 s, out binary mem, uint32 len, int32 flags, out binary from, inout uint32 fromlen, uint32 timeout) -> int32
def recvfrom(s, len, flags, fromlen, timeout) :
    codec = Codec(16, 14, MTYPE_INVOKE, "iIiII", "I{}I{}Ii")
    return perform_request(codec, s, len, flags, fromlen, timeout)

# rpc_lwip_send(int32 s, in binary dataptr, int32 flags) -> int32
def send(s, dataptr, flags) :
    codec = Codec(16, 15, MTYPE_INVOKE, "iI{}i", "i")
    return perform_request(codec, s, dataptr, flags)

# rpc_lwip_sendmsg(int32 s, in binary msg_name, in binary msg_iov, in binary msg_control, int32 msg_flags, int32 flags) -> int32
def sendmsg(s, msg_name, msg_iov, msg_control, msg_flags, flags) :
    codec = Codec(16, 16, MTYPE_INVOKE, "iI{}I{}I{}ii", "i")
    return perform_request(codec, s, msg_name, msg_iov, msg_control, msg_flags, flags)

# rpc_lwip_sendto(int32 s, in binary dataptr, int32 flags, in binary to, uint32 tolen) -> int32
def sendto(s, dataptr, flags, to, tolen) :
    codec = Codec(16, 17, MTYPE_INVOKE, "iI{}iI{}I", "i")
    return perform_request(codec, s, dataptr, flags, to, tolen)

# rpc_lwip_socket(int32 domain, int32 l_type, int32 protocol) -> int32
def socket(domain, l_type, protocol) :
    codec = Codec(16, 18, MTYPE_INVOKE, "iii", "i")
    return perform_request(codec, domain, l_type, protocol)

# rpc_lwip_write(int32 s, in binary dataptr, uint32 size) -> int32
def write(s, dataptr, size) :
    codec = Codec(16, 19, MTYPE_INVOKE, "iI{}I", "i")
    return perform_request(codec, s, dataptr, size)

# rpc_lwip_writev(int32 s, in binary iov, int32 iovcnt) -> int32
def writev(s, iov, iovcnt) :
    codec = Codec(16, 20, MTYPE_INVOKE, "iI{}i", "i")
    return perform_request(codec, s, iov, iovcnt)

# rpc_lwip_select(int32 maxfdp1, in binary readset @nullable, in binary writeset @nullable, in binary exceptset @nullable, in binary timeout @nullable) -> int32
def select(maxfdp1, readset, writeset, exceptset, timeout) :
    codec = Codec(16, 21, MTYPE_INVOKE, "ib{}b{}b{}b{}", "i")
    return perform_request(codec, maxfdp1, readset, writeset, exceptset, timeout)

# rpc_lwip_ioctl(int32 s, uint32 cmd, in binary in_argp, out binary out_argp) -> int32
def ioctl(s, cmd, in_argp) :
    codec = Codec(16, 22, MTYPE_INVOKE, "iII{}", "I{}i")
    return perform_request(codec, s, cmd, in_argp)

# rpc_lwip_fcntl(int32 s, int32 cmd, int32 val) -> int32
def fcntl(s, cmd, val) :
    codec = Codec(16, 23, MTYPE_INVOKE, "iii", "i")
    return perform_request(codec, s, cmd, val)

# rpc_lwip_errno() -> int32
def errno() :
    codec = Codec(16, 24, MTYPE_INVOKE, "", "i")
    return perform_request(codec)

# rpc_netconn_gethostbyname(string name, out binary addr) -> int8
def netconn_gethostbyname(name) :
    codec = Codec(16, 25, MTYPE_INVOKE, "I{}", "I{}b")
    return perform_request(codec, name)

# rpc_dns_gethostbyname_addrtype(string hostname @retain, out binary addr @retain, uint32 found, in binary callback_arg @nullable @retain, uint8 dns_addrtype) -> int8
def dns_gethostbyname_addrtype(hostname, found, callback_arg, dns_addrtype) :
    codec = Codec(16, 26, MTYPE_INVOKE, "I{}Ib{}B", "I{}b")
    return perform_request(codec, hostname, found, callback_arg, dns_addrtype)

#------------------------------------------------------------------------
import struct

def htons(x) :
    return ((x & 0xFF00) >> 8) | ((x & 0x00FF) << 8)

ntohs = htons

def getipbyname(x) :
    # return (x, y, z, w) tuple, not hostent.
    (addr, ret) = netconn_gethostbyname(x)
    if ret != 0 : return None
    return struct.unpack("<4B", addr)


    

