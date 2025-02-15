# palindrome number
n=int(input("Enter number: "))
num=n
rev=0
while n>0:
    d=n%10
    rev= rev*10+d
    n=n//10
print("rverse:",rev)
if rev==num:
    print("palindrome number")
else:
    print("not palindrome number")