# Fibonnic series
n_term=int(input("Eneter number of terms: "))
n_1=0
n_2=1
if n_term<=0:
    print("please enter a postive number: ")
elif n_term==1:
    print("fibonnic series: ",n_1)  
else:
    print("fibonnic series: ", end=" ")
    print(n_1,n_2,end="")
    for i in range( 3,n_term+1):
        n_th=n_1+n_2
        print(" ",n_th,end=" ")
        n_1=n_2
        n_2=n_th
