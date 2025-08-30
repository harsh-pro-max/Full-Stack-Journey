# 1. Write a Python script to print first N even natural numbers.
N=int(input("input last Even no:"))
if N%2!=0:
    N=N-1
r1=range(2,N+1,2)
for e in r1:
    print(e,end=' ')

# 2. Write a Python script to print first N odd natural numbers.
N=int(input("input last Odd no:"))
if N%2==0:
    N=N-1
r2=range(1,N+1,2)
for e in r2:
    print(e,end=' ')

# 3. Write a Python script to print squares of first N natural numbers.
sqr=int(input("input last N no:"))
r3=range(1,sqr+1)
for e in r3:
    print(e**2,end=' ')
# 4. Write a Python script to print cubes of first N natural numbers.
cube=int(input("input last N no:"))
r4=range(1,cube+1)
for e in r4:
    print(e**3,end=' ')
print()
# 5. Write a Python script to display all prime numbers within a range.
#    (Range start = 15, end = 45)
r5=range(15,45+1,1)
for e in r5:
    flag=True
    for i in range(2,e,1):
        if(e%i==0):
            flag=False
    if(flag==True):
            print(e,end=' ')
