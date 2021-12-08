import uctypes as ct

PORT_GROUP = {
  'DIR'	: 0x00 | ct.UINT32,
  'DIRCLR'	: 0x04 | ct.UINT32,
  'DIRSET'	: 0x08 | ct.UINT32,
  'DIRTGL'	: 0x0C | ct.UINT32,
  'OUT'	: 0x10 | ct.UINT32,
  'OUTCLR'	: 0x14 | ct.UINT32,
  'OUTSET'	: 0x18 | ct.UINT32,
  'OUTTGL'	: 0x1C | ct.UINT32,
  'IN'	: 0x20 | ct.UINT32,
  'CTRL'	: 0x24 | ct.UINT32,
  'WRCONFIG'	: ( 0x28, {
    'reg'	:   0x00 | ct.UINT32,
    'PINMASK'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 16 << ct.BF_LEN,
    'PMUXEN'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'INEN'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'PULLEN'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'DRVSTR'	:   0x00 | ct.BFUINT32 | 22 << ct.BF_POS |  1 << ct.BF_LEN,
    'PMUX'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  4 << ct.BF_LEN,
    'WRPMUX'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  1 << ct.BF_LEN,
    'WRPINCFG'	:   0x00 | ct.BFUINT32 | 30 << ct.BF_POS |  1 << ct.BF_LEN,
    'HWSEL'	:   0x00 | ct.BFUINT32 | 31 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x2C, {
    'reg'	:   0x00 | ct.UINT32,
    'PID0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  5 << ct.BF_LEN,
    'EVACT0'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  2 << ct.BF_LEN,
    'PORTEI0'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'PID1'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  5 << ct.BF_LEN,
    'EVACT1'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  2 << ct.BF_LEN,
    'PORTEI1'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'PID2'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  5 << ct.BF_LEN,
    'EVACT2'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  2 << ct.BF_LEN,
    'PORTEI2'	:   0x00 | ct.BFUINT32 | 23 << ct.BF_POS |  1 << ct.BF_LEN,
    'PID3'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  5 << ct.BF_LEN,
    'EVACT3'	:   0x00 | ct.BFUINT32 | 29 << ct.BF_POS |  2 << ct.BF_LEN,
    'PORTEI3'	:   0x00 | ct.BFUINT32 | 31 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'PMUX'	: ( 0x30 | ct.ARRAY, 16, {
    'reg'	:   0x00 | ct.UINT8,
    'PMUXE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'PMUXO'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'PINCFG'	: ( 0x40 | ct.ARRAY, 32, {
    'reg'	:   0x00 | ct.UINT8,
    'PMUXEN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'INEN'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PULLEN'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'DRVSTR'	:   0x00 | ct.BFUINT8 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DUMMY_FILLER'	: 0x7F | ct.UINT8,
}

PORT_ = {
  'GROUP'	: ( 0x00 | ct.ARRAY, 4, PORT_GROUP ),
}

PORT = ct.struct(0x41008000, PORT_, ct.LITTLE_ENDIAN)
