# largest of three num simple

a=int(input("Enter a num: "))
b=int(input("Enter a num: "))
c=int(input("Enter a num: "))
if a>b and a>c:
    print(a,"is largest number")
elif b>a and b>c:
    print(b,"is largest number")
elif c>b and c>a:
    print(c,"is largest number")
else:
    print("All three are same")