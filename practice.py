for i in range (1,11):
    i = i * i * i
    print("The Cube of number is: ",i)
print("--------------------------")
print("---Leap year code---")
year = int(input("Input a year: "))
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
print("----------------------")
print("---Largest number code---")
num1 = 2
num2 = 6
num3 = 3

if num1 >= num2 and num1 >=num3:
    print("Largest Number is: ",num1)
elif num2 >= num1 and num2 >=num3:
    print("Largest Number is: ",num2)
else:
    print("Largest Number is: ",num3)
print("-----------------------------")
m = "m"
f = "f"
print("Input Your Gneder m for male and f for female:")
gender = input()
if ( gender == m):
    print("Male")
elif gender == f:
    print("Female")
else:
    print("Invalid input")
print("-----------------------------------------")
print("Series of odd numbers:")
for z in range (1,10):
    if z % 2 != 0:
        print(z)
print("----------------------------------------")
print("Input R for Red, G for Green , B for Blue")
R = "R"
B = "B"
G = "G"
color = input()
if color == R:
    print("The color is Red")
elif color == G:
    print("The color is Green")
elif color == B:
    print("The color is Blue")
else:
    print("Invalid Input")
print("-----------------------------")
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6
sunday = 7
print("Input Day Number:")
day = input()
day1 = int(day)
if day1 ==monday:
    print("Today is monday")
elif day1 ==tuesday:
    print("Today is tuesday")
elif day1 ==wednesday:
    print("Today is wednesday")
elif day1 ==thursday:
    print("Today is thursday")
elif day1 ==friday:
    print("Today is friday")
elif day1 ==saturday:
    print("Today is saturday")
elif day1 ==sunday:
    print("Today is sunday")
else:
    ("Invalid input")
print("-----------------------------")