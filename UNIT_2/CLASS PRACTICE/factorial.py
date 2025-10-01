#factorial of a number 
n= int(input("Enter a number: "))
fact = 1
if n>=0:
 for i in range(1, n + 1):
    fact *= i
 print("The factorial of", n, "is:", fact)
else:
    print("You have entered negative number")    