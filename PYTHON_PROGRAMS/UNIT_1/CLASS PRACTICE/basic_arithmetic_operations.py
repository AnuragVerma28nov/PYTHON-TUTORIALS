# Basic Arithmetic Operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    print("Error: Division by zero")
    division = "Not applicable"
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

