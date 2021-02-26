#   Hibiscus Sense - Exercise 06 Pushbutton Status
#   
#   There are 2x Pushbutton on-board:
#   1x for RESET button
#   1x connected to GPIO0.
#   
#   The IO0 pushbutton applying pull-down resistor, therefore whenever it is pressed,
#   the circuit is completed and the GND connected to GPIO0 and
#   ESP32 sense LOW state at GPIO0, otherwise HIGH state.
# 
from machine import Pin
from time import sleep

push = Pin(0, Pin.IN, Pin.PULL_UP) # declaring GPIO0 as an INPUT pin.
led = Pin(2, Pin.OUT) # declaring GPIO2 as an OUTPUT pin.

while True:
    
   # we use if() function to compare the GPIO0 reading state with the LOW state.
   # if the GPIO0 reading is LOW, light ON the LED on GPIO2 with LOW state.
   #  else means, the GPIO0 reading is HIGH, light OFF the LED on GPIO2 with HIGH state.
    if push.value() == 0:
        led.value(0)
        sleep(0.5)
      
    led.value(1)
    