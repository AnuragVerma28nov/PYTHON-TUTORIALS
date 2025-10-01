# Create a file, write name and father’s name, then read and print it
with open("file.txt", "w") as f:
    f.write("Name: John\nFather's Name: Smith")
with open("file.txt", "r") as f:
    print(f.read())
