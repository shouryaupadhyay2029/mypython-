#object oriented program
#to map with realworld scenarios we started using objects in code

#creating class
class student:
    name="Shourya upadhyay"
#creating object
s1=student()
print(s1.name)

class Car:
    color="blue"
    brand="bmw"
c1=Car()
print(c1.color)

#__init__function(constructor)
#all classes have a function called _init_() which ic alwaysw excecuted whenthe class is being initiated


class college:
    name1= "usar"
    def __init__(self):
        print("i am studying in usaar")
n1=college()

class car:
    def __init__(self,fullname):
        self.name=fullname
        print("new car")
c2=car("mercedes")
print(c2.name)
    
c3=car("audi")
print(c3.name)

class fresher: 
    college_name="usar"    #something common among diff objects can be stored one time only

    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
f1=fresher("shourya",9)
print(f1.name,f1.cgpa,f1.college_name)

f3=fresher("shreya",9.7)
print(f3.name,f3.cgpa,f3.college_name)

f2=fresher("piyush",9.5)
print(f2.name,f2.cgpa)
    
#class and instance attributes
#self.something is diff for every object
#something common among diff objects can be stored one time only

#methods(functions that belong to objects)

class newbie:
    def __init__(self,name,level):
        self.name=name
        self.level=level

    def welcome(self):
        print("welcome newbie",self.name)

    def rank(self):
        print("your rank is :", self.level)

e1=newbie("godkiller",67)
e1.welcome()
e1.rank()  #*****


class movies:
    def __init__(self,name,actor):
        self.name=name
        self.actor=actor
    def actor_name(self):
        print("actor in this movie is :",self.actor)

m1=movies("spider man 2","tobey")
m1.actor_name()

m2=movies("fight club","brad pitt")
m2.actor_name()

class superheroes:
    def __init__(self,name,marks):
        self.name= name
        self.marks=marks
    def avg_marks(self):
        sum = self.marks[0] + self.marks[1] + self.marks[2] 
        print("hi",self.name, "your score is:", sum/3)

sup1=superheroes("iron man",[99,100,99])
print(sup1.name)
sup1.avg_marks()

sup2=superheroes("thor",[69,30,78])
print(sup2.name)
sup2.avg_marks()

#STATIC METHOD(methods that dont use the self parameter)
#absraction(hiding the implentation details of a class and onlyshowingthe essential features to the user)
#encapsulation(wrapping data and functions into a single unit )

class Car:
    def __init__(self):
        self.acc=False
        self.clutch=False
        self.brk=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started....")

car3=Car()
car3.start()


#hw*****
class bank:
    def __init__(self,balance,account):
        self.balance=balance
        self.account=account
    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount,"was debited")
        print("total balance;",self.rem_balance())
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance;",self.rem_balance())
    def rem_balance(self):
        return self.balance
acc1=bank(10000,123456789)
acc1.debit(999)
acc1.credit(15000)



        
