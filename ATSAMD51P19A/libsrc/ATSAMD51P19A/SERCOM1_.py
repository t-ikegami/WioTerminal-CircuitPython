import uctypes as ct
from .SERCOM0_ import SERCOM_

SERCOM1 = ct.struct(0x40003400, SERCOM_, ct.LITTLE_ENDIAN)
