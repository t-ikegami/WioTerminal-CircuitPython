import array
from micropython import const

# Left-shift CRC16-CCITT
_CRC16_POLY  = const(0x1021)
_CRC16_START = const(0xEF4A)

def _crc16(data, start = _CRC16_START) :
    """Compute CRC16 for bytes/bytearray/memoryview data"""

    crc = start

    for b in data :
        crc ^= b << 8
        for _ in range(8) :
            crc = ((crc << 1) & 0xFFFF) ^ _CRC16_POLY if crc & 0x8000 else (crc << 1)
            
    return crc

def _compute_crc16_table() :
    return array.array("H", (_crc16(bytes([i]), 0) for i in range(256)))

_CRC16_TABLE = _compute_crc16_table()

def crc16(data) :
    """Compute CRC16 for bytes/bytearray/memoryview data"""
    
    crc = _CRC16_START
    for b in data :
        crc = ((crc << 8) & 0xFFFF) ^ _CRC16_TABLE[(crc >> 8) ^ b]
    return crc

