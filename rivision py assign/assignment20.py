#                       Assignment-20:for loop and range 

# 1. Write a python script to print the first 10 multiple of 5.
r1=range(5,10*5+1,5)
for e in r1:
    print(e,end=' ')

# 2. Write a python script to print first 10 multiple of N.
# use different method
N=int(input("which number you to print multiple:"))
for e in range(1,10+1):
    print(e*N,end=' ')

# 3. Write a python script to print first M mulitiples of N.
N=int(input("which number you to print multiple"))
M=int(input("how much multiple you to print multiple:"))
for e in range(1,M+1):
    print(e*N,end=' ')

# 4. Write a python script to print the first 10 multiples of N in reverse order.
N=int(input("which number you to print multiple"))
M=int(input("how much multiple you to print:"))
for e in range(M,0,-1):
    print(e*N,end=' ')

# 5. Write a python script to print table of user's choice.
t=int(input("which number you to print table:"))
for e in range(1,11,1):
    print(e*t,end=' ')

