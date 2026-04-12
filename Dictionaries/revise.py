
# price=[600,700,1000,1500,2000,2500]

# # print(price)

# price.append(1750)
# price.remove(700)

# # print(price)

# for i in price:
#     print(i)

#Dictionaries

# d= {"name":"Ram","age":"20","Height":"2 feet"}

# d["name"]= "Priyanshu "
# d["id"]= 40

# print(d)

#list of dictionaries
# mark= [
#     {'name ': 'A','mark':'40'},
#     {'name':'B','mark':'50'},
#     {'name':'C','mark':'45'}
# ]

# detail={'name':'A','id':'2', }
# print(detail["name"])

# detail["name"]= "Ram" #update
# detail["mark"]= 25

# print(detail["name"])
# print(detail["mark"])

#loop in Dictionaries

# house= {
#     'room':'4',
#     'hall':'1',
#     'kitchen':'2'
# }
#loop in key
# for key in house:
#     print(key)

#loop in values

# for value in house.values():
#     print(value)

#loop through key+values

# for key,value in house.items():
#     print(key,":",value)

students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 60},
    {"name": "C", "marks": 40}
]
#print
#A → 80
#B → 60

for i in range(0,2):
    print(students[i]["name"],"→",students[i]["marks"])