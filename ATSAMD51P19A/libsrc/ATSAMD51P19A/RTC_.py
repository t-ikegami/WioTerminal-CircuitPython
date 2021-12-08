import uctypes as ct

RTC_MODE0 = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT16,
    'SWRST'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MODE'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
    'MATCHCLR'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'PRESCALER'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  4 << ct.BF_LEN,
    'BKTRST'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'GPTRST'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'COUNTSYNC'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CTRLB'	: ( 0x02, {
    'reg'	:   0x00 | ct.UINT16,
    'GP0EN'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP2EN'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBMAJ'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBASYNC'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'RTCOUT'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'DMAEN'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBF'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'ACTF'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'PEREO0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO2'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO3'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO5'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO6'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO7'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMPEO0'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMPEO1'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPEREO'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVFEO'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPEVEI'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT16,
    'PER0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER2'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER3'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER4'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER5'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER6'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER7'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPER'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVF'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x0A, {
    'reg'	:   0x00 | ct.UINT16,
    'PER0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER2'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER3'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER4'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER5'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER6'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER7'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPER'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVF'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT16,
    'PER0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER2'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER3'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER4'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER5'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER6'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER7'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPER'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVF'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DBGCTRL'	: ( 0x0E, {
    'reg'	:   0x00 | ct.UINT8,
    'DBGRUN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'FREQCORR'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'COUNT'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMP0'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMP1'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'COUNTSYNC'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'FREQCORR'	: ( 0x14, {
    'reg'	:   0x00 | ct.UINT8,
    'VALUE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  7 << ct.BF_LEN,
    'SIGN'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'COUNT'	: 0x18 | ct.UINT32,
  'COMP'	: ( 0x20 | ct.ARRAY, 2 | ct.UINT32 ),
  'GP'	: ( 0x40 | ct.ARRAY, 4 | ct.UINT32 ),
  'TAMPCTRL'	: ( 0x60, {
    'reg'	:   0x00 | ct.UINT32,
    'IN0ACT'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'IN1ACT'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
    'IN2ACT'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  2 << ct.BF_LEN,
    'IN3ACT'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  2 << ct.BF_LEN,
    'IN4ACT'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  2 << ct.BF_LEN,
    'TAMLVL0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMLVL1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMLVL2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMLVL3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMLVL4'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC0'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC1'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC2'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC3'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC4'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'TIMESTAMP'	: 0x64 | ct.UINT32,
  'TAMPID'	: ( 0x68, {
    'reg'	:   0x00 | ct.UINT32,
    'TAMPID0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPID1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPID2'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPID3'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPID4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPEVT'	:   0x00 | ct.BFUINT32 | 31 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'BKUP'	: ( 0x80 | ct.ARRAY, 8 | ct.UINT32 ),
}

RTC_MODE1 = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT16,
    'SWRST'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MODE'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
    'PRESCALER'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  4 << ct.BF_LEN,
    'BKTRST'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'GPTRST'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'COUNTSYNC'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CTRLB'	: ( 0x02, {
    'reg'	:   0x00 | ct.UINT16,
    'GP0EN'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP2EN'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBMAJ'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBASYNC'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'RTCOUT'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'DMAEN'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBF'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'ACTF'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'PEREO0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO2'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO3'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO5'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO6'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO7'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMPEO0'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMPEO1'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMPEO2'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMPEO3'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPEREO'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVFEO'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPEVEI'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT16,
    'PER0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER2'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER3'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER4'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER5'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER6'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER7'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP2'	:   0x00 | ct.BFUINT16 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP3'	:   0x00 | ct.BFUINT16 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPER'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVF'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x0A, {
    'reg'	:   0x00 | ct.UINT16,
    'PER0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER2'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER3'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER4'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER5'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER6'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER7'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP2'	:   0x00 | ct.BFUINT16 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP3'	:   0x00 | ct.BFUINT16 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPER'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVF'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT16,
    'PER0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER2'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER3'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER4'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER5'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER6'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER7'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP2'	:   0x00 | ct.BFUINT16 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP3'	:   0x00 | ct.BFUINT16 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPER'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVF'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DBGCTRL'	: ( 0x0E, {
    'reg'	:   0x00 | ct.UINT8,
    'DBGRUN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'FREQCORR'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'COUNT'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMP0'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMP1'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMP2'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'COMP3'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'COUNTSYNC'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'FREQCORR'	: ( 0x14, {
    'reg'	:   0x00 | ct.UINT8,
    'VALUE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  7 << ct.BF_LEN,
    'SIGN'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'COUNT'	: 0x18 | ct.UINT16,
  'PER'	: 0x1C | ct.UINT16,
  'COMP'	: ( 0x20 | ct.ARRAY, 4 | ct.UINT16 ),
  'GP'	: ( 0x40 | ct.ARRAY, 4 | ct.UINT32 ),
  'TAMPCTRL'	: ( 0x60, {
    'reg'	:   0x00 | ct.UINT32,
    'IN0ACT'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'IN1ACT'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
    'IN2ACT'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  2 << ct.BF_LEN,
    'IN3ACT'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  2 << ct.BF_LEN,
    'IN4ACT'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  2 << ct.BF_LEN,
    'TAMLVL0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMLVL1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMLVL2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMLVL3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMLVL4'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC0'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC1'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC2'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC3'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC4'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'TIMESTAMP'	: ( 0x64, {
    'reg'	:   0x00 | ct.UINT32,
    'COUNT'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
  'TAMPID'	: ( 0x68, {
    'reg'	:   0x00 | ct.UINT32,
    'TAMPID0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPID1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPID2'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPID3'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPID4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPEVT'	:   0x00 | ct.BFUINT32 | 31 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'BKUP'	: ( 0x80 | ct.ARRAY, 8 | ct.UINT32 ),
}

RTC_MODE2 = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT16,
    'SWRST'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MODE'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
    'CLKREP'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'MATCHCLR'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'PRESCALER'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  4 << ct.BF_LEN,
    'BKTRST'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'GPTRST'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'CLOCKSYNC'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CTRLB'	: ( 0x02, {
    'reg'	:   0x00 | ct.UINT16,
    'GP0EN'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP2EN'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBMAJ'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBASYNC'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'RTCOUT'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'DMAEN'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBF'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'ACTF'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'PEREO0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO2'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO3'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO5'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO6'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PEREO7'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALARMEO0'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALARMEO1'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPEREO'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVFEO'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPEVEI'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT16,
    'PER0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER2'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER3'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER4'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER5'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER6'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER7'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALARM0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALARM1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPER'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVF'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x0A, {
    'reg'	:   0x00 | ct.UINT16,
    'PER0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER2'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER3'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER4'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER5'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER6'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER7'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALARM0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALARM1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPER'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVF'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT16,
    'PER0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER2'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER3'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER4'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER5'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER6'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER7'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALARM0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALARM1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPER'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVF'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DBGCTRL'	: ( 0x0E, {
    'reg'	:   0x00 | ct.UINT8,
    'DBGRUN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'FREQCORR'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CLOCK'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALARM0'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALARM1'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'MASK0'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'MASK1'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'CLOCKSYNC'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'GP3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'FREQCORR'	: ( 0x14, {
    'reg'	:   0x00 | ct.UINT8,
    'VALUE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  7 << ct.BF_LEN,
    'SIGN'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CLOCK'	: ( 0x18, {
    'reg'	:   0x00 | ct.UINT32,
    'SECOND'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  6 << ct.BF_LEN,
    'MINUTE'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  6 << ct.BF_LEN,
    'HOUR'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  5 << ct.BF_LEN,
    'DAY'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  5 << ct.BF_LEN,
    'MONTH'	:   0x00 | ct.BFUINT32 | 22 << ct.BF_POS |  4 << ct.BF_LEN,
    'YEAR'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  6 << ct.BF_LEN,
  }),
  'GP'	: ( 0x40 | ct.ARRAY, 4 | ct.UINT32 ),
  'ALARM0'	: ( 0x20, {
    'reg'	:   0x00 | ct.UINT32,
    'SECOND'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  6 << ct.BF_LEN,
    'MINUTE'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  6 << ct.BF_LEN,
    'HOUR'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  5 << ct.BF_LEN,
    'DAY'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  5 << ct.BF_LEN,
    'MONTH'	:   0x00 | ct.BFUINT32 | 22 << ct.BF_POS |  4 << ct.BF_LEN,
    'YEAR'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  6 << ct.BF_LEN,
  }),
  'MASK0'	: ( 0x24, {
    'reg'	:   0x00 | ct.UINT8,
    'SEL'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'ALARM1'	: ( 0x28, {
    'reg'	:   0x00 | ct.UINT32,
    'SECOND'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  6 << ct.BF_LEN,
    'MINUTE'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  6 << ct.BF_LEN,
    'HOUR'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  5 << ct.BF_LEN,
    'DAY'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  5 << ct.BF_LEN,
    'MONTH'	:   0x00 | ct.BFUINT32 | 22 << ct.BF_POS |  4 << ct.BF_LEN,
    'YEAR'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  6 << ct.BF_LEN,
  }),
  'MASK1'	: ( 0x2C, {
    'reg'	:   0x00 | ct.UINT8,
    'SEL'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'TAMPCTRL'	: ( 0x60, {
    'reg'	:   0x00 | ct.UINT32,
    'IN0ACT'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'IN1ACT'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
    'IN2ACT'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  2 << ct.BF_LEN,
    'IN3ACT'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  2 << ct.BF_LEN,
    'IN4ACT'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  2 << ct.BF_LEN,
    'TAMLVL0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMLVL1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMLVL2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMLVL3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMLVL4'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC0'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC1'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC2'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC3'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
    'DEBNC4'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'TIMESTAMP'	: ( 0x64, {
    'reg'	:   0x00 | ct.UINT32,
    'SECOND'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  6 << ct.BF_LEN,
    'MINUTE'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  6 << ct.BF_LEN,
    'HOUR'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  5 << ct.BF_LEN,
    'DAY'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  5 << ct.BF_LEN,
    'MONTH'	:   0x00 | ct.BFUINT32 | 22 << ct.BF_POS |  4 << ct.BF_LEN,
    'YEAR'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  6 << ct.BF_LEN,
  }),
  'TAMPID'	: ( 0x68, {
    'reg'	:   0x00 | ct.UINT32,
    'TAMPID0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPID1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPID2'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPID3'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPID4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'TAMPEVT'	:   0x00 | ct.BFUINT32 | 31 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'BKUP'	: ( 0x80 | ct.ARRAY, 8 | ct.UINT32 ),
}

RTC_ = {
  'MODE0'	: ( 0x00, RTC_MODE0 ),
  'MODE1'	: ( 0x00, RTC_MODE1 ),
  'MODE2'	: ( 0x00, RTC_MODE2 ),
}

RTC = ct.struct(0x40002400, RTC_, ct.LITTLE_ENDIAN)
