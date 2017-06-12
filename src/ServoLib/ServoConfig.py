__author__ = 'robert'

import json

class ServoConfig():

    def __init__(self, id, CCW, CW):
        self.servo_id = id
        self.CCW = CCW
        self.CW = CW

    @staticmethod
    def choose_servo(id, servo_type):
        with open('ServoData.json') as json_data:
            config = json.load(json_data)

        for s in config["servos"]:
            if s["type"] is servo_type:
                CCW = s["ccw_on_time"]
                CW=s["cw_on_time"]
                servo_config = ServoConfig(id, CCW, CW)
                return servo_config

        return None

    @staticmethod
    def pick_servo_type(id):
        with open('ServoData.json') as json_data:
            config = json.load(json_data)

        print("Pick a servo type")
        index = 0
        for s in config["servos"]:
            print("{}) {}".format(index, s["Description"]))
            index += 1

        servo_idx = int(raw_input("choice: "))

        servo_data = config["servos"][servo_idx]
        CCW = servo_data["ccw_on_time"]
        CW=servo_data["cw_on_time"]
        servo_config = ServoConfig(id, CCW, CW)
        return servo_config
