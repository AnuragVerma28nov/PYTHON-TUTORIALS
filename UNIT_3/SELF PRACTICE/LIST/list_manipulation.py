# append()
l1= [1,2,3,"anurag"]
print("original list: ",l1)
l1.append("verma")
print("after appending: ",l1)

# max() & min() 
l2 = [1,2,3,4,5]
print("given list: ",l2)
print("the maximum number of ablove list: ",max(l2))
print("the minimum number of ablove list: ",min(l2))

# reverse()
l3 = [1,2,3,"anu","musu","susu"]
print("original list: ",l3)
l3.reverse()
print("revsersed list: ",l3)

# remove()
l4 = [1,2,3,4,"anu","musu","susu"]
print("original list: ",l4)
l4.remove("musu")
print("after moving: ",l4)

# sort()
l5 = [1,6,5,4,2,3]
print("original list: ",l5)
l5.sort() #ascending order 
print("ascending order: ",l5)
l5.sort(reverse=True) #descending order
print("descending order; ",l5)