from Inex import *
from cnex import *
from arays import *
from importent import *
from classes import *
from erorrMSG import *
import mysql.connector
from mydb import *
from Users import *
import sys

'''main application'''
'''start of kernal'''
good_kernal = True
bad_kernal = False

try:
    from kernal import *
except:
    bad_kernal = True
    print("you dont have the file kernal")
if bad_kernal == False:
    print("Starting kernal")
    print("[OK]kernal condition")
    checkALLimport()
    alltest()
'''end of kernal'''
'''loading scereen'''
loading_os()
'''end of loading screen'''
while True:
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"), end="\r")
    sys.stdout.flush()
    time.sleep(1.2)
    break
'''login proses'''

input_name = input("Enter user name:")
if input_name == "admin":
    print("welcome admin")
if input_name != "admin" and input_name != "root":
    ErrorMag()
    login()
#    sys.exit()
    #GUI_IN_ = input("Do you want Anex GUI:")
    #if GUI_IN_ == "yes":
       # GUI_ANEX()
	#login()
#else:
	#ErrorMag()
if input_name == "root":
    print("~")
if input_pass == "root12":
    print("ok")
input_pass = input("Enter password:")

if input_pass != "admin12" and input_pass != "root12":
    ErrorMag2()
    print("wrong pass")
if input_pass == "admin12":
    print("welcome back")

# to direcky load the GUI
if input_name == "GUI":
    GUI_ANEX()
print("please wait")
time.sleep(.10)
if input_pass == "root12":
    root()
'''end of login proses'''

