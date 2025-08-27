name = (input("ENTER THE USER NAME: "))
print("HEY!",name , "WELCOME! TO THIS NEW USER INTERFACE TO MOVE FORWARD ENTER THE REQUIRED PASSWORD")
inp_password = int(input("ENTER THE PASSWORD : "))
passward =  123456
if passward == inp_password:
    print("Welcome back,", name)
else: print("sorry wrong password")