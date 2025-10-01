# Implement String Libraries

import string
s = input("Enter a string: ")
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Title Case:", s.title())
print("Digits:", any(c.isdigit() for c in s))
