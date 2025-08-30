# write a program to calculate sum of first n multiples of x.
n=int(input("how much multiple to add:"))
x=int(input("which values you multiply:"))
r1=range(x,n*x+1,x)
sum=0
for e in r1:
    sum+=e
print("%d %d of sum=%d"%(n,x,sum))

# write a program to print first n natural numbrs. [use range and for]
n=int(input("input n:"))
r2=range(1,n+1,1)
for e in r2:
    print(e,end=' ')

# write a program to print squres of firt n natural numbers
for e in r2:
    print(e**2,end=' ')

# write a program to print first n even natural numbers in reverse order.
n=int(input("input last n even "))
for e in range(n,1,-2):
    print(e,end=' ')

# write a program to print first N natural numbers.[use range and for]
N=int(input("How many number you to print:"))
r1=range(1,N+1,1)
for i in r1:
    print(i,end=' ')
# second methord
for e in range(1,int(input("enter a number:"))+1):
    print(e,end=' ')

#Write a program to print squres of first N natural numbers.
for e in range(1,int(input("enter a number:"))+1):
    print(e**2,end=' ')

# write a program to print first n even natural numbers in reverse order.
for e in range(int(input("enter a number")),0,-1):
    print(e,end=' ')

# Write a program to calcualte sum of first n multiple of x.
x=int(input("which value you to print multiple:"))
n=int(input("how much number you to print:"))
r1=range(x,n*x+1,x)
for e in r1:
    print(e,end=' ')
