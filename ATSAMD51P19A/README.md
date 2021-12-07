# ATSAMD51P19A

**DANGER:** it is very easy to crash Wio Terminal with this.
Any safeguard and consistency under the CircuitPython can be broken.

## Summary
Access bare metal peripherals of [SAMD51](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU32/ProductDocuments/DataSheets/SAM_D5x_E5x_Family_Data_Sheet_DS60001507G.pdf) by using uctypes module of MicroPython.
Every single bit of registers can be manipulated.
[A custom firmware](./MyCircuitPython7.0+UCTYPES.uf2) with uctypes enabled is required.

The module is generated from [a SVD file](https://github.com/posborne/cmsis-svd/blob/master/data/Atmel/ATSAMD51P19A.svd).
A crude version of [the converter](./svd2uctypes.py) (written in CPython) is also provided.

## Example
This example is heavily owed to [デバイスビジネス開拓団](https://jhalfmoon.com/dbc/2021/08/25/iot何をいまさら91-atsamd51、ccl、極小のオンチップfpga/).

- Enable main clock to Configurable Custom Logic (CCL).
- Prepare DigitalInOut PA04-07 to be used as input (04-06) and output(07).
- Setup peripheral multiplexers for the pins above, to be used by CCL.
- Reset and setup CCL registers.
- Test if CCL works.  The Truth table is 0x82, meaning that PA07 becomes True only when (PA04, PA05, PA06) = (1, 0, 0) or (1, 1, 1).

```
import digitalio as dio
import microcontroller as mc
from ATSAMD51P19A import MCLK, PORT, CCL

MCLK.APBCMASK.CCL = 1
PORTA = PORT.GROUP[0]

pa04 = dio.DigitalInOut(mc.pin.PA04)	# CCL IN[0], 33
pa05 = dio.DigitalInOut(mc.pin.PA05)	# CCL IN[1], 26
pa06 = dio.DigitalInOut(mc.pin.PA06)	# CCL IN[2], 37
pa07 = dio.DigitalInOut(mc.pin.PA07)	# CCL OUT[0], 16

PORTA.PMUX[2].reg = 0xDD		# FUNC_N = CCL
PORTA.PMUX[3].reg = 0xDD
PORTA.PINCFG[7].PMUXEN = 1

CCL.CTRL.SWRST = 1
lut = CCL.LUTCTRL[0]
lut.TRUTH = 0x82
lut.INSEL2 = lut.INSEL1 = lut.INSEL0 = 0x04
lut.ENABLE = 1
CCL.CTRL.ENABLE = 1

def output() :
    print(f"{pa04.value:1d} {pa05.value:1d} {pa06.value:1d} -> {pa07.value:1d}")

pa04.pull = pa05.pull = pa06.pull = dio.Pull.DOWN	# PMUX bit is cleard!!
PORTA.PINCFG[4].PMUXEN = 1
PORTA.PINCFG[5].PMUXEN = 1
PORTA.PINCFG[6].PMUXEN = 1

output()
pa04.pull = dio.Pull.UP
PORTA.PINCFG[4].PMUXEN = 1
output()
pa05.pull = dio.Pull.UP
PORTA.PINCFG[5].PMUXEN = 1
output()
pa06.pull = dio.Pull.UP
PORTA.PINCFG[6].PMUXEN = 1
output()
```
↓
```
0 0 0 -> 0
1 0 0 -> 1
1 1 0 -> 0
1 1 1 -> 1
```

