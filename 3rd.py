#list**(it can store elements of diff types )
#marks [44,66,44,33,11,99]  marks[0] is 44 marks[5] is 11
#student = ["me", 00,"delhi"] student[0] is me
#student[0] is shourya is possible here
#len(student) returns length

marks = [ 11,22,33,44,55]
print(marks)
print(type(marks))
print(marks[3])
print(len(marks))

marks1 = ["shreya", "binita", 11]   #MUTABLE***8
marks1[0] = "shourya"
print(marks1)

#LIST SLICING

marks2 = [22,33,88,99,99.9]
print(marks2[0:2])

#LIST METHODS*********
#list.append() adds one given element at the end
#list.sort() arranges in ascending order
#list.sort(reverse=true) in descending order
#list.reverse() reverses the lisy
#list.insert(idx,el) inserts element at given index

marks3 = [24,33,88,97]

print(marks3.append(7))
print(marks3.sort())
print(marks3)

#LIST KA KOI BHI METHOD USE KARNE KE BAAD JB TK PRINT(LIST) NHI KARENGE TB TK NEW UPDATED LIST SHOW NHI HOGS INSTEAD NONE SHOW HOGA

#list.remove() removes first occurence of element
#list.pop(idx) remkves elemetn of given index

#TUPLES(BUILT IN DATA TYPE THAT LETS US CREATE IMMUTABLE SEQUENCE OF VALUES)
#EG tup = (1,2,3,4,5,6)
#tup[0]=9 mutablility is not allowed in tuples like list

tup = (1,2,3,4,5,6)
print(tup)
print(type(tup)) 

tup1 = (1)
print(type(tup1))  
#in a single data type tuple type is assigned by element given if you want the data to be tuplethen add comma after single elemt

tup2 = ("hello",)
print(type(tup2))

#tup.index(el) returns index of first occurenceof given element
#tup.count() counts total occurence of given element

tup3 = (1,1,1,55,8,8,1)
print(tup3.count(1))
print(tup3.index(1))

#hw***
movie1 = input("enter first movie")
movie2 = input("enter 2nd movie")
movie3 = input("enter 3rd movie")
print([movie1,movie2,movie3])


grade = [10,9,8,7,6,5,4,3,2,1]
grade.sort()
print(grade)