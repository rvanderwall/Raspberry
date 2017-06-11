#!/usr/bin/python

import time
from Servo import Servo
from Position import Position

servo0 = Servo(0)
servo1 = Servo(1)
p = Position()

x_pos = -1.0
y_pos = 0.0
while x_pos < 1.0:
        #(x_pos, y_pos, z_pos) = p.get_position()
	print
	print
        #print("X:{} Y:{} Z:{}".format(x_pos, y_pos, z_pos))
        print("X:{}".format(x_pos))

        x_pos_target  = int((1.0 + x_pos) * 50)
        servo0.move_to_position(x_pos_target)

        y_pos_target  = int((1.0 + y_pos) * 50)
        #servo1.move_to_position(y_pos_target)

	time.sleep(1)
	x_pos += 0.10
