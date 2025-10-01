# Reverse a Number and Checking Palindrome
num = int(input("Enter a number: "))
rev = 0
while num:
    rev = rev * 10 + num % 10 # or use digit = num % 10 and then rev = rev * 10 + digit
    num //= 10
print("The reverse of the number is:", rev)
if rev == num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")