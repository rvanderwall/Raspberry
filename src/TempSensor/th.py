import board
import adafruit_sht31d
import time

i2c = board.I2C()
sensor = adafruit_sht31d.SHT31D(i2c)


while True:
    c = sensor.temperature
    f = 9.0 / 5.0 * c + 32.0
    h = sensor.relative_humidity
    print(f"Temp: {f:.1f}/{c:.1f}")
    print(f"Humidity: {h:.1f}")
    time.sleep(2)

