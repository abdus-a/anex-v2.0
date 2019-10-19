import tkinter
import mysql.connector
true = True
false = False


class GUI:
    def test(text):
        tkw = tkinter.Tk()
        l1 = tkinter.Label(tkw, text=text)
        l1.pack()

        b1 = tkinter.Button(tkw, text=text)
        b1.pack()
        e1 = tkinter.Entry(tkw)
        e1.pack()
        tkw.mainloop()


class Sys:
    def out(prompt):
        print(prompt)
        return prompt

    def scan(prompt):
        prompt = input(prompt)
        return prompt


class DATABASE:
    def info(host_name, user_name, password, database, query, showInfo):
        mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password, database=database)
        mycursor = mydb.cursor()
        mycursor.execute(query)
        if showInfo == true:
            for i in mycursor:
                print(i)
            else:
                print("")


aout = Sys.out
ain = Sys.scan
