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
    def lis3d_setup(cls) :
        cls.count += 1
        if cls.i2c is not None : return
        assert cls.acc is None and cls.int is None and cls.count == 1
        cls.i2c = busio.I2C(board.GYROSCOPE_SCL, board.GYROSCOPE_SDA)
        cls.int = dio.DigitalInOut(board.GYROSCOPE_INT)
        cls.acc = LIS3DH_I2C(cls.i2c, address = 0x18, int1 = cls.int)
        cls.acc.set_tap(1, 80)

    @classmethod
    def lis3d_free(cls) :
        cls.count -= 1
        if cls.count > 0 : return
        cls.lis3d = None
        cls.int.deinit()
        cls.int = None
        cls.i2c.deinit()
        cls.i2c = None

    def __init__(self, mid = 3.0) :
        self.lis3d_setup()
        self.state = 0
        self.mid = mid		# mid threshold
        self.motion()		# fill state

    def deinit(self) :
        if self.state is None : raise RuntimeError("MotionEvents is already deinited.")
        self.lis3d_free()
        self.state = None
        
    def motion(self) :
        acc = self.acc.acceleration
        state = 0
        state |= self.M_FACE_MID  if abs(acc[2]) < self.mid else \
                 self.M_FACE_UP   if acc[2] < 0 else \
                 self.M_FACE_DOWN
        state |= self.M_HEAD_MID  if abs(acc[0]) < self.mid else \
                 self.M_HEAD_UP   if acc[0] > 0 else \
                 self.M_FACE_DOWN
        state |= self.M_LEFT_MID  if abs(acc[1]) < self.mid else \
                 self.M_LEFT_UP   if acc[1] < 0 else \
                 self.M_LEFT_DOWN

        events = (self.state ^ state) & state
        if self.acc.tapped : events |= self.M_TAPPED
        self.state = state

        return events

    
