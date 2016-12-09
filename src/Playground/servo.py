__author__ = 'robert'

from Servo1.Servo import Servo

s = Servo(2)
while True:
    pos = raw_input("Enter Position")
    s.move_to_position(pos)