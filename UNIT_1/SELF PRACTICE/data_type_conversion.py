# implicit data_type_conversion
a=10
b=20.50
c=a+b
print(c,type(c))

# explicit data_type_conversion
a="2025"
print(type(a)); print(type(int(a)))
b="10010"
print(type(b)); print(type(bool(b)))
print(int(b,2))
d=19.99
print(int(d))
