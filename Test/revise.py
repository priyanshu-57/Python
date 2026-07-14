
# # print("Hi, I am back")
# # a= 10
# # print(a)

# age= 24
# name= "Priyanshu"

# print(f"{name} is {age} years old")

# # height= int(input("Enter the height: "))

# # print(f"His height is {height}")

# mark= int(input("Enter your mark: "))

# if mark>40:
#     print("Pass")
# else:
#     print("Fail")
# num=1
# for i in range(1,10,1):
#     num= num+2
#     print(num)

# num=0
# while num<50:
#     num= num+10
#     print(num)

# num= int(input("Enter your number:"))
# def result(num):
#     if num>40:
#         print("Pass")
#     else:
#         print("Fail")

# result(num)

# num=[1,2,3,4,6]

# print(num)

# num.append(5)
# num.remove(6)
# print(num)
# sum=0
# max=num[0]
# for n in num:
#     # print(n)
# #     sum=sum+n

# # print(sum)
#     if n> max:
#         max= n

# print("Max:",max)

#count even number in list

# n= [1,3,5,4,8,10]
# ch=0
# for i in n:
#     if i% 2== 0:
#         ch +=1

# print("total even numbers", ch)

#Remove the dulpicant from list

num= [2,2,3,4,5]

new= []

for i in num:
    if i not in new:
        new.append(i)

print(new)