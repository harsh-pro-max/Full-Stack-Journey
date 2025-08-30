#                   Assignment:26 string manipulation date:13/08/2025

# 1. Write a Python script to create a string in 3 different possible ways.
s1='string 1'
s2="string 2"
s3="""string 3"""
s4='''string 4'''

# 2. Write a python script to get the characters from the start to postion 5 (Given string : "iNeuron" using slice syntax).
s5="iNeuron"
subs5=s5[0:5]
print(subs5)

# 3. Write a python script to demonstrate string concatenation adding space in between (Given Strings: a="Learning",b="Python").
a="Learning"
b="Python"
c=a+" " + b
print(c)

# 4. Write a Python script to get the characters from position 2 to postion 5.(Given string: "Hello Learners" using slicing syntax).
s6="Hello learners"
subStr=s6[2:5]
print(subStr)

# 5. Write a Python script to get the count of total number of characters in a string.(given string:"iNeuron").
s7="iNeuron"
length=len(s7)
print(length)

# 6. Write a Python script to reverse a string("iNeuron").
s8="iNeuron"
rev=s8[::-1]
print(rev)

# 7. Write a Python script to determine whether a string contains a spdific substring.
main_string = "Welcome to iNeuron"
substring = "iNeuron"
if substring in main_string:
    print("yes part of main_string")
else:
    print("no,not a part of main_string")

# 8. Write a Python script to check if a string contains only numbers.
num="563"
if num.isdigit():
    print("only number")
else:
    print("alphabet character also")

# 9. Write a python script to check if a string contains only characters of the alphabet.
str="string only"
if str.isalpha():
    print("only alphabets")
else:
    print("numbers also")

# 10. Write a python script to convert an integer to a string.
num=88932
str=str(num)
print(type(str),str)

