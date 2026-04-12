
#write

# with open("intro.txt","w") as f:
#     f.write("Name: Priyanshu Kushawaha \n")
#     f.write("Age: 24")

#read

# with open("intro.txt","r") as f:
#     content= f.read()
#     print(content)

#read line by line

with open("intro.txt","r") as f:
    for line in f:
        print(line.strip())