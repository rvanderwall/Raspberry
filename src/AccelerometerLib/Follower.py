#!/usr/bin/python

import time
from ServoLib.Servo import Servo
from ServoLib.ServoConfig import ServoConfig
from PositionSensor import PositionSensor

config0 = ServoConfig.pick_servo_type(0)
servo0 = Servo(config0)
config1 = ServoConfig.pick_servo_type(1)
servo1 = Servo(config1)

p = PositionSensor()

while True:
    (x_pos, y_pos, z_pos) = p.get_position()
    print
    print
    print("X:{} Y:{} Z:{}".format(x_pos, y_pos, z_pos))

    x_target_angle  = int((1.0 + x_pos) * 90)
    servo0.move_to_angle(x_target_angle)

    y_target_angle  = int((1.0 + y_pos) * 50)
    servo1.move_to_angle(y_target_angle)
    time.sleep(0.1)
