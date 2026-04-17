
# num = [0,1,2,3,4,5]

# num.append(6)
# num.remove(0)

# # print(num)

# for i in num:
#     print(i)

# num= [1,2,1,2,3,4,5]

# real= []

# for i in num:
#     if i not in real:
#         real.append(i)
    
# print(real)

#reverse a list

# num= [1,2,3,4,5]
# rev=[]

# for i in range(len(num)-1, -1, -1):
#     rev.append(num[i])

# print(rev)


# cars= {
#     'name': 'BYD',
#     'range': '500',
#     'TopSpeed': '200'
# }

# cars["color"]= "black"
# cars["range"]= "1000"

# print(cars["name"])

# #loop in key

# for key in cars:
#     print(key)

#loop in value

# for value in cars.values():
#     print(value)

#loop in key+value

# for key,value in cars.items():
#     print(key,value)


#list of dictionaries

cars= [{'name': 'BYD','range': '500','TopSpeed': '200'},
       {'name': 'Tesla','range': '1000','TopSpeed': '150'},
       {'name': 'KIA','range': '600','TopSpeed': '120'}
       ]

#kia topspeed

for i in cars:
    if i["name"] == "KIA":
        print(i["TopSpeed"])
   
