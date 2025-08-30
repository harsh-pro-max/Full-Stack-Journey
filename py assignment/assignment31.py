# Python Assignments: Recursion

# 1. Write a recursive Python function to print first N natural numbers.
# N=int(input("input how many print number:"))
def Nnatural(N):
    if(N==0):
        return 1
    Nnatural(N-1)
    print(N)
# Nnatural(N)

# 2. Write a recursive Python function to print first N natural numbers in reverse order.
# N=int(input("input how many print number:"))
def Nnatural(N):
    if(N==0):
        return 1
    print(N)
    Nnatural(N-1)
  
# Nnatural(N)

# 3. Write a recursive Python function to print first N odd natural numbers.
# odd=int(input("Enter a number to print odd number:"))
def firstOdd(N):
    if(N>0):
        firstOdd(N-1)
        print(2*N-1)

# firstOdd(odd)

# 4. Write a recursive Python function to print first N odd natural numbers in reverse order.
# odd=int(input("Enter a number to print odd number:"))
def revOdd(N):
    if(N>0):
        print(2*N-1)
        revOdd(N-1)
# revOdd(odd)

# 5. Write a recursive Python function to print first N even natural numbers.
# even=int(input("enter how many print even no:"))
def Neven(N):
    if N>0:
        Neven(N-1)
        print(2*N)
# Neven(even)

# 6. Write a recursive Python function to print first N even natural numbers in reverse order.
# even=int(input("how many you to  print rev even no:"))
def revEven(N):
    if N>0:
        print(2*N)
        revEven(N-1)
# revEven(even)

# 7. Write a recursive Python function to print squares of first N natural numbers.
# N=int(input("how many squres you to print"))
def squre(N):
    if(N>0):
        squre(N-1)
        print(N**2)
# squre(N)

# 8. Write a recursive Python function to print cubes of first N natural numbers.
# N=int(input("how many cubes you to print:"))
def cube(N):
    if(N>0):
        cube(N-1)
        print(N**3)
# cube(N)

# 9. Write a recursive Python function to print first N multiples of a given number.
# num=int(input("Enter a number to print table:"))
def table(N):
    if N>0:
        table(N-1)
        print(N*num)
# table(N=10)

# 10. Write a recursive Python function to print a number in reverse order.
num=int(input("enter a big number:"))
def rev(N):
    if N>0:
        print(N%10,end='')
        rev(N//10)
rev(num)