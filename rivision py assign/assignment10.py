# 1.Write a python script to remove the last digit from a given number. (for example,if user enters 2534 then your output should be 253)

number=2534
number=number//10
print("output:",number)

# 2.write a python script to get the digit from a given number.(for example ,if user enters 2089 then your output shoud be 9).
mod=2089
mod=mod%10
print("last digit is:",mod)

# 3.Write a python to swap data of two variables
a=67
b=89
c=a
a=b
b=c
print("swap values:",a,b)

# 4.Write a python script which takes a three digit number from the user and displays only its first digit.

num=int(input("input 3 digit number:"))
print("output:",num//100)

# 5.Write a python script which takes a three digit number from the user and displays only its middle digit.
num=int(input("Enter three digit:"))
num=num//10
num=num%10
print("output:",num)