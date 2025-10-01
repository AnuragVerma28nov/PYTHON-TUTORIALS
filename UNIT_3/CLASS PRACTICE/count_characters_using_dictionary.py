# Count Characters using Dictionary

s = input("Enter a string: ")
char_counts = {}
for char in s:
    char_counts[char] = char_counts.get(char, 0) + 1
for key, value in sorted(char_counts.items()):
    print(f"{key}: {value}")