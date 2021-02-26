#  Hibiscus Sense - Exercise 04 Melody
#   
#   There is 1x Small Buzzer on-board.
#   This is a passive buzzer and it is connected to GPIO13.
#   We need to generate Pulse Width Modulation (PWM) to control the vibration of the piezo element.
#   
#   In Arduino ESP32 programming there is no analogWrite() function as usual.
#   ESP32 has 16 channel, from 0 - 15. Channel does not mean GPIO number!
#   Therefore in the sketch,
#   we will use PWM.duty() and PWM.freq()
#   to generate the PWM signal on GPIO13.

from machine import Pin,PWM
from time import sleep

# declare the GPIO number for PWM signal output
buzzer = PWM(Pin(13))
# declare Tone frequency.
buzzer.freq(5000)

while True:
    
    # PWM duty cycle number.
    buzzer.duty(294)
    sleep(0.5)
    
    
    buzzer.duty(0) #buzzer has no sound since PWM duty cycle is 0.
    sleep(0.5)
    

