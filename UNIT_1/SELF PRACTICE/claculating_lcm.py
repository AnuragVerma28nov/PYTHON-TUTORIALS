# Calculate the LCM
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
a, b = num1, num2
while b:
    a, b = b, a % b
    lcm = (num1 * num2) // a
print("The LCM of", num1, "and", num2, "is:",lcm)