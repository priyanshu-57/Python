#input types

#string input

name= input("Enter your name : ")  #by default

#Interger input

age= int(input("Enter your age :"))

#float

height= float(input("Enter your height: "))


print(name)
print(age)
print(height)
#multiple input

x,y= input("Enter x and y: ").split()
print(x,y)

#specify type in multiple input

a,b= map(int,input("Enter two number").split())
print("First no.",a,"Second no.",b)
p,q= map(int,input("Enter two no.").split())

print("First no is :",p, "The second no. is: ",q)

