# Python Assignments: Full Stack Development

# 1. Write a Python script to reverse a number.
# N=int(input("enter a number:"))
# rev=0
# while N:
#     mod=N%10
#     rev=rev*10+mod
#     N=N//10
# print("reverse of no:",rev)

# 2. Write a Python script to check whether a given number is Prime or not.
# N=int(input("enter a number:"))
# r1=range(2,N)
# flag=True
# for e in r1:
#     if N%e==0:
#         flag=False
# if flag==True:
#     print("prime number")
# else:
#     print("not prime")
# 3. Write a Python script to print all Prime numbers under 100.
N=int(input("enter a number"))

r1=range(2,N+1)
for e in r1:
    r2=range(2,e)
    flag=True
    for e2 in r2:
        if(e%e2==0):
            flag=False
    if flag==True:
        print(e,end=' ')

# 4. Write a Python script to print all Prime numbers between two given numbers (both values inclusive).

N=int(input("enter a number"))
N2=int(input("enter second no:"))
r1=range(N,N2+1,1)
for e in r1:
    r2=range(2,e)
    flag=True
    for e2 in r2:
        if(e%e2==0):
            flag=False
    if flag==True:
        print(e,end=' ')

# 5. Write a Python script to find the next prime number of a given number.
N=int(input("Enter a number to print next prime"))
while N:
    N+=1
    temp=N
    flag=True
    r2=range(2,N)
    for e2 in r2:
        if(temp%e2==0):
            flag=False
            break
    if flag==True:
            print("Next prime number is:",temp)
            break    

# 6. Write a Python script to print the first N prime numbers.
import math

n = int(input("How many prime numbers to print: "))  
next = 2  # Prime number finding ka start point

while n != 0:  # Jab tak n primes mil nahi jate
    flag = True  # Prime hone ka assumption
    
    if next == 2:  # Special case: 2 is always prime
        print(next, end=' ')  
        n -= 1  
        next += 1
        continue  # Jump to next iteration

    for i in range(2, int(math.sqrt(next)) + 1):  # Sirf sqrt(next) tak check karenge
        if next % i == 0:  # Agar divisible ho gaya toh prime nahi hai
            flag = False  
            break  

    if flag:  # Agar prime hai toh print karo
        print(next, end=' ')  
        n -= 1  # Prime mil gaya, toh count reduce karo

    next += 1  # Agla number check karne ke liye badhao    
    

# 7. Write a Python script to check whether a given pair of numbers are Co-Prime numbers or not.
x=int(input("Enter 1 numbers:"))
y=int(input("Enter 2 number"))

r1=range(min(x,y),0,-1)
for i in r1:
    if(x%i==0 and y%i==0):
        if i==1:
            print("co-prime number")
            break
        else:
            print("not a co-prime number")
            break   

# 8. Write a Python script to print the first N terms of a Fibonacci series.

N=int(input("Input a number to print fibonachi:"))
a=0
b=1
if N==1:
    print(a,end=' ')
if N==2:
    print(b,end=' ')
else:
    print(a,b,end=' ')
while(N>2):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    N-=1

# 9. Write a Python script to calculate the LCM of two numbers.
import math
a=int(input("Enter 1 number:"))
b=int(input("Enter 2 number:"))
lcm=math.lcm(a,b)
print("%d and %d of lcm:"%(a,b),lcm)

# 10. Write a Python script to calculate the HCF of two numbers.
a=int(input("Enter 1 number:"))
b=int(input("Enter 2 number:"))
hcf=math.gcd(a,b)
print("%d and %d of hcf:"%(a,b),hcf)