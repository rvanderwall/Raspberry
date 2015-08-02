#!/usr/bin/python

#  sudo apt-get install python-webpy

import web
import smbus
import math
import time

urls = (
    '/', 'index'
)

# Power Management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

bus = smbus.SMBus(1)
address = 0x68                    # from i2cdetect

ACCEL_SCALE = 16384.0


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

class index:
    def GET(self):

        x_accel = read_word_2c(0x3b)
        y_accel = read_word_2c(0x3d)
        z_accel = read_word_2c(0x3f)

        x_scaled = x_accel / ACCEL_SCALE
        y_scaled = y_accel / ACCEL_SCALE
        z_scaled = z_accel / ACCEL_SCALE

        x_rotation = get_x_rotation(x_scaled, y_scaled, z_scaled)
        y_rotation = get_y_rotation(x_scaled, y_scaled, z_scaled)

	result = str(x_rotation) + " " + str(y_rotation)
	return result

if __name__ == "__main__":
    # Wake up the 6050 since it powers up in sleep mode
    bus.write_byte_data(address, power_mgmt_1, 0)

    app = web.application(urls, globals())
    app.run()

