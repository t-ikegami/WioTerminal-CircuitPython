import uctypes as ct
from .SERCOM0_ import SERCOM_

SERCOM5 = ct.struct(0x43000400, SERCOM_, ct.LITTLE_ENDIAN)
