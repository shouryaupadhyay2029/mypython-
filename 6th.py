#FUNCTION(BLOCK OF STATEMENTS THAT PERFORM SPECIFIC TASK)def
#def func_name(parameter1, parameter2):
#some work
#return value

def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum
calc_sum(3,4)   #reduces repeatation in python coding complets same task by a single function
calc_sum(99,19999)

def calc_fact(c,d):
    fact = c**d
    print(fact)
    return fact
calc_fact(99,10)

def print_hello():
    print(print_hello)

#try to find average for 3 numebers

def calc_avg(e,f,g):
    sum = e+f+g
    avg=sum/3
    print(avg)
    return avg
calc_avg(1,2,3)
calc_avg(10,10,10)

#types of functions
#built in function print(),len(),type(),range()
#user defined functions

#default parametre
def calc_prod(h,j=3):  #def calc_....(a=2,b): is not allowed
    prod = h*j
    print(h*j)
    return prod
calc_prod(2,)

#hw*
list=[1,2,3,4,5,6,6,8,9,10]
list2=["ironman","thor","hulk","sentry"]
def print_len(list):
    print(len(list))
print_len(list)
print_len(list2)

#hw**(print list in single line)
list3=[0,0,0,0,0,0,"heroes"]
def single_line(list):
    for val in list:
        print(val,end=" ")  #end=" " means to print something in single line
    
single_line(list3)


#hw
def money_conversion(dollar,rupee=83):
    conversion = dollar*rupee
    print(conversion)
    return conversion
money_conversion(1,)
money_conversion(10,)

#RECURSION(when a function calls itself repeatedly)
#print n to 1 backwards
def show(n):
    if(n==0):   #recursion is advanced version of loops
        return
    print(n)
    show(n-1)
show(5)

def fact(n):
    if(n==0 or n==1):  #base case
        return 1  
    return n * fact(n-1)
print(fact(5))

#inheritence are of 3 types
#single level inht.
#multi level inht.
#multiple inht.




    