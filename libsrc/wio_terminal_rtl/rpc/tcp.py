from . import MTYPE_INVOKE, perform_request
from ..Codec import Codec

# rpc_tcp_connect(in binary pcb_in, out binary pcb_out,in binary ipaddr,uint16 port,in binary connected) -> int32
def connect(pcb_in, ipaddr, port, connected) :
    codec = Codec(15, 20, MTYPE_INVOKE, "I{}I{}HI{}", "I{}i")
    return perform_request(codec, pcb_in, ipaddr, port, connected)

# rpc_tcp_recved(in binary pcb_in, out binary pcb_out,uint16 len) -> int32
def recved(pcb_in, len) :
    codec = Codec(15, 21, MTYPE_INVOKE, "I{}H", "I{}i")
    return perform_request(codec, pcb_in, len)

# rpc_tcp_abort(in binary pcb_in, out binary pcb_out) -> int32
def abort(pcb_in) :
    codec = Codec(15, 22, MTYPE_INVOKE, "I{}", "I{}i")
    return perform_request(codec, pcb_in)

# rpc_tcp_write(in binary pcb_in, out binary pcb_out,in binary data,uint8 apiflags) -> int32
def write(pcb_in, data, apiflags) :
    codec = Codec(15, 23, MTYPE_INVOKE, "I{}I{}B", "I{}i")
    return perform_request(codec, pcb_in, data, apiflags)

# rpc_tcp_output(in binary pcb_in, out binary pcb_out) -> int32
def output(pcb_in) :
    codec = Codec(15, 24, MTYPE_INVOKE, "I{}", "I{}i")
    return perform_request(codec, pcb_in)

# rpc_tcp_close(in binary pcb_in, out binary pcb_out) -> int32
def close(pcb_in) :
    codec = Codec(15, 25, MTYPE_INVOKE, "I{}", "I{}i")
    return perform_request(codec, pcb_in)

# rpc_tcp_bind(in binary pcb_in, out binary pcb_out,in binary ipaddr,uint16 port) -> int32
def bind(pcb_in, ipaddr, port) :
    codec = Codec(15, 26, MTYPE_INVOKE, "I{}I{}H", "I{}i")
    return perform_request(codec, pcb_in, ipaddr, port)

# rpc_tcp_new_ip_type(uint8 ip_type, out binary pcb_out) -> int32
def new_ip_type(ip_type) :
    codec = Codec(15, 27, MTYPE_INVOKE, "B", "I{}i")
    return perform_request(codec, ip_type)

# rpc_tcp_arg(in binary pcb_in, out binary pcb_out,in binary func_arg) -> int32
def arg(pcb_in, func_arg) :
    codec = Codec(15, 28, MTYPE_INVOKE, "I{}I{}", "I{}i")
    return perform_request(codec, pcb_in, func_arg)

# rpc_tcp_err(in binary pcb_in, out binary pcb_out,in binary func_err) -> int32
def err(pcb_in, func_err) :
    codec = Codec(15, 29, MTYPE_INVOKE, "I{}I{}", "I{}i")
    return perform_request(codec, pcb_in, func_err)

# rpc_tcp_recv(in binary pcb_in, out binary pcb_out,in binary func_recv) -> int32
def recv(pcb_in, func_recv) :
    codec = Codec(15, 30, MTYPE_INVOKE, "I{}I{}", "I{}i")
    return perform_request(codec, pcb_in, func_recv)

# rpc_tcp_sent(in binary pcb_in, out binary pcb_out,in binary func_sent) -> int32
def sent(pcb_in, func_sent) :
    codec = Codec(15, 31, MTYPE_INVOKE, "I{}I{}", "I{}i")
    return perform_request(codec, pcb_in, func_sent)

# rpc_tcp_accept(in binary pcb_in, out binary pcb_out,in binary func_accept) -> int32
def accept(pcb_in, func_accept) :
    codec = Codec(15, 32, MTYPE_INVOKE, "I{}I{}", "I{}i")
    return perform_request(codec, pcb_in, func_accept)

# rpc_tcp_poll(in binary pcb_in, out binary pcb_out,in binary func_poll,uint8 interval) -> int32
def poll(pcb_in, func_poll, interval) :
    codec = Codec(15, 33, MTYPE_INVOKE, "I{}I{}B", "I{}i")
    return perform_request(codec, pcb_in, func_poll, interval)

# rpc_tcp_listen_with_backlog(in binary pcb_in, out binary pcb_out,uint8 backlog) -> int32
def listen_with_backlog(pcb_in, backlog) :
    codec = Codec(15, 34, MTYPE_INVOKE, "I{}B", "I{}i")
    return perform_request(codec, pcb_in, backlog)

# rpc_pbuf_free(in binary p) -> int32
def pbuf_free(p) :
    codec = Codec(15, 35, MTYPE_INVOKE, "I{}", "i")
    return perform_request(codec, p)

# rpc_ip4addr_ntoa(in binary ip4_addr_in)-> string
def ip4addr_ntoa(ip4_addr_in) :
    codec = Codec(15, 36, MTYPE_INVOKE, "I{}", "I{}")
    return perform_request(codec, ip4_addr_in)

# rpc_inet_chksum(in binary dataptr_in) -> uint16
def inet_chksum(dataptr_in) :
    codec = Codec(15, 37, MTYPE_INVOKE, "I{}", "H")
    return perform_request(codec, dataptr_in)

