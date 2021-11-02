import board
import displayio as dpio
import adafruit_imageload as imgload
import wifi_start_ap as ap
from wio_terminal_rtl.WiFiServer import WiFiServer
from ButtonEvents import ButtonEvents

bmp, pal = imgload.load("LED.bmp")
pal.make_transparent(3)
tg = dpio.TileGrid(bmp, pixel_shader = pal)
disp = board.DISPLAY
g = dpio.Group()
g.append(tg)
g.x = 110
g.y = 40
disp.show(g)

def LED(on) :
    pal[1] = 0xFF0000 if on else 0x550000

LED(False)
    
ap.wifi_start_ap("Lchika_AP", "Wio Terminal")
server = WiFiServer(80)
server.begin()

be = ButtonEvents()
while not be.get_pressed() :
    client = server.available()
    if client is None : continue
    txt = client.read()
    # print(txt)
    if txt.startswith(b"POST") : LED("LED+ON" in txt)
    
    client.write("""\
HTTP/1.1 200 OK\r
Content_type:text/html\r
\r
<html><head></head><body>
<h1>Wio Terminal</h1>
<form action='/' method='POST'>
  <input type='submit' name='action' value='LED ON'>
  <input type='submit' name='action' value='LED OFF'>
</form>
</body></html>
""")
    client.stop()

be.deinit()
ap.wifi.off()
