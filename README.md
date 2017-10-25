# Littlearm_BIG

This document is aiming to help you setting up the LittleArm Big. It describes most of the steps I had to take before I figured out how it really works. Let me know if something is really wrong or if you had to face different problems.

## 1. Construction ##

Use this website to put the robot-arm together:
[Construction of LittleArm_BIG](http://www.instructables.com/id/LittleArm-Big/  "Construction of LittleArm_BIG")

#### Problems I have had while doing that: ####
* one servo did not work at the beginning -> opened it and put it back together -> servo moved
* had to file the *elbow* to let the arm move without resistance
insert picture here: **picture here** ![file here](/path/img.jpg "elbow")
* one of the servo gripper fingers broke
* the wrist yoke broke and I had to glue it with the strongest glue the IT had (wait 24h)
* power supply cable stopped to work

## 2. First steps ##
1. Connect power supply and switch on the Arduino board (there is a small switch directly next to the entrance of the power supply cable; under the USB cable if it is already plugged in)
2. Did the arm move to a starting-position?
      -> **YES**, great have a look at the Code section of this README **CODE link**.  
      -> **NO**, check the following things:  
          Is it possible to upload Arduino Sketches onto the board?  
          -> **YES**, upload the sketch you will find in the .zip folder or just download this: **zipfile here**  
          -> **NO**, you probably have a cloned Arduino Nano. You will have to reboot it and please follow the instructions [here.](http://www.instructables.com/id/How-To-Burn-a-Bootloader-to-Clone-Arduino-Nano-30/  "Bootloader") If you successfully did that have a look at the **YES** section above and upload the right sketch onto your Arduino Nano.

## 3. Code ##

### Download ##
Have a look at the original [LittleArm download website](https://www.littlearmrobot.com/downloads.html  "Downloads")

The package for the LittleArm Big can be downloaded from this repository as well. **link to .zip**

### Bluetooth App (Android) ###

How does it work?
* connect Bluetooth antenna to board
* open Bluetooth devices on your phone -> add the Arduino
* open the app you downloaded at the PlayStore **link to playstoreapp**
* select the right Bluetooth device and start moving the arm!

### Python Desktop App ###
Open the LittleArmBIG_GUI_VO_4.1.py and run it on your computer/Mac

#### Good to know: ####
* You will need the **USB-cable** as well as the **power supply** cable connected to the board
* The code is written in Python 2.7, make sure you do not run it with Python 3
* Download the following libraries for Python 2.7:
    * tkinter
    * pySerial
    * time
    * math
    * numpy
    * pyaudio
    * speech_recognition

  for downloading them for the specific python2 version try to use the following command:

  `> python2 pip -m <libary>`


All the code that we used by now is from the LittleArm_BIG Website **website**. In the following I will explain my own code and what I aimed to do with it. To understand how the serial connection works and how to program these just have a look

## 4. My Code ##
**to be continued...**
