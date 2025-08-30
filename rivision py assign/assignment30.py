#               Assignment-30 Function-Based Challenges Date: 17/08/2025

# 1. Write a Python program to create function that takes a list and returns a new list with the original list's unique elements.
def UniqueList(l2):
    l1=[]
    for e in l2:
        if e not in l1:
            l1.append(e)
    return l1

l2=[4,2,52,2,1,2,1]
newlist=UniqueList(l2)
for e in newlist:
    print(e,end=' ')

# 2. Write a Python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def PrimeChecker(num):
    for e in range(2,num):
        if num%e==0:
            print("not prime number")
            break
    else:
        print("%d is prime number"%(num))

num=int(input("enter a number to check prime or not:"))
PrimeChecker(num)

# second method
import math

def PrimeChecker2(num):
    if num < 2:
        print("not prime number")
        return
    for e in range(2, int(math.sqrt(num)) + 1):
        if num % e == 0:
            print("not prime number")
            break
    else:
        print(f"{num} is prime number")

num = int(input("enter a number to check prime or not: "))
PrimeChecker(num)

# 3. Write a Python program to create a function that prints the even numbers from a given list. Sample 

def evenList(l1):
    newlist=[]
    for e in l1:
        if e%2==0:
            newlist.append(e)
    return newlist

list=[1,2,3,4,5,6,7,8,9]
for e in evenList(list):
    print(e,end=' ')

# 4. Write a Python program to create a function to find the Min of three numbers.
def FindMin(*t):
    return min(t)

print(FindMin(23,2,552))

# 5. Write a Python program to create a function that checks whether a passed string is plandrome or not.
def CheckPalindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            print(f"{s} is not a palindrome")
            break
        start += 1
        end -= 1
    else:
        print(f"{s} is palindrome")

CheckPalindrome("harsh")

# 6. Write a Python program to create a function and print a list where the values are squares of numbers between 1 and 30.
def SqureList():
    num=int(input("how much squres you to print:"))
    l1=[]
    for e in range(1,num+1,1):
        l1.append(e**2)
    return l1

for e in SqureList():
    print(e,end=' ')

# 7. Write a Python program to create a function inside another function.
def squre(num):
    print("squre: ",num**2)
    def cube(num):
        print("cube:",num**3)
    cube(num)

squre(5)

# 8. Write a Python program to create a function that accepts a string and calculates the number of uppercase and lowercase letters.

def countUcaseLcase(str):
    Ucase=0
    Lcase=0
    for e in str:
        if e >='a' and e<='z':
            Lcase+=1
        elif e>='A' and e<='Z':
            Ucase+=1
    print("%s in string UpperCase count is %s"%(str,Ucase))
    print("%s in string Lowercase count is %s"%(str,Lcase))

countUcaseLcase("harsh kushwaha")

# 9. Write a Python program to create a function to check whether a string is a pangram or not.

def checkPangram(str):
    copy=str.lower()
    pangram="abcdefghijklmnopqrstuvwxyz"
    list=[]
    print(len(pangram))
    for e in copy:
        if e>='a' and e<'z' or e>='A' and e<='Z':
            if e not in list:
                list.append(e)
    # aage ke steps tum likh do keval camparision karna rah gaya hai
    if set(list) == set(pangram):
        print("This string is pangram")
    else:
        missing = set(pangram) - set(list)
        print("Not a pangram. Missing letters:", ''.join(sorted(missing)))

