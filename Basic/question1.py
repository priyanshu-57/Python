"""
Take three space-separated inputs from the user:
	•	Name (string)
	•	Age (integer)
	•	Height in meters (float)

Then print a message using an f-string like this:
"Hello, I am Priyanshu. I am 23 years old and 1.75 meters tall."
 Challenge: Use input(), split(), typecasting, and f-string in one program.

 """
# name=input("Enter your name: ")
# age= int(input("enter your age:"))
# height= float(input("Enter your height in meter: "))

# print(f"Hello, I am {name}.I am {age} years old and {height} meters tall. ")

name, age, height= input("Enter your name , age and height in meter").split()
age=int(age) #type casting
height= float(height) 

print(f"Hello, I am {name}. I am {age} years old and {height   } meters tall.")

# Question no 2

# Take two space-separated inputs:
# 	•	First input: a decimal number (float)
# 	•	Second input: an integer

# Print their sum and a sentence showing both values using f-string formatting with 2 decimal places.


a = float(input("Enter fist no.: "))
b = int(input("Enter 2nd no.: "))

a,b= map(float, input("Enter first number and second number: ").split())

b=int(b)
sum= a+b

print(f"Sum= {sum:.2f} . You entered {a} as the float and {b} as the integer")


