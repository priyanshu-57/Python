
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

# cars= [{'name': 'BYD','range': '500','TopSpeed': '200'},
#        {'name': 'Tesla','range': '1000','TopSpeed': '150'},
#        {'name': 'KIA','range': '600','TopSpeed': '120'}
#        ]

#kia topspeed

# for i in cars:
#     if i["name"] == "KIA":
#         print(i["TopSpeed"])
   

#file handling

# with open("revise.txt","w") as f:

#     for i in cars:
#         #available models
#         f.write(f"Avaiable models: {i['name']} \n")

#read file

# with open("revise.txt","r") as f:
#     data= f.read()
#     print(data)

#read line by line

# with open("revise.txt", "r") as f:
#     for line in f:
#         print(line.strip())

#numpy

#array
# import numpy as np

# arr= np.array([1,2,3,4,5]) #convert normal List to numpy array

# print(arr)

# #basic operation

# print(arr.mean())
# print(arr.max())
# print(arr.min())

# #arithmetic operation

# print(arr + 10)

# print(arr * 10)

# import numpy as np

# prime= np.array([2,3,5,7])

# print(prime)

# print(prime.mean())

# print(prime.max())

# print(prime.min())

# print(prime * 10)

import pandas as pd

data= {
    "name": ["A","B","C"],
    "marks": [80,60,40]}

x= pd.DataFrame(data)

# print(x)

# print(x.head())
# print(x.describe())

#column access

# print(x["name"])

#filtering
# print(x[x["marks"]>=50])

# #add new column
# x['result']= x["marks"]>=50

# print(x)

# print(x["result"].value_counts())

# import numpy as np

# x= np.array([1,2,3,4,5])

# print(x)

# print(x.mean())
# print(x.max())
# print(x.min())

# print(x+10)

import pandas as pd

data= {
    "name": ["A", "B", "c"],
    "mark": [50,40,90]

}

x= pd.DataFrame(data)

# print(x)

# print(x.head())
# print(x.describe())

# print(x["name"])

# print(x[x["mark"]>=50])

x["result"]= x["mark"]>=50

print(x["result"].value_counts())
