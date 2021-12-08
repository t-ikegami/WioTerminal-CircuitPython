import uctypes as ct

PM_ = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'IORET'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SLEEPCFG'	: ( 0x01, {
    'reg'	:   0x00 | ct.UINT8,
    'SLEEPMODE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT8,
    'SLEEPRDY'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x05, {
    'reg'	:   0x00 | ct.UINT8,
    'SLEEPRDY'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x06, {
    'reg'	:   0x00 | ct.UINT8,
    'SLEEPRDY'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STDBYCFG'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT8,
    'RAMCFG'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'FASTWKUP'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'HIBCFG'	: ( 0x09, {
    'reg'	:   0x00 | ct.UINT8,
    'RAMCFG'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'BRAMCFG'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'BKUPCFG'	: ( 0x0A, {
    'reg'	:   0x00 | ct.UINT8,
    'BRAMCFG'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'PWSAKDLY'	: ( 0x12, {
    'reg'	:   0x00 | ct.UINT8,
    'DLYVAL'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  7 << ct.BF_LEN,
    'IGNACK'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
}

PM = ct.struct(0x40000400, PM_, ct.LITTLE_ENDIAN)
