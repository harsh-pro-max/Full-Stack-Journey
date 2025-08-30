#                   Assignment-14: Match 
# 1. Write a python script to check whether a given number is a three digit number or not.
num=int(input("Enter a number:"))
match num:
    case _ if num>=100 and num<=999:
        print("three digit number")
    case _:
        print("not 3 digit number")

# 2. Write a python scrip to check whether a given number is postive, negative or zero.

num=int(input("enter a number to check +,-,or 0"))
match num:
    case _ if num>0:
        print("positve number")
    case _ if num<0:
        print("negative number")
    case _:
        print("this is zero")

# 3.Write apython scrip tot make a menu driven program in which user has to choose one of the option from four given options -1) ODD-Even ,2)postive -non Postive, 3) Simple interest and 4) find roots of quadratic equaion. Match and execute appropriate code on user selection.
print("1.Odd,Even check \n 2.postive -Non Postive check \n 3.Simple Interest calcualte \n 4.find roots of quadratic equation")
opt=int(input("choose your options"))
match opt:
    case 1:
        print("Welcome to even or odd cheker program")
        num=int(input("enter a number:"))
        print("even") if num%2==0 else print("even")
    case 2:
        print("Welcome to positive or non-postive number checker")
        num=int(input("Enter a number"))
        print("positve") if num>=0 else print("Non-positve")
    case 3:
        print("Welcome to Simple Interest checker")
        p=int(input("Enter principal:"))
        r=int(input("Enter rate of interest per annum:"))
        t=int(input("Enter time (in year):"))
        si=(p*r*t)/100
        print("simple Interest is (p=%d r=%d t=%d):" %(p,r,t),si)
    case 4:
        pass
    case _:
        print("oops, you click wrong options please try again")

# 4.Write a python script to take one data from use and evaluate the type of data. If the data is of int tpe then print Monday , if the data is of float type then print Tuesday,if the data is of complex type then print Wednesday, if the data is of type ool then print Tuesday.
data = input("Enter any type of data: ")

try:
    value = eval(data) # converts '5' -> int, '5.5' -> float, '2+3j' -> complex


except:
    value = data  # fallback to string

match type(value):
    case t if t is int:
        print("Monday")
    case t if t is float:
        print("Tuesday")
    case t if t is complex:
        print("Wednesday")
    case t if t is bool:
        print("Thursday")
    case t if t is str:
        print("It's a string")
    case _:
        print("Unknown type")

# 5.Write a python script to take a string from the user.If the string is a part of mysirg then print "One ", if the string is a part of "eduacaiton" then print "Two" and is a part of "services" then print "Three".
st=str(input("enter a string"))
match st:
    case _ if st in "mysirg":
        print("one")
    case _ if st in "educaiotn":
        print("two")
    case _ if st in "services":
        print("three")
    case _:
        print("not match any case")

