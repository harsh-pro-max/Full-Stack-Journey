# Python Assignments: Function-Based Challenges

# 1. Write a Python program to create a function that takes a list and returns a 
#    new list with the original list's unique elements.
def unique_list(l1):
    l2=[]
    for e in l1:
        if e not in l2:
            l2.append(e)
    return l2
n=int(input("enter how many input a list: "))
l1=[]
while n:
    l1.append(int(input("Enter a number:")))
    n-=1
l2=unique_list(l1)
for e in l2:
    print(e,end=' ')
    
# 2. Write a Python program to create a function that takes a number as a parameter 
#    and checks if the number is prime or not.
def primeCheck(num):
    r1=range(2,num,1)
    for e in r1:
        if(num%e==0):
            return print("not a prime a number")
            
    else:
        return print("prime number")
        # second methord
import math 
def primeCheck2(num):
    squre=int(math.sqrt(num))
    r1=range(2,squre+1)
    for e in r1:
        if num%e==0:
            return print("not a prime number")
    else:
        return print("prime number")
N=int(input("enter a number to check prime:"))
primeCheck2(N)
primeCheck(N)



# 3. Write a Python program to create a function that prints the even numbers 
#    from a given list. Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9].
def evenPrint(list):
    for e in list:
        if e%2==0:
            print(e,end=' ')


List= [1, 2, 3, 4, 5, 6, 7, 8, 9]
evenPrint(List)

# 4. Write a Python program to create a function that checks whether a passed 
#    string is palindrome or not.
def palindromeCheck(num):
    temp=num
    newNum=0
    while temp:
        mode=temp%10
        newNum=newNum*10+mode
        temp=temp//10
    if num==newNum:
        print("palindrome number")
    else:
        print("not a palindrome ")
palin=int(input("enter a number:"))
palindromeCheck(palin)


# 5. Write a Python program to create a function to find the Min of three numbers.
def min_val(a,b,c):
    if a<b and a<c:
        print("a is minimum")
    elif b<a and b<c:
        print("b is minimum ")
    else:
        print("c is minimum")
def min_val2(a,b,c):
    print("minimum value is",min(a,b,c))
min_val(45,2,63)
min_val2(45,12,53)

# 6. Write a Python program to create a function and print a list where the values 
#    are squares of numbers between 1 and 30.
def list_sqr(li):
    for e in range(1,li+1):
        print(e**2,end=' ')
N=30
list_sqr(N)

# 7. Write a Python program to access a function inside another function.
def sqr(num):
    print("squre of number is:",num**2)
    def cubee(num):
        print("cube of number is:",num**3)
    cubee(num)
sqr(5)

# 8. Write a Python program to create a function that accepts a string and calculates 
#    the number of uppercase and lowercase letters.
def countU_Lcase(string):
    Lcase=0
    Ucase=0
    Ncase=0
    Scase=0
    for e in string:
        if e>="A" and e<='Z':
            Ucase=Ucase+1
        elif e>='a' and e<='z':
            Lcase=Lcase+1
        elif e>=48 and e<=57:
            Ncase=Ncase+1
        else:
            Scase=Scase+1
    else:
        print("Lcase is:",Lcase)
        print("Ucase is:",Ucase)
        print("Ncase is:",Ncase)
        print("Special case is:",Scase)

str1=str(input("enter a string"))
countU_Lcase(str1)

# 9. Write a Python program to create a function to check whether a string is a pangram or not.
def pangram(s1):
    pan='abcdefghijklmnopqrstuvwxyz'
    temp=str()
    copy=set(s1.lower())
    if len(copy)<len(pan):
        print("not pangram")
    for e in copy:
        if e>='a' and e<='z':
            temp=e
    else:
        if temp == pan:
            print("this is pangram")
        else:
            print("not a pangram")
s1=str(input("Enter a stiring:"))#The quick brown fox jumps over the lazy dog
pangram(s1)


# 10. Write a Python program to create a function to check whether a string is an anagram or not.
def anagram(s1,s2):
    if s1==s2:
        print("strings are anagram")
    else:
        print("not a anagram")
s1=set("harsh")
s2=set("hashr")
anagram(s1,s2)