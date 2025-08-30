from functools import reduce
def sum(a,b):
    return a+b
x=reduce(lambda a,b:a+b,[1,2,3,4,5])
y=reduce(sum,[1,2,3,4])
print(x)
print(y)