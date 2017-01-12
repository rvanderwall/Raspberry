#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

servoMin = 100  # Min pulse length out of 4096
servoMax = 700  # Max pulse length out of 4096

class Servo():
    def __init__(self, servo_id):
        self.servo_id = servo_id
        self.old_position = servoMin
        self.__servo_offset = servoMin
        self.__servo_scale = (servoMax - servoMin)/100

    def setServoPulse(channel, pulse):
      pulseLength = 1000000                   # 1,000,000 us per second
      pulseLength /= 60                       # 60 Hz
      print "%d us per period" % pulseLength
      pulseLength /= 4096                     # 12 bits of resolution
      print "%d us per bit" % pulseLength
      pulse *= 1000
      pulse /= pulseLength
      pwm.setPWM(channel, 0, pulse)


    def move_to_position(self, position):
        if position < 0:
            position = 0
        if position > 100:
            position = 100

        off_time = 0
        on_time = self.__servo_scale * position + self.__servo_offset
        pwm.setPWM(self.servo_id, off_time, on_time)
        delta = self.old_position - position
        if delta < 0:
            delta = -delta
        self.old_position = position
        sleep_time = delta / 20
        print("Delay for {} second".format(sleep_time))
        time.sleep(sleep_time)
        

