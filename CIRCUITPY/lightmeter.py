import board            
from analogio import AnalogIn
from Meter import Meter
from ButtonEvents import ButtonEvents

light = AnalogIn(board.LIGHT)
meter = Meter(500, 63000, "LIGHT")
disp = board.DISPLAY
disp.show(meter)
be = ButtonEvents()

value = light.value
while not be.get_pressed() :
    value = value * 0.98 + light.value * 0.02
    # print(value)
    meter.set_value(value, 20)
