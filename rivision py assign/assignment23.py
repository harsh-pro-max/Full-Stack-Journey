#                       Assignment-23: more on loops  date- 05/08/2025

# 1. Write a Python script to calculate the factorial of a given number.
N=int(input("Enter a natural number to calculate factorial:"))
r1=range(1,N+1)
fact=1
for e in r1:
    fact*=e
print("factorial of %d is:%d"%(N,fact))

# 2. Write a Python script to count the digits in a given number.
# first method
n = int(input("Enter a big number to count digits: "))
temp = n
count = 0

# Assuming number has at most 20 digits
for i in range(1, 21):
    if temp == 0:
        break
    temp = temp // 10
    count += 1

print("The number %d has %d digits." % (n, count))

# second method
N = int(input("Enter a big number to count the digits: "))
i = 0
temp = N  # Save original value
while temp > 0:
    temp = temp // 10
    i += 1
print("The number %d has %d digits." % (N, i))

# 3. Write a Python script to calculate the sum of digts of a given number.
N = int(input("Enter a big number to calculate  digits sum: "))
i = 0
temp = N  # Save original value
digSum=0
while temp > 0:
    mod=temp%10
    digSum+=mod
    temp = temp // 10
print("%d digits sum is:%d" % (N, digSum))

# 4. Write a Python script to print the binary equivalent of a given decimal number(witout using bin() method).


