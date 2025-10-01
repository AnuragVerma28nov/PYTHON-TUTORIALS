''' Pattern
1
010
10101
0101010'''

n = 5 
for i in range(n):
    if i % 2 == 0:
        print("1" + "01" * i)
    else:
        print("0" + "10" * i)


