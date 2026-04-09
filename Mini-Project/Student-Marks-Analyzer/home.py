# Enter all the students mark , calculate avg, highest, lowest and pass count(>=50)

mark= [] # to store the marks

n= int(input("Enter the no. of students:"))

for i in range(n):
    m= int(input("Enter the marks:"))
    mark.append(m)

#average funtion
    
def average(mark):
    total=0
    for j in mark:
        total += j
    return total/len(mark)
    

#highest mark

def highest(mark):
    high=mark[0]
    for k in mark:
        if k > high:
            high=k
    return high

#lowest mark
def lowest(mark):
    low=mark[0]
    for l in mark:
        if l < low:
            low= l
    return low

#pass count(>=50)

def passcount(mark):
    ch=0
    for m in mark:
        if m>=50:
            ch += 1
    return ch

#grade system (A,B,C, fail)

def grade(mark):
    A=B= C= F=0
    for p in mark:
        if p>=80  :
            A +=1
        elif  p>=60:
            B +=1
        elif  p>=50:
            C +=1
        else:
            F +=1

    return A,B, C, F

A,B,C,F= grade(mark) #return value stored
print("Average:",average(mark))
print("Highest:",highest(mark))
print("Lowest: ",lowest(mark))
print("Passed students: ",passcount(mark))
print(f"A:{A}, B: {B}, C:{C} , Fail:{F}")




