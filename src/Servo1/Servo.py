#!/usr/bin/python

import time

from AdaFruitLib.Adafruit_PWM_Servo_Driver import PWM


# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

# 100 Hz seems to work well.  60 seems to jitter a lot
pwm.setPWMFreq(100)

#
# Angle is in degrees between 0 and 180
#
CCW_ANGLE = 0.0
CW_ANGLE = 180.0

servoMin = 0     # Min pulse length out of 4096
servoMax = 4000  # Max pulse length out of 4096

class Servo():
    def __init__(self, servo_id, ccw_on_time, cw_on_time):
        self.servo_id = servo_id
	self.__servo_offset = ccw_on_time
        self.__servo_scale = (cw_on_time - ccw_on_time) / CW_ANGLE
        print("scale:{}  offset:{}".format(self.__servo_scale, self.__servo_offset))

        self.old_angle = 0

    def move_to_angle(self, angle):
        if angle < CCW_ANGLE:
            angle = CCW_ANGLE
        if angle > CW_ANGLE:
            angle = CW_ANGLE

        #print("angle: {}".format(angle))

        off_time = 0
        on_time = int(angle * self.__servo_scale + self.__servo_offset)
        #print("Set servo off:{}  on:{}".format(off_time, on_time))
        pwm.setPWM(self.servo_id, off_time, on_time)

        delta = self.old_angle - angle
        if delta < 0:
            delta = -delta
        self.old_angle = angle
        sleep_time = delta / 50
        sleep_time = 0.200
        time.sleep(sleep_time)
        
    def set_on_time_directly(self, on_time):
        off_time = 0
        pwm.setPWM(self.servo_id, off_time, on_time)

    def setServoPulse(channel, pulse):
      pulseLength = 1000000                   # 1,000,000 us per second
      pulseLength /= 60                       # 60 Hz
      print "%d us per period" % pulseLength
      pulseLength /= 4096                     # 12 bits of resolution
      print "%d us per bit" % pulseLength
      pulse *= 1000
      pulse /= pulseLength
      pwm.setPWM(channel, 0, pulse)

