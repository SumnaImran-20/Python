cities = ["Atlanta", "Baltimore,", "Chicago", "New York", "Denmark"]
print("Welcome to "+ cities[3])
print("--------------------------------------------")
cities = [1, "Baltimore,", "Chicago", "New York", "Denmark"]
print("welcome to " +cities[3])
print("--------------------------------------------")
cities.append("Los Angles")
print(cities)
print("--------------------------------------------")
cities = cities + ["Dubuques", "New Orleans"]
print(cities)
print("--------------------------------------------")
cities.insert(0, "New York")
print(cities)
print("--------------------------------------------")
smaller_list_of_cities = cities[2:5]
print(smaller_list_of_cities)
print(cities[3])
print("--------------------------------------------")
del cities [6]
print(cities)
print("--------------------------------------------")
name=["Zaid", "Daud", "Shahveer", "Farhan"]
listpop= name.pop(1)
print(listpop)
print(name)
print("--------------------------------------------")
cities = ["Atlanta", "Baltimore,", "Chicago", "New York", "Denmark"]
for x in cities:
    print(x)
print("-------------------------------------------")
for y in  range (61):
    if y == 0:
        print("ignore")
    elif y % 6 == 0:
        print("Valid Number ", y)
print("-------------------------------------------")
print("Factorial Of a number")
z = 1
for i in range (0,9):
    z = z * (i+1)
    print(z)