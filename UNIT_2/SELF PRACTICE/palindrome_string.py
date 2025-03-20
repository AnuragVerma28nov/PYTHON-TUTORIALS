# palindrome string

str=input("Enter string: ")
if (str==str[::-1]):
    print("Palindrome string")
else:
    print("Not palindrome string")