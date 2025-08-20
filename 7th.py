#file i/o(cab be used to perform operations on a file read and write datA)
#types of all files
#text files .txt, .docx,.log
#binaryfiles .mp4,.mov,.png,.jpeg

#open read close files
#f= open("file_name","mode")  
#"file_mode" is sample.txt or demo.docx
#"mode" is read mode and wirte mode
#data = f.read()
#f.close()



f =open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

#r = open for reading
#w = open for writing,truncating the file first
#x = create a new file open it for writign
#a = open for writing appending to the end of the fil;e
#b = binary code
#t = text mode
#+ = open a disk file for updating
#if we want to open binary file then in "mode" we must write "rb","wb","ab"etcn

f= open("demo.txt","r")
data=f.read(5)
print(data)
f.close()

#data=f.readline() #reads one line at a time

f = open("demo.txt","r")
data=f.readline()
print(data)
f.close()

#writing to a file
#f = open("demo.txt","w")
#f.write("this is a new line") #overwrites the entire file

# OR f=open("demo.txt","a")
#f.write("this is a new file")

f= open("demo.txt","a")
f.write("hi hi hi hi hi hi hi hi hi hi")
f.close()

f=open("demo1.txt","w")
f.write("i have overwrote  this page")
f.close()


#if weopen and edit a filethat doesnt exist then after we runthe pr0gram the wirtten name of the file will automatically be created

#r+ = open forreading and writing  overwrites the files in the start by replacing the new word or sentance by the first word 

f = open("demo.txt","r+")

f.write("whyyy")
print(f.read())
f.close()

#with syntax
#with open("demo.txt","a") as f:
#data=f.read()

with open("demo.txt","r") as f:
    data = f.read()
    print(data)

#deleting a file(using the os module)

import os
os.remove("demo1.txt")  #file gets deleted


#hw
with open("p1.txt","r") as f:
    data = f.read()
    print(data)
    new_data=data.replace("java","python")
    print(new_data)

with open("p1.txt","w") as f:
    f.write(new_data)
