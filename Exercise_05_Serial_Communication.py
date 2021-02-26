#   Hibiscus Sense - Exercise 05 Serial Communication
#   
#   In Arduino ESP32 programming Shell is used to program the UART controller
#   Main functions of Serial library are:
#   
#   print() function to transmit data
#   
#   read() function to read data in receving buffer

from time import sleep

counter = 0

while True:
    counter += 1
    print (counter)
    sleep (1)