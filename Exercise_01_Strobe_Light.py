# Hibiscus Sense - Exercise 01 Strobe Light
# 
# There is 1x blue LED.
# This LED is connected to GPIO2 of ESP32 microcontroller.
# The circuit is an active-low circuit, therefore we need to pull the pins LOW,
# in order to complete the circuit to the GND.
# 
# Therefore in the sketch,
# we need to call LOW state in the digitalWrite function, to light ON the LED,
# while call HIGH state, to light OFF the LED.

from machine import Pin
from time import sleep

# declaring GPIO2 as an OUTPUT pin.
led = Pin(2, Pin.OUT)

while True:
    # strobe light effect, such on the aeroplane.
    led.value(0)
    sleep(0.1)
    led.value(1)
    sleep(0.1)
    
    led.value(0)
    sleep(0.1)
    led.value(1)
    sleep(2)
        
       
    