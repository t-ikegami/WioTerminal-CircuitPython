import uctypes as ct
from .SERCOM0_ import SERCOM_

SERCOM3 = ct.struct(0x41014000, SERCOM_, ct.LITTLE_ENDIAN)
