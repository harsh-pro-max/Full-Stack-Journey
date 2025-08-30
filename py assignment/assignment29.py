# Python Assignments: Functions

# 1. Write a Python program to create a simple function which prints "MySirG".
def name():
    print("MySirG")
name()

# 2. Write a Python program to create a function which expects two arguments 
#    and prints them in the function body.
def argus(a,b):
    print("a:",a,"b:",b)
num=23
num2=44
argus(num,num2)
# 3. Write a Python program to create a function which expects an unknown number of arguments.
def avg(*t):
    avge=sum(t)/len(t)
    return avge
t1=(5,2,3,56,32)
# print(avg(10,20,53,23))
print(avg(*t1))

# 4. Write a Python program to create a function which expects kwargs (keyword arguments).
def add(a,b):
    return a+b
sum=add(b=8,a=9)
print("sum of a & b:",sum)

# 5. Write a Python program to create a function which expects a list as an argument.
def print_list(*li):
    for e in li:
        print(e,end=' ')
li=[5,2,6,3,6]
print_list(*li)

# 6. Write a Python program to create a function that finds the maximum of four numbers.
def maximum(*t):
    return max(t)
print("maximum num is:",maximum(4,64,234,78))

# 7. Write a Python program to sum all the numbers in a list.
def sumOfList(*t):
    return sum(t)
li=[45,23,66,33,532]
print("sum of list:",sumOfList(*li))

# 8. Write a Python program to multiply all the numbers in a list.
def mulOfList(*t):
    mul=1
    for e in t:
        mul=mul*e
    return mul
li=[45,23,66,33,532]
print("multiply of list:",mulOfList(*li))

# 9. Write a Python program to create a function to check whether a number falls in a given range.
def check_range(key,r1,r2):
    while r1<=r2:
        if(r1==key):
            print("%d is in range"%(key))
            break
        r1+=1
    else:
        print("%d is not available in range"%(key))
check_range(7,3,14)

# 10. Write a Python program to create a function to check whether a given number is even or odd.
def evenOrOdd(a):
    if a%2==0:
        print("Even number")
    else:
        print("Odd number")
evenOrOdd(87)