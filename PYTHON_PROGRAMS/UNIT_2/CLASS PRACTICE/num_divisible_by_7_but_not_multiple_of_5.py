# Numbers Divisible by 7 but Not Multiple of 5
def dis_num(st, en):
    for num in range(st, en + 1):
        if num % 7 == 0 and num % 5 != 0:
            print(num)

st = 1000
en = 2000
dis_num(st, en)