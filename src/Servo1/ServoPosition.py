#!/usr/bin/python

import time
from Servo import Servo
from Position import Position


CCW=250
CW=1050
servo0 = Servo(0, CCW, CW)


print("Enter an angle between 0 and 180")


angle = 1
while angle > 0:
	angle = int(raw_input('angle: '))
	servo0.move_to_angle(angle)

