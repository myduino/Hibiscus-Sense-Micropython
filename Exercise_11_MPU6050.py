#  Hibiscus Sense - Exercise 11 MPU6050
#   
#   There is 1x MPU6050, 6-axis motion tracking and temperature sensor.
#   The sensor sense 3-axis accelerometer, the gravitational acceleration, 3-axis gyroscope, the rotational velocity and temperature.
#   This sensor is interfaced to the I2C of ESP32 microcontroller.
#   

# Github source = https://github.com/adamjezek98/MPU6050-ESP8266-MicroPython

from time import sleep
from machine import SoftI2C, Pin
import mpu6050

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
accelerometer = mpu6050.accel(i2c)

print("MPU6050 Test")
print("============")

while True:
    
    # to acquire MPU6050 accelerometer, gyroscope and temperature values,
    # we need to call accelerometer.get_values() function from mpu instance.
    
    print("Accelerometer X = {}".format(accelerometer.get_values()["AcX"]))
    print("Accelerometer Y = {}".format(accelerometer.get_values()["AcY"]))
    print("Accelerometer Z = {}".format(accelerometer.get_values()["AcZ"]))
    
    print("Gyrometer X = {}".format(accelerometer.get_values()["GyX"]))
    print("Gyrometer Y = {}".format(accelerometer.get_values()["GyY"]))
    print("Gyrometer Z = {}".format(accelerometer.get_values()["GyZ"]))
    
    print("Temperature = {}".format(accelerometer.get_values()["Tmp"]))
    
    sleep(0.5)