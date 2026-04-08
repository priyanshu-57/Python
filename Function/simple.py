"""
# function to greet

def greet(name):
    print("Hi",name)

greet("Munna")
greet("Roushan")
greet("Taweshal")
"""


# #Function to add

# def add(a,b):
#     sum= a+b
#     print("Sum=",sum)

# add(2,4)
# add(4,7)

# Add function with return value

# def add(a,b):
#     return a+b

# result= add(4,3)
# print(result)

# print("sum is:",add(23,45))


#check even/ odd function

# def check(num):
#     if num % 2== 0:
#         print("even")
#     else:
#         print("odd")
    

# check(20)
# check(99)

#Find largest number among 3 using function

def larg(a,b,c):
    if a> b and a > c:
       return a
    elif b>a and b > c:
        return b
    elif c> a and c> b:
        return c
    else:
        print("All no. are equal")


print(larg(2,3,7))
print(larg(2,2,2))