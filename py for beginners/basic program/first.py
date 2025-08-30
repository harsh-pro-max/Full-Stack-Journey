# def add(a,b):
#     return a+b

# x=add
# print(x)
# print(add)
# print(x(3,4))

s=lambda a:1 if a==0 else a*s(a-1)

print(s(7))