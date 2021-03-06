import uctypes as ct

TC_COUNT8 = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MODE'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
    'PRESCSYNC'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  2 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONDEMAND'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'PRESCALER'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'ALOCK'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'CAPTEN0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'CAPTEN1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'COPEN0'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'COPEN1'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
    'CAPTMODE0'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  2 << ct.BF_LEN,
    'CAPTMODE1'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'CTRLBCLR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT8,
    'DIR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'LUPD'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONESHOT'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMD'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'CTRLBSET'	: ( 0x05, {
    'reg'	:   0x00 | ct.UINT8,
    'DIR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'LUPD'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONESHOT'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMD'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x06, {
    'reg'	:   0x00 | ct.UINT16,
    'EVACT'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
    'TCINV'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCEI'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVFEO'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEO0'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEO1'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT8,
    'OVF'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ERR'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC1'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x09, {
    'reg'	:   0x00 | ct.UINT8,
    'OVF'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ERR'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC1'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x0A, {
    'reg'	:   0x00 | ct.UINT8,
    'OVF'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ERR'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC1'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUS'	: ( 0x0B, {
    'reg'	:   0x00 | ct.UINT8,
    'STOP'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLAVE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PERBUFV'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCBUFV0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCBUFV1'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'WAVE'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT8,
    'WAVEGEN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'DRVCTRL'	: ( 0x0D, {
    'reg'	:   0x00 | ct.UINT8,
    'INVEN0'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEN1'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DBGCTRL'	: ( 0x0F, {
    'reg'	:   0x00 | ct.UINT8,
    'DBGRUN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CTRLB'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'STATUS'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'COUNT'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'CC0'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'CC1'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'COUNT'	: 0x14 | ct.UINT8,
  'PER'	: 0x1B | ct.UINT8,
  'CC'	: ( 0x1C | ct.ARRAY, 2 | ct.UINT8 ),
  'PERBUF'	: 0x2F | ct.UINT8,
  'CCBUF'	: ( 0x30 | ct.ARRAY, 2 | ct.UINT8 ),
}

TC_COUNT16 = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MODE'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
    'PRESCSYNC'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  2 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONDEMAND'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'PRESCALER'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'ALOCK'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'CAPTEN0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'CAPTEN1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'COPEN0'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'COPEN1'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
    'CAPTMODE0'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  2 << ct.BF_LEN,
    'CAPTMODE1'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'CTRLBCLR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT8,
    'DIR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'LUPD'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONESHOT'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMD'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'CTRLBSET'	: ( 0x05, {
    'reg'	:   0x00 | ct.UINT8,
    'DIR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'LUPD'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONESHOT'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMD'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x06, {
    'reg'	:   0x00 | ct.UINT16,
    'EVACT'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
    'TCINV'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCEI'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVFEO'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEO0'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEO1'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT8,
    'OVF'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ERR'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC1'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x09, {
    'reg'	:   0x00 | ct.UINT8,
    'OVF'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ERR'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC1'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x0A, {
    'reg'	:   0x00 | ct.UINT8,
    'OVF'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ERR'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC1'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUS'	: ( 0x0B, {
    'reg'	:   0x00 | ct.UINT8,
    'STOP'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLAVE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PERBUFV'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCBUFV0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCBUFV1'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'WAVE'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT8,
    'WAVEGEN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'DRVCTRL'	: ( 0x0D, {
    'reg'	:   0x00 | ct.UINT8,
    'INVEN0'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEN1'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DBGCTRL'	: ( 0x0F, {
    'reg'	:   0x00 | ct.UINT8,
    'DBGRUN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CTRLB'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'STATUS'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'COUNT'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'CC0'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'CC1'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'COUNT'	: 0x14 | ct.UINT16,
  'CC'	: ( 0x1C | ct.ARRAY, 2 | ct.UINT16 ),
  'CCBUF'	: ( 0x30 | ct.ARRAY, 2 | ct.UINT16 ),
}

TC_COUNT32 = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MODE'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
    'PRESCSYNC'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  2 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONDEMAND'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'PRESCALER'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'ALOCK'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'CAPTEN0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'CAPTEN1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'COPEN0'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'COPEN1'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
    'CAPTMODE0'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  2 << ct.BF_LEN,
    'CAPTMODE1'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'CTRLBCLR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT8,
    'DIR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'LUPD'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONESHOT'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMD'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'CTRLBSET'	: ( 0x05, {
    'reg'	:   0x00 | ct.UINT8,
    'DIR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'LUPD'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONESHOT'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMD'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x06, {
    'reg'	:   0x00 | ct.UINT16,
    'EVACT'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
    'TCINV'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCEI'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVFEO'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEO0'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEO1'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT8,
    'OVF'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ERR'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC1'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x09, {
    'reg'	:   0x00 | ct.UINT8,
    'OVF'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ERR'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC1'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x0A, {
    'reg'	:   0x00 | ct.UINT8,
    'OVF'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ERR'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC1'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUS'	: ( 0x0B, {
    'reg'	:   0x00 | ct.UINT8,
    'STOP'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLAVE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PERBUFV'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCBUFV0'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCBUFV1'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'WAVE'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT8,
    'WAVEGEN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'DRVCTRL'	: ( 0x0D, {
    'reg'	:   0x00 | ct.UINT8,
    'INVEN0'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEN1'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DBGCTRL'	: ( 0x0F, {
    'reg'	:   0x00 | ct.UINT8,
    'DBGRUN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CTRLB'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'STATUS'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'COUNT'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'CC0'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'CC1'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'COUNT'	: 0x14 | ct.UINT32,
  'CC'	: ( 0x1C | ct.ARRAY, 2 | ct.UINT32 ),
  'CCBUF'	: ( 0x30 | ct.ARRAY, 2 | ct.UINT32 ),
}

TC_ = {
  'COUNT8'	: ( 0x00, TC_COUNT8 ),
  'COUNT16'	: ( 0x00, TC_COUNT16 ),
  'COUNT32'	: ( 0x00, TC_COUNT32 ),
}

TC0 = ct.struct(0x40003800, TC_)
