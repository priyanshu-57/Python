#lists
# num= [10,20,30,40]
# print(num)

#basic operation

# num = [10,20,30,50]

# num.append(40)
# num.remove(50)

# print(num)

#loop in list

# num= [2,4,6,8]

# for n in num:
#     print(n)



#sum of list

# num= [1,2,3,4,5]
# total=0
# for n in  num:
#     total += n

# print("Sum:",total)


#find max in list

# num= [23,45,63,15,35]
# x= num[0]

# for n in num:
#     if n>x :
#         x= n
# print("max in list",x)


# Task 9: Count even numbers in list

num= [2,3,4,5,6]
ch= 0
for n in num:
    if n % 2 ==0:
        ch += 1
print("total counts",ch)
