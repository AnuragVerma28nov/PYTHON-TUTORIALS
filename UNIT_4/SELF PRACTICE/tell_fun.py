# tell() function

f = open("example.txt", "r+")
print(f.tell())  # prints 0
f.seek(10)
print(f.tell())  # prints 10
f.close()