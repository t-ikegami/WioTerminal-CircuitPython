import struct
import board
import busio
import digitalio as dio
from adafruit_lis3dh import LIS3DH_I2C

# On Wio Terminal, the positive direction of the acceleration vector
# is oriented to (top, right, back) of the screeen.  That is, under
# the stationary condition with the normal gravitation, the zenith
# direction is measured with (top, right, back) coordinate.  For
# example, under the face-up situation, acceleration gives (0, 0,
# -9.8).

class MotionEvents :
    i2c   = None
    acc   = None
    int   = None
    count = 0

    M_FACE_UP   = 1 << 0
    M_FACE_MID  = 1 << 1
    M_FACE_DOWN = 1 << 2
    M_HEAD_UP   = 1 << 4
    M_HEAD_MID  = 1 << 5
    M_HEAD_DOWN = 1 << 6
    M_LEFT_UP   = 1 << 8
    M_LEFT_MID  = 1 << 9
    M_LEFT_DOWN = 1 << 10
    M_TAPPED    = 1 << 12

    @classmethod
    def lis3dh_setup(cls) :
        """Setup LIS3DH as 3 axis enabled, +-2g range, 400 Hz data rate,
        high-resolution & BDU, and latch interrupt for single tap
        detection.

        """
        cls.count += 1
        if cls.i2c is not None : return
        assert cls.acc is None and cls.int is None and cls.count == 1
        cls.i2c = busio.I2C(board.GYROSCOPE_SCL, board.GYROSCOPE_SDA)
        cls.int = dio.DigitalInOut(board.GYROSCOPE_INT)
        cls.acc = LIS3DH_I2C(cls.i2c, address = 0x18, int1 = cls.int)
        cls.acc.set_tap(1, 80)

    @classmethod
    def lis3dh_free(cls) :
        cls.count -= 1
        if cls.count > 0 : return
        cls.acc = None
        cls.int.deinit()
        cls.int = None
        cls.i2c.deinit()
        cls.i2c = None

    def __init__(self, mid = 5000) :
        self.lis3dh_setup()
        self.state = 0
        self.mid = mid		# mid threshold; 5000 is about 3 m/s**2
        self.motion()		# fill state

    def deinit(self) :
        if self.state is None : raise RuntimeError("MotionEvents is already deinited.")
        self.lis3dh_free()
        self.state = None

    @property
    def acceleration(self) :
        """Returns accelerations for (x, y, z) axes."""
        return self.acc.acceleration
    
    def get_raw_acc(self) :
        """Returns +-32768 raw values which should be mapped on +-2g range."""
        return struct.unpack("<hhh", self.acc._read_register(0xA8, 6))

    def motion(self) :
        acc = self.get_raw_acc()
        state = 0
        state |= self.M_FACE_MID  if abs(acc[2]) < self.mid else \
                 self.M_FACE_UP   if acc[2] < 0 else \
                 self.M_FACE_DOWN
        state |= self.M_HEAD_MID  if abs(acc[0]) < self.mid else \
                 self.M_HEAD_UP   if acc[0] > 0 else \
                 self.M_HEAD_DOWN
        state |= self.M_LEFT_MID  if abs(acc[1]) < self.mid else \
                 self.M_LEFT_UP   if acc[1] < 0 else \
                 self.M_LEFT_DOWN

        events = (self.state ^ state) & state
        if self.acc.tapped : events |= self.M_TAPPED

        self.state = state

        return events

    
