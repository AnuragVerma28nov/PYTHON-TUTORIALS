# Display Unique Vowels

s = input("Enter a string: ")
vowels = set(c for c in s.lower() if c in 'aeiou')
print(vowels)