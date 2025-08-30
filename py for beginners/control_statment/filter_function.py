def f(x):
    if x%2==0:
        return x
t=(2,4,6,3,5,8)
y=filter(f,t)
print(y)
for e in y:
    print(e)
 