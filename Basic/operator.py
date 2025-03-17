#logical- and, or and nor, not

print(True and True)
print(True and False)
print(False and True)
print(False and False)


print(True or True)
print(True and False)
print(False and True)
print(False and False)


#Ternary Operator
a= 10
b= "grater than 18" if (a>18) else "none below 18"

print(b)


#Wap in ternary operator to print if the no. is even or odd

a=4
b="a is even" if (a % 2==0) else "a is odd"

print (b)

#indentifier is, is not

a=10
b=20
c="30"
d="f"
print( a is not b)
print( a is b)

print(c is d)

#list, tuple,set and dict

array=[0,1,2,3,4,5]

#methods in-build

array.append(1)
print(array)
print(array.index(1))

array.pop()
print(array)


array.remove(0)
print(array)


b=array.copy()
array.clear()
print(array)

print(b)


b.reverse()
print(b)


#tuple
tup=(1,2,3,4,5)
print(tup)
# tup(0)=0
# print(tup) #we cant add in tuple



ab=tup.count(5)
print(ab)
bc= tup.index(1)
print(bc)

#type conversion
#string,float,int

a=10
b= float(a)
print(b)

# b= string(a)
# print(type0f(b))


#tuple -list

cd=list(tup)
cd.append(6)
cd.insert(0,7)


#list-tuple
ef=tuple(cd)
print(ef)


#set -
set1= {1,2,3,4,5,6}
print(set1)

set1.add(7)
print(set1)

set2= set1.copy()
print(set2,"set2")


set1.pop() #remove first index
print(set1)

# set1.clear
# print(set1)

set2={4,5,6,7}
print(set1.difference(set2))
print(set1.union(set2))
print(set1.intersection(set2))

#dict

dict1= {
    "name": "hari",
    "age":23

}
print(dict1)

print(dict1.items())
print(dict1.keys())
print(dict1.values())

abc=None
print(abc)

for keys, values in dict1, items():
    print(keys , values)


#print set
for i in set2:
    print(i)

#print list
for i in b:
    print(i)

#print tuple
for cde in cd:
    print(cde)

#print set into list

x={8,9,10,11,12}
print(x)


    


