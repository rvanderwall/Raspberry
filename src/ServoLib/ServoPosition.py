#!/usr/bin/python

import json
from ServoConfig import ServoConfig
from Servo import Servo


servo_config = ServoConfig.pick_servo_type(0)
servo0 = Servo(servo_config)

print("Enter an angle between 1 and 180. 0 to quit")
angle = 1
while angle > 0:
    angle = int(raw_input('angle: '))
    servo0.move_to_angle(angle)