''' application starts'''
while computer_off != computer_on and input_pass == "admin12":

    ''' all commands go bellow'''
    # to get the input for commands
    input_user_2 = input("py/user/admin:-$~")
    # to show user info(present in arays.py)
    if input_user_2 == "sudo show user info":
        force_S_in = input("enter pass:")
        if force_S_in == "admin12":
            print(users)
    # to show GUI commands(presentin erorrMSG.py)
    if input_user_2 == "cmd-H":
        CmdHuman()
    # to show the user passwords(present in arays.py)
    if input_user_2 == "sudo show user pass":
        force_S_in = input("enter pass")
        if force_S_in == "admin12":
            print(password)
    # to lanch the commandline calculater
    if input_user_2 == "cal":
        # This function adds two numbers
        def add(x, y):
            return x + y


        # This function subtracts two numbers
        def subtract(x, y):
            return x - y


        # This function multiplies two numbers
        def multiply(x, y):
            return x * y


        # This function divides two numbers
        def divide(x, y):
            return x / y


        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        # Take input from the user
        choice = input("Enter choice(1/2/3/4):")

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Invalid input")
    # to show the time
    if input_user_2 == "time":
        while True:
            now = datetime.datetime.now()
            print(now.strftime("%H:%M:%S"), end="\r")
            sys.stdout.flush()
            time.sleep(2.4)
            break
    if input_user_2 == "sudo force shut":
        print("shuting down...")
        time.sleep(3)
        break
    # to shut down the program
    if input_user_2 == "shut down":
        input_shut_down = input("Are you sure you want to shut down:")
        if input_shut_down == "yes":
            print("shuting down...")
            time.sleep(3)
            break
    # to lanch the clock app
    if input_user_2 == "launch clock":
        # !/usr/bin/env python
        # coding: UTF-8
        # license: GPL
        #
        ## @package _08c_clock
        #
        #  A very simple analog clock.
        #
        #  The program transforms worldcoordinates into screencoordinates
        #  and vice versa according to an algorithm found in:
        #  "Programming principles in computer graphics" by Leendert Ammeraal.
        #
        #  Based on the code of Anton Vredegoor (anton.vredegoor@gmail.com)
        #
        #  @author Paulo Roma
        #  @since 01/05/2014
        #  @see https://code.activestate.com/recipes/578875-analog-clock
        #  @see http://orion.lcg.ufrj.br/python/figuras/fluminense.png

        import sys, types, os
        from time import localtime
        from datetime import timedelta, datetime
        from math import sin, cos, pi
        from threading import Thread

        try:
            from tkinter import *  # python 3
        except ImportError:
            try:
                from mtTkinter import *  # for thread safe
            except ImportError:
                from Tkinter import *  # python 2

        hasPIL = True
        # we need PIL for resizing the background image
        # in Fedora do: yum install python-pillow-tk
        # or yum install python3-pillow-tk
        try:
            from PIL import Image, ImageTk
        except ImportError:
            hasPIL = False


        ## Class for handling the mapping from window coordinates
        #  to viewport coordinates.
        #
        class mapper:
            ## Constructor.
            #
            #  @param world window rectangle.
            #  @param viewport screen rectangle.
            #
            def __init__(self, world, viewport):
                self.world = world
                self.viewport = viewport
                x_min, y_min, x_max, y_max = self.world
                X_min, Y_min, X_max, Y_max = self.viewport
                f_x = float(X_max - X_min) / float(x_max - x_min)
                f_y = float(Y_max - Y_min) / float(y_max - y_min)
                self.f = min(f_x, f_y)
                x_c = 0.5 * (x_min + x_max)
                y_c = 0.5 * (y_min + y_max)
                X_c = 0.5 * (X_min + X_max)
                Y_c = 0.5 * (Y_min + Y_max)
                self.c_1 = X_c - self.f * x_c
                self.c_2 = Y_c - self.f * y_c

            ## Maps a single point from world coordinates to viewport (screen) coordinates.
            #
            #  @param x, y given point.
            #  @return a new point in screen coordinates.
            #
            def __windowToViewport(self, x, y):
                X = self.f * x + self.c_1
                Y = self.f * -y + self.c_2  # Y axis is upside down
                return X, Y

            ## Maps two points from world coordinates to viewport (screen) coordinates.
            #
            #  @param x1, y1 first point.
            #  @param x2, y2 second point.
            #  @return two new points in screen coordinates.
            #
            def windowToViewport(self, x1, y1, x2, y2):
                return self.__windowToViewport(x1, y1), self.__windowToViewport(x2, y2)


        ## Class for creating a new thread.
        #
        class makeThread(Thread):
            """Creates a thread."""

            ## Constructor.
            #  @param func function to run on this thread.
            #
            def __init__(self, func):
                Thread.__init__(self)
                self.__action = func
                self.debug = False

            ## Destructor.
            #
            def __del__(self):
                if (self.debug): print("Thread end")

            ## Starts this thread.
            #
            def run(self):
                if (self.debug): print("Thread begin")
                self.__action()


        ## Class for drawing a simple analog clock.
        #  The backgroung image may be changed by pressing key 'i'.
        #  The image path is hardcoded. It should be available in directory 'images'.
        #
        class clock:
            ## Constructor.
            #
            #  @param deltahours time zone.
            #  @param sImage whether to use a background image.
            #  @param w canvas width.
            #  @param h canvas height.
            #  @param useThread whether to use a separate thread for running the clock.
            #
            def __init__(self, root, deltahours=0, sImage=True, w=400, h=400, useThread=False):
                self.world = [-1, -1, 1, 1]
                self.imgPath = './images/fluminense.png'  # image path
                if hasPIL and os.path.exists(self.imgPath):
                    self.showImage = sImage
                else:
                    self.showImage = False

                self.setColors()
                self.circlesize = 0.09
                self._ALL = 'handles'
                self.root = root
                width, height = w, h
                self.pad = width / 16

                if self.showImage:
                    self.fluImg = Image.open(self.imgPath)

                self.root.bind("<Escape>", lambda _: root.destroy())
                self.delta = timedelta(hours=deltahours)
                self.canvas = Canvas(root, width=width, height=height, background=self.bgcolor)
                viewport = (self.pad, self.pad, width - self.pad, height - self.pad)
                self.T = mapper(self.world, viewport)
                self.root.title('Clock')
                self.canvas.bind("<Configure>", self.resize)
                self.root.bind("<KeyPress-i>", self.toggleImage)
                self.canvas.pack(fill=BOTH, expand=YES)

                if useThread:
                    st = makeThread(self.poll)
                    st.debug = True
                    st.start()
                else:
                    self.poll()

            ## Called when the window changes, by means of a user input.
            #
            def resize(self, event):
                sc = self.canvas
                sc.delete(ALL)  # erase the whole canvas
                width = sc.winfo_width()
                height = sc.winfo_height()

                imgSize = min(width, height)
                self.pad = imgSize / 16
                viewport = (self.pad, self.pad, width - self.pad, height - self.pad)
                self.T = mapper(self.world, viewport)

                if self.showImage:
                    flu = self.fluImg.resize((int(0.8 * 0.8 * imgSize), int(0.8 * imgSize)), Image.ANTIALIAS)
                    self.flu = ImageTk.PhotoImage(flu)
                    sc.create_image(width / 2, height / 2, image=self.flu)
                else:
                    self.canvas.create_rectangle([[0, 0], [width, height]], fill=self.bgcolor)

                self.redraw()  # redraw the clock

            ## Sets the clock colors.
            #
            def setColors(self):
                if self.showImage:
                    self.bgcolor = 'antique white'
                    self.timecolor = 'dark orange'
                    self.circlecolor = 'dark green'
                else:
                    self.bgcolor = '#000000'
                    self.timecolor = '#ffffff'
                    self.circlecolor = '#808080'

            ## Toggles the displaying of a background image.
            #
            def toggleImage(self, event):
                if hasPIL and os.path.exists(self.imgPath):
                    self.showImage = not self.showImage
                    self.setColors()
                    self.resize(event)

            ## Redraws the whole clock.
            #
            def redraw(self):
                start = pi / 2  # 12h is at pi/2
                step = pi / 6
                for i in range(12):  # draw the minute ticks as circles
                    angle = start - i * step
                    x, y = cos(angle), sin(angle)
                    self.paintcircle(x, y)
                self.painthms()  # draw the handles
                if not self.showImage:
                    self.paintcircle(0, 0)  # draw a circle at the centre of the clock

            ## Draws the handles.
            #
            def painthms(self):
                self.canvas.delete(self._ALL)  # delete the handles
                T = datetime.timetuple(datetime.utcnow() - self.delta)
                x, x, x, h, m, s, x, x, x = T
                self.root.title('%02i:%02i:%02i' % (h, m, s))
                angle = pi / 2 - pi / 6 * (h + m / 60.0)
                x, y = cos(angle) * 0.70, sin(angle) * 0.70
                scl = self.canvas.create_line
                # draw the hour handle
                scl(self.T.windowToViewport(0, 0, x, y), fill=self.timecolor, tag=self._ALL, width=self.pad / 3)
                angle = pi / 2 - pi / 30 * (m + s / 60.0)
                x, y = cos(angle) * 0.90, sin(angle) * 0.90
                # draw the minute handle
                scl(self.T.windowToViewport(0, 0, x, y), fill=self.timecolor, tag=self._ALL, width=self.pad / 5)
                angle = pi / 2 - pi / 30 * s
                x, y = cos(angle) * 0.95, sin(angle) * 0.95
                # draw the second handle
                scl(self.T.windowToViewport(0, 0, x, y), fill=self.timecolor, tag=self._ALL, arrow='last')

            ## Draws a circle at a given point.
            #
            #  @param x,y given point.
            #
            def paintcircle(self, x, y):
                ss = self.circlesize / 2.0
                sco = self.canvas.create_oval
                sco(self.T.windowToViewport(-ss + x, -ss + y, ss + x, ss + y), fill=self.circlecolor)

            ## Animates the clock, by redrawing everything after a certain time interval.
            #
            def poll(self):
                self.redraw()
                self.root.after(200, self.poll)


        ## Main program for testing.
        #
        #  @param argv time zone, image background flag,
        #         clock width, clock height, create thread flag.
        #
        def main(argv=None):
            if argv is None:
                argv = sys.argv
            if len(argv) > 2:
                try:
                    deltahours = int(argv[1])
                    sImage = (argv[2] == 'True')
                    w = int(argv[3])
                    h = int(argv[4])
                    t = (argv[5] == 'True')
                except ValueError:
                    print("A timezone is expected.")
                    return 1
            else:
                deltahours = 3
                sImage = True
                w = h = 400
                t = False

            root = Tk()
            root.geometry('+0+0')
            # deltahours: how far are you from utc?
            # Sometimes the clock may be run from another timezone ...
            clock(root, deltahours, sImage, w, h, t)

            root.mainloop()


        if __name__ == '__main__':
            sys.exit(main())

    # to show user the info availabe in the study(present in arays.py)
    if input_user_2 == "study":

        input_file_name = input("enter subject:")
        if input_file_name == file_name[0]:
            file_ch_input = input("enter chapter name:")
            if file_ch_input == "one":
                print(file_info_hist_for_ch_one)

        note_ch_one_history = input("Do you want to get the note's for this ")
        if note_ch_one_history == "yes":
            print(ch_note_history, ch_note_history_2, ch_note_history_3)
    # to show info of the OS(present in arays.py)
    if input_user_2 == "pc info":
        print("os:- anex 4.0.0 , os type:- terminal Based , os programed in:- python3")
    # to show human command that are availabe(present in arays.py)
    if input_user_2 == "cmd":
        print("sudo show user info,sudo show user pass, cal, time , shut down,launch clock, study,pc info, cmd-H, inex")
    # to show human command that are availabe in GUIl(present in erorrMSG.py)
    if input_user_2 == "cmd-H":
        CmdHuman()
    # To load game "mine"
    if input_user_2 == "mine":
        window = tkinter.Tk()

        window.title("Minesweeper")

        # prepare default values

        rows = 10
        cols = 10
        mines = 10

        field = []
        buttons = []

        colors = ['#FFFFFF', '#0000FF', '#008200', '#FF0000', '#000084', '#840000', '#008284', '#840084', '#000000']

        gameover = False
        customsizes = []


        def createMenu():
            menubar = tkinter.Menu(window)
            menusize = tkinter.Menu(window, tearoff=0)
            menusize.add_command(label="small (10x10 with 10 mines)", command=lambda: setSize(10, 10, 10))
            menusize.add_command(label="medium (20x20 with 40 mines)", command=lambda: setSize(20, 20, 40))
            menusize.add_command(label="big (35x35 with 120 mines)", command=lambda: setSize(35, 35, 120))
            menusize.add_command(label="custom", command=setCustomSize)
            menusize.add_separator()
            for x in range(0, len(customsizes)):
                menusize.add_command(label=str(customsizes[x][0]) + "x" + str(customsizes[x][1]) + " with " + str(
                    customsizes[x][2]) + " mines", command=lambda customsizes=customsizes: setSize(customsizes[x][0],
                                                                                                   customsizes[x][1],
                                                                                                   customsizes[x][2]))
            menubar.add_cascade(label="size", menu=menusize)
            menubar.add_command(label="exit", command=lambda: window.destroy())
            window.config(menu=menubar)


        def setCustomSize():
            global customsizes
            r = tkinter.simpledialog.askinteger("Custom size", "Enter amount of rows")
            c = tkinter.simpledialog.askinteger("Custom size", "Enter amount of columns")
            m = tkinter.simpledialog.askinteger("Custom size", "Enter amount of mines")
            while m > r * c:
                m = tkinter.simpledialog.askinteger("Custom size", "Maximum mines for this dimension is: " + str(
                    r * c) + "\nEnter amount of mines")
            customsizes.insert(0, (r, c, m))
            customsizes = customsizes[0:5]
            setSize(r, c, m)
            createMenu()


        def setSize(r, c, m):
            global rows, cols, mines
            rows = r
            cols = c
            mines = m
            saveConfig()
            restartGame()


        def saveConfig():
            global rows, cols, mines
            # configuration
            config = configparser.SafeConfigParser()
            config.add_section("game")
            config.set("game", "rows", str(rows))
            config.set("game", "cols", str(cols))
            config.set("game", "mines", str(mines))
            config.add_section("sizes")
            config.set("sizes", "amount", str(min(5, len(customsizes))))
            for x in range(0, min(5, len(customsizes))):
                config.set("sizes", "row" + str(x), str(customsizes[x][0]))
                config.set("sizes", "cols" + str(x), str(customsizes[x][1]))
                config.set("sizes", "mines" + str(x), str(customsizes[x][2]))

            with open("config.ini", "w") as file:
                config.write(file)


        def loadConfig():
            global rows, cols, mines, customsizes
            config = configparser.SafeConfigParser()
            config.read("config.ini")
            rows = config.getint("game", "rows")
            cols = config.getint("game", "cols")
            mines = config.getint("game", "mines")
            amountofsizes = config.getint("sizes", "amount")
            for x in range(0, amountofsizes):
                customsizes.append((config.getint("sizes", "row" + str(x)), config.getint("sizes", "cols" + str(x)),
                                    config.getint("sizes", "mines" + str(x))))


        def prepareGame():
            global rows, cols, mines, field
            field = []
            for x in range(0, rows):
                field.append([])
                for y in range(0, cols):
                    # add button and init value for game
                    field[x].append(0)
            # generate mines
            for _ in range(0, mines):
                x = random.randint(0, rows - 1)
                y = random.randint(0, cols - 1)
                # prevent spawning mine on top of each other
                while field[x][y] == -1:
                    x = random.randint(0, rows - 1)
                    y = random.randint(0, cols - 1)
                field[x][y] = -1
                if x != 0:
                    if y != 0:
                        if field[x - 1][y - 1] != -1:
                            field[x - 1][y - 1] = int(field[x - 1][y - 1]) + 1
                    if field[x - 1][y] != -1:
                        field[x - 1][y] = int(field[x - 1][y]) + 1
                    if y != cols - 1:
                        if field[x - 1][y + 1] != -1:
                            field[x - 1][y + 1] = int(field[x - 1][y + 1]) + 1
                if y != 0:
                    if field[x][y - 1] != -1:
                        field[x][y - 1] = int(field[x][y - 1]) + 1
                if y != cols - 1:
                    if field[x][y + 1] != -1:
                        field[x][y + 1] = int(field[x][y + 1]) + 1
                if x != rows - 1:
                    if y != 0:
                        if field[x + 1][y - 1] != -1:
                            field[x + 1][y - 1] = int(field[x + 1][y - 1]) + 1
                    if field[x + 1][y] != -1:
                        field[x + 1][y] = int(field[x + 1][y]) + 1
                    if y != cols - 1:
                        if field[x + 1][y + 1] != -1:
                            field[x + 1][y + 1] = int(field[x + 1][y + 1]) + 1


        def prepareWindow():
            global rows, cols, buttons
            tkinter.Button(window, text="Restart", command=restartGame).grid(row=0, column=0, columnspan=cols,
                                                                             sticky=tkinter.N + tkinter.W + tkinter.S + tkinter.E)
            buttons = []
            for x in range(0, rows):
                buttons.append([])
                for y in range(0, cols):
                    b = tkinter.Button(window, text=" ", width=2, command=lambda x=x, y=y: clickOn(x, y))
                    b.bind("<Button-3>", lambda e, x=x, y=y: onRightClick(x, y))
                    b.grid(row=x + 1, column=y, sticky=tkinter.N + tkinter.W + tkinter.S + tkinter.E)
                    buttons[x].append(b)


        def restartGame():
            global gameover
            gameover = False
            # destroy all - prevent memory leak
            for x in window.winfo_children():
                if type(x) != tkinter.Menu:
                    x.destroy()
            prepareWindow()
            prepareGame()


        def clickOn(x, y):
            global field, buttons, colors, gameover, rows, cols
            if gameover:
                return
            buttons[x][y]["text"] = str(field[x][y])
            if field[x][y] == -1:
                buttons[x][y]["text"] = "*"
                buttons[x][y].config(background='red', disabledforeground='black')
                gameover = True
                tkinter.messagebox.showinfo("Game Over", "You have lost.")
                # now show all other mines
                for _x in range(0, rows):
                    for _y in range(cols):
                        if field[_x][_y] == -1:
                            buttons[_x][_y]["text"] = "*"
            else:
                buttons[x][y].config(disabledforeground=colors[field[x][y]])
            if field[x][y] == 0:
                buttons[x][y]["text"] = " "
                # now repeat for all buttons nearby which are 0... kek
                autoClickOn(x, y)
            buttons[x][y]['state'] = 'disabled'
            buttons[x][y].config(relief=tkinter.SUNKEN)
            checkWin()


        def autoClickOn(x, y):
            global field, buttons, colors, rows, cols
            if buttons[x][y]["state"] == "disabled":
                return
            if field[x][y] != 0:
                buttons[x][y]["text"] = str(field[x][y])
            else:
                buttons[x][y]["text"] = " "
            buttons[x][y].config(disabledforeground=colors[field[x][y]])
            buttons[x][y].config(relief=tkinter.SUNKEN)
            buttons[x][y]['state'] = 'disabled'
            if field[x][y] == 0:
                if x != 0 and y != 0:
                    autoClickOn(x - 1, y - 1)
                if x != 0:
                    autoClickOn(x - 1, y)
                if x != 0 and y != cols - 1:
                    autoClickOn(x - 1, y + 1)
                if y != 0:
                    autoClickOn(x, y - 1)
                if y != cols - 1:
                    autoClickOn(x, y + 1)
                if x != rows - 1 and y != 0:
                    autoClickOn(x + 1, y - 1)
                if x != rows - 1:
                    autoClickOn(x + 1, y)
                if x != rows - 1 and y != cols - 1:
                    autoClickOn(x + 1, y + 1)


        def onRightClick(x, y):
            global buttons
            if gameover:
                return
            if buttons[x][y]["text"] == "?":
                buttons[x][y]["text"] = " "
                buttons[x][y]["state"] = "normal"
            elif buttons[x][y]["text"] == " " and buttons[x][y]["state"] == "normal":
                buttons[x][y]["text"] = "?"
                buttons[x][y]["state"] = "disabled"


        def checkWin():
            global buttons, field, rows, cols
            win = True
            for x in range(0, rows):
                for y in range(0, cols):
                    if field[x][y] != -1 and buttons[x][y]["state"] == "normal":
                        win = False
            if win:
                tkinter.messagebox.showinfo("Gave Over", "You have won.")


        if os.path.exists("config.ini"):
            loadConfig()
        else:
            saveConfig()

        createMenu()

        prepareWindow()
        prepareGame()
        window.mainloop()
    # To load game "snake"
    if input_user_2 == "snake":
        WIDTH = 500
        HEIGHT = 500


        class Snake(Frame):

            def __init__(self):
                Frame.__init__(self)
                # Set up the main window frame as a grid
                self.master.title("Snake *** Try to beat the high score! ***")
                self.grid()

                # Set up main frame for game as a grid
                frame1 = Frame(self)
                frame1.grid()

                # Add a canvas to frame1 as self.canvas member
                self.canvas = Canvas(frame1, width=WIDTH, height=HEIGHT, bg="white")
                self.canvas.grid(columnspan=3)
                self.canvas.focus_set()
                self.canvas.bind("<Button-1>", self.create)
                self.canvas.bind("<Key>", self.create)

                # Create a "New Game" button
                newGame = Button(frame1, text="New Game", command=self.new_game)
                newGame.grid(row=1, column=0, sticky=E)

                # Create a label to show user his/her score
                self.score_label = Label(frame1)
                self.score_label.grid(row=1, column=1)

                self.high_score_label = Label(frame1)
                self.high_score_label.grid(row=1, column=2)

                # Direction label (for debugging purpose)
                # self.direction_label = Label(frame1, text = "Direction")
                # self.direction_label.grid(row = 1, column = 2)

                self.new_game()

            def new_game(self):
                self.canvas.delete(ALL)
                self.canvas.create_text(WIDTH / 2, HEIGHT / 2 - 50, text="Welcome to Snake!" \
                                                                         + "\nPress arrow keys or click in the window" \
                                                                         + " to start moving!", tag="welcome_text")

                rectWidth = WIDTH / 25

                # Initialize snake to 3 rectangles
                rect1 = self.canvas.create_rectangle(WIDTH / 2 - rectWidth / 2, HEIGHT / 2 - rectWidth / 2,
                                                     WIDTH / 2 + rectWidth / 2 \
                                                     , HEIGHT / 2 + rectWidth / 2, outline="#dbf", fill="#dbf" \
                                                     , tag="rect1")
                rect2 = self.canvas.create_rectangle(WIDTH / 2 - rectWidth / 2, HEIGHT / 2 - rectWidth / 2,
                                                     WIDTH / 2 + rectWidth / 2 \
                                                     , HEIGHT / 2 + rectWidth / 2, outline="#dbf", fill="#dbf" \
                                                     , tag="rect2")
                rect3 = self.canvas.create_rectangle(WIDTH / 2 - rectWidth / 2, HEIGHT / 2 - rectWidth / 2,
                                                     WIDTH / 2 + rectWidth / 2 \
                                                     , HEIGHT / 2 + rectWidth / 2, outline="#dbf", fill="#dbf" \
                                                     , tag="rect3")

                # initialize variables that contribute to smooth gameplay below:
                #
                # set rectangle width and height variables for use with new rectangles on the canvas
                self.rectWidth = rectWidth

                # lastDirection recorded because first 2 rectangles always overlap while moving,
                # but if user goes right then immediately left the snake should run into itself and
                # therefore end the game (See below functions self.check_collide and self.end_game)
                self.lastDirection = None
                self.direction = None

                # Used to force snake to expand out on first move
                self.started = False

                # Used to force game loop to halt when a collision occurs/snake out of bounds
                self.game_over = False

                # Initialize game score to 0
                self.score = 0

                # Initialize high score from file
                if (os.path.isfile("high_score.txt")):
                    scoreFile = open("high_score.txt")
                    self.high_score = int(scoreFile.read())
                    scoreFile.close()
                else:
                    self.high_score = 0

                self.high_score_label["text"] = "High Score: " + str(self.high_score)

                self.rectangles = [rect1, rect2, rect3]

                # Initialize the "dot" (which the snake "eats")
                self.dot = None

                # Start thread for snake to move when direction is set
                self.move()

            def create(self, event):
                self.lastDirection = self.direction
                if self.game_over == False:
                    if event.keycode == 111:
                        self.direction = "up"
                    elif event.keycode == 114:
                        self.direction = "right"
                    elif event.keycode == 116:
                        self.direction = "down"
                    elif event.keycode == 113:
                        self.direction = "left"
                    elif event.x < WIDTH / 2 and HEIGHT / 3 < event.y < HEIGHT - HEIGHT / 3:
                        self.direction = "left"
                        # (Debug)
                        # self.direction_label["text"] = "LEFT"
                    elif event.x > WIDTH / 2 and HEIGHT / 3 < event.y < HEIGHT - HEIGHT / 3:
                        self.direction = "right"
                        # (Debug)
                        # self.direction_label["text"] = "RIGHT"
                    elif WIDTH / 3 < event.x < WIDTH - WIDTH / 3 and event.y < HEIGHT / 2:
                        self.direction = "up"
                        # (Debug)
                        # self.direction_label["text"] = "UP"
                    elif WIDTH / 3 < event.x < WIDTH - WIDTH / 3 and event.y > HEIGHT / 2:
                        self.direction = "down"
                        # (Debug)
                        # self.direction_label["text"] = "DOWN"

            def first_movement(self):
                w = self.rectWidth
                self.canvas.delete("welcome_text")
                # Expand snake in direction chosen
                if self.direction == "left":
                    self.canvas.move("rect1", -w, 0)
                    self.canvas.after(100)
                    self.canvas.move("rect1", -w, 0)
                    self.canvas.move("rect2", -w, 0)
                elif self.direction == "down":
                    self.canvas.move("rect1", 0, w)
                    self.canvas.after(100)
                    self.canvas.move("rect1", 0, w)
                    self.canvas.move("rect2", 0, w)
                elif self.direction == "right":
                    self.canvas.move("rect1", w, 0)
                    self.canvas.after(100)
                    self.canvas.move("rect1", w, 0)
                    self.canvas.move("rect2", w, 0)
                elif self.direction == "up":
                    self.canvas.move("rect1", 0, -w)
                    self.canvas.after(100)
                    self.canvas.move("rect1", 0, -w)
                    self.canvas.move("rect2", 0, -w)
                self.canvas.after(100)

            def _move(self):
                w = self.rectWidth
                while True:
                    self.score_label["text"] = "Score: " + str(self.score)
                    if self.started == False and self.direction != None:
                        self.first_movement()
                        self.started = True
                    elif self.started == True and self.game_over == False:
                        if self.dot == None:
                            self.make_new_dot()
                        lock = threading.Lock()
                        lock.acquire()
                        endRect = self.rectangles.pop()
                        frontCoords = self.canvas.coords(self.rectangles[0])
                        endCoords = self.canvas.coords(endRect)
                        # (Below for Debugging)
                        # print self.direction
                        # print "Front: " + str(frontCoords) + " Back: " + str(endCoords)
                        if self.direction == "left":
                            self.canvas.move(self.canvas.gettags(endRect), int(frontCoords[0] - endCoords[0]) - w, \
                                             int(frontCoords[1] - endCoords[1]))
                        elif self.direction == "down":
                            self.canvas.move(self.canvas.gettags(endRect), int(frontCoords[0] - endCoords[0]), \
                                             int(frontCoords[1] - endCoords[1]) + w)
                        elif self.direction == "right":
                            self.canvas.move(self.canvas.gettags(endRect), int(frontCoords[0] - endCoords[0]) + w, \
                                             int(frontCoords[1] - endCoords[1]))
                        elif self.direction == "up":
                            self.canvas.move(self.canvas.gettags(endRect), int(frontCoords[0] - endCoords[0]), \
                                             int(frontCoords[1] - endCoords[1]) - w)
                        self.canvas.after(100)
                        self.rectangles.insert(0, endRect)
                        lock.release()
                        self.check_bounds()
                        self.check_collide()
                    elif self.game_over == True:
                        break;

            def move(self):
                threading.Thread(target=self._move).start()

            def make_new_dot(self):
                if self.dot != None:
                    self.canvas.delete(self.dot)
                    self.dot = None
                dotX = random.random() * (WIDTH - self.rectWidth * 2) + self.rectWidth
                dotY = random.random() * (HEIGHT - self.rectWidth * 2) + self.rectWidth
                self.dot = self.canvas.create_rectangle(dotX, dotY, dotX + self.rectWidth, dotY + self.rectWidth \
                                                        , outline="#ddd", fill="#ddd", tag="dot")

            def grow(self):
                w = self.rectWidth
                lock = threading.Lock()
                lock.acquire()

                # Increase the score any time the snake grows
                self.score += 100

                endCoords = self.canvas.coords(self.rectangles[len(self.rectangles) - 1])
                # (Debug)
                # print "endCoords: " + str(endCoords)
                thisTag = "rect" + str(len(self.rectangles) + 1)
                x1 = int(endCoords[0])
                y1 = int(endCoords[1])
                x2 = int(endCoords[2])
                y2 = int(endCoords[3])

                if self.direction == "left":
                    x1 += w
                    x2 += w
                elif self.direction == "right":
                    x1 -= w
                    x2 -= w
                elif self.direction == "down":
                    y1 -= w
                    y2 -= w
                elif self.direction == "up":
                    y1 += w
                    y2 += w
                # (Debug)
                # print self.direction
                # print "new coords: " + str(x1) + ", " + str(y1) + ", " + str(x2) + ", " + str(y2)
                thisRect = self.canvas.create_rectangle(x1, y1, x2, y2, outline="#dbf", \
                                                        fill="#dbf", tag=thisTag)
                # print str(self.rectangles)
                self.rectangles.append(thisRect)
                # print str(self.rectangles)
                lock.release()

            def check_bounds(self):
                coordinates = self.canvas.coords(self.rectangles[0])
                if len(coordinates) > 0:
                    if coordinates[0] < 0 or coordinates[1] < 0 or coordinates[2] > WIDTH \
                            or coordinates[3] > HEIGHT:
                        self.end_game()

            def check_collide(self):
                frontCoords = self.canvas.coords(self.rectangles[0])

                # (For Debugging)
                # for rect in self.rectangles:
                # coords = self.canvas.coords(rect)
                # print "Front: " + str(frontCoords) + "coords: " + str(coords)

                # Check to see if the snake's head(front) is overlapping anything and handle it below
                overlapping = self.canvas.find_overlapping(frontCoords[0], frontCoords[1] \
                                                           , frontCoords[2], frontCoords[3])
                for item in overlapping:
                    if item == self.dot:
                        # Snake collided with dot, grow snake and move dot
                        self.grow()
                        self.make_new_dot()
                    if item in self.rectangles[3:]:
                        # Snake has collided with its body, end game
                        self.end_game()

                # Snake tried to move backwards (therefore crashing into itself)
                if (self.lastDirection == "left" and self.direction == "right") or \
                        (self.lastDirection == "right" and self.direction == "left") or \
                        (self.lastDirection == "up" and self.direction == "down") or \
                        (self.lastDirection == "down" and self.direction == "up"):
                    self.end_game()

            def end_game(self):
                self.game_over = True
                self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text="GAME OVER!")
                if self.score > self.high_score:
                    scoreFile = open("high_score.txt", "w")
                    scoreFile.write(str(self.score))
                    scoreFile.close()
                    self.canvas.create_text(WIDTH / 2, HEIGHT / 2 + 20, text= \
                        "You beat the high score!")

                # (Debug)
                # self.direction_label["text"] = "ENDED"


        Snake().mainloop()
    # To load the game "Bubble Blaster"
    if input_user_2 == "Bubble Blaster":
        HEIGHT = 768
        WIDTH = 1366
        window = Tk()
        colors = ["darkred", "green", "blue", "purple", "pink", "lime"]
        health = {
            "ammount": 3,
            "color": "green"
        }
        window.title("Bubble Blaster")
        c = Canvas(window, width=WIDTH, height=HEIGHT, bg="darkblue")
        c.pack()
        ship_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill="green")
        ship_id2 = c.create_oval(0, 0, 30, 30, outline="red")
        SHIP_R = 15
        MID_X = WIDTH / 2
        MID_Y = HEIGHT / 2
        c.move(ship_id, MID_X, MID_Y)
        c.move(ship_id2, MID_X, MID_Y)
        ship_spd = 10
        score = 0


        def move_ship(event):
            if event.keysym == "Up":
                c.move(ship_id, 0, -ship_spd)
                c.move(ship_id2, 0, -ship_spd)
            elif event.keysym == "Down":
                c.move(ship_id, 0, ship_spd)
                c.move(ship_id2, 0, ship_spd)
            elif event.keysym == "Left":
                c.move(ship_id, -ship_spd, 0)
                c.move(ship_id2, -ship_spd, 0)
            elif event.keysym == "Right":
                c.move(ship_id, ship_spd, 0)
                c.move(ship_id2, ship_spd, 0)
            elif event.keysym == "P":
                score += 10000


        c.bind_all('<Key>', move_ship)
        from random import randint

        bub_id = list()
        bub_r = list()
        bub_speed = list()
        bub_id_e = list()
        bub_r_e = list()
        bub_speed_e = list()
        min_bub_r = 10
        max_bub_r = 30
        max_bub_spd = 10
        gap = 100


        def create_bubble():
            x = WIDTH + gap
            y = randint(0, HEIGHT)
            r = randint(min_bub_r, max_bub_r)
            id1 = c.create_oval(x - r, y - r, x + r, y + r, outline="white", fill="lightblue")
            bub_id.append(id1)
            bub_r.append(r)
            bub_speed.append(randint(5, max_bub_spd))


        def create_bubble_e():
            x = WIDTH + gap
            y = randint(0, HEIGHT)
            r = randint(min_bub_r, max_bub_r)
            id1 = c.create_oval(x - r, y - r, x + r, y + r, outline="black", fill="red")
            bub_id_e.append(id1)
            bub_r_e.append(r)
            bub_speed_e.append(randint(6, max_bub_spd))


        def create_bubble_r():
            x = WIDTH + gap
            y = randint(0, HEIGHT)
            r = randint(min_bub_r, max_bub_r)
            id1 = c.create_oval(x - r, y - r, x + r, y + r, outline="white", fill=colors[0])
            bub_id.append(id1)
            bub_r.append(r)
            bub_speed.append(randint(6, max_bub_spd))


        def move_bubbles():
            for i in range(len(bub_id)):
                c.move(bub_id[i], -bub_speed[i], 0)
            for i in range(len(bub_id_e)):
                c.move(bub_id_e[i], -bub_speed_e[i], 0)


        from time import sleep, time

        bub_chance = 30


        def get_coords(id_num):
            pos = c.coords(id_num)
            x = (pos[0] + pos[2]) / 2
            y = (pos[1] + pos[3]) / 2
            return x, y


        def del_bubble(i):
            del bub_r[i]
            del bub_speed[i]
            c.delete(bub_id[i])
            del bub_id[i]


        def clean():
            for i in range(len(bub_id) - 1, -1, -1):
                x, y = get_coords(bub_id[i])
                if x < -gap:
                    del_bubble(i)


        def distance(id1, id2):
            x1, y1 = get_coords(id1)
            x2, y2 = get_coords(id2)
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


        def collision():
            points = 0
            for bub in range(len(bub_id) - 1, -1, -1):
                if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
                    points += (bub_r[bub] + bub_speed[bub])
                    del_bubble(bub)
            return points


        def cleanAll():
            for i in range(len(bub_id) - 1, -1, -1):
                x, y = get_coords(bub_id[i])
                del_bubble(i)


        def collision_e():
            for bub in range(len(bub_id_e) - 1, -1, -1):
                if distance(ship_id2, bub_id_e[bub]) < (SHIP_R + bub_r_e[bub]):
                    window.destroy()
                    print("You were killed by a red bubble...")
                    print("You got ", score, " score!")
                    sleep(100)


        c.create_text(50, 30, text="SCORE", fill="white")
        st = c.create_text(50, 50, fill="white")
        c.create_text(100, 30, text="TIME", fill="white")
        tt = c.create_text(100, 50, fill="white")


        def show(score):
            c.itemconfig(st, text=str(score))


        evil_bub = 50
        # MAIN GAME LOOP
        while True:
            if randint(1, bub_chance) == 1:
                create_bubble()
            if randint(1, evil_bub) == 1:
                create_bubble_e()
            if randint(1, 100) == 1:
                create_bubble_r()
            move_bubbles()
            collision_e()
            clean()
            score += collision()
            if score >= 400:
                evil_bub = 40
                bub_chance = 25
                if score >= 1000:
                    evil_bub = 30
                    bub_chance = 20
            show(score)
            window.update()
            shuffle(colors)
            sleep(0.01)
    # for encitionr
    if input_user_2 == "su encript":
        force_S_in = input("enter pass")
        if force_S_in == "admin123":
            class Encript():
                def translate(phrase):
                    translation = ""
                    for letter in phrase:
                        if letter in "aA":
                            translation = translation + "!>"
                        if letter in "bB":
                            translation = translation + "@>"
                        if letter in "cC":
                            translation = translation + "#>"
                        if letter in "dD":
                            translation = translation + "$>"
                        if letter in "eE":
                            translation = translation + "%>"
                        if letter in "fF":
                            translation = translation + "^>"
                        if letter in "gG":
                            translation = translation + "&>"
                        if letter in "hH":
                            translation = translation + "*>"
                        if letter in "iI":
                            translation = translation + "!!>"
                        if letter in "jJ":
                            translation = translation + "@@>"
                        if letter in "kK":
                            translation = translation + "##>"
                        if letter in "lL":
                            translation = translation + "$$>"
                        if letter in "mM":
                            translation = translation + "%%>"
                        if letter in "nN":
                            translation = translation + "^^>"
                        if letter in "oO":
                            translation = translation + "&&>"
                        if letter in "pP":
                            translation = translation + "**>"
                        if letter in "qQ":
                            translation = translation + "!!!>"
                        if letter in "rR":
                            translation = translation + "@@@>"
                        if letter in "sS":
                            translation = translation + "###>"
                        if letter in "tT":
                            translation = translation + "$$$>"
                        if letter in "uU":
                            translation = translation + "%%%>"
                        if letter in "vV":
                            translation = translation + "^^^>"
                        if letter in "wW":
                            translation = translation + "&&&>"
                        if letter in "xX":
                            translation = translation + "***>"
                        if letter in "Yy":
                            translation = translation + "!!!!>"
                        if letter in "Zz":
                            translation = translation + "@@@@>"
                    return translation

                print(translate(input("entar a phrase: ")))
    # to load the GUI(present in erorrMSG.py
    if input_user_2 == "load GUI":
        GUI_ANEX()
    if input_user_2 == "root me":
        root()
    if input_user_2 == "google":
        Kernal_App_check_WEB()
        if webbrowser_availabel == True:
            WEBforGoogle()
        else:
            print("you dont have the webbrowser module, you can't browse the web!!!")
    if input_user_2 == "main root":
        MainRoot()
    if input_user_2 == "inex":
        Inex()
