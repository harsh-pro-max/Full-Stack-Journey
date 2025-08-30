def f1():
    a=int(input("Enter a numbe:"))
    b=a**2
    print("Square of",a,"is",b)

f1() 
# write a function to calculate average f two numbers.

def f2(a,b):
    avg=(a+b)/2
    print(avg)

f2(4,5)

def f3(*t):
    avg=sum(t)/len(t)
    return avg

print(f3(4,4,2,12))
