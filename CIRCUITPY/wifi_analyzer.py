import time
import board
import displayio as dpio
from BitmapFrameBuffer import setup_standard_display, CENTER
from wio_terminal_rtl.rpc import wifi
from wio_terminal_rtl.rpc.struct_wifi import Struct
import wio_terminal_rtl.rpc.constants as C
from ButtonEvents import ButtonEvents

RSSI_CEILING = -40
RSSI_FLOOR   = -100

# setup graphics
#
disp = board.DISPLAY
bf = setup_standard_display()

g = dpio.Group()
g.append(bf)
disp.show(g)

graph_height = 80
graph24_baseline = 100
graph50_baseline = 210
channel24_width = 320 // 17
channel50_width = 320 // 62

# Initialize netowrk
#
wifi.off()
wifi.on(1)

def scan_network() :
  wifi.scan_start()
  while wifi.is_scaning() :
    time.sleep(0.5)
  n = wifi.scan_get_ap_num()
  (records, ret) = wifi.scan_get_ap_records(n)
  s = Struct.get_info("rtw_scan_result")[0][0]
  records = [ Struct("rtw_scan_result", memoryview(records)[s*i:s*(i+1)]) for i in range(n) ]
  return records

def channelIdx(channel) :
    if channel <=  14 : return channel - 1			# 2.4 GHz,  1-14
    if channel <=  64 : return 14 + ((channel - 32) >> 1)	# 5.0 GHz, 32-64
    if channel ==  68 : return 31
    if channel ==  96 : return 33
    if channel <= 144 : return 34 + ((channel - 100) >> 1)
    return 58 + ((channel - 149) >> 1)

def channelPos(channel) :
    idx = channelIdx(channel)
    if idx <= 14 :
        baseline = graph24_baseline
        width    = channel24_width << 1
        offset   = (idx + 2) * channel24_width
    else :
        baseline = graph50_baseline
        width    = channel50_width << 1
        offset   = (idx - 14 + 2) * channel50_width
    return (idx, offset, baseline, width)

def get_ssid(r) :
    if r.SSID_len > 0 :
        return r.SSID[:r.SSID_len].decode()
    else :
        return ":".join(f"{x:02X}" for x in r.BSSID)

def draw_record(r, title = False) :
    channel = r.channel
    rssi    = max(r.signal_strength, RSSI_FLOOR)
    (idx, x, y, width) = channelPos(channel)

    height = (rssi - RSSI_FLOOR) * graph_height // (RSSI_CEILING - RSSI_FLOOR)
    color  = (idx % 7) + 1
    bf.line(x, y - height, x - width, y, color)
    bf.line(x, y - height, x + width, y, color)

    if not title : return

    ssid = get_ssid(r)
    security = "*" if r.security == C.SECURITY_OPEN else ""
    bf.draw_text(x, y - height + 4, f"{ssid}({rssi}){security}", color, align = CENTER)

def draw_screen(records) :
    bf.fill(0)
    bf.draw_text(2, 16, "Wio", bf.Blue)
    bf.draw_text(2, 16, "    WiFi Analyzer", bf.White)

    if len(records) == 0 :
        bf.draw_text(10, 34, "No networks found.", bf.White)
        return
    
    bf.draw_text(200, 16, f"{len(records)} networks found.", bf.White)
    
    rssi_max = dict()
    count = dict()
    for r in records :
        channel = r.channel
        rssi    = r.signal_strength
        rssi_max[channel] = max( rssi, rssi_max.get(channel, RSSI_FLOOR) )
        count[channel] = count.get(channel, 0) + 1

    for r in records :
        draw_record(r, r.signal_strength == rssi_max[r.channel])

    bf.hline(0, graph24_baseline, 320, bf.White)
    bf.hline(0, graph50_baseline, 320, bf.White)
    for channel, count in count.items() :
        (idx, x, y, width) = channelPos(channel)
        color  = (idx % 7) + 1
        bf.draw_text(x, y + 15, str(channel), color, align = CENTER)
        bf.draw_text(x, y + 29, str(count), bf.Gray, align = CENTER)

def print_records(records) :
    print(f"\n{'SSID':20s} {'ch':3s} {'rssi':4s} {'security':12s}")
    for r in records :
        ssid = get_ssid(r)
        ch   = r.channel
        rssi = r.signal_strength
        security = hex(r.security)
        print(f"{ssid:20s} {ch:3d} {rssi:4d} {security:12s}")
        
records = scan_network()
draw_screen(records)

be = ButtonEvents()
while True :
    time.sleep(0.5)
    b = be.buttons()

    if   b & be.K_SELECT : break
    elif b & be.K_O :
        records = scan_network()
        draw_screen(records)
    elif b & be.K_START :
        disp.show(None)
        for i in range(0, len(records), 15) :
            print_records(records[i:i+15])
            while be.buttons() : pass
            while True :
                time.sleep(0.5)
                if be.buttons() & be.K_START : break
        disp.show(g)

be.deinit()
disp.show(None)
    
