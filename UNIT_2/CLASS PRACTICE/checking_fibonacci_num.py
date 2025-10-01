#checking Fibonacci Number without using function
num = int(input("Enter a number: "))
a = 0
b = 1
while b < num:
    temp = a + b
    a = b
    b = temp
if b == num:
    print(num, "is a Fibonacci number.")
else:
    print(num, "is not a Fibonacci number.")


