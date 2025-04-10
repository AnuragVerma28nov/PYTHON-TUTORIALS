# reverse of number
n=int(input("Enter a num: "))
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n//=10
print("Reverse no: ",rev)