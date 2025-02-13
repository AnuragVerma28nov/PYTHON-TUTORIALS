# Sum of n Natural Numbers
n = int(input("Enter a number: "))
sum = n * (n + 1) // 2
print("The sum of", n, "natural numbers is:", sum)
num = int(input("Enter a number: "))
sum = 0
while num:
    sum += num % 10
    num //= 10
print("The sum of the digits is:", sum)