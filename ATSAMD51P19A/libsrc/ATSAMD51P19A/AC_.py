import uctypes as ct

AC_ = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'SWRST'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CTRLB'	: ( 0x01, {
    'reg'	:   0x00 | ct.UINT8,
    'START0'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'START1'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x02, {
    'reg'	:   0x00 | ct.UINT16,
    'COMPEO0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMPEO1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'WINEO0'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMPEI0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMPEI1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEI0'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEI1'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT8,
    'COMP0'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMP1'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'WIN0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x05, {
    'reg'	:   0x00 | ct.UINT8,
    'COMP0'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMP1'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'WIN0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x06, {
    'reg'	:   0x00 | ct.UINT8,
    'COMP0'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMP1'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'WIN0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUSA'	: ( 0x07, {
    'reg'	:   0x00 | ct.UINT8,
    'STATE0'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'STATE1'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'WSTATE0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'STATUSB'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT8,
    'READY0'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'READY1'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DBGCTRL'	: ( 0x09, {
    'reg'	:   0x00 | ct.UINT8,
    'DBGRUN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'WINCTRL'	: ( 0x0A, {
    'reg'	:   0x00 | ct.UINT8,
    'WEN0'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'WINTSEL0'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'SCALER'	: ( 0x0C | ct.ARRAY, 2, {
    'reg'	:   0x00 | ct.UINT8,
    'VALUE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  6 << ct.BF_LEN,
  }),
  'COMPCTRL'	: ( 0x10 | ct.ARRAY, 2, {
    'reg'	:   0x00 | ct.UINT32,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'SINGLE'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'INTSEL'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  2 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'MUXNEG'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'MUXPOS'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  3 << ct.BF_LEN,
    'SWAP'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'SPEED'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  2 << ct.BF_LEN,
    'HYSTEN'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'HYST'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  2 << ct.BF_LEN,
    'FLEN'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  3 << ct.BF_LEN,
    'OUT'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x20, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'WINCTRL'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMPCTRL0'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMPCTRL1'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CALIB'	: ( 0x24, {
    'reg'	:   0x00 | ct.UINT16,
    'BIAS0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
}

AC = ct.struct(0x42002000, AC_)
