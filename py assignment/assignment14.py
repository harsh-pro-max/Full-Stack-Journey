# Write a python script to check whether a given nmber is a three digit number or not.
# Write a Python script to check whether a given number is positive, negative, or zero.Checking if a number is odd or even.
"""
print("1.to know no 3 digit or not.")
print("2.positive or negative")
print("3.Even Or odd")

print("3.exit ")

opt=int(input("Enter any option:"))
match opt:
    case 1:
        num=int(input("enter a number:"))
        if(num>99 and num<1000):
            print("Three digit number") 
        else:
            print("not three digit no:") 
    case 2:
        num2=int(input("entar a number:"))
        if(num2>0):
            print("num is positive")
        else:
            print("num is negative")
    case 3:
         num2=int(input("entar a number:"))
         if(num2%2==0):
             print("even no")
         else:
            print("odd no")
    case 4:
        print("end of program")
        exit(0) 
    case _:
        print("wrong input")
"""
# Ek menu-driven program banao jisme user ko 4 options diye gaye ho:
# - Odd-Even check
# - Positive - Non-Positive check
# - Simple Interest calculate karna
# - Quadratic equation ke roots find karna
'''
print("1.odd even check\n2.positive - non- positive check \n3. simple Interest calculte check \n4.Quadratic equation ke roots find\n5.exit ")
opt=int(input("Enter your choice:"))
match opt:
    case 1:
        num1=int(input("enter a number:"))
        if(num1%2==0):
            print("Even no")
        else:
            print("odd no")
    case 2:
        num=int(input("input any number:"))
        if(num>0):
            print("positve")
        else:
            print("negative")
    case 3:
        p=int(input("Enter principle rate:"))
        r=int(input("Enter rate:"))
        t=int(input("Enter time:"))
        si=(p*r*t)/100
        print("Simple Interest=",si)
    case 4:
        import math
        a=int(input("Enter value of a:"))
        b=int(input("Enter vlaue of b:"))
        c=int(input("Enter vlaue of c:"))
        D=b**2-4*a*c
        if D>=0:
            x=(-b+math.sqrt(D))/2*a
            print("positive lene pe value of x:",x)
            x2=(-b-math.sqrt(D))/2*a
            print("negative lene pe value of x:",x2)
        else:
            print("learn how to solve")

    case 5:
        print("end of program")
        exit(0)
    case _:
        print("wrong input")
'''
"""
Ek Python script likho jo ek string le user se aur check kare:
- Agar string "one" ka part hai toh "One" print karo.
- Agar string "education" ka part hai toh "Two" print karo.
- Agar string "services" ka part hai toh "Three" print karo.
"""
opt2=str(input("choose option,[one,Education,services]"))
match opt2:
    case "one":
        print("1 one")
    case "education":
        print("Two")
    case "services":
        print("Three")
    case _:
        print("wrong input")