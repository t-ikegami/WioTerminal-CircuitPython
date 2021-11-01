"""
A helper module that initializes the display and buttons for the uGame
game console. See https://hackaday.io/project/27629-game
"""

import board
import digitalio
import analogio
import stage
import ButtonEvents

display = board.DISPLAY

buttons = ButtonEvents.ButtonEvents()
K_X      = buttons.K_X     
K_DOWN   = buttons.K_DOWN  
K_LEFT   = buttons.K_LEFT  
K_RIGHT  = buttons.K_RIGHT 
K_UP     = buttons.K_UP    
K_O      = buttons.K_O     
K_START  = buttons.K_START 
K_SELECT = buttons.K_SELECT

class DummyAudio:
    def play(self, f, loop=False):
        pass

    def stop(self):
        pass

    def mute(self, mute):
        pass

audio = DummyAudio()

