# armstrong number
num=int(input("Enter a number: "))
sum=0
n=num
while n>0:
    d=n%10
    sum+=d**len(str(num))
    n//=10
if sum==num:
    print("armstrong number")
else:
    print("not armstrong number")