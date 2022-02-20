print("---Leap year code---")
#year = int(input("Input a year: "))
year = 2000
if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 == 0:
            print("It is a leap year:",year)
        else:
            print("It is not a leapt year:",year)
    else:
        print("It is a leap year:",year)
else:
    print("It is not a leapt year:",year)
print("--------------------------------")
#OOP 
# Creating class in python
class Student:
     name = "sumna"
     age = 21

#Creating Object
student = Student()
print("Hello " + student.name)
print("your age is: ",student.age)

# Creating class in python
class Student:
    def __init__(self, name, age):
     self.name = name
     self.age = age

#Creating Object
student = Student("Sumna",21)
print("Hello " + student.name)
print("your age is: ",student.age)
print("-------------------------------------")

class Employee:
    #Class Variable = propert that are hold by class and are share 
    no_of_leaves=8


obj1 = Employee()
#Instance variable = variables that holde property of object
obj1.name ="Harry"
obj1.std =12
obj1.age = 20
print("Name is: ",obj1.name)
print("Class is: ",obj1.std)
print("Age is: ",obj1.age)
print("No of leaves is: ",obj1.no_of_leaves)
#__dict__ returns dictionary which shows how many varibale are there
print(obj1.__dict__)

obj2 = Employee()
obj2.name ="Larry"
obj2.std =11
obj2.age = 22
obj2.no_of_leaves =2
print("Name is: ",obj2.name)
print("Class is: ",obj2.std)
print("Age is: ",obj2.age)
print("No of leaves is: ",obj2.no_of_leaves)
print(obj2.__dict__)
Employee.no_of_leaves = 5
print(Employee.no_of_leaves)
print("-----------------------------------------")

class Student:
    def __init__(self, aname, asalary, aage):
        self.name = aname
        self.salary = asalary
        self.age = aage
    
    def printdetails(self):
        return f"Name is {self.name} Age is {self.age} salary is {self.salary}" 

harry = Student("Harry",25000,20)
print(harry.age)
print(harry.printdetails())
print("-------------------------------------")

def addfunction(first_number,second_number):
    add = first_number+ second_number
    print("Ths sum is:",add)

def subfunction(first_number,second_number):
    sub = first_number-second_number
    print("Ths difference is:",sub)

def mulfunction(first_number,second_number):
    mul = first_number * second_number
    print("Ths product is:",mul)

def divfunction(first_number,second_number):
    div = first_number/second_number
    print("Ths quotient is:",div)

f_number = int((input("Input First Number Please: ")))
s_number = int((input("Input Second Number Please: ")))

addfunction(f_number,s_number)
subfunction(f_number,s_number)
mulfunction(f_number,s_number)
divfunction(f_number,s_number)
print("-------------------")
num1 = int(input("Input First Number: "))
num2 = int(input("Input Second Number: "))
string = input("Input String here: ")
add = num1 + num2 
sub = num1 - num2
print(add)
print(sub)
print("HackerRank "+ string)

