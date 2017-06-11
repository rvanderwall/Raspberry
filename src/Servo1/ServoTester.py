#!/usr/bin/python

import time
from Servo import Servo
from Position import Position

on_time = 4000
servo0 = Servo(0, 0, on_time)
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
		on_time -=50
	if char == ']':
		on_time += 50

	print('on_time:{}'.format(on_time))
	servo0.set_on_time_directly(on_time)
	char = raw_input("")


ccw = int(raw_input('enter the Counterclock wise value: '))
cw = int(raw_input('enter the Clockwise value: '))


servo0 = Servo(0, ccw, cw )


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

