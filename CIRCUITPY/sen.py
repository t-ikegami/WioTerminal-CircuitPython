import os
import time
import board
import displayio as dpio
from Sentence import Sentence
from RictyKanji import draw_text, set_palette
from ButtonEvents import ButtonEvents
import bitmaptools as bmt
import gc

disp = board.DISPLAY
g = dpio.Group()
bmp = dpio.Bitmap(304, 224, 4)
pal = dpio.Palette(4)
set_palette(pal)
tg = dpio.TileGrid(bmp, pixel_shader = pal)
g.append(tg)
g.x = 8
g.y = 8
disp.show(g)
be = ButtonEvents()

draw_text(bmp, 0, 0, """\
┌─────────────────┐
│　　　　　　　　　　　　　　　　　│
├─────────────────┤
│　　　　　　　　　　　　　　　　　│
│　　　　　　　　　　　　　　　　　│
│　　　　　　　　　　　　　　　　　│
│　　　　　　　　　　　　　　　　　│
│　　　　　　　　　　　　　　　　　│
│　　　　　　　　　　　　　　　　　│
│　　　　　　　　　　　　　　　　　│
│　　　　　　　　　　　　　　　　　│
│　　　　　　　　　　　　　　　　　│
│　　　　　　　　　　　　　　　　　│
└─────────────────┘""")

def clear(bmp, x, y, width, height) :
    bmt.fill_region(bmp, x << 4, y << 4, (x + width) << 4, (y + height) << 4, 0)

def setup(fname) :
    gc.collect()
    dict = Sentence("sen_dic/" + fname)
    clear(bmp, 1, 1, 17, 1)
    draw_text(bmp, 152 - len(dict.title) * 8, 16, dict.title)
    return dict

def update(txt) :
    clear(bmp, 1, 3, 17, 10) 
    draw_text(bmp, 32, 64, txt, width = 15)

# Dict = [ "Proverb.dic", "News.dic", "Prophet.dic", "Kempo.dic", "Food.dic",
#          "Alabian.dic", "Autograph.dic", "Popz.dic" ]
Dict = os.listdir("sen_dic")

Idx  = -1
dict = setup(Dict[Idx])

key = 0    
while True :
    update(dict.sentence())

    t = time.monotonic()
    while key : key = be.get_pressed()	# wait until key release
    while key == 0 and time.monotonic() - t < 15 :
        time.sleep(0.1)
        key = be.get_pressed()
    if key & be.K_SELECT : break

    if key & be.K_RIGHT :
        Idx += 1
        if Idx >= len(Dict) : Idx = 0
        del dict
        dict = setup(Dict[Idx])
    if key & be.K_LEFT :
        Idx -= 1
        if Idx < 0 : Idx += len(Dict)
        del dict
        dict = setup(Dict[Idx])

be.deinit()        
disp.show(None)

