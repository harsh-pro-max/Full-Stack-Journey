# 1.Write a python script to print True if the string 'my' is a member in a string entered by user.
st=str(input("enter a string:"))
# if st=="my":
#     print("True")
print(st in "my")
# 2.Write a python script to input two strings from the user and display whether the two variables referred to the same object or not. Print True or False.
s1=str(input("Enter a string:"))
s2=str(input("Enter a string:"))
print(id(s1))
print(id(s2))

print(id(s1)==id(s2))
# or use of is operator
print(s1 is s2)

# 3.what will be the output of the python expression 5>10<5?
print(5>10<5)

# 4.What will be the output of the python expression True or False?
print(True or False)