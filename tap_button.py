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

def serial_connection():
    ser = serial.Serial(ser, 9600, timeout = .5)
    if (ser.isOpen()==True):
        print ("Serial is connected")
    return ser

def check_command(command):
    ''' checks if the command has possible angles for the robotarm '''

    print(command)
    check_list = command.strip().split(',')
    check_list_int = [ int(x) for x in check_list ]
    # print(check_list)
    # print("check list int: ")
    # print(check_list_int)

    if (4 < check_list_int[0] and check_list_int[1] and check_list_int[2] and check_list_int[3] and check_list_int[4] < 176) and 23 < check_list_int[5]< 76 and 7 < check_list_int[6] < 22:
        move_it(command)
    else:
        print("The arm isn't able to move into this position. Please try again.")
        menu()


def move_it(command):
    ser.flushInput()
    ser.flushOutput()
    #print command
    ser.write(command)
    print ("Just moved!")


    #menu()


#
# ser = serial.Serial("/dev/tty.wchusbserial1420", 9600, timeout = .5)
# if (ser.isOpen()==True):
#     print ("yes")
def specific_position():
    try:
        base = int(raw_input("Please give ancle for base (5 - 175):  "))
        shoulder = int(raw_input("Please give ancle for shoulder (5 - 175):  "))
        elbow = int(raw_input("Please give ancle for elbow (5 - 175):  "))
        wRot = int(raw_input("Please give ancle for wRot (5 - 175):  "))
        wFlex = int(raw_input("Please give ancle for wFlex (5 - 175):  "))
        gripper = int(raw_input("Please give ancle for gripper (24 - 75):  "))
        speed = int(raw_input("Please give ancle for speed (3 - 8):  "))
    except ValueError:
        print("This is not a valid input. Please try again.")
        menu()
    #print(type(base))
    command = str(base) + ',' + str(shoulder) + ',' + str(elbow) + ',' + str(wRot) + ',' + str(wFlex) + ',' + str(gripper) + ',' + str(25 - speed) + '\n'
    #print (command)
    check_command(command)

    # right_num = False
    # # check whether input is in possible range of servo
    # # try:
    # #     4 < base == True and base < 181 == True and 4 < shoulder == True and shoulder < 181 == True and 4 < elbow == True and elbow < 181 == True and 4 < wRot == True and wRot < 181 == True and 4 < wFlex == True and wFlex < 181 == True and 24< gripper == True and gripper < 75 == True and 2 < speed == True and speed < 9 == True
    # #     #base or shoulder or elbow or wRot or wFlex or gripper or speed != ""
    # #     right_num = True
    # # except:
    # #     right_num = False
    #
    # right_num = False
    #
    # if (4 < base < 181 and 4 < shoulder < 181 and 4 < elbow < 181 and 4 < wRot < 181 and 4 < wFlex < 181 and 24 < gripper < 75 and 3 < speed < 9) == True:
    #     right_num = True
    # else:
    #     right_num = False
    #
    # if right_num == True:
    #     command = str(base) + ',' + str(shoulder) + ',' + str(elbow) + ',' + str(wRot) + ',' + str(wFlex) + ',' + str(gripper) + ',' + str(25 - speed) + '\n'
    #     print (command)
    #     move_it(command)

    # else:
    #     print("You either entered a wrong number or no number, go try again: ")
    #     menu()
def wave(positions):
    try:
        ans = int(raw_input("How often do you want me to wave? Please enter a number:  "))
    except ValueError:
        print ("You didn't enter a number. Try again.")
        wave()
    #positions = ["72,43,123,56,133,72,8","72,55,50,56,100,72,8","72,104,101,56,69,60,8","72,137,65,79,58,60,8","72,161,85,79,90,60,8"]
    reverse = list(reversed(positions))
    del reverse[0]

    print("reverse: ", reverse)
    while ans > 0:
        for i in positions:
            check_command(i)
            time.sleep(1)
        for j in reverse:
            check_command(j)
            time.sleep(1)
        ans = ans-1
        if ans == 0:
            break
    menu()

# def wave2():
#     try:
#         ans = int(raw_input("How often do you want me to wave? Please enter a number:  "))
#     except ValueError:
#         print ("You didn't enter a number. Try again.")
#         wave()
#
#     positions = ["72,70,123,56,133,72,8","72,104,101,56,69,60,8","72,140,85,79,90,60,8"]
#
#     reverse = list(reversed(positions))
#     del reverse[0]
#     while ans > 0:
#         for i in positions:
#             check_command(i)
#             time.sleep(.9)
#         for j in reverse:
#             check_command(j)
#             time.sleep(.9)
#         ans = ans-1
#         if ans == 0:
#             break
# def wave3():
#     try:
#         ans = int(raw_input("How often do you want me to wave? Please enter a number:  "))
#     except ValueError:
#         print ("You didn't enter a number. Try again.")
#         wave()
#
#     positions = ["72,98,135,56,133,72,8","72,110,101,56,69,60,8","72,120,50,79,90,60,8"]
#
#     reverse = list(reversed(positions))
#     del reverse[0]
#     while ans > 0:
#         for i in positions:
#             check_command(i)
#             time.sleep(.9)
#         for j in reverse:
#             check_command(j)
#             time.sleep(.9)
#         ans = ans-1
#         if ans == 0:
#             break


def press_button():
    positions = ["108,48,146,68,120,29,8","108,90,100,94,97,65,8"]

    for i in positions:
        check_command(i)
        time.sleep(1)
    print("pressed button")
    #time.sleep(1)
    #menu()

def happy():
    # positions = "72,70,123,56,133,72,8",
    #             "72,104,101,56,69,60,8",
    #             "72,140,85,79,90,60,8"]

    positions = ["72,104,123,30,70,70,8","90,104,101,100,90,25,8","55,104,123,30,70,70,8","90,104,101,100,90,25,8","72,104,123,30,70,70,8","90,104,101,100,90,25,8","55,104,123,30,70,70,8"]
    for i in positions:
        check_command(i)
        time.sleep(1)
    #menu()

def sad():
    press_button()
    time.sleep(4)
    positions = ["108,116,146,100,100,34,22","108,116,175,68,163,32,22","108,116,128,68,119,57,22"]
    for i in positions:
        move_it(i)
        time.sleep(3)

def angry():
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
    elif ans == 2:

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
    elif ans == 3:
        press_button()

    elif ans == 4:
        #press_button()
        sad()
    elif ans == 5:
        press_button()
        time.sleep(3)
        happy()


    elif ans == 6:
        press_button()
        angry()
    elif ans == 7:
        check_command("108,35,136,100,100,60,8")
        exit()
    else:
        print("Your entered a wrong number. Please try again:  ")
        menu()


def main():
    global ser
    ser = serial.Serial("/dev/tty.wchusbserial1420", 9600, timeout = .5)
    if (ser.isOpen()==True):
        print ("Serial is connected")

    #serial_connection("/dev/tty.wchusbserial1420")
    menu()



if __name__ == '__main__':
    main()
