
marks=[]
with open("marks.txt","r") as f:
    for line in f:
        marks.append(int(line.strip()))

print(marks)

#average funtion
def avg(marks):
    total=0
    for i in marks:
        total += i
    return total/len(marks)

#highest

def high(marks):
    h=marks[0]
    for i in marks:
        if i>h :
            h=i
    return h

#lowest

def lowest(marks):
    low=marks[0]
    for i in marks:
        if i < low:
            low=i
    return low

#pass count

def passcount(marks):
    ch = 0 
    for i in marks:
        if i >= 50:
            ch +=1
    return ch

# print(avg(marks))
# print(high(marks))
# print(lowest(marks))
# print(passcount(marks))                

students=[]
names=["A","B","C", "D","E"]

for i in range(len(marks)):
    students.append({'names':names[i],'marks': marks[i]})
    
# print(students)

#add grades
def grade(marks):
    if marks>80:
        return "A"
    elif marks >60:
        return "B"
    elif marks >50:
        return "c"
    else:
        return "F"
    
for j in students:
    j["grade"]= grade(j["marks"])


print(students)

#who scored highest

for k in students:
    if k["marks"]== high(marks):
        print(f"{k['names']} got the highest")


#write to file

with open("result.txt","w") as f:
    
    #write student data

    for s in students:
        f.write(f"{s["names"]}-{s["marks"]}-{s["grade"]}\n")

        f.write("\n")

        #write summary
    f.write(f"Average mark: {avg(marks)}\n")
    f.write(f"Highest mark:{high(marks)}\n")
    f.write(f"Lowest mark:{lowest(marks)}\n")
    f.write(f"No. of Pass students:{passcount(marks)}\n")

# highest scorer name
    for k in students:
        if k["marks"] == high(marks):
            f.write(f"Topper: {k['names']}\n")

    