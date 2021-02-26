# Hibiscus Sense - Exercise 07 RGB LED
#   
#   There is 1x RGB LED.
#   This RGB LED is connected to GPIO16 and integrated with WS2812.
#   WS2812 is an LED controller, which use single-wire control protocol to control the LEDs.

from machine import Pin
from neopixel import NeoPixel
from time import sleep

pin = Pin(16, Pin.OUT) # set GPIO0 to output to drive NeoPixels
RGB = NeoPixel(pin, 1) # create NeoPixel driver on GPIO16 for 1 pixels

while True:
    
    # set the first pixel to green
    RGB[0] = (0, 255, 0)
    # write data to all pixels
    RGB.write()
    sleep(0.5)
    
    