'''pattern_1
*
**
***
****----'''
rows=int(input("Enter the no of rows: "))
for i in range(rows):
    for j in range (i+1):
     print("*",end=" ")
    print("\n")