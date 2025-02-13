'''pattern 
*
**
***
*****
****
***
**
*                  
''' 
p = [1, 2, 3, 5, 4, 3, 2, 1]
for i in p:
    print("*" * i)
    print("\n")
'''*
**
***
****
*****
****
***
**
*'''
n = 5  
for i in range(1, n + 1):
    print("*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i)
