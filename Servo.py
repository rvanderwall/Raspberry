#!/usr/bin/python

import smbus
import math
import time

from Adafruit_PWM_Servo_Driver import PWM


pwm = None
class Servo:
    servoMin = 100  # Min pulse length out of 4096
    servoMax = 700 # Max pulse length out of 4096
    servo_number = 0
    
    def __init__(self, servo_num):
        global pwm
        self.servo_number = servo_num
        # Initialise the PWM device using the default address
        if pwm == None:
            pwm = PWM(0x40, debug=False)
            pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

    def move_to_position(self, position):
        pulse = self.__position_to_pulse_width(position)
        pwm.setPWM(self.servo_number, 0, pulse)

    def __position_to_pulse_width(self, position):
        conversion = (self.servoMax - self.servoMin)/100
        pulse = conversion * position + self.servoMin
        return pulse
    
def main():
    servo0 = Servo(0)
    servo1 = Servo(1)
    position = 0
    direction = 1
    while(True):
        if position > 100:
            direction = -1
        if position < 0:
            direction = 1
        position += direction
        servo0.move_to_position(position)
        servo1.move_to_position(position)
        time.sleep(0.01)
        
if __name__ == "__main__":
    main()
