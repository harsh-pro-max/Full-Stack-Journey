# Write a Python script to check whether a given number is a three-digit number or not

# num=int(input("Enter a number:"))
# if(num>99 and num<1000):
#     print("number is three digit")
# else:
#     print("not 3 digit no")

# Write a Python script to check whether a given number is positive, negative, or zero.

# if(num>0):
#     print("positve")
# elif (num<0):
#     print("negative")
# else:
#     print("zero")

# Write a Python script to check whether a given quadratic equation has two real and distinct roots, real and equal roots, or imaginary roots.

# Input coefficients of the quadratic equation
# a = float(input("Enter the coefficient a: "))
# b = float(input("Enter the coefficient b: "))
# c = float(input("Enter the coefficient c: "))

# Check if 'a' is non-zero
# if a == 0:
#     print("This is not a quadratic equation.")
# else:
    # Calculate the discriminant
    # D = b**2 - 4*a*c

    # Determine the nature of the roots
    # if D > 0:
    #     print("The equation has real and distinct roots.")
    # elif D == 0:
    #     print("The equation has real and equal roots.")
    # else:
    #     print("The equation has imaginary roots.")

# Write a Python script to check whether a given year is a leap year or not.
year=int(input("input year:"))
if(year%100):
    print("leap year")
elif(year%4==0):
    print("leap year")
else:
    print("not! leap year")

# Write a Python script to print the greater among three numbers. Print the number only once, even if the numbers are the same.
a=int(input("input a:"))
b=int(input("input b:"))
c=int(input("input c:"))

if(a>b and a>c):
    pass
elif(b>a and b>c):
    pass
elif(a==b==c):
    print("a b c are equal")
else:
    pass
