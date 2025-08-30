# Python Assignments: Recursive Functions

# 1. Write a recursive Python function to calculate the sum of first N natural numbers.
# N=int(input("enter a number to sum natural num:"))
def sumOfNatural(N):
    if N==1:
        return 1
    s=N+sumOfNatural(N-1)
    return s
# print(sumOfNatural(N))

# 2. Write a recursive Python function to calculate the sum of first N odd natural numbers.
# od=int(input("enter a num to sum of N odd number:"))
def sumOfodd(N):
    if N==1:
        return 1
    s=N*2-1+sumOfodd(N-1)
    return s
# print(sumOfodd(od))

# 3. Write a recursive Python function to calculate the sum of first N even natural numbers.
# ev=int(input("enter a natural number to print sum of even no:"))
def sumOfEven(N):
    if N==1:
        return 2
    s=N*2+sumOfEven(N-1)
    return s
# print(sumOfEven(ev))

# 4. Write a recursive Python function to calculate the sum of squares of first N natural numbers.
# s=int(input("enter a natural number to cal sum of sqre:"))
def squreSum(N):
    if N==1:
        return 1
    s=N**2+squreSum(N-1)
    return s
# print(squreSum(s))


# 5. Write a recursive Python function to calculate the sum of cubes of first N natural numbers.
# s=int(input("enter a natural number to cal sum of cube:"))
def cubeSum(N):
    if N==1:
        return 1
    s=N**3+cubeSum(N-1)
    return s
# print(cubeSum(s))

# 6. Write a recursive Python function to calculate the factorial of a number.
# fact=int(input("enter a number to print factorial:"))
def factorial(f):
    if f==0:
        return 1
    factor=f*factorial(f-1)
    return factor
# print(factorial(fact))

# 7. Write a recursive Python function to calculate the sum of the digits of a given number.
# num=int(input("enter a big number to print sum of digit:"))
def sumOfDigit(num):
    if num==0:
        return 0
    s=num%10+sumOfDigit(num//10)
    return s 
# print(sumOfDigit(num))    

# 8. Write a recursive Python function to print the binary of a given decimal number.
def binary(num):
    if(num>0):
        binary(num//2)
        print(num%2,end='')
# N=int(input("enter a number to print in binary:"))
# binary(N)

# 9. Write a recursive Python function to print the octal of a given decimal number.
def octal(num):
    if(num>0):
        octal(num//8)
        print(num%8,end='')
# oc=int(input("enter a number to print in octal :"))
# octal(oc)
# 10. Write a recursive Python function to find the Nth term of the Fibonacci series.

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)  # Recursive call

# Test the function
n = int(input("Enter the position N: "))
print(f"The {n}th term in Fibonacci sequence is {fibonacci(n)}")