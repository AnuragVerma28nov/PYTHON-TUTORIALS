# searchmany(s, x, k)

def smany(s, x, k):
    return s.count(x) <= k

print(smany([10, 17, 15, 12], 15, 1)) 
print(smany([10, 12, 12, 12], 12, 2))  
print(smany([10, 12, 15, 11], 17, 18)) 
