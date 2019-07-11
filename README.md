# gateway-python-grovepi
Python-based gateway service for GrovePi.

This code is based on [gateway-python-SDK](https://wwwin-github.cisco.com/DevIoT/gateway-python-sdk). You need to install SDK before using this repo. The way to install SDK will be explained in the instruction part.

You can also refer to the learning labs about DevIoT in [Cisco DevNet](https://developer.cisco.com/), Cisco's developer program.
Sign up now and enjoy various free contents.
The learning lab for connecting Raspberry Pi to DevIoT is [here](https://developer.cisco.com/learning/lab/rp-deviot/step/1)

### Prerequisite
#### Hardware
* [Raspberry-Pi](https://www.raspberrypi.org/)
* [GrovePi+ Starter Kit](http://www.dexterindustries.com/grovepi/)

#### Software
* [Python](https://www.python.org/downloads/): This SDK is based on Python 2 or 3.
&nbsp;
## Run code on GrovePi (Raspberry Pi)
### Build the hardware
#### 1. Prepare your Raspberry Pi OS environment on your SD card
* If your SD card is not Raspberry Pi preloaded, you need to install Raspberry Pi OS (Raspbian) in the SD card. There are two options to install Raspbian: (1) Install the OS image on the card (2) Install the installer (NOOBS). We recommend the second option, NOOBS. It is very easy. The only thing to do is extracting the installer file to the card.
* You can download the latest OS image or the installer from [here](https://www.raspberrypi.org/downloads/).
* But Raspberry OS is usually not stable right after its release. The new OS, buster is released on June 24, 2019. You can download the 'stretch' version of NOOBS from [here](http://downloads.raspberrypi.org/NOOBS/images/NOOBS-2019-04-09/).

* The SD card should be formatted as **FAT16** or **FAT32**.
* When you use Windows to install the OS image, you can use [Win32 Disk Manager](https://sourceforge.net/projects/win32diskimager/).
* On macOS, you can use the 'Disk Utility' program to format. Choose the format MS-DOS (FAT) when erasing your SD card.
* Extract the zip file of NOOBS to the root directory of the SD card. **The files should be at the root directory.**
* Insert the SD card to the Raspberry Pi.

You also can follow [this instruction](https://www.raspberrypi.org/documentation/installation/noobs.md).

#### 2. Connect your GrovePi board to the Raspberry Pi board

#### 3. Connect sensors to the GrovePi board

#### 4. Connect Raspberry Pi with the power and network, screen.
&nbsp;
### Build the software environment
#### 5. Check if Raspberry Pi has Python. 
* The Raspberry Pi OS has Python. If not, you can follow the [instruction](https://www.raspberrypi.org/documentation/linux/software/python.md).

#### 6. Install GrovePi SDK.

* Make sure your Raspberry Pi is connected to the **Internet**.
* Open Terminal.
* Type the following commands in the terminal window.
    
        sudo apt-get update
        sudo apt-get install rpi.gpio
    
* Set up the GrovePi software

        curl -kL dexterindustries.com/update_grovepi | bash
        sudo reboot

Refer to the [tutorial](http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/).

* flash the firmware
        cd ~/Dexter/GrovePi/Firmware
        bash firmware_update.sh

* check the firmware version
        cd ~/Dexter/GrovePi/Software/Python
        python grove_firmware_version_check.py

You can check the firmware version of 1.4.0 or higher.
    
Your SD card now has what it needs to start using the GrovePi.
[More information about installing GrovePi SDK](http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/)
&nbsp;
### Run GrovePi gateway service on Raspberry Pi

#### 8. Install SDK and GrovePi gateway (on Raspberry Pi)
* Download and install DevIoT Python SDK.

        git clone https://wwwin-github.cisco.com/DevIoT/gateway-python-sdk.git
        cd gateway-pythohn-sdk
        python setup.py install

* Download the gateway service for GrovePi.
        
        cd ../
        git clone https://wwwin-github.cisco.com/DevIoT/gateway-python-grovepi.git
        cd gateway-python-grovepi

#### 9. Configure sensors.json and run the gateway service

* Configure sensors.json according to types and pin of connected sensors.

    You can use Text Editor in Raspberry Pi, or Vim editor in the terminal window.

        vim sensors.json

    In Vim editor, you can only change the file in insert mode. Press 'i' and change the content. After modifying, press 'Esc' button and save the file and exit Vim editor by type ':wq' and press 'Enter'.

In sensors.json, there is the information about each sensor inside the parenthesis {}.

```
{
    "type": "light",
    "pin": "A2",
    "name": "GroveLight",
    "options": {}
}
```

  1. **type**: The name of a sensor class file. The python file having this name should be in *cisco_grovepi* directory.
  2. **pin**: The pin which the sensor is connected to on the GrovePi board. It should be a string like  "A1" or "D4", or pin number. You can check the details about it in [here].(https://www.dexterindustries.com/GrovePi/engineering/port-description/).
  3. **name**: The display name of the sensor on DevIoT.
  4. **options**: The parameter for setting additional values. It can be omitted, or left with {}. It is **not** necessary for pre-defined classes in *cisco_grovepi* directory. You can utilize this value when you define a new class.

* Run gateway service on Raspberry Pi. Replace 'your_id@cisco.com' with your DevIoT account. 

        python main.py --account your_id@cisco.com
