# vowel count in a string

str = input("Enetr a string(lower case): ")
v_c = 0
for char in str:
    if char.lower() in "aeiou":
        v_c += 1
print("No. of vowels in",str,":",v_c)