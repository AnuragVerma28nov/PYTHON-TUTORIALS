'''pattern_2
*****
****
***
**
*---'''
row=int(input("Enter the no of rows: "))
for i in range (row,0,-1):
    for j in range ( 0,i): 
        print("*",end=" ")
    print("\n")