print("---sets in python---")
#sets are undored , mutable and no duplicates
myset = {1,2,3,4,5}
print(myset)
#set() method is mutable 
sets =set([2,4,6,8,10])
print(sets)
sets =set(["hello world!"])
print(sets)
#how many differeny character are there in a sets
sets =set("hello world!")
print(sets)
#empty set 
myset = set()
print(type(myset))
print("-------------")

#adding elements in a set
myset1 =set()
myset1.add(1)
myset1.add(2)
myset1.add(3)
myset1.add(4)
myset1.add(6)
print(myset1) 

#removing or discarding an element
myset1.remove(2)
myset1.remove(6)
print(myset1)

#popping an element
print(myset1.pop())
print("-------------")

#loop on a set
for i in myset1:
    print(i)
print("-------------")

#union and intersection
odd ={1,3,5,7,9}
even ={0,2,4,6,8,10}
primenumber={2,3,5,7,11}
u = odd.union(even)
print("the union is: ",u)
i = odd.intersection(even)
print("the intersection is: ",i)
ep = even.intersection(primenumber)
print("the even prime number is: ",ep)
print("-------------")

#Operations on sets
setA={1,2,3,4,5,6,7,8,9}
setB={10,11,12,13,1,2,3}
diff = setA.difference(setB)
print(diff)
diff1 = setB.difference(setA)
print(diff1)
diff2 = setA.symmetric_difference(setB)
print("the symetric difference is: ",diff2)
setA={1,2,3,4,5,6,7,8,9}
setB={10,11,12,13,1,2,3}
setA.update(setB)
print("now set A is:",setA)
setA={1,2,3,4,5,6,7,8,9}
setB={10,11,12,13,1,2,3}
setA.intersection_update(setB)
print("now set A is:",setA)
setA={1,2,3,4,5,6,7,8,9}
setB={10,11,12,13,1,2,3}
setA.difference_update(setB)
print("now set A is:",setA)
setA={1,2,3,4,5,6,7,8,9}
setB={10,11,12,13,1,2,3}
setA.symmetric_difference_update(setB)
print("now set A is:",setA)

setA={1,2,3,4,5,6}
setB={1,2,3}
setC ={7,8}
print("is set A is a subset of B: ",setA.issubset(setB))
print("is set B is a subset of A: ",setB.issubset(setA))
print("is set A is a superset of B: ",setA.issuperset(setB))
print("is set B is a superset of A: ",setB.issuperset(setA))
print("is set A is a disjoint of C: ",setA.isdisjoint(setC))
print("-------------")

#coping in sets
setA={1,2,3,4,5,6}
setB= setA.copy()
setB.add(7)
##setB= set(setA) can also be used for coping
print(setB)
print(setA)

#frozen sets are immutable
a=frozenset([2,3,4,5,6,7,8,9,10,11,12,13,14])
#a.add(15) gives an error
#a.remove(2) gives an error 
print(a)