
# num= [121,123,124,125]

# num.append(122)
# # num.remove(121)

# for i in num[:2]:
#     print (i)

#remove duplicate from list

# num=[1,2,2,3,4,4,5]

# new=[]

# for i in num:
#     if i not in new:
#         new.append(i)

# print(new)        

# #reverse the list

# rev=[]

# for j in range(len(new)-1,-1,-1):
#     rev.append(new[j])

# print(rev)

# students={
#     'name':'Ram',
#     'age': '26',
#     'grade': '9'

# }

# # print(students)
# students['mark']='90' #add
# students['grade']= '10' #update
# # print(students)

# # for key in students:
# #     print(key)

# # for value in students.values():
# #     print(value)

# for key,value in students.items():
#     print(key,value)

#List of Dictionaries

students=[
    {'name':'A', 'mark ': '50'},
    {'name':'B', 'mark ': '70'},
    {'name':'C', 'mark ': '90'},
    
]
# A → 80
# B → 60

for i in students[:2]:
    print(f"{i['name']}→ {i['mark ']}")

#create and write into file

with open("data.txt",'w') as f:
    # for k in students:
    #     f.write(f"{k}\n")
    f.write(f"{students}")
