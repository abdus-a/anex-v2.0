import mysql.connector
comm = ""
host_name = "localhost"
user_name = "root"
password_of_user = "password"
database_name = "anex"
passs = "admin"
outPut = ""
all_commands = ["show all info", "show info", "show pass", "show databases", "show private info of", "end"]
def command_all_info():
        mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password_of_user, database=database_name)
        mycursor = mydb.cursor()
        mycursor.execute("select * from user_info")
        for i in mycursor:
                print(i)
def command_show_user_pass_name():
        Id_input = input("Enter id no: ")
        mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password_of_user, database=database_name)
        mycursor = mydb.cursor()
        mycursor.execute("select * from user_info where user_id = " + Id_input)
        for i in mycursor:
                print(i)
def command_show_pass_only():
        Id_input = input("enter id: ")
        mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password_of_user, database=database_name)
        mycursor = mydb.cursor()
        mycursor.execute("select userpass from user_info where user_id = " + Id_input)
        for i in mycursor:
                print(i)
def command_show_all_user_private():
        mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password_of_user, database=database_name)
        mycursor = mydb.cursor()
        mycursor.execute("select * from user_private")
        for i in mycursor:
                print(i)
def command_select_per_form_user_private():
        mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password_of_user, database=database_name)
        mycursor = mydb.cursor()
        pass_for_private_info = input("enter password for private: ")
        if pass_for_private_info == "admin":
                Id_input_up = input("enter user id")
                mycursor.execute("select * from user_private where user_id = " + Id_input_up)
                for i in mycursor:
                        print(i)
def show_all_command():
        print(all_commands)
def sssc():
    check = input("enter pass: ")
    if check == passs:
            print("[OK]")
            while True:
                    if check == passs:
                            comm = input("enter command: ")
                            if comm == "show all info;":
                                    command_all_info()
                            if comm == "show info;":
                                    command_show_user_pass_name()
                            if comm == "end":
                                    print("command line stop")
                                    break
                            if comm == "show pass":
                                    command_show_pass_only()
                            if comm == "show databases;":
                                    print("[user_id], [user_private], [dose_what], [commands_for_normal]")

                            if comm == "show private info of;":
                                    command_select_per_form_user_private()
                            if comm == "show all commands;":
                                    show_all_command()
                            else:
                                    print(comm + " is not a command type \"show all command\" for commands")
    else:
            print("incorect pass restart")
            print("_____end______[restart]")
            print("{off________---}")

def Main():
    sssc()
