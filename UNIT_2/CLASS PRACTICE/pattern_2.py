'''pattern
   *
  ***
 *****
******* '''
r = 4
for i in range(r):
        sp = " " * (r - i - 1)
        st = "*" * (2 * i + 1)
        print(sp + st)

