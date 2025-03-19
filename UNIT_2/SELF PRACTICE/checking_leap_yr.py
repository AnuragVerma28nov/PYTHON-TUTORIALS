# checking a leap year

lp=int(input("Enter a year: "))
if lp%400 == 0:
    print(lp,"is a leap year")
elif lp%100 == 0:
    print(lp,"is not leap year")
elif lp%4==0:
    print( lp,"is leap year")
else:
    print(lp,"is not leap year")