import time
import board
from ButtonEvents import ButtonEvents
from wio_terminal_rtl import rpc
from wio_terminal_rtl.rpc import wifi, tcpip_adapter
import wio_terminal_rtl.rpc.constants as C

disp = board.DISPLAY
disp.auto_refresh = False
disp.brightness = 0.0

rpc.reset()
tcpip_adapter.init()
wifi.off()
time.sleep(0.1)
wifi.on(C.MODE_STA_AP)
time.sleep(0.1)
authmode = C.SECURITY_WPA2_AES_PSK
passwd = "DummyPassword"
channel = 11

wifi.start_ap("AP Clock", passwd, authmode, channel)

be = ButtonEvents()
tm0 = None
while True :
    time.sleep(1)
    if be.buttons()  & be.K_SELECT : break

    t = time.localtime()
    if tm0 == t.tm_min : continue
    tm0 = t.tm_min
    ssid = f"{t.tm_year:02d}/{t.tm_mon:02d}/{t.tm_mday:02d} {t.tm_hour:02d}:{t.tm_min:02d}"
    wifi.restart_ap(ssid, passwd, authmode, channel)

be.deinit()
disp.brightness = 1.0
disp.auto_refresh = True
wifi.off()
