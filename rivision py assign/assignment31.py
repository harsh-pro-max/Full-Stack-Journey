#               Assignment-32  Recursive Functions Date:18/07/2025

# 1. Write a recursive Python function to calculate the sum of first N natural numbers.
def naturalSum(N):
    if N==1:
        return 1
    return N+naturalSum(N-1)

n=int(input("Enter a natural to print 1 from N sum:"))
sum=naturalSum(n)
print("sum of 1 to %d num sum is:"%(n),sum)

# 2. Write a recursive Python function to calculate the sum of first N odd natural numbers.
# sum of 1 from n between odd natural sum
def naturalOddSum(N):
    if N>0:
        naturalOddSum(N-1)
        return N*2-1

# N natural number sum
def oddSum(n):
    if n==1:
        return 1
    s=2*n-1 +oddSum(n-1)
    return s

n=int(input("Enter a natural to print 1 from N odd sum:"))

print("sum of 1 to %d num odd sum is:"%(n),oddSum(n))

# 3. Write a recursive Python function to calculate the sum of first N even natural numbers.

def evenSum(n):
    if n==0:
        return 0
    s=2*n+evenSum(n-1)
    return s
n=int(input("Enter a natural to print 1 from N even sum:"))

print("sum of 1 to %d num even sum is:"%(n),evenSum(n))

# 4. Write a recursive Python function to calculate the sum of squares of first N natural numbers.

def sqrSum(n):
    if n==1:
        return 1
    s=n**2+sqrSum(n-1)
    return s
n=int(input("Enter a natural to print 1 from N squres sum:"))

print("sum of 1 to %d num squres sum is:"%(n),sqrSum(n))


# 5. Write a recursive Python function to calculate the sum of cubes of first N natural numbers.

def cubeSum(n):
    if n==1:
        return 1
    s=n**3+cubeSum(n-1)
    return s
n=int(input("Enter a natural to print 1 from N cubes sum:"))

print("sum of 1 to %d num cubes sum is:"%(n),cubeSum(n))

# 6. Write a recursive Python function of calculate the factorial of a number.

def factorial(n):
    if n==1:
        return 1
    return n* factorial(n-1)

n=int(input("Enter a number to calcualte the factorial"))

print("factorial of %d is:"%(n),factorial(n))

# 7. Write a recursive Python to calculate the sum of the digits of a given number.

def digitSum(n):
    if n==0:
        return 0
    s=n%10+digitSum(n//10)
    return s

n=int(input("Enter a number to calcualte sum of num digit"))
print("sum of num is ",digitSum(105))

#  8. Write a recursive python function to print binary of a given decimal number.

def binary(n):
    if n>0:
        binary(n//2)
        print(n%2,end='')
n=int(input("generate decimal to binary num , enter a number:"))
print("binary of %d "%(n),digitSum(105))

