print("---Functions---")
def addnumber():
    firstnumber = 2
    secondnumber = 3
    total = firstnumber + secondnumber
    print("Sum is: ",total)
addnumber()
print("-------------")

def add_numbers(first_number, second_number): #parameters are also called signature
    total = first_number + second_number
    print("Sum is: ",total)
add_numbers(1.11,2.22)
add_numbers("sumna", "fazila")
#add_numbers("sumna", 2) can not be concatenate
print("-------------")

#Named argumnets/ labelled arguments
def say_name_of_couple(husband_name, wife_name):
    print("The name of the couple are " + husband_name + " and "+wife_name)
say_name_of_couple(husband_name="Bill", wife_name ="Zelda")
print("-------------")

def calc_tax(sales_total, tax_rate = .05):
    print("Answer is: ",sales_total * tax_rate)
calc_tax(sales_total=101.37)
print("----------------------")

def calc_tax(sales_total, tax_rate):
    print("Answer is: ",sales_total * tax_rate)
calc_tax(101.37,tax_rate = .05)

def give_greeting(greeting, first_name):
    print(greeting + " , "+ first_name)
give_greeting("Hello There", first_name= "Sir Taqi")
print("----------------------")
#Customer dictionary kay ander ek or dictionary ha 
cutomers = {
    0: {
        "first_name" : "John",
        "last name" : "Ogden",
        "address" : "301 Arbor Rd.",
    },
    1: {
        "first_name" : "Ann",
        "last name" : "Sattermyer",
        "address" : "PO Box 1145",
    },
    2: {
        "first_name" : "Jill",
        "last name" : "Somers",
        "address" : "3 Main St.",
    },
}
def find_something(dict, inner_dict, target):
    print(dict[inner_dict][target])

find_something(cutomers, 2, "last name")
print("------------------------")

#TASK
f_name = input("Input your first name: ")
l_name = input("Input your last name: ")

def fullname(f_name , l_name=""):
    full_name= f_name + " "+ l_name + "."
    print("Hello ",full_name)
fullname(f_name,l_name)