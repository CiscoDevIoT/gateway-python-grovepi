# gateway-python-grovepi
Python-based gateway service for GrovePi.

This code is based on [gateway-python-SDK](https://wwwin-github.cisco.com/DevIoT/gateway-python-sdk). You need to install SDK before using this repo. The way to install SDK is explained

### Prerequisite
#### Hardware
* [Raspberry-Pi](https://www.raspberrypi.org/)
* [GrovePi+ Starter Kit](http://www.dexterindustries.com/grovepi/)

#### Software
* [Python 2.7](https://www.python.org/downloads/): This SDK is based on the Python 2.7.3
&nbsp;
## Run code on GrovePi (Raspberry Pi)
### Build the hardware
#### 1. Prepare your Raspberry Pi os environment in your SD card
* Download the OS for Raspberry Pi form [RASPBIAN JESSIE](https://www.raspberrypi.org/downloads/raspbian/)
* Format you SD card
* Use window install the OS image to the SD card. you can use [Win32 Disk Manager](https://sourceforge.net/projects/win32diskimager/).
    I strongly recommend you do this using Windows, I have met many issues when i installed it by mac OS
* Attach the SD card to the Raspberry Pi

You also can follow [this instructions](https://www.raspberrypi.org/documentation/installation/noobs.md)

#### 2. Connect the GrovePi to the Raspberry Pi

#### 3. Connect sensors to GrovePi

#### 4. Connect Raspberry Pi with the power and network

#### 5. Connect Raspberry Pi with Display using HDMI cable
&nbsp;
### Build the software environment
#### 6. Install the Python 2.7. 
* Check the version of python that Raspberry Pi has. This sample code is based on python 2.7.3 or later. in most time, the Raspberry Pi os have installed the python 2.7.3 or later, if not, you can install the python follow [here](https://www.raspberrypi.org/documentation/linux/software/python.md).

#### 7. Install GrovePi SDK.

* Make sure your Raspberry Pi is connected to the Internet.
* Open Terminal.
* Type the following commands in terminal window.
    
        sudo apt-get update
        sudo apt-get install rpi.gpio
    
* [Follow the tutorial for setting up the GrovePi](http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/).
* Reboot your Raspberry Pi board.
    
Your SD card now has what it needs to start using the GrovePi.
[More information about installing GrovePi SDK](http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/)
&nbsp;
### Run GrovePi gateway service on Raspberry Pi

#### 8. Install SDK and run code on Python 2 (on Raspberry Pi)
* Download and install DevIoT python SDK.

        git clone https://wwwin-github.cisco.com/DevIoT/gateway-python-sdk.git
        cd gateway-pythohn-sdk
        python setup.py install

* Download the gateway service for GrovePi.
        
        cd ../
        git clone https://wwwin-github.cisco.com/DevIoT/gateway-python-grovepi.git
        cd gateway-python-grovepi

* Modify sensors.json according to the types of sensors and the pin number.

    You can use Text Editor in Raspberry Pi, or vim editor in the terminal window.

        vim sensors.json

    In Vim editor, you can only change the file in insert mode. Press 'i' and change the content. After modifying, press 'Esc' button and save the file and exit Vim editor by type ':wq' and press 'Enter'.

* Run gateway service on Raspberry Pi.
        python main.py
