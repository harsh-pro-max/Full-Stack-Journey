#           Assignment-19: for loop

# 1. Write a python script to print each character of a string with its corestponding Unicode.
st=input("Enter a string to print unicode:")
for i in st:
    print(i,"->",ord(i))

# 2. Write a Python script to print only vowels of the given string.
st=input("Enter a string to print only vowels in this string:")
# first methord
vol="aeiouAEIOU"
for i in st:
    for e in vol:
        if e==i:
            print(i)

# second methord
vol="aeiouAEIOU"
for i in st:
    if i in vol:
        print(i,end='')

# 3. Write a Python script to print occurrence of spaces in a given string.
st=input("Enter a string to count the spaces:")
count=0
for e in st:
    if e==' ':
        count+=1
print(count)

# 4. Write a python script to print unique digits of a given integer.
num = input("Enter a number: ")
unique_digits = ""

for digit in num:
    if digit not in unique_digits:
        unique_digits += digit

print("Unique digits are:", unique_digits)

# 5. Write a Python script to count number of digits in a given integer.
num=input("Enter a big digit number:")
count=0
for i in num:
    count+=1
print(count)


