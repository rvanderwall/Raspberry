#!/usr/bin/python

import smbus
import math
import time

# Accelerometer:  (ADXL345 / MPU-6050)
#   vcc -  pin 01   3.3V
#   gnd - pin 09   gnd
#   scl -   pin 06   GPIO03 (SCL1 - I2C)
#   sda -  pin 03   GPIO02 (SDA1 - I2C)

class Position:
    # Power Management registers
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c
    address = 0x68                    # from i2cdetect
    x_gyro_channel = 0x43
    y_gyro_channel = 0x45
    z_gyro_channel = 0x47
    gyro_scale = 131

    x_accelerometer_channel = 0x3b
    y_accelerometer_channel = 0x3d
    z_accelerometer_channel = 0x3f
    accel_scale = 16384.0
    

    bus = None
    
    def __init__(self):
        self.bus = smbus.SMBus(1)
        # Wake up the 6050 since it powers up in sleep mode
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)

    def get_position(self):
        (ax, ay, az) = self.__get_accelerometer_values()
        return ax/self.accel_scale, ay/self.accel_scale, az/self.accel_scale

    def get_x_rotation(self):
        (x, y, z) = self.get_position()
        radians = math.atan2(y, self.__dist(x,z))
        return math.degrees(radians)

    def get_y_rotation(self):
        (x, y, z) = self.get_position()
        radians = math.atan2(x, self.__dist(y,z))
        return math.degrees(radians)

    def get_gyro(self):
        (gx, gy, gz) = self.__get_gyro_values()
        return gx/self.gyro_scale, gy/self.gyro_scale, gz/self.gyro_scale
    
    def __get_gyro_values(self):
        gyro_xout = self.__read_word_2c(self.x_gyro_channel)
        gyro_yout = self.__read_word_2c(self.y_gyro_channel)
        gyro_zout = self.__read_word_2c(self.z_gyro_channel)
        return gyro_xout, gyro_yout, gyro_zout

    def __get_accelerometer_values(self):
        accel_xout = self.__read_word_2c(self.x_accelerometer_channel)
        accel_yout = self.__read_word_2c(self.y_accelerometer_channel)
        accel_zout = self.__read_word_2c(self.z_accelerometer_channel)
        return accel_xout, accel_yout, accel_zout

    # Convert from two's complement
    def __read_word_2c(self, channel):
        val = self.__read_word(channel)
        if (val > 0x8000):
            return -((65535 - val) + 1)
        else:
            return val
        
    def __read_word(self, channel):
        high = self.__read_byte(channel)
        low =  self.__read_byte(channel+1)
        val = (high <<8) + low
        return val

    def __read_byte(self, channel):
        return self.bus.read_byte_data(self.address, channel)

    def __dist(self, a,b):
        return math.sqrt((a*a) + (b*b))





def main():

    position = Position()
    
    while True:
        print
        print("gyro data")
        print("------------")
        (gyro_xout, gyro_yout, gyro_zout) = position.get_gyro()
        print("gyro_xout:{0}".format(gyro_xout))
        print("gyro_yout:{0}".format(gyro_yout))
        print("gyro_zout:{0}".format(gyro_zout))

        print
        print("accelerometer data")
        print("-------------------------")
        (accel_xout, accel_yout, accel_zout) = position.get_position()
        print("accel_xout:{0}".format(accel_xout))
        print("accel_yout:{0}".format(accel_yout))
        print("accel_zout:{0}".format(accel_zout))

        x_rotation = position.get_x_rotation()
        y_rotation = position.get_y_rotation()
        print("x_rotation:{0}".format(x_rotation))
        print("y_rotation:{0}".format(y_rotation))

        time.sleep(0.5)

if __name__ == "__main__":
    main()


