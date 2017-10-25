# LittleArm BIG

In this document I will put together the steps I took working with the Kickstarter Project LittleArm BIG during my internship at the [Social Robot lab](http://www.soba-lab.com) at Bangor University. Besides making the work with the robot easier for the next person in the lab I wanted to share my experiences and complications working with it.

## 1. Construction ##

Use this website to put the robot-arm together:
[Construction of LittleArm_BIG](http://www.instructables.com/id/LittleArm-Big/  "Construction of LittleArm_BIG")

#### Problems I have had during construction: ####
* one servo did not work at the beginning -> opened it up and put it back together -> servo worked
* had to file the *elbow* to let the arm move without resistance
insert picture here: **picture here** ![file here](/path/img.jpg "elbow")
* one of the servo gripper fingers broke
* the wrist yoke broke and I had to glue it with the strongest glue the IT had (waited 24h)
* power supply cable stopped to work

## 2. First steps ##
1. Connect power supply to the Arduino board and switch it on (there is a small switch directly next to the entrance of the power supply cable; under the USB cable if it is already plugged in)
2. Did the arm move to its starting-position?  
      - **YES**. Great, have a look at the [code section](https://github.com/egiacomazzi/Littlearm_BIG/blob/master/README.md#3-code) of this README.  
      - **NO**. Check the following things:  
          Is it possible to upload Arduino Sketches onto the board?  
              - **YES**. Upload this [sketch](https://github.com/egiacomazzi/Littlearm_BIG/blob/master/LittleArmBIG_Sketch.ino) you can also find it in the [LittleArm Big Package](https://github.com/egiacomazzi/Littlearm_BIG/blob/master/littlearm_big_software.zip).  
              - **NO**. You probably have a cloned Arduino Nano board. You will have to reboot it by following these instructions [here.](http://www.instructables.com/id/How-To-Burn-a-Bootloader-to-Clone-Arduino-Nano-30/  "Bootloader") If you successfully did that have a look at the **YES** section above and upload the right [sketch](https://github.com/egiacomazzi/Littlearm_BIG/blob/master/LittleArmBIG_Sketch.ino) onto your Arduino Nano.

## 3. Code ##

### Download ##
Have a look at the original [LittleArm download website](https://www.littlearmrobot.com/downloads.html  "Downloads").

The package for the LittleArm Big can be downloaded from this repository as well. It is the zip file I mentioned earlier: [LittleArm Big Package](https://github.com/egiacomazzi/Littlearm_BIG/blob/master/littlearm_big_software.zip).

### Bluetooth App (Android) ###

How does it work?
* connect Bluetooth antenna to board
* open Bluetooth devices on your phone -> add the Arduino to it
* open the [app](https://play.google.com/store/apps/details?id=appinventor.ai_slantconcepts.LittleArmBig) you downloaded at the Google Play store
* select the right Bluetooth device and start moving the arm!

### Python Desktop App ###
Open the [LittleArmBIG_GUI_VO_4.1.py](https://github.com/egiacomazzi/Littlearm_BIG/blob/master/LittleArmBig_GUI_V0_4.1.py) and run it on your computer/Mac.

#### Good to know: ####
* You will need the **USB-cable** as well as the **power supply** cable connected to the board
* The code is written in Python 2.7, make sure you do not run it with Python 3
* Download the following packages for Python 2.7:
    * [Tkinter](https://docs.python.org/2/library/tkinter.html)
    * [pySerial](https://pypi.python.org/pypi/pyserial/2.7)
    * [numpy](http://www.numpy.org)
    * [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/docs/)
    * [speech_recognition](https://pypi.python.org/pypi/SpeechRecognition/)

  for downloading them for the specific python2 version I used the following command:

  `python2 -m pip install <name of package>`


All the code that we used by now is from the [LittleArm Website](https://www.littlearmrobot.com/). In the following I will explain my own code and what I aimed to do with it. To understand how the serial connection works and how to program these just have a look

## 4. My Code ##

Have a look at [my code](https://github.com/egiacomazzi/Littlearm_BIG/blob/master/tap_button.py) and let me know what you programmed your robot to do!
Cheers.
