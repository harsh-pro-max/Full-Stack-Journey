# Write a Python script to calculate simple interest.
p=int(input("Enter principle amount:"))
r=float(input("Enter rate:"))
t=int(input("Enter year time:"))
si=(p*r*t)/100
print("Simple interest=",si)

# Write a Python script to calculate the area of a rectangle.
l=int(input("Enter the len of rectangle:"))
b=int(input("Enter the breath of rectangle:"))
area=l*b
print("Area of rectangle:",area)

# Write a Python script to calculate the average of three numbers entered by the user
a1=int(input("Enter 1 numbers:"))
a2=int(input("Enter 2 numbers:"))
a3=int(input("Enter 3 numbers:"))
avg=(a1+a2+a3)/3
print("Average of 3 numbers:",avg)

# Write a Python script to calculate the volume of a cuboid
l=int(input("Enter lengthof cubied:"))
b=int(input("Enter breadth of cubied:"))
h=int(input("Enter height: of cubied:"))
volume=l*b*h
print("Cubied of value:",volume)

# Write a Python script to take two numbers from the user (say x and y), now calculate ( x^y ) and display the result.
x=int( input("Enter the value of x"))
y=int( input("Enter the value of y"))
print("x^y=",x**y)
