# all three functions:

f = open("example.txt", "w+")
f.write("Hello, World!")
f.flush()
print(f.tell())  # prints 13
f.seek(7)
print(f.read())  # prints "World!"
f.close()