
# student= {
#     'name': 'A',
#     'mark': '56',
#     'id': '101'
# }

# #add
# student['Grade']= 'C'

# student['mark']= 95
# # print(student)

# #list of dictionaries

# students= [
#     {'name':'A', 'mark': '75'},
#     {'name': 'B', 'mark':'56'},
#     {'name':'C', 'mark':'85'}
# ]
# #a=75, b=56

# for i in students[:2]:
#     print(f"{i['name']}= {i['mark']}")

#write file

# with open("revise.txt","w") as f:
#     f.write("My name is Priyanshu")

#read
# with open("revise.txt","r") as f:
#     content= f.read()
#     print(content)

# #read line
# with open("revise.txt","r") as f:
#     for line in f:
#         print(line.strip())

#numpy

# import numpy as np

# arr=np.array([1,2,3,4,5])

# print(arr)
# print(arr.mean())
# print(arr.max())
# print(arr.min())

#pandas
import pandas as pd

student={
    "name": ["A","B"],
    "marks" : [45, 95]
}

df= pd.DataFrame(student)
# print(df)

# print(df.head())
# print(df.describe())
# print(df.columns)

# print(df[df['marks']>60])

df["result"]= df["marks"]>50

print(df)
print(df["result"].sum())