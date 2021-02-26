#   Hibiscus Sense Example Sketch - APDS9960
#   
#   There is 1x APDS9960, a proximity sensor.
#   The sensor sense proximity, gesture and rgb color.
#   This sensor is interfaced to the I2C of ESP32 microcontroller.
#
# GitHub Source = https://github.com/liske/python-apds9960/

from time import sleep
from machine import Pin, SoftI2C
# construct a SoftSPI bus on the given pins

from apds9960.const import *
from apds9960 import uAPDS9960 as APDS9960

# polarity is the idle state of SCK
# phase=0 means sample on the first edge of SCK, phase=1 means the second
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
apds = APDS9960(i2c)

apds.enableGestureSensor()

dirs = {
    APDS9960_DIR_NONE: "none",
    APDS9960_DIR_LEFT: "left",
    APDS9960_DIR_RIGHT: "right",
    APDS9960_DIR_UP: "up",
    APDS9960_DIR_DOWN: "down",
    APDS9960_DIR_NEAR: "near",
    APDS9960_DIR_FAR: "far",
}

print("Gesture Test")
print("============")

while True:
    if apds.isGestureAvailable():
        motion = apds.readGesture()
        print("Gesture = {}".format(dirs.get(motion, "unknown")))
    
    sleep(0.5)
