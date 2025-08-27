#TASK1
name = (input("ENTER THE USER NAME: "))
print("HEY!",name , "WELCOME! TO THIS NEW USER INTERFACE TO MOVE FORWARD ENTER THE REQUIRED PASSWORD")
inp_password = int(input("ENTER THE PASSWORD : "))
passward =  123456
if passward == inp_password:
    print("Welcome back,", name)
else: print("sorry wrong password")

#TASK2
list_good_std = ["piyush","shourya","tom","jay"]

input_name = input(": ")

if input_name in list_good_std:
    print("you are a agood std")
else: print("you are a bad std")

#TASK3
list_good_std = ["piyush","shourya","tom","jay"]
input_name = input(": ")
for i in range(len(list_good_std)):
    if list_good_std[i] == input_name:
        print("yes you are there")
    else:
        print("oops!")
