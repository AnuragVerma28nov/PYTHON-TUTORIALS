# Checking Armstrong Number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp:
    digit = temp % 10
    sum += digit ** len(str(num))
    temp //= 10
if sum == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")