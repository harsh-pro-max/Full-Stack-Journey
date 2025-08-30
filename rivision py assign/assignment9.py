# 1.Write a python script to calculate simple interest.
#si=p*r*t
p=int(input("Enter principal rate:"))
r=int(input("Enter rate:"))
t=int(input("Enter time in years:"))
si=(p*r*t)/100
print("Simple interest is:",si)

# 2.write a python script to calculate area of a rectangle.
l=int(input("Enter the len of rectangle:"))
b=int(input("Enter the bredth of rectangle:"))
area=l*b
print("Rectangle of area:",area)

# 3.write a python script to calculate average of three numbers entered by user.
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
avg=(a+b+c)/3
print("avg of 3 number:",avg)

# 4.write a python script to calculate volume of a cubid.
l=int(input("enter the len:"))
b=int(input("enter bredth:"))
h=int(input("enter hight:"))
print("volume of cuboid is:",l*b*h)

# 5.write a pytho script to take two numbers from user (say x,and y),now calculate xy and display the result.

x=int(input("enter a number:"))
y=int(input("enter secnd number:"))
print("x*y is:",x*y)
