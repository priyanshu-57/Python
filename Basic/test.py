
#palindrome no.

num= int(input("Enter the no.:"))
rev=0
orginal=num
while num > 0:
    digit= num % 10
    rev= rev*10 + digit
    num= num//10

if orginal== rev:
    print("Palindrome no.")
else:
    print("Not palindrome no.")
