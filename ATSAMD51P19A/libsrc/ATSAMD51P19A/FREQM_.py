import uctypes as ct

FREQM_ = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'SWRST'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CTRLB'	: ( 0x01, {
    'reg'	:   0x00 | ct.UINT8,
    'START'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CFGA'	: ( 0x02, {
    'reg'	:   0x00 | ct.UINT16,
    'REFNUM'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  8 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT8,
    'DONE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x09, {
    'reg'	:   0x00 | ct.UINT8,
    'DONE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x0A, {
    'reg'	:   0x00 | ct.UINT8,
    'DONE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUS'	: ( 0x0B, {
    'reg'	:   0x00 | ct.UINT8,
    'BUSY'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVF'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'VALUE'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'VALUE'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 24 << ct.BF_LEN,
  }),
}

FREQM = ct.struct(0x40002c00, FREQM_, ct.LITTLE_ENDIAN)
