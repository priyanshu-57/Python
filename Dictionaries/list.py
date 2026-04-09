
student= [
{"name": "A", "mark" :"80"  },
{"name": "B", "mark":"70" },
{"name":"C", "mark":"60"},
]

# for i in student:
#     print(i)

for i in student:
    if i['name'] != "C":
        print(f"{i['name']} → {i['mark']}")