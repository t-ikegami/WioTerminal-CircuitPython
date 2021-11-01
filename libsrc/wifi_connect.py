import os
import time
from Menu import Menu
from wio_terminal_rtl import rpc
from wio_terminal_rtl.rpc import wifi, tcpip_adapter
import wio_terminal_rtl.rpc.constants as C
from wio_terminal_rtl.rpc.struct_wifi import Struct

# Prepare wifi_points.py like:
#    [ ( "Title", "SSID", "Password" ), ... ]
#
# Encrypted version (wifi_points.enc) is also supported:
# - Get encryption key on Wio Terminal
#   from microcontroller import cpu
#   from binascii import hexlify
#   hexlify(cpu.uid)
# - Encrypt wifi_points.py on Linux
#   openssl enc -aes-128-ctr -e -K <uid> -iv <uid> -in wifi_points.py -out wifi_points.enc
#
if "wifi_points.py" in os.listdir() :
    with open("wifi_points.py", "r") as f :
        wifi_point = eval("".join(f.readlines()))
else :
    with open("wifi_points.enc", "rb") as f :
        buf = f.read()
        
    import aesio
    import microcontroller as mc

    cipher = aesio.AES(mc.cpu.uid, aesio.MODE_CTR, mc.cpu.uid)
    wifi_point = bytearray(len(buf))
    cipher.decrypt_into(buf, wifi_point)
    wifi_point = eval(wifi_point)

def wifi_connect() :
    """Connect to WiFi.  Reconnection to the saved point is tried first.
    If successful, returns True silently.  A wifi-point select menu is
    displayed next, and returns None if canceled.  Returns a menu
    index if connected, or False in case of failure.

    """
    rpc.reset()
    tcpip_adapter.init()
    tcpip_adapter.dhcpc_stop(C.TCPIP_ADAPTER_IF_STA)
    wifi.off()
    time.sleep(0.1)
    wifi.on(C.MODE_STA)
    time.sleep(0.1)

    (buf, res) = wifi.get_reconnect_data()
    if res > 0 :
        rec = Struct("fast_reconnect", buf)
        name     = "reconnect"
        ssid     = rec.psk_essid.rstrip(b"\0")
        password = rec.psk_passphrase.strip(b"\0")
        security = rec.security_type

        if wifi.connect(ssid, password, security, -1, 0) == 0 :
            tcpip_adapter.dhcpc_start(C.TCPIP_ADAPTER_IF_STA)
            return True

    wifi_menu = [ x[0] for x in wifi_point ]
    idx = Menu("Choose wifi point", wifi_menu)
    if idx is None: return None

    (name, ssid, password) = wifi_point[idx]
    print("\x1b[2J")
    print(f"Connecting to {name}...")
    if wifi.connect(ssid, password, C.SECURITY_WPA2_AES_PSK, -1, 0) != 0 :
        print(f"\n\nCannot connect to {name}.")
        return False
    tcpip_adapter.dhcpc_start(C.TCPIP_ADAPTER_IF_STA)
    print("Connected.")
    return idx
