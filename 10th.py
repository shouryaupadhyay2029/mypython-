#del keyword(used to delete propertiesoor object itself)
#dels1.name  del s1

class student:                  
    def __init__(self,name):
        self.name=name

s1=student("shourya")
print(s1.name)  #will showname here 
del s1.name
print(s1.name)  #will show error because after del the name is deletd


#private(like) attributes &methods
#private attrand methods aremeant to be used only within the class and are not accessible from the outsideclass

class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass   #to make an attribute private just ADD 2 UNDERSCORE BEFORE IT 

acc1=  account("12345678","wxyz")
print(acc1.acc_no)
print(acc1.__acc_pass)  #this will show errorsince the acc_pass has been privated

class person:
    __name="annonymous"

    def __hello(self):
        print("hello person")  #WELCOME ATTRIBUTES ACCESSING HELLO ATTRIBUTESREPRESENTS THAT ATTRIBUTES INSIDE A CLASS CAN ONLY ACCESS THEMSELVES 

    def welcome(self):
        self.__hello()

p1=person()
p1.welcome()

#inheritance(when one class child derives the properties and methopds of parent class)
#class car:...    class toyotacar(car):.....

class car:
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class toyotacar(car): #all the attributes of parent class are automatically added by default to inherited class
    def __init__(self,name): #single level inht.
        self.name=name

class fortuner(toyotacar):
    def __init__(self, type):
        self.type=type
car1 = toyotacar("fortuner")
car1= fortuner("diesel")
print(car1.start())

#inheritence are of 3 types
#single level  #multi level inht.  #multiple inht.

#multiple inht. means multiple parent class and 1 child class

class cricket:
    crik="i love cricket"
class football:
    foob="i dont know football"

class both(cricket,football):
    boo="i love both"
c1=both(
)
print(c1.boo)
print(c1.crik)
print(c1.foob)

#super method(used to access methods of parent class)

class car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class toyotacar(car):
    def _init_(self,name,type):
        super().__init__(type) #access/connection btw child classs and parent class
        super().start()
        self.name=name

car1=toyotacar("prius","electric")
print(car1.type)

#class methods(bound to class and recieve the class as an implicit first argument)

class person:
    name ="anna"   #class attr 
    def changename(self,name):
        self.name=name   #this created a new name in the same class with "anna"
p1=person()
p1.changename("shourya")
print(p1.name)
print(person.name)  #it will still print anna

#here we have to make class atrr same 
#method 1 : 
class person:
    name ="anna"    
    def changename(self,name):
        person.name=name   #****
p1=person()
p1.changename("shourya")
print(p1.name)
print(person.name)

#method 2:
class person:
    name ="anna"   
    def changename(self,name):
        self.__class__.name="shourya"   #******
p1=person()
p1.changename("shourya")
print(p1.name)
print(person.name)

#property decorator(used on any method in the class to use themethod as a property)

class subjects:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        self.percent=str((self.phy+self.chem+self.maths)  / 3)

std1=student(99,91,93)
print(std1.percentage)
#now we have to change marks and percentage of one subject
std1.phy=86
std1.percentage() #it will not change like the marks changed

#method
class subjects:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.maths)  / 3) 
    
std1=student(99,91,93)
std1.phy=86
print(std1.percentage)

#polymorphism(same operator but diff meaning)

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def complexno(self):
        print(self.real,self.img)
cno1=complex(1,9)
cno1.complexno()

cno2=complex(999999,88888888)
cno2.complexno()

#operators and dunder functions
#a+b(addition)   a.__add__b

