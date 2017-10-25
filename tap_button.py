from Tkinter import *
#import speech_recognition as sr
#import pyaudio
import numpy as np
import serial
import serial.tools.list_ports
import time
import math
from Tkinter import *
import tkMessageBox
import tkFileDialog
import copy
#from tools_for_littlearm_BIG import *


def serial_connection(serial_port):
    ''' connect serial
        param: serial_port -> serial port for mac something like: "/dev/tty.wchusbserial1420";
                                for Linux/Windows something like: COM1
        return ser
    '''
    global ser
    ser = serial.Serial(serial_port, 9600, timeout = .5)
    #check if connecting worked
    if (ser.isOpen()==True):
        print ("Serial is connected")
    return ser

def check_command(command):
    ''' check angles for each servo and part of the command if it's in the correct range
        took the correct ranges from the bars in the LittleArm Big app
    '''

    print(command)
    check_list = command.strip().split(',')
    check_list_int = [ int(x) for x in check_list ]

    if (4 < check_list_int[0] and check_list_int[1] and check_list_int[2] and check_list_int[3] and check_list_int[4] < 176) and 23 < check_list_int[5]< 76 and 7 < check_list_int[6] < 22:
        move_it(command)
    else:
        print("The arm isn't able to move into this position. Please try again.", "\n")
        menu()


def move_it(command):
    ''' sends command with correct angles to Arduino
        copied from LittleArmBIG_GUI_VO_4.1.py move_it function
    '''
    ser.flushInput()
    ser.flushOutput()
    ser.write(command)
    print ("Just moved!")

def specific_position():
    ''' moves arm into a specific positions
        error handling besides nothing was entered happens in check_command()
    '''
    try:
        base = int(raw_input("Please give angle for base (5 - 175):  "))
        shoulder = int(raw_input("Please give angle for shoulder (5 - 175):  "))
        elbow = int(raw_input("Please give angle for elbow (5 - 175):  "))
        wRot = int(raw_input("Please give angle for wRot (5 - 175):  "))
        wFlex = int(raw_input("Please give angle for wFlex (5 - 175):  "))
        gripper = int(raw_input("Please give angle for gripper (24 - 75):  "))
        speed = int(raw_input("Please give angle for speed (3 - 8):  "))
    except ValueError:
        print("This is not a valid input. Please try again.")
        menu()

    command = str(base) + ',' + str(shoulder) + ',' + str(elbow) + ',' + str(wRot) + ',' + str(wFlex) + ',' + str(gripper) + ',' + str(25 - speed) + '\n'

    check_command(command)

def wave(positions):
    ''' takes list of different commands (positions) and move the arm to one after the Other

    '''
    try:
        ans = int(raw_input("How often do you want me to wave? Please enter a number:  "))
    except ValueError:
        print ("You didn't enter a number. Try again.")
        wave()
    #positions = ["72,43,123,56,133,72,8","72,55,50,56,100,72,8","72,104,101,56,69,60,8","72,137,65,79,58,60,8","72,161,85,79,90,60,8"]
    reverse = list(reversed(positions))
    count = 1
    print("reverse: ", reverse)
    while ans > 0:
        for i in positions:
            check_command(i)
            time.sleep(0.9)

        if count == 1:
            reverse.pop()

        for j in reverse:
            check_command(j)
            time.sleep(0.9)

        if count == 1:
            positions.pop()
        count = 0
        ans = ans-1
        if ans == 0:
            break



def press_button(ans):
    ''' press button in specific already
        checks if followed by a emotional reaction
    '''
    positions = ["108,48,146,68,120,29,8","108,90,100,94,97,65,8"]

    for i in positions:
        check_command(i)
        time.sleep(1)
    print("pressed button")

    if ans == 3:
        menu()
    else:
        pass


def happy():
    '''
        try to find happy movement
    '''
    positions = ["72,104,140,30,70,70,8","90,104,70,100,110,25,8","72,104,140,30,70,70,8","90,104,70,100,110,25,8","72,104,140,30,70,70,8","90,104,70,100,110,25,8","72,104,140,30,70,70,8","90,104,70,100,110,25,8"]
    for i in positions:
        check_command(i)
        time.sleep(4)

def sad():
    '''
        try to find sad movement
    '''
    positions = ["108,116,146,100,100,34,17","108,116,175,68,163,32,17","108,116,128,68,119,57,17"]
    for i in positions:
        move_it(i)
        time.sleep(4)

def angry():
    '''
        try to find angry movement
    '''
    positions = []


def menu():
    print ( "---------------------------" + "\n" + "------ LittleArm Big ------" + "\n" + "------  MAIN - MENU  ------")
    print ( "What do you want to do?")
    print ( " 1 -> Specific position")
    print ( " 2 -> wave")
    print ( " 3 -> press button")
    print ( " 4 -> press button and react sad")
    print ( " 5 -> press button and react happy")
    print ( " 6 -> press button and react angry")
    print ( " 7 -> exit the programm")

    print ( "---------------------------" )

    try:
        ans = int(raw_input("Please enter a number:  "))
    except ValueError:
        print ("You didn't enter a number.")
        menu()


    if ans == 1:
        specific_position()
        menu()
    elif ans == 2:
        # choose from 3 differnt ways of waving
        print( "Which wave do you want me to perform?")
        try:
            wave1 = int(raw_input("Please enter the number of the wave (1-3):  "))
        except ValueError:
            print ("You didn't enter a number.")
            menu()

        if wave1 == 1:
            positions = ["72,43,123,56,133,72,8","72,55,50,56,100,72,8","72,104,101,56,69,60,8","72,137,65,79,58,60,8","72,161,85,79,90,60,8"]
            wave(positions)
        elif wave1 == 2:
            positions = ["72,70,123,56,133,72,8","72,104,101,56,69,60,8","72,140,85,79,90,60,8"]
            wave(positions)
        elif wave1 == 3:
            positions = ["72,98,135,56,133,72,8","72,110,101,56,69,60,8","72,120,50,79,90,60,8"]
            wave(positions)
        menu()

    elif ans == 3:
        press_button(ans)
        menu()
    elif ans == 4:
        press_button(ans)
        time.sleep(2)
        sad()
        menu()
    elif ans == 5:
        press_button(ans)
        time.sleep(3)
        happy()
        menu()
    elif ans == 6:
        press_button(ans)
        time.sleep(3)
        angry()
        menu()
    elif ans == 7:
        check_command("108,35,136,100,100,60,8")
        print("Goooood night!")
        exit()
    else:
        print("Your entered a wrong number. Please try again:  ")
        menu()


def main():

    serial_connection("/dev/tty.wchusbserial1420")
    #ser = serial.Serial("/dev/tty.wchusbserial1420", 9600, timeout = .5)
    if (ser.isOpen()==True):
        print ("Serial is connected")

    menu()



if __name__ == '__main__':
    main()
