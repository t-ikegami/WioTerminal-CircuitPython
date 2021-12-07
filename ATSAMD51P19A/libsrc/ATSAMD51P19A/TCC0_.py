import uctypes as ct

TCC_ = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'RESOLUTION'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  2 << ct.BF_LEN,
    'PRESCALER'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'PRESCSYNC'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  2 << ct.BF_LEN,
    'ALOCK'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'MSYNC'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'DMAOS'	:   0x00 | ct.BFUINT32 | 23 << ct.BF_POS |  1 << ct.BF_LEN,
    'CPTEN0'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'CPTEN1'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'CPTEN2'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'CPTEN3'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
    'CPTEN4'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  1 << ct.BF_LEN,
    'CPTEN5'	:   0x00 | ct.BFUINT32 | 29 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'CTRLBCLR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT8,
    'DIR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'LUPD'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONESHOT'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'IDXCMD'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  2 << ct.BF_LEN,
    'CMD'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'CTRLBSET'	: ( 0x05, {
    'reg'	:   0x00 | ct.UINT8,
    'DIR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'LUPD'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONESHOT'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'IDXCMD'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  2 << ct.BF_LEN,
    'CMD'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CTRLB'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'STATUS'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'COUNT'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PATT'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'WAVE'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PER'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CC0'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CC1'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'CC2'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'CC3'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'CC4'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'CC5'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'FCTRLA'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT32,
    'SRC'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'KEEP'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'QUAL'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'BLANK'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  2 << ct.BF_LEN,
    'RESTART'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'HALT'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  2 << ct.BF_LEN,
    'CHSEL'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  2 << ct.BF_LEN,
    'CAPTURE'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  3 << ct.BF_LEN,
    'BLANKPRESC'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'BLANKVAL'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  8 << ct.BF_LEN,
    'FILTERVAL'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'FCTRLB'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'SRC'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'KEEP'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'QUAL'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'BLANK'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  2 << ct.BF_LEN,
    'RESTART'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'HALT'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  2 << ct.BF_LEN,
    'CHSEL'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  2 << ct.BF_LEN,
    'CAPTURE'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  3 << ct.BF_LEN,
    'BLANKPRESC'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'BLANKVAL'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  8 << ct.BF_LEN,
    'FILTERVAL'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'WEXCTRL'	: ( 0x14, {
    'reg'	:   0x00 | ct.UINT32,
    'OTMX'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'DTIEN0'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'DTIEN1'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'DTIEN2'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'DTIEN3'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'DTLS'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  8 << ct.BF_LEN,
    'DTHS'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  8 << ct.BF_LEN,
  }),
  'DRVCTRL'	: ( 0x18, {
    'reg'	:   0x00 | ct.UINT32,
    'NRE0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRE1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRE2'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRE3'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRE4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRE5'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRE6'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRE7'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRV0'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRV1'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRV2'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRV3'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRV4'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRV5'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRV6'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'NRV7'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEN0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEN1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEN2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEN3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEN4'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEN5'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEN6'	:   0x00 | ct.BFUINT32 | 22 << ct.BF_POS |  1 << ct.BF_LEN,
    'INVEN7'	:   0x00 | ct.BFUINT32 | 23 << ct.BF_POS |  1 << ct.BF_LEN,
    'FILTERVAL0'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  4 << ct.BF_LEN,
    'FILTERVAL1'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'DBGCTRL'	: ( 0x1E, {
    'reg'	:   0x00 | ct.UINT8,
    'DBGRUN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'FDDBD'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x20, {
    'reg'	:   0x00 | ct.UINT32,
    'EVACT0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
    'EVACT1'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  3 << ct.BF_LEN,
    'CNTSEL'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  2 << ct.BF_LEN,
    'OVFEO'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'TRGEO'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'CNTEO'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCINV0'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCINV1'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCEI0'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCEI1'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEI0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEI1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEI2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEI3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEI4'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEI5'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEO0'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEO1'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEO2'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEO3'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEO4'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCEO5'	:   0x00 | ct.BFUINT32 | 29 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x24, {
    'reg'	:   0x00 | ct.UINT32,
    'OVF'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'TRG'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CNT'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'ERR'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'UFS'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFS'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULTA'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULTB'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULT0'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULT1'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC4'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC5'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x28, {
    'reg'	:   0x00 | ct.UINT32,
    'OVF'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'TRG'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CNT'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'ERR'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'UFS'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFS'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULTA'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULTB'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULT0'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULT1'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC4'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC5'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x2C, {
    'reg'	:   0x00 | ct.UINT32,
    'OVF'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'TRG'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CNT'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'ERR'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'UFS'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFS'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULTA'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULTB'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULT0'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULT1'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC4'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'MC5'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUS'	: ( 0x30, {
    'reg'	:   0x00 | ct.UINT32,
    'STOP'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'IDX'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'UFS'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFS'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'SLAVE'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PATTBUFV'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PERBUFV'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULTAIN'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULTBIN'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULT0IN'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULT1IN'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULTA'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULTB'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULT0'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAULT1'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCBUFV0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCBUFV1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCBUFV2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCBUFV3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCBUFV4'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCBUFV5'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP0'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP1'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP2'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP3'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP4'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMP5'	:   0x00 | ct.BFUINT32 | 29 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'COUNT'	: ( 0x34, {
    'reg'	:   0x00 | ct.UINT32,
    'COUNT'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 24 << ct.BF_LEN,
  }),
  'COUNT_DITH4_MODE'	: ( 0x34, {
    'reg'	:   0x00 | ct.UINT32,
    'COUNT'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS | 20 << ct.BF_LEN,
  }),
  'COUNT_DITH5_MODE'	: ( 0x34, {
    'reg'	:   0x00 | ct.UINT32,
    'COUNT'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS | 19 << ct.BF_LEN,
  }),
  'COUNT_DITH6_MODE'	: ( 0x34, {
    'reg'	:   0x00 | ct.UINT32,
    'COUNT'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS | 18 << ct.BF_LEN,
  }),
  'PATT'	: ( 0x38, {
    'reg'	:   0x00 | ct.UINT16,
    'PGE0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGE1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGE2'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGE3'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGE4'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGE5'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGE6'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGE7'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGV0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGV1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGV2'	:   0x00 | ct.BFUINT16 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGV3'	:   0x00 | ct.BFUINT16 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGV4'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGV5'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGV6'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGV7'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'WAVE'	: ( 0x3C, {
    'reg'	:   0x00 | ct.UINT32,
    'WAVEGEN'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
    'RAMP'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  2 << ct.BF_LEN,
    'CIPEREN'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CICCEN0'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'CICCEN1'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'CICCEN2'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'CICCEN3'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'POL0'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'POL1'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'POL2'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'POL3'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'POL4'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'POL5'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
    'SWAP0'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'SWAP1'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'SWAP2'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'SWAP3'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'PER'	: ( 0x40, {
    'reg'	:   0x00 | ct.UINT32,
    'PER'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 24 << ct.BF_LEN,
  }),
  'PER_DITH4_MODE'	: ( 0x40, {
    'reg'	:   0x00 | ct.UINT32,
    'DITHER'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'PER'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS | 20 << ct.BF_LEN,
  }),
  'PER_DITH5_MODE'	: ( 0x40, {
    'reg'	:   0x00 | ct.UINT32,
    'DITHER'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  5 << ct.BF_LEN,
    'PER'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS | 19 << ct.BF_LEN,
  }),
  'PER_DITH6_MODE'	: ( 0x40, {
    'reg'	:   0x00 | ct.UINT32,
    'DITHER'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  6 << ct.BF_LEN,
    'PER'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS | 18 << ct.BF_LEN,
  }),
  'CC'	: ( 0x44 | ct.ARRAY, 6, {
    'reg'	:   0x00 | ct.UINT32,
    'CC'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 24 << ct.BF_LEN,
  }),
  'CC_DITH4_MODE'	: ( 0x44 | ct.ARRAY, 6, {
    'reg'	:   0x00 | ct.UINT32,
    'DITHER'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'CC'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS | 20 << ct.BF_LEN,
  }),
  'CC_DITH5_MODE'	: ( 0x44 | ct.ARRAY, 6, {
    'reg'	:   0x00 | ct.UINT32,
    'DITHER'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  5 << ct.BF_LEN,
    'CC'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS | 19 << ct.BF_LEN,
  }),
  'CC_DITH6_MODE'	: ( 0x44 | ct.ARRAY, 6, {
    'reg'	:   0x00 | ct.UINT32,
    'DITHER'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  6 << ct.BF_LEN,
    'CC'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS | 18 << ct.BF_LEN,
  }),
  'PATTBUF'	: ( 0x64, {
    'reg'	:   0x00 | ct.UINT16,
    'PGEB0'	:   0x00 | ct.BFUINT16 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGEB1'	:   0x00 | ct.BFUINT16 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGEB2'	:   0x00 | ct.BFUINT16 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGEB3'	:   0x00 | ct.BFUINT16 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGEB4'	:   0x00 | ct.BFUINT16 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGEB5'	:   0x00 | ct.BFUINT16 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGEB6'	:   0x00 | ct.BFUINT16 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGEB7'	:   0x00 | ct.BFUINT16 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGVB0'	:   0x00 | ct.BFUINT16 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGVB1'	:   0x00 | ct.BFUINT16 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGVB2'	:   0x00 | ct.BFUINT16 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGVB3'	:   0x00 | ct.BFUINT16 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGVB4'	:   0x00 | ct.BFUINT16 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGVB5'	:   0x00 | ct.BFUINT16 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGVB6'	:   0x00 | ct.BFUINT16 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'PGVB7'	:   0x00 | ct.BFUINT16 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'PERBUF'	: ( 0x6C, {
    'reg'	:   0x00 | ct.UINT32,
    'PERBUF'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 24 << ct.BF_LEN,
  }),
  'PERBUF_DITH4_MODE'	: ( 0x6C, {
    'reg'	:   0x00 | ct.UINT32,
    'DITHERBUF'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'PERBUF'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS | 20 << ct.BF_LEN,
  }),
  'PERBUF_DITH5_MODE'	: ( 0x6C, {
    'reg'	:   0x00 | ct.UINT32,
    'DITHERBUF'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  5 << ct.BF_LEN,
    'PERBUF'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS | 19 << ct.BF_LEN,
  }),
  'PERBUF_DITH6_MODE'	: ( 0x6C, {
    'reg'	:   0x00 | ct.UINT32,
    'DITHERBUF'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  6 << ct.BF_LEN,
    'PERBUF'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS | 18 << ct.BF_LEN,
  }),
  'CCBUF'	: ( 0x70 | ct.ARRAY, 6, {
    'reg'	:   0x00 | ct.UINT32,
    'CCBUF'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 24 << ct.BF_LEN,
  }),
  'CCBUF_DITH4_MODE'	: ( 0x70 | ct.ARRAY, 6, {
    'reg'	:   0x00 | ct.UINT32,
    'CCBUF'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'DITHERBUF'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS | 20 << ct.BF_LEN,
  }),
  'CCBUF_DITH5_MODE'	: ( 0x70 | ct.ARRAY, 6, {
    'reg'	:   0x00 | ct.UINT32,
    'DITHERBUF'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  5 << ct.BF_LEN,
    'CCBUF'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS | 19 << ct.BF_LEN,
  }),
  'CCBUF_DITH6_MODE'	: ( 0x70 | ct.ARRAY, 6, {
    'reg'	:   0x00 | ct.UINT32,
    'DITHERBUF'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  6 << ct.BF_LEN,
    'CCBUF'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS | 18 << ct.BF_LEN,
  }),
}

TCC0 = ct.struct(0x41016000, TCC_)