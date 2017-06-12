__author__ = 'robert'

from ServoLib.Servo import Servo
from ServoLib.ServoConfig import ServoConfig


class Finger:
    def __init__(self, servo_id, open_val, close_val):
        config = ServoConfig.choose_servo(servo_id, "SG90")
        self.__servo = Servo(config)
        self.__open = open_val
        self.__close = close_val

    def close(self):
        self.__servo.move_to_angle(self.__close)

    def open(self):
        self.__servo.move_to_angle(self.__open)

little_finger = Finger(0, 100, 40)
ring_finger = Finger(1, 110, 40)
middle_finger = Finger(2, 50, 110)
index_finger = Finger(3, 50, 150)
thumb = Finger(4, 60, 150)

def open_fist():
    little_finger.open()
    ring_finger.open()
    middle_finger.open()
    index_finger.open()
    thumb.open()

def close_fist():
    little_finger.close()
    ring_finger.close()
    middle_finger.close()
    index_finger.close()
    thumb.close()

while True:
    little_finger.close()
    little_finger.open()
    ring_finger.close()
    ring_finger.open()
    middle_finger.close()
    middle_finger.open()
    index_finger.close()
    index_finger.open()

    close_fist()
    open_fist()

