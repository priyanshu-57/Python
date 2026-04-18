
# num=[]

# with open("test.txt", "r") as f:
#     content= f.read()
#     print(content)

# with open("test.txt","r") as f:
#     for line in f:
#         print(line.strip())

# num=[]

# with open("test.txt", "r") as f:
#     for line in f:
#         num.append(int(line.strip()))

# print(num)

# import numpy as np

# x= np.array(num)

# print("Average: ",x.mean())
# print("Lowest:",x.min())
# print("Highest:",x.max())
# print(x+ 10)

students={
    "name":["a","b","c"],
    "marks":[40,50,70]

}
import pandas as pd

df= pd.DataFrame(students)

# print(df)
# print(df.head())
# print(df.describe())

# print(df.columns)

# print(df["name"])

print(df[df["marks"]>=50])

