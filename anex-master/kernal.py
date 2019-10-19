from importent import *
webbrowser_availabel = True
mysql_avi = True

def checkALLimport():

    try:
        import time
    except:
        print("You do not have the time module")
    try:
        import sys
    except:
        print("You do not have the sys module")
    try:
        import datetime
    except:
        print("You do not have the datetime module")
    try:
        import random
    except:
        print("You do not have the random module")
    try:
        import tkinter, configparser, random, os, tkinter.messagebox, tkinter.simpledialog
    except:
        print("You do not have the tkinter module")

    try:
        import threading
    except:
        print("You do not have the threading module")
    try:
        import os.path
    except:
        print("You do not have the os.path module")
    try:
        from math import sqrt
    except:
        print("You do not have the math module")
    try:
        from random import shuffle
    except:
        print("You do not have the random module")
    try:
        import webbrowser
    except:
        webbrowser_availabel = False
        print("you do not have the webbrowser module")
    try:
        import mysql.connector
    except:
        print("you don't have mysql.connector ")
    try:
        from Inex import *
    except:
        print("You don't have Inex.py")

def TkinterTest():
    TKTEST = tkinter.Tk()
    LL1 = Label(TKTEST, text="test")
    LL1.pack()
    TKTEST.after(1, lambda: TKTEST.destroy())
    TKTEST.mainloop()
    return True
def RANDOMTEST():
    RANDTEST = random.randint(1,10)
    print(RANDTEST)
    return True
''''''

def alltest():
    if Kernal_mysql_avil == True:
        print("[ OK ]mysql.connector")
    else:
        print("[ failed ]mysql.connector")
    if webbrowser_availabel == True:
        print("[OK]webbrowser")
    else:
        print("[failed]webbrowser")
    try:
        TkinterTest()
    except:
        print("tkinter is not working properly")
    try:
        RANDOMTEST()
    except:
        print("random is not working properly")
    if TkinterTest():
        print("[OK]tkinter")
    if RANDOMTEST():
        print("[OK]random")
    if not TkinterTest():
        print("[failed!!!!]TkinterTest")
    if not RANDOMTEST():
        print("[failed!!!!]RANDOMTEST")
def Kernal_App_check_WEB():
    try:
        import webbrowser
    except:
        webbrowser_availabel = False
        print("<<<This application cant run>>> @you do not have the webbrowser module@")
def Kernal_mysql_avil():
    try:
        import mysql.connector
    except:
        mysql_avi = False
        print("you don't have mysql.connector")
