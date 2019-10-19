
from __future__ import print_function
import tkinter
from cgitb import text
from tkinter import ttk
import tkinter as tk
from importent import *
from arays import *
import time
import sys
import datetime
import random
import tkinter, configparser,  os, tkinter.messagebox, tkinter.simpledialog
import threading
import random
import os.path
from tkinter import *
from math import sqrt
from random import shuffle
import tkinter
from tkinter import *
import tkinter.messagebox as box
import tkinter as tk
import webbrowser
import sys



''' this is for erorr masegess'''
def ErrorMag():
    ERR = tkinter.Tk()
    ERR.title("Error1")
    l1 = tkinter.Label(ERR, text="not the right username")
    l1.pack()
    ERR.mainloop()

def ErrorMag2():
    ERR = tkinter.Tk()
    ERR.title("Error2")
    l1 = tkinter.Label(ERR, text="not the right username")
    l1.pack()
    ERR.mainloop()
'''kernal start'''


''' for commands within the appliction'''
def CmdHuman():
    win = tkinter.Tk()
    win.title("commands")
    l1 = tkinter.Label(win, text="show user info")
    l2 = tkinter.Label(win, text=",show user pass,")
    l3 = tkinter.Label(win, text=" cal,")
    l4 = tkinter.Label(win, text=" time ,")
    l5 = tkinter.Label(win, text=" shut down,")
    l6 = tkinter.Label(win, text="launch clock,")
    l7 = tkinter.Label(win, text=" study,")
    l8 = tkinter.Label(win, text="pc info,")
    l9 = tkinter.Label(win, text=" mine,")
    l10 = tkinter.Label(win, text=" snake,")
    l11 = tkinter.Label(win, text="load GUI")
    l12 = tkinter.Label(win, text="Bubble Blaster")
    l1.config(fg='red')
    l2.config(fg='green')
    l3.config(fg='blue')
    l4.config(fg='red')
    l5.config(fg='blue')
    l6.config(fg='green')
    l7.config(fg='red')
    l8.config(fg='blue')
    l9.config(fg='green')
    l10.config(fg='red')
    l11.config(fg='blue')
    l12.config(fg='green')
    l1.pack()
    l2.pack()
    l3.pack()
    l4.pack()
    l5.pack()
    l6.pack()
    l7.pack()
    l8.pack()
    l9.pack()
    l10.pack()
    l11.pack()
    l12.pack()

    win.mainloop()
def GUI_ANEX():
    def Cal():
        class Calculator:
            def __init__(self, master):
                self.master = master
                master.title("Python Calculator")

                # create screen widget
                self.screen = Text(master, state='disabled', width=30, height=3, background="yellow", foreground="blue")

                # position screen in window
                self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
                self.screen.configure(state='normal')

                # initialize screen value as empty
                self.equation = ''

                # create buttons using method createButton
                b1 = self.createButton(7)
                b2 = self.createButton(8)
                b3 = self.createButton(9)
                b4 = self.createButton(u"\u232B", None)
                b5 = self.createButton(4)
                b6 = self.createButton(5)
                b7 = self.createButton(6)
                b8 = self.createButton(u"\u00F7")
                b9 = self.createButton(1)
                b10 = self.createButton(2)
                b11 = self.createButton(3)
                b12 = self.createButton('*')
                b13 = self.createButton('.')
                b14 = self.createButton(0)
                b15 = self.createButton('+')
                b16 = self.createButton('-')
                b17 = self.createButton('=', None, 34)

                # buttons stored in list
                buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]

                # intialize counter
                count = 0
                # arrange buttons with grid manager
                for row in range(1, 5):
                    for column in range(4):
                        buttons[count].grid(row=row, column=column)
                        count += 1
                # arrange last button '=' at the bottom
                buttons[16].grid(row=5, column=0, columnspan=4)

            def createButton(self, val, write=True, width=7):
                # this function creates a button, and takes one compulsory argument, the value that should be on the button

                return Button(self.master, text=val, command=lambda: self.click(val, write), width=width)

            def click(self, text, write):
                # this function handles what happens when you click a button
                # 'write' argument if True means the value 'val' should be written on screen, if None, should not be written on screen
                if write == None:

                    # only evaluate code when there is an equation to be evaluated
                    if text == '=' and self.equation:
                        # replace the unicode value of division ./.with python division symbol / using regex
                        self.equation = re.sub(u"\u00F7", '/', self.equation)
                        print(self.equation)
                        answer = str(eval(self.equation))
                        self.clear_screen()
                        self.insert_screen(answer, newline=True)
                    elif text == u"\u232B":
                        self.clear_screen()


                else:
                    # add text to screen
                    self.insert_screen(text)

            def clear_screen(self):
                # to clear screen
                # set equation to empty before deleting screen
                self.equation = ''
                self.screen.configure(state='normal')
                self.screen.delete('1.0', END)

            def insert_screen(self, value, newline=False):
                self.screen.configure(state='normal')
                self.screen.insert(END, value)
                # record every value inserted in screen
                self.equation += str(value)
                self.screen.configure(state='disabled')

        moot = Tk()
        my_gui = Calculator(moot)
        moot.mainloop()

    def dialog1():
        username = entry1.get()
        password = entry2.get()

        if (username == 'admin' and password == 'admin12'):
            box.showinfo('info', 'Correct Login')
            B1.pack()


        else:
            box.showinfo('info', 'Invalid Login')

    def Note():
        note = Tk()
        note_E1 = Entry(note)
        note_E1.config(bg='blue')
        note_E1.pack()
        note.mainloop()

    def PP():
        ro = Tk()
        ro.config(bg='green')
        B11 = Button(ro, text="note pad", command=Note)
        B22 = Button(ro, text="cal", command=Cal)
        B11.config(bg='magenta')
        B22.config(bg='magenta')
        B22.pack()
        B11.pack()

    win = Tk()
    win.title('Anex OS')
    win.config(bg='blue')

    frame = Frame(win)
    frame.config(bg='blue')

    Label1 = Label(win, text='Username:')
    Label1.config(bg='blue')
    Label1.pack(padx=15, pady=5)

    entry1 = Entry(win, bd=5)
    entry1.pack(padx=15, pady=5)

    Label2 = Label(win, text='Password: ')
    Label2.config(bg='blue')
    Label2.pack(padx=15, pady=6)

    entry2 = Entry(win, bd=5)
    entry1.config(bg='black', fg='white')
    entry2.config(bg='black')
    entry2.pack(padx=15, pady=7)

    btn = Button(frame, text='Check Login', command=dialog1)
    btn.config(bg='orange')

    btn.pack(side=RIGHT, padx=5)
    frame.pack(padx=100, pady=19)
    B1 = Button(win, text="Enter OS", command=PP)
    B1.config(fg='white', bg='orange')

    win.mainloop()


def WEBforGoogle():
    google =  input('Google search:')
    webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)
def loading_os():
    print("welcome to anex OS")
    print("loading OS")
    time.sleep(.3)
    print("10%")
    time.sleep(.3)
    print("25%")
    time.sleep(.3)
    print("37%")
    time.sleep(.3)
    print("40%")
    time.sleep(.3)
    print("59%")
    time.sleep(.3)
    print("79%")
    time.sleep(.3)
    print("87%")
    time.sleep(.3)
    print("99%")
    time.sleep(.6)
    print("100%")
def login():
	input_name = input("Enter user name:")
	if input_name == "admin":
	    print("welcome admin")
	if input_name != "admin":
		ErrorMag()
		sys.exit()
