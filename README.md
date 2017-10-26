# LittleArm BIG

In this document I will put together the steps I took working with the Kickstarter Project [LittleArm BIG](https://www.kickstarter.com/projects/slantrobotics/littlearm-big-a-robot-arm-for-makers-and-education?lang=de) during my internship at the [Social Robot lab](http://www.soba-lab.com) at Bangor University. Besides making the work with the robot easier for the next person in the lab I wanted to share my experiences and complications working with it.

## 1. Construction ##

Use this website to put the robot-arm together:
[Construction of LittleArm_BIG](http://www.instructables.com/id/LittleArm-Big/  "Construction of LittleArm_BIG")

#### Problems I had during construction: ####
* one servo did not work at the beginning -> opened it up and put it back together -> servo worked
* had to file the *elbow* to let the arm move without resistance
insert picture here: **picture here** ![file here](/path/img.jpg "elbow")
* one of the servo gripper fingers broke
* the wrist yoke broke and I had to glue it with the strongest glue the IT had (waited 24h)
* power  cable stopped working

## 2. First steps ##
1. Connect power cable to the Arduino board and switch it on (there is a small switch directly next to the entrance of the power supply cable; under the USB cable if it is already plugged in)
2. Did the arm move to its starting-position?  
      - **YES**. Great, have a look at the [code section](https://github.com/egiacomazzi/Littlearm_BIG/blob/master/README.md#3-code) of this README.  
      - **NO**. Check the following things:  
          Is it possible to upload Arduino Sketches onto the board?  
              - **YES**. Upload this [sketch](https://github.com/egiacomazzi/Littlearm_BIG/blob/master/LittleArmBIG_Sketch.ino). You can also find it in the [LittleArm Big Package](https://github.com/egiacomazzi/Littlearm_BIG/blob/master/littlearm_big_software.zip) I downloaded from the [LittleArm download website](https://www.littlearmrobot.com/downloads.html  "Downloads").  
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
* You will need the **USB-cable** as well as the **power cable** connected to the board
* The code is written in Python 2.7, make sure you do not run it with Python 3
* Download the following packages for Python 2.7:
    * [Tkinter](https://docs.python.org/2/library/tkinter.html)
    * [pySerial](https://pypi.python.org/pypi/pyserial/2.7)
    * [numpy](http://www.numpy.org)
    * [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/docs/)
    * [speech_recognition](https://pypi.python.org/pypi/SpeechRecognition/)

  to download them for the specific python2 version I used the following command:

  `python2 -m pip install <name of package>`

---

All the code that we used by now is from the [LittleArm Website](https://www.littlearmrobot.com/). In the following I will explain my own code and what I aimed to do with it. To understand how the serial connection works and how to program these just have a more precise look at the code they supply as well as the documentations (particularly [pySerial](https://pypi.python.org/pypi/pyserial/2.7)).

## 4. My Code ##

Have a look at [my code](https://github.com/egiacomazzi/Littlearm_BIG/blob/master/tap_button.py) I comment it to explain what I did.

#### Good to know: ####
What is this *command*?
- a string without spaces
- composed of the angles the servo should go to and the speed of the movement
```python
"108,90,100,94,97,65,8"
```

    | angle  | servo    | possible input |
    | -------|:---------:|:---------------:|
    | 108    | base     | 5 - 175        |
    | 90     | shoulder | 5 - 175        |
    | 100    | elbow    | 5 - 175        |
    | 94     | wRot     | 5 - 175        |
    | 97     | wFlex    | 5 - 175        |
    | 65     | gripper  | 24 - 75        |
    | 8      | speed    | 3 - 8          |





Let me know what you programmed your robot to do!
Cheers.
