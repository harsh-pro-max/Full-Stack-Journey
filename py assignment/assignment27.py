# Python Assignments: Set Manipulation

# 1. Write a Python program to store all the programming languages known to you using a set.
s1={"C++","COBOL","C#","JavaScript","Java","Python","HTML","CSS"}
print(type(s1))
print(s1)

# 2. Write a Python program to store your own information {name, age, gender, etc.} using a set.
info={"Name:harsh","age:20","gender:male"}
print(type(info))
print(info)


# 3. Write a Python script to get the data type of a set.
info={"Name:harsh","age:20","gender:male"}
print(type(info))

# 4. Write a Python script to find if “Python” is present in the given set.
s1={"C++","COBOL","C#","JavaScript","Java","Python","HTML","CSS"}
for e in s1:
    if(e=="Python"):
        print("available")
        break
else:
    print("not availabe") 

# 5. Write a Python program to add items from another set to the current set.
s1={1,2,3,52}
s2={5,2,3,7}
r1=range(s1)
# s3=s1+s2 cancatination is not supported in set why this is not hasble and not a sequence
for e in s2:
    s1.add(e)
print(s1)

# 6. Write a Python program to add elements of a list to a set.

l1=[4,5,23,53,"harsh","prince"]
s1=set()
for e in l1:
    s1.add(e)
print(s1)

# 7. Write a Python program to remove the last item of the given set.
s1={"C++","COBOL","C#","JavaScript","Java","Python","HTML","CSS"}
print(s1.pop())
print(s1)

# 8. Write a Python program to delete the set completely.

s1={"C++","COBOL","C#","JavaScript","Java","Python","HTML","CSS"}
print(s1.clear())
print(s1)

# 9. Write a Python program to loop through the set and print values.

s1=set()
N=int(input("enter a number:"))
while N:
    val=int(input("set values:"))
    s1.add(val)
    N-=1
print(s1)

# 10. Write a Python program to find the maximum and minimum values in a set.
s1={1,5,3,6,98,2,34,64}
print("minimum value of set:",min(s1))
print("maximum value of set:",max(s1))
