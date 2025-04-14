# Capitalize Lines

lines = []
while True:
  line = input("Enter a line (or 'q' to quit): ")
  if line.lower() == 'q':
    break
lines.append(line.upper())
