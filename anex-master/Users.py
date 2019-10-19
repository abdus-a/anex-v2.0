from arays import *
from erorrMSG import *
import time
def root():
    root_in = ""
    root_pass = "root12"
    root_in_pass = input("enter root pass:")
    if root_in_pass == root_pass:
        print("~~~")
    if root_in_pass != root_pass:
        print("root authentication failed!!! ")
    while root_in_pass == root_pass:
        root_in = input("root/admin/~$:")
        if root_in == "exit":
            break
        if root_in == "shut down":
            root_shut = input("Are you sure you want to shut down ")
            if root_shut == "yes":
                print("shutting down...")
                time.sleep(3)
                break
        if root_in == "say":
            say_input_root = input("say~:")
            print(say_input_root)
        root_in = input("root/admin/~$:")
        if root_in == "su show user info":
            force_S_in = input("enter pass")
            if force_S_in == "admin123":
                print(users)
        if root_in == "encript":
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
        if root_in == "load GUI":
            GUI_ANEX()
        if root_in == "cal":
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
            if root_in == "study":

                input_file_name = input("enter subject:")
                if input_file_name == file_name[0]:
                    file_ch_input = input("enter chapter name:")
                    if file_ch_input == "one":
                        print(file_info_hist_for_ch_one)

                note_ch_one_history = input("Do you want to get the note's for this ")
                if note_ch_one_history == "yes":
                    print(ch_note_history, ch_note_history_2, ch_note_history_3)
            # to show info of the OS(present in arays.py)
        if root_in == "pc info":
            print("os:- anex 4.0.0 , os type:- terminal Based , os programed in:- python3")
            # to show human command that are availabe(present in arays.py)
        if root_in == "cmd":
            print("show user info,show user pass, cal, time , shut down,launch clock, study,pc info")
            # to show human command that are availabe in GUIl(present in erorrMSG.py)
        if root_in == "cmd-H":
            CmdHuman()

        if root_in == game:
            print("Root dose not have acess to games, clock")
        if root_in == "google":
            WEBforGoogle()

def MainRoot():
    users = {
        "root": {
            "password": "root12",
            "group": "admin",
            "mail": []
        }
    }

    # Form validation
    def validate(form):
        if len(form) > 0:
            return False
        return True

    # Login authorization
    def loginauth(username, password):
        if username in users:
            if password == users[username]["password"]:
                print("Login successful")
                return True
        return False

    # Login
    def login():
        while True:
            username = input("Username: ")
            if not len(username) > 0:
                print("Username can't be blank")
            else:
                break
        while True:
            password = input("Password: ")
            if not len(password) > 0:
                print("Password can't be blank")
            else:
                break

        if loginauth(username, password):
            return session(username)
        else:
            print("Invalid username or password")

    # Register
    def register():
        while True:
            username = input("New username: ")
            if not len(username) > 0:
                print("Username can't be blank")
                continue
            else:
                break
        while True:
            password = input("New password: ")
            if not len(password) > 0:
                print("Password can't be blank")
                continue
            else:
                break
        print("Creating account...")
        users[username] = {}
        users[username]["password"] = password
        users[username]["group"] = "user"
        users[username]["mail"] = []
        time.sleep(1)
        print("Account has been created")

    # Send mail
    def sendmail(username):
        while True:
            recipient = input("Recipient > ")
            if not len(recipient) > 0:
                print("Recipient can't be blank")
                continue
            elif recipient not in users:
                print("There is no account with that username")
                continue
            else:
                break
        while True:
            subject = input("Subject > ")
            if not len(subject) > 0:
                print("Subject can't be blank")
                continue
            else:
                break
        while True:
            context = input("Context > ")
            if not len(context) > 0:
                print("Context can't be blank")
            else:
                break
        print("Sending mail...")
        users[recipient]["mail"].append(["Sender: " + username, "Subject: " + subject, "Context: " + context])
        time.sleep(1)
        print("Mail has been sent to " + recipient)

    # User session
    def session(username):
        print("Welcome to your account " + username)
        print("Options: view mail | send mail | logout")
        if users[username]["group"] == "admin":
            print("")
        while True:
            option = input(username + " > ")
            if option == "logout":
                print("Logging out...")
                break
            elif option == "view mail":
                print("Current mail:")
                for mail in users[username]["mail"]:
                    print(mail)
            elif option == "send mail":
                sendmail(username)
            elif users[username]["group"] == "admin":
                if option == "user mail":
                    print("Whos mail would you like to see?")
                    userinfo = input("> ")
                    if userinfo in users:
                        for mail in users[userinfo]["mail"]:
                            print(mail)
                    else:
                        print("There is no account with that username")
                elif option == "delete mail":
                    print("Whos mail would you like to delete?")
                    userinfo = input("> ")
                    if userinfo in users:
                        print("Deleting " + userinfo + "'s mail...")
                        users[userinfo]["mail"] = []
                        time.sleep(1)
                        print(userinfo + "'s mail has been deleted")
                    else:
                        print("There is no account with that username")
                elif option == "delete account":
                    print("Whos account would you like to delete?")
                    userinfo = input("> ")
                    if userinfo in users:
                        print("Are you sure you want to delete " + userinfo + "'s account?")
                        print("Options: yes | no")
                        while True:
                            confirm = input("> ")
                            if confirm == "yes":
                                print("Deleting " + userinfo + "'s account...")
                                del users[userinfo]
                                time.sleep(1)
                                print(userinfo + "'s account has been deleted")
                                break
                            elif confirm == "no":
                                print("Canceling account deletion...")
                                time.sleep(1)
                                print("Account deletion canceled")
                                break
                            else:
                                print(confirm + " is not an option")
                    else:
                        print("There is no account with that username")
            else:
                print(option + " is not an option")
            if option == "say hello":
                print("hello")
            if option == "cal":
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

    # On start
    print("Welcome to the system. Please register or login.")
    print("Options: guest | login | exit")
    while True:
        option = input("> ")
        if option == "login":
            login()
        elif option == "guest":
            register()
        elif option == "exit":
            break
        else:
            print(option + " is not an option")

    # On exit
    print("Shutting down...")
    time.sleep(1)