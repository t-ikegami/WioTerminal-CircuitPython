import uctypes as ct

OSC32KCTRL_ = {
  'INTENCLR'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'XOSC32KRDY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSC32KFAIL'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'XOSC32KRDY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSC32KFAIL'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT32,
    'XOSC32KRDY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSC32KFAIL'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUS'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT32,
    'XOSC32KRDY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSC32KFAIL'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSC32KSW'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'RTCCTRL'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT8,
    'RTCSEL'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'XOSC32K'	: ( 0x14, {
    'reg'	:   0x00 | ct.UINT16,
    'ENABLE'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'XTALEN'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'EN32K'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'EN1K'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONDEMAND'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'STARTUP'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'WRTLOCK'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'CGM'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'CFDCTRL'	: ( 0x16, {
    'reg'	:   0x00 | ct.UINT8,
    'CFDEN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'SWBACK'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CFDPRESC'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x17, {
    'reg'	:   0x00 | ct.UINT8,
    'CFDEO'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'OSCULP32K'	: ( 0x1C, {
    'reg'	:   0x00 | ct.UINT32,
    'EN32K'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'EN1K'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CALIB'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  6 << ct.BF_LEN,
    'WRTLOCK'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
}

OSC32KCTRL = ct.struct(0x40001400, OSC32KCTRL_, ct.LITTLE_ENDIAN)
