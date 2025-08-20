#loops(used to repeat instructions)
#two types while loops and for loops
#while loops   while loop: some work

count = 1 #represents initial point where output starts
while count<=5 :   #end limit/point of output
    print("hello")
    count +=1  #adds +1 till end

i = 1
while i <=100:
    print("avengers assemble",i)
    i +=1

a = 100
while a >=1:
    print("usar",a)
    a-=1

list=1
while list <=10:
    print(list**2)
    list +=1

nums = (1,4,9,16,25,36)
x=9
w=0
while w < len(nums):
    if(nums[w]==x):
        print("found x at idx",w)
    w+=1


#break keyword****
c=1
while c<=5:
    print("helllo")
    if(c==2):
        break
    c +=1
print("end of the loop")

#continue keyword****

d=0
while d<=5:
    if(d==4):  #skips this and continue till the end
        d +=1
        continue
    print(d)
    d+=1

e=0
while e<=10:
    if(e%2==0):
        e+=1
        continue
    print(e)
    e+=1

#loops are used for sequentialtraversal
#for loops

list4 = [1,2,3]
for el in list4: #in is a keyword
    print(el)

tup=(1,2,3,4,5,6,7)
for num in tup:
    print(num)

#you can use an optional else keywords to make an end of the for loop

list5=[99,100,101,102]
for nums in list5:
    print(nums)
else:
    print("end")

str = "shourya uapdhyay"
for char in str:
    print(char)
else:
    print("nothing")

str2 = "shreya jain"
for char in str2:
    if(char=='j'):
      print("j founf")
      break
    print(char)
else:
    print("end")

#hww
list6 = [1,4,9,16,225]
for nums in list6:
    print(nums)

list7 = [36,49,64,81,100,121,144]
x=100
for nums in list7:
    if(nums==100):
      print("req number founf")
      break
    print(nums)

#RANGE FUNCTION(RETURNDS A SEQUENCE OF NUMBERS STARTING FROM 0 BY DEFAULT AND INCREMENTS BY 1 STOPS BEFORE A SPECIFIED NUMBER)

for nums in range(5):
    print(nums)

for nums in range(1,4):
    print(nums)

seq =range(10)  #nothing diff jsut diff form of whst id written above
for y in seq:
    print(y)

for i in range(100,149): #range(start,stop)
    print(i)

for i in range(9,19,3): #range(start,stop,step)
    print(i)

for i in range(0,101,2):
    print(i)

#PASS STATEMENT(NULL STATEMENT THAT DOES NOTHING)

for i in range(5):
    pass
print("useful")

#hw**(sum of first n numbers)

n = int(input("enter the value of n:"))
sum=0
for i in range(1,n+1):
    sum += i
print("total sum:",sum)

k=int(input("enter:"))
fact = 1 #factorial starts and ends from 1
i = 1
while i<=k:
    fact*=i
    i+=1  
print("factorial:",fact)

































































