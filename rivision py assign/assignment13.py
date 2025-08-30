#                   Assignment-13 More on Decision Control
# 1.Write a python script to check whether a given number is a three digit number or not.
number=int(input("Enter 3 digit number:"))
if(number>=100 and number<=100):
    print("three digit number")
else:
    print("not 3 digit number")

# 2.Write a python script to check whether a given number is positive , negative or zero.
number=int(input("Enter a number:"))
if(number>0):
    print("positive") 
elif(number<0):
    print("negative ")
else:
    print("this is zero")

# 3.Write a python script to check whether a iven quadratic equation has two real & distint roots, real & equal roots or imaginary roots
a=float(input("Enter the coefficient a:"))
b=float(input("Enter the coefficient b:"))
c=float(input("Enter the coefficient c:"))

# Check if 'a' is non-zero
if a == 0:
    print("This is not a quadratic equation.")
else:
    # Calculate the discriminant
    D = b**2 - 4*a*c

    # Determine the nature of the roots
    if D > 0:
        print("The equation has real and distinct roots.")
    elif D == 0:
        print("The equation has real and equal roots.")
    else:
        print("The equation has imaginary roots.")

# 4.Write a python scrip to check whether a given year is a leap year or not.
year=int(input("enter a year:"))
if (year%400==0):
    print("Leap year")
elif(year%100==0):
    print("not leap year")
elif (year%4==0):
    print("Leap year")
else:
    print("not Leap year")

# 5.Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
# first method
a,b,c=45,23,52
if(a>b and a>c):
    print("a is grater")
elif(b>a and b>c):
    print("b is grater")
elif(a==b==c):
    print("all are equal")
else:
    print("c is grater")

# second method
a, b, c = 45, 23, 52

if a == b == c:
    print(f"All numbers are equal: {a}")
else:
    greatest = max(a, b, c)
    print(f"The greatest number is: {greatest}")