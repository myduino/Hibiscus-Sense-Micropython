# Hibiscus Sense - Exercise 03 Breathing Light
#   
#   There is 1x blue LED.
#   This LED is connected to GPIO2 of ESP32 microcontroller.
#   We need to generate PWM output signal on GPIO2 to control the brightness of this LED.
#   
#   Therefore in the sketch,
#   we configure the PWM controller, choose GPIO for PWM signal output 
#   and generate the PWM signal on chosen GPIO.

from machine import Pin,PWM
from time import sleep

# configure PWM controller congfiguration and declare the GPIO number for PWM signal output.
led = PWM(Pin(2))

duty_cycle=0

while True:
    
    # function for() to create decremental value by 1 start from 1023 --> 0
    # from OFF LED to linear increasing brightness, for active-low circuit
    for duty_cycle in range (1023, 0, -1):
        led.duty(duty_cycle)
        sleep(0.001)
     
    # function for() to create decremental value by 1 start from 0 --> 1023
    # from ON LED to linear decreasing brightness, for active-low circuit 
    for duty_cycle in range (0, 1023, 1):
        led.duty(duty_cycle)
        sleep(0.001)
        