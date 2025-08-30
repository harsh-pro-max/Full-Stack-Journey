# write a program to count the 'a' in given string.
st=input("Enter a string:")
count=0
for e in st:
    if e=='a':
        count+=1
print(count)

# print all the character of a string, but stop printing if 'r' appeard in the sequence if all the character successfully printed the print message 'all the charaters are processed'
st=input("Enter a string:")
for e in st:
    if e=='r':
        break
    print(e)
else:
    print("\n All the characters are processed")