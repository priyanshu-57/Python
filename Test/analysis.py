
#create CSV file

# with open("table.csv", "w") as f:
#     f.write("Name, marks\n A,40\n B,65\n C,90")

import pandas as pd

df= pd.read_csv("table.csv")
df.columns=df.columns.str.strip()

# print(df)


def result(mark):
    if mark >=50:
        return "pass"
    else:
        return "fail"

df["Result"]= df["marks"].apply(result)



print("Average:",df["marks"].mean())
print("Highest:",df["marks"].max())

print(df)
print(df["Result"].value_counts())