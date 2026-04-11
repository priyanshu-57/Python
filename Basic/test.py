
#prime no .check

# num= int(input("Enter the no.:"))

# if num<= 1:
#     print("Not Prime Number")
# else:
#     for i in range(2, int(num**0.5) +1):
#         if num % i == 0:
#             print("Not prime no.")
#             break
#     else:
#         print("Prime number")


#palindrome no.

num= int(input("Enter the no. :"))
rev=0
original= num
while num > 0:
    digit= num % 10
    rev = rev *10 + digit
    num= num//10

if original==rev:
    print("Palindrome")
else:
    print("not palindrome")
