import struct
from .rpc import wifi, tcpip_adapter
from .rpc import constants as C
from .rpc.struct_wifi import Struct
from .WiFiClient import WiFiClient

local_ip = (192, 168,   1, 1)
gateway  = (192, 168,   1, 1)
subnet   = (255, 255, 255, 0)

def softAP(ssid, password = None, channel = 11, ssid_hidden = False) :
    
    if password is not None and len(password) < 8 :
        raise RuntimeError("Password is too short")

    wifi.off()
    wifi.on(C.MODE_STA_AP)
    
    authmode = C.SECURITY_OPEN if password is None else C.SECURITY_WPA2_AES_PSK
    if ssid_hidden :
        res = wifi.start_ap_with_hidden_ssid(ssid, password, authmode, channel)
    else :
        res = wifi.start_ap(ssid, password, authmode, channel)
    if res < 0 : raise RuntimeError("Could not start AP")

    info = Struct("ip_info")
    info.ip = local_ip
    info.gw = gateway
    info.netmask = subnet
    tcpip_adapter.dhcps_stop(C.TCPIP_ADAPTER_IF_AP)
    if tcpip_adapter.set_ip_info(C.TCPIP_ADAPTER_IF_AP, info._data) != 0 :
        raise RuntimeError("Could not tcp_adapter.set_ip_info")
    # tcpip_adapter.dhcps_option() is not supported yet on eRPC
    if tcpip_adapter.dhcps_start(C.TCPIP_ADAPTER_IF_AP) != 0 :
        raise RuntimeError("Could not tcp_adapter.dhcps_start")
    
def get_clients() :
    (buf, res) = wifi.get_associated_client_list(10)
    if res != 0 : return None

    n = struct.unpack_from("<i", buf, 0)[0]
    clients = [ struct.unpack_from("<6B", buf, 4 + i*6) for i in range(n) ]
    return [ ":".join(f"{x:02X}" for x in c) for c in clients ]
    
def get_ip_info() :
    (buf, res) = tcpip_adapter.get_ip_info(C.TCPIP_ADAPTER_IF_AP)
    if res != 0 : return None
    return Struct("ip_info", buf)
