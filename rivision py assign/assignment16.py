#                   Assignment-16: more on while loop

# 1. Write a python script to print first 10 even natural numbers.
i=2
while i<=10*2:
    print(i,end=' ')
    i=i+2

# 2. Write a python script to print first 10 even natural numbers in reverse order.
i=10*2
while i>=2:
    print(i,end=' ')
    i=i-2

# 3. Write a python script to print squares of first 10 natural numbers.
i=1
# a=1
while i<=10:
    # a=i**2
    print(i**2,end=' ')
    i=i+1

# 4. Write a python script to print cubes of first 10 natural numbers.
i=1
while i<=10:
    print(i**3,end=' ')
    i=i+1

# 5. Write a python script to print first 10 multiple of 5.
num=int(input("which number you write to multiple:"))
i=num
while i<=num*10:
    print(i,end=' ')
    i=i+num






