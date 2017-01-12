__author__ = 'robert'

from Servo1.Servo import Servo

s1 = Servo(0)
s1.set_min_max(25, 50)

s2 = Servo(1)
s2.set_min_max(30, 55)

s3 = Servo(3)
s3.set_min_max(40, 80)

s4 = Servo(4)
s4.set_min_max(40, 80)

s5 = Servo(5)
s5.set_min_max(40, 60)

class finger:
    def __init__(self, servo, open, close):
        self.__servo = servo
        self.__open = open
        self.__close = close

    def close(self):
        self.__close()

    def open(self):
        self.__open()

finger1 = finger(s1, s1.send_to_max, s1.send_to_min)
finger2 = finger(s2, s2.send_to_max, s2.send_to_min)
finger3 = finger(s3, s3.send_to_min, s3.send_to_max)
finger4 = finger(s4, s4.send_to_min, s4.send_to_max)
finger5 = finger(s5, s5.send_to_min, s5.send_to_max)

finger1.open()
finger2.open()
finger3.open()
finger4.open()
finger5.open()

while True:
    finger1.close()
    finger1.open()
    finger2.close()
    finger2.open()
    finger3.close()
    finger3.open()
    finger4.close()
    finger4.open()
    finger5.close()
    finger5.close()

