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

# name, age, height= input("Enter your name , age and height in meter").split()
# age=int(age) #type casting
# height= float(height) 

# print(f"Hello, I am {name}. I am {age} years old and {height   } meters tall.")

# # Question no 2

# # Take two space-separated inputs:
# # 	•	First input: a decimal number (float)
# # 	•	Second input: an integer

# # Print their sum and a sentence showing both values using f-string formatting with 2 decimal places.


# a = float(input("Enter fist no.: "))
# b = int(input("Enter 2nd no.: "))

# a,b= map(float, input("Enter first number and second number: ").split())

# b=int(b)
# sum= a+b

# print(f"Sum= {sum:.2f} . You entered {a} as the float and {b} as the integer")

"""
# Count vowels

text= input("Enter the word:")
count= 0
for ch in text:
    if ch in "aeiouAEIOU":
        count +=1
    
print("Total count=", count)
    
"""
"""
# Reverse the no.

num= int(input("Enter the no.:"))
digit=0
rev= 0
while num > 0:
  digit= num % 10
  rev= rev * 10 + digit
  num= num // 10

print("Rerverse is:", rev)
"""
"""
#👉 Take a number
👉 Print:
	•	“Fizz” if divisible by 3
	•	“Buzz” if divisible by 5
	•	“FizzBuzz” if both
"""

# num= int(input("Enter the no.:"))

# if num % 3 ==0 and num % 5 ==0:
#     print("FizzBuzz")

# elif num % 3 == 0:
#     print("fizz")

# elif num % 5 ==0:
#     print("Buzz")

# else:
#     print("Non-match")


#Prime number check

# num= int(input("Enter the no.:"))
# ch = 0

# if num<= 1:
#     print("Not prime Number")
# else:
#     for i in range(2,int(num**0.5)+1): #root square
#         if num % i == 0:
#             print("Not Prime number")
#             break
#         else:
#             print("Prime number")


#palindrome

num= int(input("enter the no.:"))

if num <0 :
	print("Not palindrome")
else:
	orginal= num
	digit= 0
	rev=0
	while num >0:
		digit= num%10
		rev= rev * 10+ digit
		num =num//10

if orginal == rev:
	print("Palindrome no")
else:
	print("Not palindrome")	