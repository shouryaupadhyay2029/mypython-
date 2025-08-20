#DICTIONARY (STORE DATA VALUE IN KEY:VALUE)
#THEY ARE UNORDERED,MUTABLE
#dict = {"name":"xyz"} key is name value is xyz

dict = {"name":"shourya",
        "wife":"shreya",
        "age":"19"}
print(dict)
print(dict["name"])
dict["age"]="18"   #MUTABILITY
print(dict)


null_dict = {}
null_dict["name"] = "upadhyay"
print(null_dict)

#NESTED DICTIONARY
dict1 ={
    "name":"shourya",
    "qualification":"12th pass",
    "score":{
        "phys":"80",
        "chem":"76",
        "maths":"63"
    }
}
print(dict1)
print(dict1["score"])
print(dict1["qualification"])

#DICTIONARY METHODS****
#dict.keys() returns all keys
#dict.values() returns all values
#dict.items() returns all(key,val) pairs
#dict.get("key") returns key according to value
#dict.update(newdict) insert the specifies items to dict

dict1 ={
    "name":"shourya",
    "qualification":"12th pass",
    "score":{
        "phys":"80",
        "chem":"76",
        "maths":"63"
    }
}

print(dict1.keys())
print(dict1.values())
print(dict1.items())

#SET(COLLECTIONOF UNORDERED ITEMS)
#EACH ELEMENT IN SET MUST BE UNIQUE AND MUTABLE

#nums = {1,2,3,4}
#set2 = {1,2,2,2} repeated elemnts stored only once so it resolved to {1,2}
null_set = set()  #emoty set syntax

set ={1,2,2,3,"hello","world"}
print(set)
print(type(set))
print(len(set))

set1 = {}#this is not a set but dictionary
print(type(set1))

#to have an empty set

#collection = set()

#print(type(collection))

#set.add(el) adds an element
#set.remove(el) removes the element
#set.clear() empties the set
#set.pop() removes element of random value

set3 = {1,2,3,4,5,6,7,8}
print(set3.add(1000000))
print(set3.remove(1))
print(set3)

#set.union(set2) combines both set values and returns new
#set.intersection(set2) combines common values and returns new
set4 = {1,2,3,4,5}
set5 = {6,7,8,9,10}
print(set4.union(set5)) 
print(set4.intersection(set5)) 

dict5 = {
    "table":("a piece of furniture","list of facts&figures"),
    "cat":"a small animal"
}
print(dict5)

set6 = {
    "python","c","c++","java","javascript","python"
}
print(set6)