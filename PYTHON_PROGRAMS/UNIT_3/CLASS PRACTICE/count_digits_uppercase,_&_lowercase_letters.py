# Count Digits, Uppercase, and Lowercase Letters

s = input("Enter a string: ")
digits = sum(1 for char in s if char.isdigit())
uppercase = sum(1 for char in s if char.isupper())
lowercase = sum(1 for char in s if char.islower())
print(f"Digits: {digits}, Uppercase: {uppercase}, Lowercase: {lowercase}")