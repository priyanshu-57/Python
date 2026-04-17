
import pandas as pd

df= pd.read_csv("students.csv") #read csv files
df.columns= df.columns.str.strip()

print(df)

#analysis

print("Average:",df["marks"].mean())

# print(df.columns)

print("Highest:", df["marks"].max())

print("Lowest:",df["marks"].min())


df["result"]= df["marks"]>=50


print("Passcount:",df["result"].sum() )

#grade function

def grade(m):
    if m >=80:
        return "A"
    elif m>=60:
        return "B"
    elif m>=50:
        return "C"
    else:
        return "Fail"

df["Grade"]= df["marks"].apply(grade) #apply function

# print(df)
print(df["Grade"].value_counts())

#sort by marks
df= df.sort_values(by="marks",ascending=False)
print(df)

df.to_csv("output.csv", index=False)

#summary

summary= {"Average": df["marks"].mean(),
    "Highest": df["marks"].max(),
    "Lowest": df["marks"].min(),
    "Passcount": df["result"].sum()}


summary_df= pd.DataFrame([summary])
summary_df.to_csv("summary.csv",index=False)