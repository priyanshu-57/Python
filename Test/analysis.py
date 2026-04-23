
student= {
    'name': 'A',
    'mark': '56',
    'id': '101'
}

#add
student['Grade']= 'C'

student['mark']= 95
# print(student)

#list of dictionaries

students= [
    {'name':'A', 'mark': '75'},
    {'name': 'B', 'mark':'56'},
    {'name':'C', 'mark':'85'}
]
#a=75, b=56

for i in students[:2]:
    print(f"{i['name']}= {i['mark']}")