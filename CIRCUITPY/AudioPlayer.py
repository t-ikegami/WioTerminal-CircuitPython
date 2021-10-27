import os
import board
import audiomp3
import audioio
import mount_sd
from Menu import Menu
from ButtonEvents import ButtonEvents
import time

path = "/sd/Music"

disp  = board.DISPLAY
be    = ButtonEvents()
audio = audioio.AudioOut(board.DAC0, right_channel = board.DAC1)

files = [ name for name in os.listdir(path) if name.endswith(".mp3") ]
title = [ name[:-4] for name in files ]

idx = 0
while True :
    idx = Menu("MP3 Player", title, idx)
    if idx is None : break

    print("\x1b[2J\n"
          "             ^             ^\n"
          "           pause          stop\n")
    name = title[idx]
    pos = 25 - len(name) // 2
    print(f"\x1b[9;{pos}H{name}")

    disp.refresh()
    disp.auto_refresh = False		# seems to be fixed on CP 7.0, but left as-is
    with open(f"{path}/{files[idx]}", "rb") as data :
        with audiomp3.MP3Decoder(data) as mp3 :
            audio.play(mp3)

            count = 0
            playing = True
            while audio.playing :
                time.sleep(0.5)
                count += 1
                if count == 10 : disp.brightness = 0.0
                buttons = be.buttons()
                if buttons == 0 : continue
                count = 0
                disp.brightness = 1.0
                if buttons & (be.K_O | be.K_SELECT) :
                    audio.stop()
                    break
                if buttons & be.K_START :
                    if playing :
                        audio.pause()
                        playing = False
                        print("\x1b[3;12Hresume")
                        disp.refresh()
                    else :
                        audio.resume()
                        playing = True
                        print("\x1b[3;12Hpause ")
                        disp.refresh()

    disp.brightness = 1.0
    disp.auto_refresh = True

audio.deinit()
be.deinit()

