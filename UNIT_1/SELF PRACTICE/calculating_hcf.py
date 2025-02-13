num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
a, b = num1, num2
while b:
a, b = b, a % b
hcf = a
print("The HCF of", num1, "and", num2, "is:", hcf)