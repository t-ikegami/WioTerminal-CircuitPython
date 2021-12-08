import uctypes as ct
from .SERCOM0_ import SERCOM_

SERCOM7 = ct.struct(0x43000c00, SERCOM_, ct.LITTLE_ENDIAN)
