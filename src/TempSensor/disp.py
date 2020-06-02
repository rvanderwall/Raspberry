import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306 as SSD

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

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

# Create blank image for drawing
# mode '1' for 1-bit color
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear image
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes
padding = 2
shape_width = 20
top = padding
bottom = height - padding

# MOve left to right keeping track of current X
x = padding
draw.ellipse((x, top, x+shape_width, bottom), outline=255, fill=0)

x += shape_width+padding
draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)

x += shape_width+padding
draw.polygon([(x,bottom),(x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)

x += shape_width+padding
draw.line((x, bottom, x+shape_width, top), fill=255)
draw.line((x, top, x+shape_width, bottom), fill=255)


x += shape_width+padding
font = ImageFont.load_default()

draw.text((x,top), "Hello", font=font, fill=255)
draw.text((x,top+20), "world", font=font, fill=255)

disp.image(image)
disp.display()
print("done")
