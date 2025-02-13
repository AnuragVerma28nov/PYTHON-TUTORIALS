##Checking Fibonacci Number using function
def fib(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n
num = int(input("Enter a number: "))

if fib(num):
    print(num, "is a Fibonacci number.")
else:
    print(num, "is not a Fibonacci number.")

   
