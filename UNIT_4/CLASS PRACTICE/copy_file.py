# Copy contents of one file to another
with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    dest.write(src.read())
