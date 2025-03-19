# implicit data_type_conversion
a=10
b=20.50
c=a+b
print(c,type(c))

# explicit data_type_conversion
a="2025"
print(a,type(a))
print(a,type(int(a)))
b="10010"
print(b,type(b))
print(b,type(bool(b)))
print(b,int(b,2))
d=19.99
print(d,int(d))
print(d,str(d))
e=25
f=45
print(e,f,type(complex(e,f)))
g=complex(e,f)
print("complex form of",e, "&" ,f,g)
