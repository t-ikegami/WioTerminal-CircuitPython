import board
import busio
import struct
from .crc16 import crc16

class Transport :
    def __init__(self, tx = board.RTL_MOSI, rx = board.RTL_MISO, baudrate = 614400) :
        self.uart = busio.UART(tx, rx, baudrate = baudrate, timeout = 60, receiver_buffer_size = 4096)
        self.header = bytearray(4)

    def deinit(self) :
        self.uart.deinit()

    def reset(self) :
        self.uart.reset_input_buffer()
        
    def send(self, message) :
        struct.pack_into("<HH", self.header, 0, len(message), crc16(message))
        self.uart.write(self.header)
        self.uart.write(message)

    def receive(self) :
        if self.uart.readinto(self.header) != 4 :
            raise RuntimeError("No responce for Transport.receive.")
        size, crc = struct.unpack("<HH", self.header)
        message = self.uart.read(size)
        if crc != crc16(message) : raise RuntimeError("Invalid message CRC")
        return message
