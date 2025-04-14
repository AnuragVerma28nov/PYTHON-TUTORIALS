# Modify pointer position using seek()
with open("file.txt", "r") as f:
    f.seek(5)
    print(f.read())
