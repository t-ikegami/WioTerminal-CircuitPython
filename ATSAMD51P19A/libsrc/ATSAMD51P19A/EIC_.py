import uctypes as ct

EIC_ = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'SWRST'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CKSEL'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'NMICTRL'	: ( 0x01, {
    'reg'	:   0x00 | ct.UINT8,
    'NMISENSE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
    'NMIFILTEN'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'NMIASYNCH'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'NMIFLAG'	: ( 0x02, {
    'reg'	:   0x00 | ct.UINT16,
    'NMI'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT32,
    'EXTINTEO'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT32,
    'EXTINT'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'EXTINT'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x14, {
    'reg'	:   0x00 | ct.UINT32,
    'EXTINT'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
  'ASYNCH'	: ( 0x18, {
    'reg'	:   0x00 | ct.UINT32,
    'ASYNCH'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
  'CONFIG'	: ( 0x1C | ct.ARRAY, 2, {
    'reg'	:   0x00 | ct.UINT32,
    'SENSE0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
    'FILTEN0'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'SENSE1'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  3 << ct.BF_LEN,
    'FILTEN1'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'SENSE2'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'FILTEN2'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'SENSE3'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  3 << ct.BF_LEN,
    'FILTEN3'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'SENSE4'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  3 << ct.BF_LEN,
    'FILTEN4'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'SENSE5'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  3 << ct.BF_LEN,
    'FILTEN5'	:   0x00 | ct.BFUINT32 | 23 << ct.BF_POS |  1 << ct.BF_LEN,
    'SENSE6'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  3 << ct.BF_LEN,
    'FILTEN6'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
    'SENSE7'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  3 << ct.BF_LEN,
    'FILTEN7'	:   0x00 | ct.BFUINT32 | 31 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DEBOUNCEN'	: ( 0x30, {
    'reg'	:   0x00 | ct.UINT32,
    'DEBOUNCEN'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
  'DPRESCALER'	: ( 0x34, {
    'reg'	:   0x00 | ct.UINT32,
    'PRESCALER0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
    'STATES0'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PRESCALER1'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  3 << ct.BF_LEN,
    'STATES1'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'TICKON'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'PINSTATE'	: ( 0x38, {
    'reg'	:   0x00 | ct.UINT32,
    'PINSTATE'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
}

EIC = ct.struct(0x40002800, EIC_)
