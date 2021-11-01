import struct
import rtc
import time
import math
from wifi_connect import wifi_connect
from wio_terminal_rtl.WiFiUdp import WiFiUdp
from wio_terminal_rtl.rpc import tcpip_adapter
from wio_terminal_rtl.rpc.struct_wifi import Struct

def ntp_set_time() :
    ip_info = Struct("ip_info", tcpip_adapter.get_ip_info(0)[0])
    udp = WiFiUdp()
    udp.begin(ip_info.ip, 2390)
    buf = bytearray(48)
    buf[0:4] = bytes([ 0b11100011, 0, 6, 0xEC ])
    udp.beginPacket("ntp.nict.jp", 123)
    udp.write(buf)

    t1 = time.monotonic_ns()
    udp.endPacket()
    for i in range(10000) : 
        if udp.parsePacket() > 0 : break
    t2 = time.monotonic_ns()

    if not udp.available() :
        udp.stop()
        return False
    
    buf = udp.read(48)
    (t, sub) = struct.unpack_from(">2I", buf, 40)
    t -= 2208988800 - 9 * 3600	# - (1970y - 1900y) + JST+9hr

    t3 = time.monotonic_ns()
    delta = ( ((sub * 10**9) >> 32) + ((t2 - t1) >> 1) + (t3 - t2) ) * 1e-9
    idelta = math.ceil(delta)
    t += idelta
    time.sleep(idelta - delta)
    rtc.RTC().datetime = time.localtime(t)
    udp.stop()
    return True

status = wifi_connect()		# if None, return simply

if status is False :
    print("\nCannot connect to wifi.")
    time.sleep(3)
elif status is not None :
    if ntp_set_time() :
        t = time.localtime()
        print(f"Time set to {t.tm_year:4d}/{t.tm_mon:02d}/{t.tm_mday:02d} "
              f"{t.tm_hour:02d}:{t.tm_min:02d}:{t.tm_sec:02d}")
    else :
        print("Cannot connect to time server.")
    time.sleep(3)
