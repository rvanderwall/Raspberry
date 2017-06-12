#!/usr/bin/python

import time
from Servo import Servo, MAX_ON_TIME
from ServoConfig import ServoConfig

on_time = MAX_ON_TIME / 2
config = ServoConfig(0, 0, on_time)
servo0 = Servo(config)
servo0.set_on_time_directly(on_time)

print("< to decrease on_time, > to increase on_time")
print("[ to fast decrease, ] to fast increase")

print('Note the minimum and maximum values, they will be used as the servo parameters')

char = raw_input("")
while char != 'q':
    if char == '<':
        on_time -= 10
    if char == '>':
        on_time += 10
    if char == '[':
        on_time -= 50
    if char == ']':
        on_time += 50

    print('on_time:{}'.format(on_time))
    servo0.set_on_time_directly(on_time)
    char = raw_input("")

ccw = int(raw_input('Enter the Counterclock wise value: '))
cw = int(raw_input('Enter the Clockwise value: '))

#
# Create new servo with the measured parameters
# and make sure it behaves as expected
#
config = ServoConfig(0, ccw, cw)
servo0 = Servo(config)

for i in range(4):
    print('Moving to 0 degrees')
    servo0.move_to_angle(0.0)
    time.sleep(2)

    print('Moving to 90 degrees')
    servo0.move_to_angle(90.0)
    time.sleep(2)

    print('Moving to 180 degrees')
    servo0.move_to_angle(180.0)
    time.sleep(2)

