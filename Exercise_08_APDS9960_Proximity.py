#   Hibiscus Sense - Exercise 08 APDS9960 (Proximity)
#   
#   There is 1x APDS9960, a proximity sensor.
#   The sensor sense proximity, gesture, ambient light and rgb color.
#   This sensor is interfaced to the I2C of ESP32 microcontroller.
#   
# GitHub Source = https://github.com/liske/python-apds9960/


from time import sleep
from machine import Pin, SoftI2C
# construct a SoftSPI bus on the given pins

from apds9960.const import 
from apds9960 import uAPDS9960 as APDS9960

# polarity is the idle state of SCK
# phase=0 means sample on the first edge of SCK, phase=1 means the second
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
apds = APDS9960(i2c)

apds.enableProximitySensor()

print("Proximity Sensor Test")
print("=====================")

while True:
    val = apds.readProximity()
    print("Proximity = {}".format(val))
    
    sleep(0.25)