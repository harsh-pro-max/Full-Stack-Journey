#                   Assignment-17: While loop with user input 

# 1. Write a python script to print MySirG N itmes on the screen.
count=int(input("how many times you to print 'MySirG': "))
i=1
while i<=count:
    print(i,"->MySirG",end=' ')
    i=i+1

# 2. Write a python script to print first N natural numbers.
N=int(input("how many numbers you to print on the screen:"))
i=1
while i<=N:
    print(i,end=' ')
    i+=1

# 3. Write a python script to print first N natural numbers in reverse order.
N=int(input("printing reverse order in natural number,give last number:"))
i=N
while i>=1:
    print(i,end=' ')
    i-=1

# 4. Write a python script to print first N odd natural numbers.
N=int(input("How many you want to print odd number:"))
i=1
while i<=N*2-1:
    print(i,end=' ')
    i=i+2

# 5. Write a python script to print first N odd natural numbers in reverse order.
N=int(input("How many you want to print odd in reverse order:"))
i=N*2-1
while i>=1:
    print(i,end=' ')
    i=i-2




