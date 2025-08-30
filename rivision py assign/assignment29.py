#                   Assignment-29 Function Date:16/08/2025

# 1. Write a Python program to create a simple function which prints "MySirG".

def teacher():
    print("MySirG is my favorate teacher.")

teacher()
a=teacher()
print(a)
# 2. Write a Python program to create a function which expects two arguments and prints them in the function body.

def Sum(a,b):
    print("sum of %d + %d="%(a,b),a+b)
Sum(45,23)# called positional argument
Sum(b=45,a=23)# called keyword argument

# 3. Write a Python program to create a function which expects an unknown number of arguments.

def f3(*t):
    avg=sum(t)/len(t)
    return avg

print(f3(4,4,2,12))

# 4. Write a Python program to create a function which expects a keyword argument.
def Add(a,b):
    return a+b

print(Add(b=2,a=234))

# 5. Write a Python program to create a function which expects a list as an argument.
def MaxList(*t):
    return max(t)

l1=(4,2,5,56,21,223)
print(MaxList(*l1))

# 6. Write a Python program to sum all the numbers in a list.
def SumList(*t):
    return sum(t)

l2=(4,52,32,125,23)
print(SumList(*l2))

# 7. Write Python program to create a function that finds the maximum of for numbers.
def FindMax(*t):
    return max(t)

print(FindMax(45,22,55,12))

# 8. Wirte a Python program to multiply all the numbers in a list.
def multiplyList(*t):
    multiple=1
    for e in t:
        multiple*=e
    return multiple

l3=(52,3,2)
print(multiplyList(*l3))

# 9. Write a Python program to create a function to check whether a number falls in a given range.

def checkRange(key,start,end):
    while start!=end:
        if start==key:
            print("vlaue %d in range"%(key)) 
            break
        start+=1
    else:
        print("value %d is not in range"%(key))
   
checkRange(7,4,15)

# 10. Write a Python program to create a function to check whether a given number is even or odd.
def evenOddCheck(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

evenOddCheck(int(input("enter a number:")))
