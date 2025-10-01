# Write numbers to ODD.TXT and EVEN.TXT based on their parity
with open("Input.txt", "r") as f:
    numbers = f.readlines()
with open("ODD.TXT", "w") as odd, open("EVEN.TXT", "w") as even:
    for num in numbers:
        if int(num.strip()) % 2 == 0:
            even.write(num)
        else:
            odd.write(num)
