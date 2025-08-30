#               Assignment-21: more on for loop and range. data:04/08/2025

# 1. Write a python script to print first N even natural numbers.
N=int(input("enter a number"))
for e in range(1, N+1):
    print(e*2,end=' ')

# 2. Write a python script to print first N odd natural numbers.
N=int(input("enter a number"))
for e in range(1, N+1):
    print(e*2-1,end=' ')

# 3. Write a python script to print squares of first N natural numbers.
N=int(input("how much you want to need squre:"))
for e in range(1,N+1):
    print(e**2,end=' ')

# 4. Write a python script to print cubes of first N natural numbers.
N=int(input("how much you want to need cubes:"))
for e in range(1,N+1):
    print(e**3,end=' ')

# 5. Write a python script to display all prime numbers within a range. #range start=15 end =45
for e in range(15, 46):  # from 15 to 45 inclusive
    for i in range(2, e):
        if e % i == 0:
            break
    else:
        print(e, end=' ')
