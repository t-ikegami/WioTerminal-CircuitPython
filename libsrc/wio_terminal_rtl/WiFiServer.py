import struct
from .rpc import lwip
from .rpc import constants as C
from .rpc.struct_wifi import Struct
from .WiFiClient import WiFiClient

class WiFiServer :
    
    def __init__(self, port = 80, max_clients = 4) :
        self.fd          = None
        self.accepted_fd = None
        self.port        = port
        self.max_clients = max_clients
        self.noDelay     = False
        
    def __del__(self) :
        self.end()

    def begin(self, port = None) :
        if self.fd is not None : return
        if port is not None : self.port = port
        
        fd = lwip.socket(C.AF_INET, C.SOCK_STREAM, 0)
        if fd < 0 : raise RuntimeError("Could not create socket.")

        server = Struct("sockaddr_in")
        server.sin_family = C.AF_INET
        server.sin_addr = C.INADDR_ANY
        server.sin_port = lwip.htons(self.port)
        if lwip.bind(fd, server._data, len(server._data)) < 0 :
            lwip.close(fd)
            raise RuntimeError("Could not bind socket.")
        if lwip.listen(fd, self.max_clients) < 0 :
            lwip.close(fd)
            raise RuntimeError("Could not listen socket.")
        lwip.fcntl(fd, C.F_SETFL, C.O_NONBLOCK)

        self.fd = fd
        self.noDelay = False
        self.accepted_fd = None

    def end(self) :
        if self.accepted_fd is not None :
            lwip.close(self.accepted_fd)
            self.accepted_fd = None
        if self.fd is not None :
            lwip.close(self.fd)
            self.fd = None

    close = end
    stop  = end

    def hasClient(self) :
        if self.fd is None : return False
        if self.accepted_fd is not None : return True
        # lwip_accept of eRPC 2.1.3 is defined wrongly such that sockaddr_in is intent in
        client = Struct("sockaddr_in")
        (sz, res) = lwip.accept(self.fd, client._data, len(client._data))
        if res < 0 : return False
        self.accepted_fd = res
        return True
        
    def available(self) :
        if not self.hasClient() : return None
        
        client_fd = self.accepted_fd
        self.accepted_fd = None
        buf = struct.pack("<i", 1)
        if lwip.setsockopt(client_fd, C.SOL_SOCKET, C.SO_KEEPALIVE, buf, 4) < 0 :
            lwip.close(client_fd)
            raise RuntimeError("Could not setsockopt on client fd.")
        buf = struct.pack("<i", self.noDelay)
        if lwip.setsockopt(client_fd, C.IPPROTO_TCP, C.TCP_NODELAY, buf, 4) < 0 :
            lwip.close(client_fd)
            raise RuntimeError("Could not setsockopt TCP_NODELAY on client fd.")

        return WiFiClient(fd = client_fd)

    accept = available
    
    def setNoDelay(self, nodelay) :
        self.noDelay = nodelay
    
    def getNoDelay(self) :
        return self.noDelay
