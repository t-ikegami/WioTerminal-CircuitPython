import uctypes as ct

WDT_ = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'ENABLE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'WEN'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALWAYSON'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CONFIG'	: ( 0x01, {
    'reg'	:   0x00 | ct.UINT8,
    'PER'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'WINDOW'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'EWCTRL'	: ( 0x02, {
    'reg'	:   0x00 | ct.UINT8,
    'EWOFFSET'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT8,
    'EW'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x05, {
    'reg'	:   0x00 | ct.UINT8,
    'EW'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x06, {
    'reg'	:   0x00 | ct.UINT8,
    'EW'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT32,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'WEN'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALWAYSON'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'CLEAR'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CLEAR'	: 0x0C | ct.UINT8,
}

WDT = ct.struct(0x40002000, WDT_)
