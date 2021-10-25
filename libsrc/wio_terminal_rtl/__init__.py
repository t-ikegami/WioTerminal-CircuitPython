import board
import digitalio as dio

# On the first import, pwr.value becomes False to turn off RTL8720.
#
pwr = dio.DigitalInOut(board.RTL_PWR)
pwr.switch_to_output()

