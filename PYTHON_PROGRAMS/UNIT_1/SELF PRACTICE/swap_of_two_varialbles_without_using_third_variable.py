#swap of two varialbles without using third variable

x=int(input ("enter a number:"))
y=int(input("enter a number:"))
print("valuve of x=",x)
print("valuve of y=",y)
x=x+y
y=x-y
x=x-y
print("valuve of x after sawpping =",x)
print("valuve of y after sawpping =",y)