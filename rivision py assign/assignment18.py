#                   Assignment-18: more on while loop with user input

# 1. Write a python script to print first N even natural numbers.
N=int(input("How many you need to print Even number:"))
i=2
while i<=N*2:
    print(i,end=' ')
    i=i+2

# 2. Write a python script to print first N even natural numbers in reverse order.
N=int(input("How many you need to print Even number in rev-order:"))
i=N*2
while i>=2:
    print(i,end=' ')
    i=i-2

# 3. Write a python script to print squares of first N natural numbers.
N=int(input("how many need to print squres:"))
i=1
while i<=N:
    print(i**2,end=' ')
    i=i+1

# 4. Write a python script to print cubes of first N natural numbers.
N=int(input("how many need to print cubes:"))
i=1
while i<=N:
    print(i**3,end=' ')
    i=i+1

# 5. Write a python script to print first 10 multiple of N
N=int(input("enter which number you to print multiple:"))
i=N
while i<=N*10:
    print(i,end=' ')
    i=i+N




 