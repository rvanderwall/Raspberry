__author__ = 'robert'

from Servo1.Servo import Servo

servo_num = raw_input("Which servo?")

s = Servo(int(servo_num))
while True:
    pos = raw_input("Enter Position")
    s.move_to_position(int(pos))
