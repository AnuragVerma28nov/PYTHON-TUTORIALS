# checking a leap year

lp=int(input("Enter a year: "))
if lp % 400 == 0:
    print("leap year")
elif lp%100 == 0:
    print("not leap year")
elif lp % 4==0:
    print("leap year")
else:
    print("not leap year")