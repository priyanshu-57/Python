
# print("hello")

# a= 4.5
# print(type(a))


# for i in range(0,6):
    
#     for j in range(0,i+1):
#         print("*",end="")
#     print()

# a= int(input("Enter the no:"))
# b= int(input("Enter 2nd no:"))

# def add(x,y):
#     total= x+y
#     print("Total",total)

# add(a,b)

# num= [1,2,3]
# num.append(4)
# num.remove(1)

# for i in num:
#     print(i)

#pprime no. check

# num= int(input("Enter the no.:"))

# if num <=1:
#     print("Not prime no.")
# else:
#     for i in range(2,int(num**0.5)+1):
#         if num% i ==0:
#             print("Not prime no.")
#             break
#     else:
#         print("Prime no.")

# student= {
#     "Name":"A",
#     "Id": "6679",
#     "mark": "75"
# }

# print(student["Name"])

#list of dictionaries

student= [
    {"name":"A", 'mark':"45"},
    {"name":"B", "mark":"65"}

]

print(student)

with open("new.txt","w") as f:
    f.write("Back again\n now never discontinue")