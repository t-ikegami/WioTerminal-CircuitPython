import uctypes as ct

TRNG_ = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'ENABLE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT8 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT8,
    'DATARDYEO'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT8,
    'DATARDY'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x09, {
    'reg'	:   0x00 | ct.UINT8,
    'DATARDY'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x0A, {
    'reg'	:   0x00 | ct.UINT8,
    'DATARDY'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DATA'	: 0x20 | ct.UINT32,
}

TRNG = ct.struct(0x42002800, TRNG_)
