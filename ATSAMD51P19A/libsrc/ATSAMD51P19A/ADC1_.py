import uctypes as ct
from .ADC0_ import ADC_

ADC1 = ct.struct(0x43002000, ADC_, ct.LITTLE_ENDIAN)
