# 1. Write a python script to print the first N multiples of a given number

# N=int(input("Enter a number:"))
# for e in range(N,10*N+1,N):
#     print(e)

# 2. Write a python script to calculate the sum of the first N natural numbers

# N=int(input("Enter Natural no: "))
# sum=0
# for e in range(1,N+1):
#     sum+=e
# print("Sum of N natural no=",sum)

# 1. Write a python script to print each character of a string with its corresponding Unicode
s1=str(input("Enter a string:"))
for e in s1:
    print(e,"=",ord(e))
# 2. Write a Python script to print only vowels of the given string
s2=str(input("Enter a string:"))
r1="aeiouAEIOU"
for e in s2:
    for i in r1:
        if i==e:
            print(i,end=' ')
# 3. Write a Python script to count occurrence of spaces in a given string
print()
for e in s2:
    print(e,end=' ')
# 4. Write a Python script to print unique digits of a given integer
num2=str(input("Enter a number (123211)"))
for e in num2:
    for i in num2:
        if i==e:
            print(i)
            break



# 5. Write a Python script to count number of digits in a given number
num=str(input("Enter bigger number:"))
count=0
for e in num:
    count+=1
print("num in digits:",count)