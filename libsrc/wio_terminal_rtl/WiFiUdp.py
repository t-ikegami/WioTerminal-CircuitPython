import struct
from .rpc import lwip, wifi
from .rpc import constants as C		# To be efficient, C.XXX should be re-declared locally as _XXX
from .rpc.struct_wifi import Struct

class WiFiUdp :
    def __init__(self) :
        self.udp_server = None
        self.server_port = None
        self.remoe_port = None
        self.tx_buffer = None
        self.tx_buffer_len = 0
        self.rx_buffer = None
        self.multicast_ip = None
        
    def begin(self, address, port) :
        self.stop()
        self.server_port = port
        self.tx_buffer = memoryview(bytearray(1460))
        self.udp_server = lwip.socket(C.AF_INET, C.SOCK_DGRAM, 0)
        if self.udp_server == -1 :
            self.udp_server = None
            raise RuntimeError("Could not create socket.")
        yes = struct.pack("<i", 1)
        if lwip.setsockopt(self.udp_server, C.SOL_SOCKET, C.SO_REUSEADDR, yes, len(yes)) < 0 :
            self.stop()
            raise RuntimeError("Could not set socket option.")
        addr = Struct("sockaddr_in")
        addr.sin_family = C.AF_INET
        addr.sin_port = lwip.htons(self.server_port)
        addr.sin_addr = address
        if lwip.bind(self.udp_server, addr._data, len(addr._data)) == -1 :
            self.stop()
            raise RuntimeError("Could not bind socket.")
        lwip.fcntl(self.udp_server, C.F_SETFL, C.O_NONBLOCK)

    def beginMulticast(a, p) :
        self.begin(C.INADDR_ANY, p)
        if a == C.INADDR_ANY : return
        mreq = Struct("ip_mreq")
        mreq.imr_multiaddr = a
        mreq.imr_interface = C.INADDR_ANY
        if lwip.setsockopt(self.udp_server, C.IPPROTO_IP, C.IP_ADD_MEMBERSHIP,
                           mreq._data, len(mreq._data)) < 0 :
            self.stop()
            raise RuntimeError("Could not join igmp.")
        self.multicast_ip = a
            
    def stop(self) :
        self.tx_buffer = None
        self.tx_buffer_len = 0
        self.rx_buffer = None
        if self.udp_server is None : return
        if self.multicast_ip is not None :
            mreq = Struct("ip_mreq")
            mreq.imr_multiaddr = self.multicast_ip
            mreq.imr_interface = C.INADDR_ANY
            lwip.setsockopt(self.udp_server, C.IPPROTO_IP, C.IP_DROP_MEMBERSHIP,
                            mreq._data, len(mreq._data))
            self.multicast_ip = None
        lwip.close(self.udp_server)
        self.udp_server = None
        self.multicast_ip = None

    def beginMulticastPacket(self) :
        if self.server_port is None or self.multicast_ip is None :
            raise RuntimeError("Could not start Multicast.")
        self.remote_ip = self.multicast_ip
        self.remote_port = self.server_port
        self.beginPacket()
        
    def beginPacket(self, ip, port) :
        if isinstance(ip, str) : ip = lwip.getipbyname(ip)
        self.remote_ip = ip
        self.remote_port = port

        if self.tx_buffer is None :
            self.tx_buffer = memoryview(bytearray(1460))

        self.tx_buffer_len = 0
        if self.udp_server is not None : return

        self.udp_server = lwip.socket(C.AF_INET, C.SOCK_DGRAM, 0)
        if self.udp_server == -1 :
            self.udp_server = None
            raise RuntimeError("Could not create socket.")
        lwip.fcntl(self.udp_server, C.F_SETFL, C.O_NONBLOCK)

    def endPacket(self) :
        recipient = Struct("sockaddr_in")
        recipient.sin_addr = self.remote_ip
        recipient.sin_family = C.AF_INET
        recipient.sin_port = lwip.htons(self.remote_port)
        if lwip.sendto(self.udp_server, self.tx_buffer[:self.tx_buffer_len], 0,
                       recipient._data, len(recipient._data)) < 0 :
            raise RuntimeError("Could not send data.")
        
    def write(self, data) :
        if isinstance(data, int) :
            mv = memoryview([data])
        else :
            mv = memoryview(data)
        while len(mv) > 0 :
            if self.tx_buffer_len >= 1460 :
                self.endPacket()
                self.tx_bufer_len = 0
            l = min(len(mv), 1460 - self.tx_buffer_len)
            self.tx_buffer[self.tx_buffer_len:self.tx_buffer_len + l] = mv[:l]
            self.tx_buffer_len += l
            mv = mv[l:]
        
    def parsePacket(self) :
        if self.rx_buffer is not None: return 0
        fromlen = Struct.get_info("sockaddr_in")[0][0]
        (b_mem, b_from, fromlen, gotlen) = lwip.recvfrom(self.udp_server, 1460,
                                                        C.MSG_DONTWAIT, fromlen, 1460 * 10)
        if gotlen == -1 :
            if lwip.errno() == C.EWOULDBLOCK : return 0
            raise RuntimeError("Could not receive data.")
        if gotlen > 0 : self.rx_buffer = memoryview(b_mem[:gotlen])
        si_other = Struct("sockaddr_in", b_from)
        self.remote_ip = si_other.sin_addr
        self.remote_port = lwip.ntohs(si_other.sin_port)

        return gotlen

    def available(self) :
        return self.rx_buffer is not None
        
    def read(self, size = None) :
        if self.rx_buffer is None : return 0
        if size == None :
            size = 1
            ret = self.rx_buffer[0]
        else :
            ret = self.rx_buffer[:size]
        self.rx_buffer = self.rx_buffer[size:]
        if len(self.rx_buffer) == 0 : self.rx_buffer = None

        return ret

    def peek(self) :
        if self.rx_buffer is None : return -1
        return self.rx_buffer[0]

    def flush(self) :
        self.rx_buffer = None
