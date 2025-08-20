

str3 = "hdjeksdjrke"
print(len(str3))

#indexing*****
#every alphabet or numerical is assigned an index from 0 to x till the end of the word
#eg S(0)H(1)O(2)U(3)R(4)Y(5)A(6)
#here str[4] is R str[6] is A
# str[1] z is not allowed
#indexing can alsobe done by negative integer in reverse order
#eg P(-4)I(-3)H(-2)U(-1)


#slicing******(accessing part of the string)#
#str.endswith("") returns true if its is correct      ****
#str.capitalize()  captilizes first letter             ****
#str.replace(old,new)                                  ****
#str.find(word) gives 1st index of 1st occurence       ****
#str.count() counts all occurence of given element     ****

str5= "SSHHHOUURYAA"

print(str5.endswith("AA"))

print(str5.capitalize())

print(str5.count("H"))

#hw
str6 = input("enter your first name:")
print(len(str6))

#hw
str8 ="welcome to my vs code i am learning python"
print(str8.count("a"))

#condtionL statements********(if elif else)

age = int(input("enter your age please:"))

if(age>=18):
    print("you can apply for driving license")
else:
    print("sorry not applicable")

age2  = int(input("please enter your age"))

if(age2>=18):
    print("yes you can apply")
elif(age2>=80 ):
    print("sorry not ideal for this age")
else:
    print("sorry not applicable")

#hw
marks = int(input("enter your marks:"))

if(marks>=90):
    grade = "A"
elif(marks>=80):
    grade = "B"
elif(marks>=70):
    grade ="c"
else:
    grade ="d"

print("grade of the student is :", grade)


#nesting*****
age3 = int(input("please enter your age:"))

if(age3>=18):
    if(age3>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

