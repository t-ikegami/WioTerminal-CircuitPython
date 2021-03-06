import uctypes as ct

I2S_ = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'SWRST'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CKEN0'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CKEN1'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXEN'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXEN'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CLKCTRL'	: ( 0x04 | ct.ARRAY, 2, {
    'reg'	:   0x00 | ct.UINT32,
    'SLOTSIZE'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'NBSLOTS'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  3 << ct.BF_LEN,
    'FSWIDTH'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  2 << ct.BF_LEN,
    'BITDELAY'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'FSSEL'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'FSINV'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'FSOUTINV'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'SCKSEL'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'SCKOUTINV'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCKSEL'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCKEN'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCKOUTINV'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCKDIV'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  6 << ct.BF_LEN,
    'MCKOUTDIV'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  6 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT16,
    'RXRDY0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXRDY1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXOR0'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXOR1'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXRDY0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXRDY1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXUR0'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXUR1'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT16,
    'RXRDY0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXRDY1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXOR0'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXOR1'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXRDY0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXRDY1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXUR0'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXUR1'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x14, {
    'reg'	:   0x00 | ct.UINT16,
    'RXRDY0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXRDY1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXOR0'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXOR1'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXRDY0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXRDY1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXUR0'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXUR1'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x18, {
    'reg'	:   0x00 | ct.UINT16,
    'SWRST'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CKEN0'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CKEN1'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXEN'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXEN'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'TXDATA'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXDATA'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'TXCTRL'	: ( 0x20, {
    'reg'	:   0x00 | ct.UINT32,
    'SERMODE'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'TXDEFAULT'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
    'TXSAME'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'CLKSEL'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTADJ'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'DATASIZE'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'WORDADJ'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'EXTEND'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  2 << ct.BF_LEN,
    'BITREV'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS4'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS5'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS6'	:   0x00 | ct.BFUINT32 | 22 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS7'	:   0x00 | ct.BFUINT32 | 23 << ct.BF_POS |  1 << ct.BF_LEN,
    'MONO'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'DMA'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'RXCTRL'	: ( 0x24, {
    'reg'	:   0x00 | ct.UINT32,
    'SERMODE'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'CLKSEL'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTADJ'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'DATASIZE'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'WORDADJ'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'EXTEND'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  2 << ct.BF_LEN,
    'BITREV'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS4'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS5'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS6'	:   0x00 | ct.BFUINT32 | 22 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLOTDIS7'	:   0x00 | ct.BFUINT32 | 23 << ct.BF_POS |  1 << ct.BF_LEN,
    'MONO'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'DMA'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'RXLOOP'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'TXDATA'	: 0x30 | ct.UINT32,
  'RXDATA'	: 0x34 | ct.UINT32,
}

I2S = ct.struct(0x43002800, I2S_)
