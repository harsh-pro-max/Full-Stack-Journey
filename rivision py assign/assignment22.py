#                   Assignment-22: Loops date:05/08/2025

# 1. Write a Python script to calculate sum of first n natural numbers.
N=int(input("Enter a natural number to calcluate between sum:"))
sum=0
for e in range(1,N+1):
    sum=sum+e
print("Sum of %d natural number is %d"%(N,sum))

# 2. Write a Python script to calculate sum of squares of fist N natural numbers.
N=int(input("Enter a natural number to calculalte squares from 1 to N:"))
sqr_sum=1
for e in range(1,N+1):
    sqr_sum+=e**2
print("squre sum from 1 to %d natural number is %d"%(N,sqr_sum))

# 3. Write a Python script to calculate sum of cubes of first N natural numbers.
N=int(input("Enter a natural number to calculalte cubes from 1 to N:"))
cube_sum=1
for e in range(1,N+1):
    cube_sum+=e**3
print("cube sum from 1 to  %d natural number is %d"%(N,cube_sum))

# 4. Write a Python script to calculate sum of first N odd natural numbers.
N=int(input("Enter a natural number to calcualte sum of first N odd numbers:"))
oddSum=0
for e in range(1,N+1):
    oddSum+=e*2-1
print("sum of  %d odd number is: "%(N),oddSum)

# 5. Write a Python script to calculate sum of first N even natural numbers.
N=int(input("Enter a natural number to calucate sum of first N even numbers"))
evenSum=0
for e in range(1,N+1):
    evenSum+=e*2
print("sum of %d even number is:"%(N),evenSum)

