states = ("Delaware", "Pennsylvania", "New Jersey", "Gerogia")
print(states)
#Tuples representation k liye use nhi hota 
print("-----------------------------------------------------")
for i in states:
    print(i)
print("----------------------------------------------------")
#Dictionaries
cutomer_2987 = {"first name":"David","last name":"Elliot", "address":"4803 Wellesley St."}
print(cutomer_2987)
first_name= cutomer_2987["first name"]
last_name= cutomer_2987["last name"]
address= cutomer_2987["address"]
print("First name of customer is:",first_name)
print("Last name of customer is:",last_name)
print("Address of customer is: ",address)
print("---------------------------------------------------")
# Dictionary data type 
things_to_remember ={ 0:"lowest number", "a dozen": 12, "snake eye":"pair of ones", 13: "a baker's dozen"}
print(things_to_remember)
print(things_to_remember[0])
print(things_to_remember["a dozen"])
print(things_to_remember["snake eye"])
print(things_to_remember[13])
print("The length is: ",len(things_to_remember))
print("---------------------------------------------------")
#Duplicates are not allowed in dictionaries
cars={
    "brand": "Fords",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(cars["year"])
print("----------------------------------------------------")



