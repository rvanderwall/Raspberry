import board
import adafruit_sht31d
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306 as SSD

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def getSensor():
    i2c = board.I2C()
    sensor = adafruit_sht31d.SHT31D(i2c)
    return sensor


def getDisp():
    RST = None  # PiOLED doesn't use this
    DC = 23
    SPI_PORT = 0
    SPI_DEVICE = 0

    disp = SSD.SSD1306_128_32(rst=RST, i2c_bus=1)

    # Initialize Library
    disp.begin()

    # Clear display
    disp.clear()
    disp.display()
    return disp


def getCanvas(disp):
    # Create blank image for drawing
    # mode '1' for 1-bit color
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))

    # Get drawing object to draw on
    draw = ImageDraw.Draw(image)

    return image, draw


def renderText(canvas, text, font, line):
    padding = 2
    (font_width, font_height) = font.getsize(text)
    x = padding
    y = line * font_height + padding
    canvas.text((x,y), text, font=font, fill=255)

def repaint(disp, image):
    disp.clear()
    disp.image(image)
    disp.display()

def runApp():
    display = getDisp()
    font = ImageFont.load_default()
    sensor = getSensor()
    while True:
        c = sensor.temperature
        f = 9.0 / 5.0 * c + 32.0
        h = sensor.relative_humidity
        image, canvas = getCanvas(display)
        renderText(canvas, f"Temp: {f:.1f}/{c:.1f}", font, 0)
        renderText(canvas, f"Humidity: {h:.1f}", font, 1)
        repaint(display, image)
        time.sleep(2)

if __name__ == "__main__":
    runApp()
