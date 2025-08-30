# Python Assignments: String Manipulation

# 1. Write a Python script to create a string in 3 different possible ways.
s1="harsh"
s2='prince'
s3=""" mysirg teacher """
s4='''3 single cot\'s'''
s5=str()
print(s1,s2,s3,s5,s4,sep='!->')


# 2. Write a Python script to get the characters from the start to position 5 
#    (Given String: "iNeuron" using slice syntax).
str="iNeuron"
for i in str:
    print(i,end=' ')
print(str[0:5:1])

# 3. Write a Python script to get the characters from position 2 to position 5 
#    (Given String: "Hello Learners" using slice syntax).
str="Hellow Learners"
print(str[2:5:1])

# 4. Write a Python script to demonstrate string concatenation adding space in between 
#    (Given Strings: a = "Learning", b = "Python").
a="Learning"
b="Python"
l1=[a,b]
s1=" ".join(l1)
print(s1)

# 5. Write a Python script to get the count of total number of characters in a string 
#    (Given String: "iNeuron").
str="INeuron"
print(len(str))

# 6. Write a Python script to reverse a string ("iNeuron").
str="INeuron"
print(str[-1:-8:-1])

# 7. Write a Python script to determine whether a string contains a specific substring.
text="leaning python is fun"
l1=text.split(' ')
for i in l1:
    if i=="is":
        print("is in substring")
        break
    
# 8. Write a Python script to check if a string contains only numbers.
str_value = "258"
if str_value.isdigit():
    print("Only numbers")
else:
    print("Not only numbers")

# 9. Write a Python script to check if a string contains only characters of the alphabet.
s1="myharsh"
if s1.isalpha():
    print("only alphabet value")
else:
    print("all character")

# 10. Write a Python script to convert an integer to a string.
num=1343
st=str(num)
print(type(st))