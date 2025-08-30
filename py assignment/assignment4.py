# 1.Write a Python script containing a variable with some integer value, print the value of this variable.

# a=int(input("Enter the value of a:"))
# print("Enter value is:",a)

# 2.Write a Python script to print the value of a variable. The variable contains your name as data.

# a=str(input("Enter your name:"))
# print("Your name:",a)

# 3.Write a Python script to print values of three variables, each in a new line. All three variables are filled with some integer values.
x=89
y=10
z=123
print(x)
print(y)
print(z)

#4.Create 5 variables, each containing different types of data (e.g., 35, True, "MySirG", 5.46, 3+4j, etc). Write a Python script to print values of all the variables along with their data types.

intger=35
boolean=True
string="MySirG"
flow=5.46
com=3+4j
print(type(intger),intger)
print(type(boolean),boolean)
print(type(string),string)
print(type(flow),flow)
print(type(com),com)

# 5.First variable contains day number.Second variable contains month number.Third variable contains year number Write a Python script to display the date in the standard way (e.g., 29/11/2022).

dd=29
mm=11
yyyy=2022
# print("%d'/'%d'/'%d",dd,mm,yyyy)#me use but wrong
# print(f"{dd}/{mm}/{yyyy}")
print("%d/%d/%d" % (dd, mm, yyyy))


