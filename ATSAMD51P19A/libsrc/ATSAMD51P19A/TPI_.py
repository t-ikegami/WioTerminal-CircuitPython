import uctypes as ct

TPI_ = {
  'SSPSR'	: 0x00 | ct.UINT32,
  'CSPSR'	: 0x04 | ct.UINT32,
  'ACPR'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'PRESCALER'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 13 << ct.BF_LEN,
  }),
  'SPPR'	: ( 0xF0, {
    'reg'	:   0x00 | ct.UINT32,
    'TXMODE'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'FFSR'	: ( 0x300, {
    'reg'	:   0x00 | ct.UINT32,
    'FlInProg'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'FtStopped'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCPresent'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'FtNonStop'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'FFCR'	: ( 0x304, {
    'reg'	:   0x00 | ct.UINT32,
    'EnFCont'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'TrigIn'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'FSCR'	: 0x308 | ct.UINT32,
  'TRIGGER'	: ( 0xEE8, {
    'reg'	:   0x00 | ct.UINT32,
    'TRIGGER'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'FIFO0'	: ( 0xEEC, {
    'reg'	:   0x00 | ct.UINT32,
    'ETM0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  8 << ct.BF_LEN,
    'ETM1'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  8 << ct.BF_LEN,
    'ETM2'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  8 << ct.BF_LEN,
    'ETM_bytecount'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  2 << ct.BF_LEN,
    'ETM_ATVALID'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'ITM_bytecount'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  2 << ct.BF_LEN,
    'ITM_ATVALID'	:   0x00 | ct.BFUINT32 | 29 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'ITATBCTR2'	: ( 0xEF0, {
    'reg'	:   0x00 | ct.UINT32,
    'ATREADY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'ITATBCTR0'	: ( 0xEF8, {
    'reg'	:   0x00 | ct.UINT32,
    'ATREADY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'FIFO1'	: ( 0xEFC, {
    'reg'	:   0x00 | ct.UINT32,
    'ITM0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  8 << ct.BF_LEN,
    'ITM1'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  8 << ct.BF_LEN,
    'ITM2'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  8 << ct.BF_LEN,
    'ETM_bytecount'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  2 << ct.BF_LEN,
    'ETM_ATVALID'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'ITM_bytecount'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  2 << ct.BF_LEN,
    'ITM_ATVALID'	:   0x00 | ct.BFUINT32 | 29 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'ITCTRL'	: ( 0xF00, {
    'reg'	:   0x00 | ct.UINT32,
    'Mode'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CLAIMSET'	: 0xFA0 | ct.UINT32,
  'CLAIMCLR'	: 0xFA4 | ct.UINT32,
  'DEVID'	: ( 0xFC8, {
    'reg'	:   0x00 | ct.UINT32,
    'NrTraceInput'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'AsynClkIn'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'MinBufSz'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  3 << ct.BF_LEN,
    'PTINVALID'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'MANCVALID'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRZVALID'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DEVTYPE'	: ( 0xFCC, {
    'reg'	:   0x00 | ct.UINT32,
    'SubType'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'MajorType'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
}

TPI = ct.struct(0xe0040000, TPI_, ct.LITTLE_ENDIAN)
