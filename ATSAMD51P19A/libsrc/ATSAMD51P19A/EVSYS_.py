import uctypes as ct

EVSYS_CHANNEL = {
  'CHANNEL'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'EVGEN'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  7 << ct.BF_LEN,
    'PATH'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  2 << ct.BF_LEN,
    'EDGSEL'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  2 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONDEMAND'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CHINTENCLR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT8,
    'OVR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'EVD'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CHINTENSET'	: ( 0x05, {
    'reg'	:   0x00 | ct.UINT8,
    'OVR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'EVD'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CHINTFLAG'	: ( 0x06, {
    'reg'	:   0x00 | ct.UINT8,
    'OVR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'EVD'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CHSTATUS'	: ( 0x07, {
    'reg'	:   0x00 | ct.UINT8,
    'RDYUSR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSYCH'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
}

EVSYS_ = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'SWRST'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SWEVT'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'CHANNEL0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL2'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL3'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL5'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL6'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL7'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL8'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL9'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL10'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL11'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL12'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL13'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL14'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL15'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL16'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL17'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL18'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL19'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL20'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL21'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL22'	:   0x00 | ct.BFUINT32 | 22 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL23'	:   0x00 | ct.BFUINT32 | 23 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL24'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL25'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL26'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL27'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL28'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL29'	:   0x00 | ct.BFUINT32 | 29 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL30'	:   0x00 | ct.BFUINT32 | 30 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHANNEL31'	:   0x00 | ct.BFUINT32 | 31 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'PRICTRL'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT8,
    'PRI'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'RREN'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTPEND'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT16,
    'ID'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'OVR'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'EVD'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'READY'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSY'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTSTATUS'	: ( 0x14, {
    'reg'	:   0x00 | ct.UINT32,
    'CHINT0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHINT1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHINT2'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHINT3'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHINT4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHINT5'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHINT6'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHINT7'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHINT8'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHINT9'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHINT10'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'CHINT11'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'BUSYCH'	: ( 0x18, {
    'reg'	:   0x00 | ct.UINT32,
    'BUSYCH0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSYCH1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSYCH2'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSYCH3'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSYCH4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSYCH5'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSYCH6'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSYCH7'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSYCH8'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSYCH9'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSYCH10'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'BUSYCH11'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'READYUSR'	: ( 0x1C, {
    'reg'	:   0x00 | ct.UINT32,
    'READYUSR0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'READYUSR1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'READYUSR2'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'READYUSR3'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'READYUSR4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'READYUSR5'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'READYUSR6'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'READYUSR7'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'READYUSR8'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'READYUSR9'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'READYUSR10'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'READYUSR11'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CHANNEL'	: ( 0x20 | ct.ARRAY, 32, EVSYS_CHANNEL ),
  'USER'	: ( 0x120 | ct.ARRAY, 67, {
    'reg'	:   0x00 | ct.UINT32,
    'CHANNEL'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  6 << ct.BF_LEN,
  }),
}

EVSYS = ct.struct(0x4100e000, EVSYS_)
