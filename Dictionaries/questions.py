
students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 60},
    {"name": "C", "marks": 40}
]
# #print
# #A → 80
# #B → 60

# # for i in range(0,2):
# #     print(students[i]["name"],"→",students[i]["marks"])

# for i in students[:2]:
#     print(i["name"],"→",i["marks"])

#count how many student passed(>=50)
ch=0
for i in students:
    if i["marks"] >= 50:
        ch +=1

print("Total pass count:",ch)
