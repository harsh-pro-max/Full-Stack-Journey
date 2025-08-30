# 1. Write a Python script to print the first 10 multiples of 5.
r1=range(5,5*10+1,5)
for e in r1:
    print(e,end=' ')
# 2. Write a Python script to print the first 10 multiples of N.
N=int(input("Enter a number to print table:"))
r1=range(N,N*10+1,N)
for e in r1:
    print(e,end=' ')
# 3. Write a Python script to print the first M multiples of N.
N=int(input("Enter a no to print multiple:"))
M=int(input("input a no to how many print multilple:"))
r2=range(N,N*M+1,N)
for e in r2:
    print(e,end=' ')
# 4. Write a Python script to print the first 10 multiples of N in reverse order.
N=int(input("Enter a number:"))
r3=range(N*10,N,-N)
for e in r3:
    print(e,end=' ')
# 5. Write a Python script to print a table of user's choice.
ch=int(input("which no you print table:"))
r4=range(ch,ch*10+1,ch)
for e in r4:
    print(e,end=' ')