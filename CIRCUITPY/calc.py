import time
import board
import displayio as dpio
from RictyKanji import draw_text, set_palette, han2zen
from Calculator import Calculator
from Cursor import Cursor
import bitmaptools as bmt
from IRKit import IRIn

disp = board.DISPLAY
g = dpio.Group()
bmp = dpio.Bitmap(288, 240, 4)
pal = dpio.Palette(4)
set_palette(pal)
tg = dpio.TileGrid(bmp, pixel_shader = pal)
g.append(tg)
g.x = 16
g.y = 0
disp.show(g)

draw_text(bmp, 0, 0, """\
┌────────────────┐
│　　　　　　　　　　　　　　　　│
└────────────────┘
┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐
│７││８││９││÷││ｓ││Ｃ│
└─┘└─┘└─┘└─┘└─┘└─┘
┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐
│４││５││６││×││ｃ││ｒ│
└─┘└─┘└─┘└─┘└─┘└─┘
┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐
│１││２││３││－││ｔ││ｅ│
└─┘└─┘└─┘└─┘└─┘└─┘
┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐
│０││±││・││＋││π││＝│
└─┘└─┘└─┘└─┘└─┘└─┘""")

cur = Cursor(44, 44, (2, 50), (242, 194), (48, 48), (5, 0), events = {
    (0, 0) : "7",  (1, 0) : "8",  (2, 0) : "9",  (3, 0) : "/",  (4, 0) : "s",  (5, 0) : "C",
    (0, 1) : "4",  (1, 1) : "5",  (2, 1) : "6",  (3, 1) : "*",  (4, 1) : "c",  (5, 1) : "r",
    (0, 2) : "1",  (1, 2) : "2",  (2, 2) : "3",  (3, 2) : "-",  (4, 2) : "t",  (5, 2) : "e",
    (0, 3) : "0",  (1, 3) : "p",  (2, 3) : ".",  (3, 3) : "+",  (4, 3) : "P",  (5, 3) : "=",
    (None, 0) : "Q",
    (None, 1) : "M",
    (None, 2) : "R",
    (None, 30) : None,
})

g.append(cur)

ir = IRIn()
ir_keys = { (0x80, 0x12) : "/",  (0x80, 0x1A) : "-",  (0x80, 0x1E) : "C",
            (0x80, 0x01) : "*",  (0x80, 0x02) : "+",  (0x80, 0x03) : "r",             
            (0x80, 0x04) : "7",  (0x80, 0x05) : "8",  (0x80, 0x06) : "9",             
            (0x80, 0x07) : "4",  (0x80, 0x08) : "5",  (0x80, 0x09) : "6",             
            (0x80, 0x0A) : "1",  (0x80, 0x1B) : "2",  (0x80, 0x1F) : "3",             
            (0x80, 0x0C) : "0",  (0x80, 0x0D) : ".",  (0x80, 0x0E) : "=",
           }

# ir_keys = { (0x80, 0x0C) : "7",  (0x80, 0x0A) : "8",  (0x80, 0x07) : "9",
#             (0x80, 0x0D) : "4",  (0x80, 0x1B) : "5",  (0x80, 0x08) : "6",
#             (0x80, 0x0E) : "1",  (0x80, 0x1F) : "2",  (0x80, 0x09) : "3",
#
#             (0x80, 0x04) : "C",  (0x80, 0x01) : "*",  (0x80, 0x12) : "/",
#             (0x80, 0x05) : ".",  (0x80, 0x02) : "+",  (0x80, 0x1A) : "-",
#             (0x80, 0x06) : "0",  (0x80, 0x03) : "=",  (0x80, 0x1E) : "r",
#            }

cal = Calculator()

def show() :
    txt = han2zen( str(cal.x).rstrip("0").lstrip("+") )
    pos = 272 - 16 * len(txt)

    bmt.fill_region(bmp, 16, 16, 272, 32, 0)
    draw_text(bmp, pos, 16, txt)

show()
while True :
    ev = cur.get_event(null = True) or ir_keys.get(ir.recv())
    if ev is None : continue
    if ev == "Q" : break
    cal.event(ev)
    show()

disp.show(None)

