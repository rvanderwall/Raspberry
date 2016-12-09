#!/usr/bin/python

from Servo import Servo
from Position import Position

servo0 = Servo(0)
servo1 = Servo(1)
p = Position()

while True:
        (x_pos, y_pos, z_pos) = p.get_position()
        print("X:{} Y:{} Z:{}".format(x_pos, y_pos, z_pos))

        x_pos_target  = int((1.0 + x_pos) * 50)
        y_pos_target  = int((1.0 + y_pos) * 50)

        servo0.move_to_position(x_pos_target)
        servo1.move_to_position(y_pos_target)
