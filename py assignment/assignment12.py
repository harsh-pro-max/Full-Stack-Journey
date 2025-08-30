# Write a python script to check whether a given number is positive or non-positive.
num=int(input("Enter a number:"))
if(num>0):
    print("positive number")
else:
    print("negtive number")

# Write a python script to check whether a given number is divisible by 5 or not.
if(num%5==0):
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# Write a python script to check whether a given number is even or odd.
if(num%2==0):
    print("Even number")
else:
    print("odd number:")

# Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
g1=int(input("Enter a number:"))
g2=int(input("input second no:"))
if(g1>g2):
    print("%d is grater"%(g1))
else:
    print("%d is grater"%(g2))

# Write a python script to print two given words in dictionary order.
st1=str(input("input string:"))
st2=str(input("input string:"))
if(st1<st2):
    print(st1,st2)
else:
    print(st2,st1)