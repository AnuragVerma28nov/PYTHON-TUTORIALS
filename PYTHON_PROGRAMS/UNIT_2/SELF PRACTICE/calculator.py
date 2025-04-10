# calculator

a=float(input("Enter a number_1: "))
b=float(input("Enter a number_2: "))
c= input("Enter a operation(,-,*,/,//,%,**): ")
if c=="+":
    print("addtion: ",a+b)
elif c=="-":
    print("subtraction: ",a-b)
elif c=="*":
    print("multiplication: ",a*b)
elif c=="**":
    print("Exponent: ",a**b )
elif b!=0:
    if c=="/":
      print("division: ",a/b)
    elif c=="//":
      print("floor division: ",a//b)
    elif c=="%":
      print("modolous: ",a%b)
elif b==0:
    print("number_2 = 0 Division not posssible!")
else:
    print("Error! Wrong input.")