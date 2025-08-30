# 1. Write a Python script to calculate sum of first n natural numbers.
N=int(input("enter value of N:"))
r1=range(1,N+1,1)
sum=0
for e in r1:
    sum+=e
print("sum N natural no:",sum)
# 2. Write a Python script to calculate sum of squares of first N natural numbers.
N=int(input("enter value N:"))
r2=range(1,N+1,1)
sum=0
for e in r2:
    sum+=e**2
print("sum of N numbers sqrs:",sum)
# 3. Write a Python script to calculate sum of cubes of first N natural numbers.
N=int(input("enter value N:"))
r3=range(1,N+1,1)
sum=0
for e in r3:
    sum+=e**3
print("sum of N numbers cubes:",sum)
# 4. Write a Python script to calculate sum of first N odd natural numbers.
N=int(input("enter value N:"))
if N%2==0:
    N=N-1
r4=range(1,N+1,2)
sum=0
for e in r4:
    sum+=e
print("sum of first odd natural no is:",sum)

# 5. Write a Python script to calculate sum of first n even natural numbers.
N=int(input("enter value N:"))
if N%2!=0:
    N=N-1
r5=range(2,N+1,2)
sum=0
for e in r5:
    sum+=e
print("sum of first odd natural no is:",sum)

# Python Assignments: Full Stack Development

# 6. Write a Python script to calculate the factorial of a given number.
N=int(input("Enter a no to cal factorial:"))
fact=1
r1=range(1,N+1)
for e in r1:
    fact=fact*e
print("Factorial of No:",fact)

# 7. Write a Python script to count the digits in a given number.
N=int(input("Enter a bigger No:"))
count=0
while N!=0:
    count+=1
    N=N//10
print("digit count=",count)

# 8. Write a Python script to calculate the sum of digits of a given number.
N=int(input("enter a bigger number:"))
sum=0
while N:
    sum=sum+N%10
    N=N//10
print("sum of digit:",sum)

# 9. Write a Python script to print the binary equivalent of a given decimal number (without using bin() method).
N=int(input("Enter a number:"))
dec_bin=[]
temp=N
while N:
    dec_bin.append(N%2)
    N=N//2
dec_bin.reverse()
print("%d in binary:"%temp,dec_bin)

# 10. Write a Python script to print the octal equivalent of a given decimal number (without using oct() method).
N = int(input("Enter an octal number: "))  # Input in octal form
oct_dec = 0
temp = N
e = 0  # e ko loop ke bahar initialize karo

while N:
    rem = N % 10  # Extract last digit
    oct_dec += rem * (8 ** e)  # Multiply with power of 8
    N = N // 10  # Remove last digit (octal base)
    e += 1  # Increment power

print("%d in decimal:" % temp, oct_dec)