# 1. Write a python script to print MySirG N times on the screen
num=int(input("enter string how many times print (mySirG):"))
while num!=0:
    print("MysirG",end=' ')
    num-=1
# 2. Write a python script to print first N natural numbers
print()
N=int(input("Enter last natural num"))
i=1
while i<=N:
    print(i,end=' ')
    i+=1
# 3. Write a python script to print first N natural numbers in reverse order
rev=int(input("Enter last natural no:"))
while rev>0:
    print(rev,end=' ')
    rev-=1
# 4. Write a python script to print first N odd natural numbers
num=int(input("input no:"))
i=1
while i<num*2:
    print(i,end=' ')
    i+=2 
# 5. Write a python script to print first N odd natural numbers in reverse order
num1=int(input("enter last odd no to print:"))
if num1%2==0:
    num1=num1-1
while num1>=1:
    print(num1,end=' ')
    num1-=2