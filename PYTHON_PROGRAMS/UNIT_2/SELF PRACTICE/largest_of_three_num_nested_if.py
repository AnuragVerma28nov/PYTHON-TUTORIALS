# largest of three num nested if elif

a=int(input("Enter a num: "))
b=int(input("Enter a num: "))
c=int(input("Enter a num: "))
if a>b:
    if a>c:
        print(a,"is largest number")
    else:
        print(c,"is largest number")
elif b>a:
    if b>c:
        print(b,"is largest number")
    else:
        print(c,"is largest number")
else:
    print("All three are same")