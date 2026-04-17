
import pandas as pd

data= {
    "name": ["A", "B", "C"],
    "marks": [ 80,60,40]
}

df= pd.DataFrame(data)
# print (df)

# print(df.head())  

# print(df.describe())

# #column access

# print(df["marks"])

# #filtering
# print(df[df["marks"]>=50])

#Add new column
df["result"]= df["marks"] >=50
print(df)

#pass counts
print(df["result"].sum())
