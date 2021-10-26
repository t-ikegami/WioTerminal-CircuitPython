import os
import time
import board
import displayio as dpio
from NankaiBakabon import NankaiBakabon
from KanjiTerminal import KanjiTerminal
from random import randrange
from ButtonEvents import ButtonEvents
import gc

disp = board.DISPLAY
kt = KanjiTerminal(19, 14)
kt.x = kt.y = 8
disp.show(kt)
be = ButtonEvents()

# Dict = [ "bantio.nb1", "es.nb1", "keiyaku.nb1", "risukei.nb1", 
#          "deus.nb1", "incest.nb1", "nanba.nb1", "nost.nb1", "shiso.nb1" ]
Dict = os.listdir("nanba_dic")

Idx  = -1
dict = NankaiBakabon("nanba_dic/" + Dict[Idx])

kt.locate(0, 0)
key = 0
words = []
while True :
    if len(words) <= 0 : dict.paragraph(words)
    w = words.pop(0)
    time.sleep(len(w) * 0.05)
    kt.print(w, delay = 0.1)
    
    buttons = be.buttons()
    if buttons & be.K_SELECT : break

    if buttons & (be.K_RIGHT | be.K_DOWN) :
        Idx += 1
        if Idx >= len(Dict) : Idx = 0
    if buttons & (be.K_LEFT  | be.K_UP) :
        Idx -= 1
        if Idx < 0 : Idx += len(Dict)
    if buttons & (be.K_RIGHT | be.K_LEFT) :
        del dict
        gc.collect()
        dict = NankaiBakabon("nanba_dic/" + Dict[Idx])
        kt.print("\n\n")
        words.clear()
    if buttons & (be.K_UP | be.K_DOWN) :
        dict.read_dict("nanba_dic/" + Dict[Idx])
        kt.print("\n")
        words.clear()

be.deinit()
disp.show(None)

