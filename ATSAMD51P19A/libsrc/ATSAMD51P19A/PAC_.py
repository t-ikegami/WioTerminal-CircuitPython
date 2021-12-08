import uctypes as ct

PAC_ = {
  'WRCTRL'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'PERID'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 16 << ct.BF_LEN,
    'KEY'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  8 << ct.BF_LEN,
  }),
  'EVCTRL'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT8,
    'ERREO'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT8,
    'ERR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x09, {
    'reg'	:   0x00 | ct.UINT8,
    'ERR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAGAHB'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'FLASH'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'FLASH_ALT'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'SEEPROM'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'RAMCM4S'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'RAMPPPDSU'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'RAMDMAWR'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'RAMDMACICM'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'HPB0'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'HPB1'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'HPB2'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'HPB3'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'PUKCC'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'SDHC0'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'SDHC1'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'QSPI'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'BKUPRAM'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAGA'	: ( 0x14, {
    'reg'	:   0x00 | ct.UINT32,
    'PAC'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PM'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCLK'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'RSTC'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'OSCCTRL'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'OSC32KCTRL'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'SUPC'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'GCLK'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'WDT'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'RTC'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'EIC'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'FREQM'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM0'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM1'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC0'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC1'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAGB'	: ( 0x18, {
    'reg'	:   0x00 | ct.UINT32,
    'USB'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'DSU'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'NVMCTRL'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMCC'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PORT'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'DMAC'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'HMATRIX'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'EVSYS'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM2'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM3'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCC0'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCC1'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC2'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC3'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'RAMECC'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAGC'	: ( 0x1C, {
    'reg'	:   0x00 | ct.UINT32,
    'TCC2'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCC3'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC4'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC5'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PDEC'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'AC'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'AES'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TRNG'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'ICM'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'PUKCC'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'QSPI'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCL'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAGD'	: ( 0x20, {
    'reg'	:   0x00 | ct.UINT32,
    'SERCOM4'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM5'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM6'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM7'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCC4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC6'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC7'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'ADC0'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'ADC1'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'DAC'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'I2S'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'PCC'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUSA'	: ( 0x34, {
    'reg'	:   0x00 | ct.UINT32,
    'PAC'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'PM'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'MCLK'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'RSTC'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'OSCCTRL'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'OSC32KCTRL'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'SUPC'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'GCLK'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'WDT'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'RTC'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'EIC'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'FREQM'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM0'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM1'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC0'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC1'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUSB'	: ( 0x38, {
    'reg'	:   0x00 | ct.UINT32,
    'USB'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'DSU'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'NVMCTRL'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CMCC'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PORT'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'DMAC'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'HMATRIX'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'EVSYS'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM2'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM3'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCC0'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCC1'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC2'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC3'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'RAMECC'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUSC'	: ( 0x3C, {
    'reg'	:   0x00 | ct.UINT32,
    'TCC2'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCC3'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC4'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC5'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'PDEC'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'AC'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'AES'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'TRNG'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'ICM'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'PUKCC'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'QSPI'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCL'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUSD'	: ( 0x40, {
    'reg'	:   0x00 | ct.UINT32,
    'SERCOM4'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM5'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM6'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'SERCOM7'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'TCC4'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC6'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'TC7'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'ADC0'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'ADC1'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'DAC'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'I2S'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'PCC'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
}

PAC = ct.struct(0x40000000, PAC_, ct.LITTLE_ENDIAN)
