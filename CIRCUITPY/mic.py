import time
import array
import analogio as aio
import board
import gc
import microcontroller as mc
import ulab.numpy as np
from ulab.scipy.signal import spectrogram
from ButtonEvents import ButtonEvents

m = aio.AnalogIn(board.MIC)
n = 1024
d = array.array("H", [0] * n)

def record() :
    r = range(n)
    gc.disable()
    mc.disable_interrupts()
    t0 = time.monotonic_ns()
    for i in r : 
      d[i] = m.value
      mc.delay_us(52)			# this gives about 10.24 kHz sampling
    t1 = time.monotonic_ns()
    mc.enable_interrupts()
    gc.enable()

    return 1 / ((t1-t0) * 1e-9)

def get_peak() :
    a = np.array(d)
    b = spectrogram(a - np.mean(a))[0:n//2]
    i = np.argmax(b)
    return (i, b[i])

be = ButtonEvents()
while True :
    f = record()
    (i, p) = get_peak()
    if p > 1e6 : print(f * i)

    if be.buttons() : break
be.deinit()
