# Read a file character by character and print each character
with open("file.txt", "r") as f:
    while True:
        char = f.read(1)
        if not char:
            break
        print(char, end=" ")
