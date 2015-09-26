#!/usr/bin/python

import smbus
import math
import time

# Accelerometer:
#   vcc -  pin 01   3.3V
#   gnd - pin 09   gnd
#   scl -   pin 06   GPIO03 (SCL1 - I2C)
#   sda -  pin 03   GPIO02 (SDA1 - I2C)


# Power Management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high <<8) + low
    return val

# Convert from two's complement
def read_word_2c(adr):
    val = read_word(adr)
    if (val > 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a) + (b*b))

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return math.degrees(radians)

bus = smbus.SMBus(1)
address = 0x68                    # from i2cdetect

# Wake up the 6050 since it powers up in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

max_x = 0.0
max_y = 0.0
max_z = 0.0

while False:
    print
    print "gyro data"
    print "------------"
    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)

    print "gyro_xout: ",+ gyro_xout, " scaled: ", (gyro_xout/131)
    print "gyro_yout: ",+ gyro_yout, " scaled: ", (gyro_yout/131)
    print "gyro_zout: ",+ gyro_zout, " scaled: ", (gyro_zout/131)

    print
    print "accelerometer data"
    print "-------------------------"

    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled
    print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled
    print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled

    x_rotation = get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
    y_rotation = get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

    print "x_rotation: ", x_rotation
    print "y_rotation: ", y_rotation

    time.sleep(1.0)

while True:
    accel_x = read_word_2c(0x3b)
    accel_y = read_word_2c(0x3d)
    accel_z = read_word_2c(0x3f)

    accel_x_scaled = accel_x / 16384.0
    accel_y_scaled = accel_y / 16384.0
    accel_z_scaled = accel_z / 16384.0

    changed = False
    if math.fabs(accel_x_scaled) > math.fabs(max_x):
        max_x = accel_x_scaled
        changed = True
    if math.fabs(accel_y_scaled) > math.fabs(max_y):
        max_y = accel_y_scaled
        changed = True
    if math.fabs(accel_z_scaled) > math.fabs(max_z):
        max_z = accel_z_scaled
        changed = True

    print
    print "accel_xout: ", accel_x, " scaled: ", accel_x_scaled
    print "accel_yout: ", accel_y, " scaled: ", accel_y_scaled
    print "accel_zout: ", accel_z, " scaled: ", accel_z_scaled

    if changed:
        print "max_x: ", max_x, " scaled: ", accel_x_scaled
        print "max_y: ", max_y, " scaled: ", accel_y_scaled
        print "max_z: ", max_z, " scaled: ", accel_z_scaled
        
    time.sleep(0.5)
