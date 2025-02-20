# Create a file, write name and father’s name, then read and print it
with open("info.txt", "w") as f:
    f.write("Name: John\nFather's Name: Smith")
with open("info.txt", "r") as f:
    print(f.read())
