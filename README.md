# Hibiscus Sense ESP32 Micropython Tutorial (English)

<p align="right">
<a href="https://myduino.com/product/myd-036/"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fmyinvent%2Fhibiscus-sense-micropython&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>
</p>

![](https://github.com/NaimFuad/hibiscus-sense-micropython-1/blob/main/Image/Hibiscus-Sense-V1.0-Overview.jpg)
***

# Getting Started  - Flashing Your Hibiscus Sense ESP32 IoT Developtment Board
To get started with MicroPython on your Hibiscus Sense ESP32 Development Board, you will need to flash it with MicroPython firmware with a handy tool called esptool.py. 

## Prerequisite
* Python 3.7X or latest - [Python](https://www.python.org/downloads/)
* MicroPython firmware for ESP32 - [Micropython Firmware](https://micropython.org/download/esp32/)

## 1. Download and Install Python

Download Python and install it. Make sure the option for Add Python To Environment Variable was ticked

## 2. Download MicroPython Firmware

MicroPython are available for various microcontroller ranging from STM32, Raspberry Pi Pico and also Espressif's ESP32 board. You need to make sure you download the right firmware for this development board. Download from the link and save on your machine. ( I recommend to save it in Downloads folder)

![MicroPython Firmware](https://github.com/NaimFuad/hibiscus-sense-micropython-1/blob/main/Image/MicroPython-Firmware.jpg)

You will later install this firmware through terminal and to make life easier, you will need to rename the file when downloading it as something simpler rather than typing the whole name.

![Renamed](https://github.com/NaimFuad/hibiscus-sense-micropython-1/blob/main/Image/Micropython-Firmware-Renamed.JPG)

## 3. Installing esptool.py

1. To start, you will need to access terminal on windows. , click the Windows button and type in _cmd_ and click the Command Prompt application.
2. Run the following command

`pip install esptool`

You should now be able to run esptool. If you type esptool.py and run it there will be a few argument printed on the terminal.

### 4. Erase ESP32

You will need to erase whatever firmware in the ESP32 and back to a clean slate.

1. On the terminal,run the following command

`esptool.py --chip esp32 erase_flash`

![Erase ESP32](https://github.com/NaimFuad/hibiscus-sense-micropython-1/blob/main/Image/erase-esp32.JPG)

In my case, I have a few USB device connected and it automatically choose the one with ESP32 on COM11, (more on this later)

## 5. Flash MicroPython ESP32 Firmware

1. The first thing to do is to identify what is the port number your ESP32 is assigned. To do so, click Windows button on your machine and run _Device Manager_ application. If you collapse the _Ports (COM & LPT)_ option, you will what is the port number assigned to your ESP32 by referring to the deviced named as Silicon Labs CP210x (USB driver IC). Mine was COM11.

![](https://github.com/NaimFuad/hibiscus-sense-micropython-1/blob/main/Image/Port-assignments.JPG)


2. Navigate to the folder where you save your MicroPython firmware. In my case, I saved it in Downloads folder on my machine and to navigate to the folder;

`C:\Users\[user]\Downloads`

![](https://github.com/NaimFuad/hibiscus-sense-micropython-1/blob/main/Image/Navigate-to-Downloads.JPG)

3. Run the following command and replace the serial port number and the name of the firmware

`esptool.py --chip esp32 --port [serial_port] write_flash -z 0x1000 [esp32.bin]`

It should look like this

![](https://github.com/NaimFuad/hibiscus-sense-micropython-1/blob/main/Image/flash-firmware-command.JPG)

The final result will look like this

![](https://github.com/NaimFuad/hibiscus-sense-micropython-1/blob/main/Image/flash-firmware.JPG)

***

# Installing and Setting Up Thonny IDE for Micropython

## Prerequisite

* Thonny - [Thonny IDE](https://thonny.org/)

## 1.Download and Install Thonny

1. On the website, choose the Windows version and download it.

![](https://github.com/NaimFuad/hibiscus-sense-micropython-1/blob/main/Image/thonny-main-page.JPG)

2. Install and run it.

## 2.Setting Up Thonny MicroPython Intrepreter

1. Setup interpreter on Thonny by going to  

> Tools > Option >Intrepreter > Micropython (Generic)

2. Setup Port

> Tools > Option >Intrepreter > Port >

![](https://github.com/NaimFuad/hibiscus-sense-micropython-1/blob/main/Image/Thonny.JPG)


