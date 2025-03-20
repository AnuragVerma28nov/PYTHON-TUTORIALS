# Count Letter Occurrences

s = input("Enter a string: ")
letter_counts = {}
for letter in s:
    if letter.isalpha():
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
print(letter_counts)