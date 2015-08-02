import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.OUT)

BLINKING=0
STEADY_ON=1
STEADY_OFF=2


class LED():
    LED_ON = 0
    LED_OFF = 1
    cur_led_state = LED_OFF
    id = 0

    def __init__(self, pin_id):
        self.id = pin_id

    def TURN_ON(self):
        GPIO.output(self.id, GPIO.HIGH)
        self.cur_led_state = self.LED_ON

    def TURN_OFF(self):
        GPIO.output(self.id, GPIO.LOW)
        self.cur_led_state = self.LED_OFF

    def TOGGLE(self):
        if self.cur_led_state == self.LED_OFF:
            self.TURN_ON()
        else:
            self.TURN_OFF()


def handle_led(desired_state, led1, led2):
    time.sleep(0.2)

    if desired_state == BLINKING:
        led1.TOGGLE()
        led2.TOGGLE()
    elif desired_state == STEADY_ON:
        led1.TURN_ON()
        led2.TURN_OFF()
    else:
        led1.TURN_OFF()
        led2.TURN_ON()


led23 = LED(23)
led25 = LED(25)
cur_state = STEADY_OFF

while True:
    handle_led(cur_state, led23, led25)
    if (GPIO.input(24) == 1):
        cur_state = STEADY_OFF
    if (GPIO.input(24) == 0):
        cur_state = BLINKING

GPIO.cleaup()




