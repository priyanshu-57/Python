# #How to print(output) and different types

# #print string
# print(" hey there")


# #print varibles

# age= 23
# print("Your age is", age)


# #print multiple variables

# name="Priyanshu"
# age=23

# print("My name is",name,"and I am",age)


# #print using f -string(modern and clean)


# EmpName= "Prinanshu"
# Id= 10425

# print(f"Employee name is {EmpName} and his id is {Id}")

#  #insert expresion in f string printing
# a,b= map(int,input("Enter two no.: ").split())

# print(f"Sum of {a} and {b} is {a+b}")


# #print on same line or add a seperator

# print("Priyanshu ",end="")  #dont go in new line
# print("Kushawaha")

# #adding seperator

# print("A","B", "C",sep="-")


#print the data type of input 

a= "Earth"
b= 23
c= 23.45
d= ("a","b","c","d")
e= ["a","b","c","d"]

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))