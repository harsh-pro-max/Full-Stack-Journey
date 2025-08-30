# Write a Python script to take your name as input from the user and then print it.
# name=str(input("Enter your name:"))
# print("Hello:",name)

# Write a Python script to take input of two numbers from the user, then calculate their sum and display the result.
num1=int(input("Enter a number:"))
num2=int(input("Enter second no:"))
sum=num1+num2
print("sum of %d + %d = %d"%(num1,num2,sum))

#Write a Python script which takes the radius from the user and displays the area of the circle.
r=int(input("Enter radius:"))
area=3.141*r*r
print("Area of %d radius is:%d"%(r,area))

# Write a Python script to calculate the square of a number. The number is entered by the user.
num1=int(input("Enter the value to cal sqr:"))
squre=num1*num1
print("Squre is",squre)

# Write a Python script which takes a character from the user and displays its Unicode.
chr=str(input("Enter any character:"))
print(chr,ord(chr))