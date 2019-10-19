c_ON = True
c_OFF = False
stored_Var = ""
var_availabele = False
ain_promt_storege = ""
IN_from_user_ain = ""
when_apoint_storage = ""
apoint_var_input_availabel = False


class PRINT:
    def __init__(self, Command):
        self.Command = Command


class STORE:
    def __init__(self, var_name, var):
        self.var_name = var_name
        self.var = var


class AIN:
    def __init__(self, promt):
        self.promt = promt


class apoint_var_input:
    def __init__(self, call_name):
        self.call_name = call_name


def main():
    PRINT.Command = input("}>")


def Inex():
    while c_ON != c_OFF:
        MAIN_INPUT = input(">>")
        if MAIN_INPUT == "out{":
            main()
            POut = PRINT.Command
            print(POut)
        if MAIN_INPUT == "DCV{":
            STORE.var = input("VAR{")
            stored_Var = STORE.var
            var_availabele = True
        if MAIN_INPUT == "outVar{":
            if var_availabele == True:
                print(stored_Var)
            else:
                print("error:!var was not declared ")
        if MAIN_INPUT == "Ain{":
            AIN.promt = input("In}")
            ain_promt_storege = AIN.promt
            input(ain_promt_storege)
            IN_from_user_ain = ain_promt_storege
        if MAIN_INPUT == "exit()":
            print("[ OK ]")
            break

