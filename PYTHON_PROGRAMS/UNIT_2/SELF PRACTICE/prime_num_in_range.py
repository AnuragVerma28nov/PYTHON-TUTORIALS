# prime number in range

start=int(input("Enter starting range: "))
end=int(input("Enter end range: "))
print("Prime numbers b/w",start,"&",end,"(ranges are included):")
for num in range( start,end+1):
    if num>1:
        for i in range (2,num):
             if num%i==0:
              break
        else:
            print(num,end=" ")    
            
        
       
        
        