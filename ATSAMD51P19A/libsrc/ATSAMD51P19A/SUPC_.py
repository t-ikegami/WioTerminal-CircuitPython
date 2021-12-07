import uctypes as ct

SUPC_ = {
  'INTENCLR'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'BOD33RDY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'BOD33DET'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'B33SRDY'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'VREGRDY'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'VCORERDY'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'BOD33RDY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'BOD33DET'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'B33SRDY'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'VREGRDY'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'VCORERDY'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT32,
    'BOD33RDY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'BOD33DET'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'B33SRDY'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'VREGRDY'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'VCORERDY'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUS'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT32,
    'BOD33RDY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'BOD33DET'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'B33SRDY'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'VREGRDY'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'VCORERDY'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'BOD33'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'ACTION'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
    'STDBYCFG'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'RUNHIB'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'RUNBKUP'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'HYST'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  4 << ct.BF_LEN,
    'PSEL'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  3 << ct.BF_LEN,
    'LEVEL'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  8 << ct.BF_LEN,
    'VBATLEVEL'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  8 << ct.BF_LEN,
  }),
  'VREG'	: ( 0x18, {
    'reg'	:   0x00 | ct.UINT32,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'SEL'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'RUNBKUP'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'VSEN'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'VSPER'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'VREF'	: ( 0x1C, {
    'reg'	:   0x00 | ct.UINT32,
    'TSEN'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'VREFOE'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'TSSEL'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONDEMAND'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'SEL'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'BBPS'	: ( 0x20, {
    'reg'	:   0x00 | ct.UINT32,
    'CONF'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'WAKEEN'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'BKOUT'	: ( 0x24, {
    'reg'	:   0x00 | ct.UINT32,
    'ENOUT0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENOUT1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CLROUT0'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CLROUT1'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'SETOUT0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'SETOUT1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'RTCTGLOUT0'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'RTCTGLOUT1'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'BKIN'	: ( 0x28, {
    'reg'	:   0x00 | ct.UINT32,
    'BKIN0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'BKIN1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
}

SUPC = ct.struct(0x40001800, SUPC_)
