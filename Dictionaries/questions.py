students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 60},
    {"name": "C", "marks": 40}
]

# A → 80
# B → 60

for i in students[:2]:
    print(f"{i["name"]}→ {i["marks"]}")