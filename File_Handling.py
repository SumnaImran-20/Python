import os
print("---File Handling---")
#mode: write and read 
#syntax: file = open(file name,mode)

#opening a file in python 
file = open("D:\Python\Aptech\File_Handling\demofile.txt","r")
for each in file:
    print(each)
print("-------------------------------")
#another way of opening a file in pyton
file = open("D:\Python\Aptech\File_Handling\demofile.txt","r")
print(file.read())
print("-------------------------------")

#another way to read a file to call a certain number in python
file=open("D:\Python\Aptech\File_Handling\demofile.txt","r")
print("first 10 characters in a file are:",file.read(10))
print("-------------------------------")

#OUTPUT 
"""--File Handling---
Hello! Welcome to demofile.txt

This file is for testing purposes.

Good Luck!
-------------------------------
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
-------------------------------
first 10 characters in a file are: Hello! Wel
-------------------------------
"""
#creating a file in python
file = open("D:\Python\Aptech\File_Handling\demofile.txt","w")
file.write("you entered a new line in this file.")
file.write("\nyou are doing so great.")
#The close() command terminates all the resources in use and frees the system of this particular program.
file.close()
file= open("D:\Python\Aptech\File_Handling\demofile.txt","r")
print(file.read())

#append will add to the end of the file 
file=open("D:\Python\Aptech\File_Handling\demofile.txt","a")
file.write("\nnow the file has more content!.")
file.write("\nHello")
file.close()
file= open("D:\Python\Aptech\File_Handling\demofile.txt","r")
print(file.read()) 
print("-------------------------------")
#output 
"""
---File Handling---
you entered a new line in this file.

you are doing so great.

now the file has more content!.

Hello
-------------------------------
you entered a new line in this file.
you are doing so great.
now the file has more content!.
Hello
-------------------------------
first 10 characters in a file are: you entere
-------------------------------
you entered a new line in this file.
you are doing so great.
you entered a new line in this file.
you are doing so great.
now the file has more content!.
Hello

To create a new file in Python, use the open() method, with one of the following parameters:
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
"""
#new file created 
#file =open("D:\Python\Aptech\File_Handling\myfile.txt","x")
#file =open("D:\Python\Aptech\File_Handling\sahifile.txt","x")

#delete a file
#os.remove("D:\Python\Aptech\File_Handling\sahifile.txt")
if os.path.exists("D:\Python\Aptech\File_Handling\sahifile.txt"):
    os.remove("D:\Python\Aptech\File_Handling\sahifile.txt")
else:
    print("the file does not exists!")
print("--------------------------------")
with open("D:\Python\Aptech\File_Handling\myfile.txt") as file: 
    data = file.read()

#We can also use the write function along with the  with() function:
with open("D:\Python\Aptech\File_Handling\myfile.txt", "w") as f:
    f.write("Hello World!!!")

#We can also split lines using file handling in Python. This splits the variable when space is encountered.
#You can also split using any characters as we wish. Here is the code:
with open("D:\Python\Aptech\File_Handling\myfile.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
print("----------------")
