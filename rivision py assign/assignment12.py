#               Assignment-12 Decision Control
#.Write a python script to check whether a given number is positive or non-positive.

a=int(input("Enter a number:"))
print("positve" if a>0 else "non-positive")

num=int(input("enter a number:"))
if(num>0):
    print("positive number")
if(num<0):
    print("non positve")
# second methord
print("positve number") if num>0 else print("non positive")

# third method
if(num>0):
    print("positive number")
else:
    print("non positive number")

# 2.Write a python script to check whether a given number is positve,negative or zero.

b=int(input("Enter a number:"))
if(b>0):
    print("positive")
elif b<0:
    print("negative")
else:
    print("zero")

# 3.Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots.
# Input coefficients of the quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

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
# 4.Write a python script to check whether a given year is a leap year or not.
year=int(input("enter a year:"))
if (year%400==0):
    print("Leap year")
elif(year%100==0):
    print("not leap year")
elif (year%4==0):
    print("Leap year")
else:
    print("not Leap year")
# 5.Write a python script to print greater among three numbers.Print number only once even if the nubmers are the same.
a,b,c=5,6,2
if( a>b and a>c):
    print("a is grater")
elif (b>c and b>a):
    print("b is grater")
elif (a==b==c):
    print("number are same")
else:
    print("c is grater")