from micropython import const
import time
import struct
from .rpc import lwip
from .rpc import constants as C
from .rpc.struct_wifi import Struct

_KEEPALIVE_TIMEOUT_NS = const(500_000_000)
_MAX_WRITE_RETRY      = const(10)
_SELECT_TIMEOUT_US    = const(1_000_000)

class WiFiClient :
    fdset = Struct("fd_set")
    tv    = Struct("timeval")
    tv.tv_sec  = 0
    tv.tv_usec = _SELECT_TIMEOUT_US
    
    def __init__(self, fd = None) :
        self.fd = fd
        self.conn_staus = 0
        self.rxbuf = None
        if fd is not None : self.fdset.set = 1 << fd
        
    def __del__(self) :
        self.stop()

    def connect(self, ip, port, timeout = None) :
        if isinstance(ip, str) : ip = lwip.getipbyname(ip)
        fd = lwip.socket(C.AF_INET, C.SOCK_STREAM, 0)
        if fd < 0 : raise RuntimeError("Could not create socket.")
        self.fdset.set = 1 << fd
        lwip.fcntl(fd, C.F_SETFL, lwip.fcntl(fd, C.F_GETFL, 0) | C.O_NONBLOCK)
        
        serveraddr = Struct("sockaddr_in")
        serveraddr.sin_family = C.AF_INET
        serveraddr.sin_addr = ip
        serveraddr.sin_port = lwip.htons(port)

        if timeout is not None :
            tv = Struct("timeval")
            tv.tv_sec = 0
            tv.tv_usec = timeout * 1000
            timeout = tv._data

        res = lwip.connect(fd, serveraddr._data, len(serveraddr._data))
        if res < 0  and  lwip.errno() != C.EINPROGRESS :
            lwip.close(fd)
            raise RuntimeError("Could not connect to socket.")

        res = lwip.select(fd + 1, None, self.fdset._data, None, timeout)
        if res < 0 :
            lwip.close(fd)
            raise RuntimeError("Could not select socket.")
        elif res == 0 :
            lwip.close(fd)
            raise RuntimeError("Select returned due to timeout.")

        sockerr = struct.pack("<i", 0)
        (sockerr, _, res) = lwip.getsockopt(fd, C.SOL_SOCKET, C.SO_ERROR, sockerr, 4)
        if res < 0 :
            lwip.close(fd)
            raise RuntimeError("Could not getsockopt.")
        sockerr = struct.unpack("<i", sockerr)[0]
        if sockerr != 0 :
            lwip.close(fd)
            raise RuntimeError("Socket error:" + str(sockerr))

        lwip.fcntl(fd, C.F_SETFL, lwip.fcntl(fd, C.F_GETFL, 0) & (~C.O_NONBLOCK))

        self.fd = fd
        self.conn_staus = time.monotonic_ns()

        return 1

    def write(self, data) :
        if self.fd is None : return 0
        
        if isinstance(data, int) :
            mv = memoryview(bytex([data]))
        else :
            mv = memoryview(data)

        totalBytesSent = 0
        retry = _MAX_WRITE_RETRY
        while len(mv) > 0 :
            retry -= 1
            if retry <= 0 : break
            
            # check if socket is ready for writing
            if lwip.select(self.fd + 1, None, self.fdset._data, None, self.tv._data) < 0 : return 0

            # eRPC lwip_select does not update fdset; the following check code is meaningless.
            # if not (fdset.set & (1 << self.fd)) : continue

            res = lwip.send(self.fd, mv, C.MSG_DONTWAIT)
            if res > 0 :
                totalBytesSent += res
                mv = mv[res:]
                retry = _MAX_WRITE_RETRY
            elif res < 0  and  lwip.errno() != C.EAGAIN :
                self.stop()
                raise RuntimeError("Could not send to socket.")
            
        return totalBytesSent

    def _available(self) :
        if self.fd is None : return False
        return lwip.available(self.fd) > 0

    def _read(self, max = 1024) :
        if not self._available() : return None
        (buf, res) = lwip.recv(self.fd, max, C.MSG_DONTWAIT, 10 * max)
        if res < 0 :
            self.stop()
            raise RuntimeError("Could not recv.")
        if res == 0 : return None
        return buf

    def _peek(self) :
        if self.fd is None : return -1
        (buf, res) = lwip.recv(self.fd, 1, C.MSG_PEEK, 10)
        if res < 0 :
            self.stop()
            raise RuntimeError("Could not recv.")
        if res == 0 : return -1
        return buf[0]

    def available(self) :
        if self.rxbuf is None : self.rxbuf = self._read()
        return self.rxbuf is not None
    
    def peak(self) :
        if self.rxbuf is None : self.rxbuf = self._read()
        if self.rxbuf is None : return -1
        return self.rxbuf[0]
        
    def read(self) :
        ret = [ b"" ] if self.rxbuf is None else [ self.rxbuf ]
        self.rxbuf = None
        while True :
            buf = self._read()
            if buf is None : break
            ret.append(buf)
        return b"".join(ret)

    def read_until(self, sep) :
        if self.rxbuf is None : self.rxbuf = self._read()
        if self.rxbuf is None : return b""
        while True :
            idx = self.rxbuf.find(sep)
            if idx >= 0 : break
            buf = self._read()
            if buf is None :
                ret = self.rxbuf
                self.rxbuf = None
                return ret
            self.rxbuf += buf
        idx += len(sep)
        ret = self.rxbuf[:idx]
        self.rxbuf = self.rxbuf[idx:]
        if len(self.rxbuf) == 0 : self.rxbuf = None
        return ret
    
    def flush(self) :
        self.rxbuf = None
        while True :
            if self._read() is None : break

    def stop(self) :
        if self.fd is None : return
        lwip.close(self.fd)
        self.fd = None

    def connected(self) :
        if self.fd is None : return False
        interval = time.monotonic_ns() - self.conn_staus
        if interval < _KEEPALIVE_TIMEOUT_NS : return True

        lwip.recv(self.fd, 0, C.MSG_DONTWAIT, 0)
        errno = lwip.errno()
        if errno in (C.EWOULDBLOCK, C.ENOENT) :
            self.conn_staus = time.monotonic_ns()
        elif errno in (C.ENOTCONN, C.EPIPE, C.ECONNRESET, C.ECONNREFUSED, C.ECONNABORTED) :
            self.stop()
        else :
            print(f"### unexpected error: {errno}")
            self.conn_staus = time.monotonic_ns()

        return self.fd is not None

    def setSocketOption(self, option, buf) :
        return lwip.setsockopt(self.fd, C.SOL_SOCKET, option, buf, len(buf))
    
    def setOption(self, option, value) :
        buf = struct.pack("<i", value)
        return lwip.setsockopt(self.fd, C.IPPROTO_TCP, option, buf, 4)
    
    def getOption(self, option) :
        value = struct.pack("<i", 0)
        (value, _, res) = lwip.getsockopt(self.fd, C.IPPROTO_TCP, option, value, 4)
        value = struct.unpack("<i", value)[0]
        return (value, res)
    
    def setTimeout(self, seconds) :
        tv = Struct("timeval")
        tv.tv_sec = seconds
        tv.tv_usec = 0
        if self.setSocketOption(C.SO_RCVTIMEO, tv._data) < 0 : return -1
        return self.setSocketOption(C.SO_SNDTIMEO, tv._data)
    
    def setNoDelay(self, nodelay) :
        return self.setOption(C.TCP_NODELAY, nodelay)
    
    def getNoDelay(self) :
        return self.getOption(C.TCP_NODLEAY)[0]
    
    def remoteIP(self, fd = None) :
        if fd is None : fd = self.fd
        sz = Struct.get_info("sockaddr_in")[0][0]
        (buf, sz, res) = lwip.getpeername(fd, sz)
        addr = Struct("sockaddr_in", buf)
        return addr.sin_addr

    def remotePort(self, fd = None) :
        if fd is None : fd = self.fd
        sz = Struct.get_info("sockaddr_in")[0][0]
        (buf, sz, res) = lwip.getpeername(fd, sz)
        addr = Struct("sockaddr_in", buf)
        return lwip.ntohs(addr.sin_port)

    def localIP(self, fd = None) :
        if fd is None : fd = self.fd
        sz = Struct.get_info("sockaddr_in")[0][0]
        (buf, sz, res) = lwip.getsockname(fd, sz)
        addr = Struct("sockaddr_in", buf)
        return addr.sin_addr

    def localPort(self, fd = None) :
        if fd is None : fd = self.fd
        sz = Struct.get_info("sockaddr_in")[0][0]
        (buf, sz, res) = lwip.getsockname(fd, sz)
        addr = Struct("sockaddr_in", buf)
        return lwip.ntohs(addr.sin_port)
    
