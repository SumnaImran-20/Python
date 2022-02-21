#Strings are immutable , ordered and text representation
from hashlib import new


print("---Strings in python---")

#using single or double qoutes
mystring='Hello World!'
print(mystring)
mystring= "i am a coder."
print(mystring)
mystring= "i am a 'coder'."
print(mystring)

#escaping blacklash
my_string = 'I\' m  a "Geek"'
my_string = 'I\' m a \'Geek\''
print(my_string)

# triple quotes for multiline strings
my_string = """Hello
World"""
print(my_string)

# backslash if you want to continue in the next line
my_string = "Hello \
World"
print(my_string)
print("----------------------")

#Accesing character annd substring
mystring= "Hello World!"
a = my_string[0]
print(a)
#note that last index is not included
b=my_string[0:4]
print(b)
#from beginning
b=my_string[:8]
print(b)
#until the end
b=my_string[6:]
print(b)
#start to end with every second in item
b=my_string[::2]
print(b)
#reverse the string with negative step
b=my_string[::-1]
print(b)
print("----------------------")

#Concatinating two or more string
greeting= "hello"
name = "tom"
sentence = greeting +" "+ name
print(sentence)
print("----------------------")

#iterating 
for x in my_string:
    print(x) 
print("----------------------")

#check if a character or substring exists
if "e" in "sentence":
    print("yes")
if "tence" in "sentence":
    print("yes")
else:
    print("no")
print("----------------------")

#usefull methods
my_string = '     Hello World '
my_string = my_string.strip() #strip() remove extra spaces
print(my_string)
my_string = mystring.upper() #change character into capital
print(my_string)
my_string = mystring.lower() #change character into lower
print(my_string)

#start and end withs which returns and false
print("hello".startswith("he"))
print("hello".endswith("lo"))

#find first index of the string
print("Hello".find("H"))

# count number of characters/substrings
#if does not find the string it will return -1
print("Hello".count("l"))

#replacing a substring with another string
message = "Hello World"
new_message = message.replace("World","Universe")
print(new_message)

#split the string into list
my_string = "how,are,you,doing"
a_list = my_string.split(",") #default argument is null " "
print(a_list)
my_string = "one,two,three"
a_list = my_string.split(",")
print(a_list)
my_string = "how are you doing"
a_list = my_string.split()
print(a_list)

#joining elements of a lists into a string
my_list = ['How', 'are', 'you', 'doing']
a = ' '.join(my_list) # the given string is the separator, e.g. ' ' between each argument
print(a)
print("----------------------")