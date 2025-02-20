# Remove newline characters from a file
with open("file.txt", "r") as f:
    content = f.readlines()
content = [line.strip() for line in content]
print(content)
