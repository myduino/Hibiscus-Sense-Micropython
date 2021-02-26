#  Hibiscus Sense - Exercise 10 BME280
#   
#   There is 1x BME280, an environment sensor.
#   The sensor sense altitude, barometric pressure, humidity and temperature.
#   This sensor is interfaced to the I2C of ESP32 microcontroller.
#   
#   
# GitHub Source = https://github.com/SebastianRoll/mpy_bme280_esp8266

from time import sleep
from machine import Pin, SoftI2C
# construct a SoftSPI bus on the given pins

from bme280 import BME280

# polarity is the idle state of SCK
# phase=0 means sample on the first edge of SCK, phase=1 means the second
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
bme = BME280(i2c=i2c)

print("BME280 Test")
print("============")

while True:
    #  bme.values[1], this function will return barometric pressure value in Pascals.
    #  bme.values[2], this function will return humidity value in % Relative Humidity.
    #  bme.values[0], this function will return temperature value in celcius.
    print("Temperature = {}".format(bme.values[0]))
    print("Barometer = {}".format(bme.values[1]))
    print("Humidity = {}".format(bme.values[2]))
    
    sleep(0.5)