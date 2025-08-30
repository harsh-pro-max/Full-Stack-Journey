# wap to count 'a' in a given strings, using for loop
count=0
st=str(input("Enter a string:"))
for i in  st:
    if(i=='a'):
        count=count+1
print("this strings no of a is:",count)

# print all the character of a string but stop printing if 'r' appeared in the sequence if all the character successfully printed the print message "all the characters are processed"
strR=str(input("Enter a string:"))
for i in strR:
    if(i=='r'):
        print("r is appeared ")
        break
    else:
        print(i,end=',')
else:
    print("All characters are processed")