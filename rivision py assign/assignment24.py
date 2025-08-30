#                   Assignment-24: Lists and Data Handling data: 05/08/2025

# 1. Write a Python script to store multiple items in a single variable.
l1=["name","harsh","class","BCA","sem-fee:",8000 ,'year:',2023, 'married',False,True]
print(l1)
# print all the data 
for e in l1:
    print(e,end=' ')

# 2. Write a Python script to get the data type of a list.
print(type(l1))

# 3. Write a Python script to get the last itme of the list. 
mylist=["java",'c','python']
print(mylist[-1])

# 4. Write a Python script to change the values"SQL" and "Reactnative" with the values "NoSQL" and "flutter".
mylist=["java",'c','python']
mylist.append("SQL")
mylist.append("NoSQL")
for e in mylist:
    print(e,end=' ')
mylist[3]="Reactnative"
mylist[4]="flutter"
print("\n")
for e in mylist:
    print(e,end=' ')

# 5. Write a Python script to add an item to the end of the list.add "javaScript"
mylist=["java",'c','python']
mylist.append("javaScript")
for e in mylist:
    print(e,end=' ')

# 6. Write a python program to append elements from another list to the current list.
firstList=["Java","Python","SQL"]
secondList=["C","C++","NoSQL"]
firstList.append(secondList)
for e in firstList:
    print(e)

# use extend methord
firstList = ["Java", "Python", "SQL"]
secondList = ["C", "C++", "NoSQL"]
firstList.extend(secondList)

for e in firstList:
    print(e)

# 7.Write a Python program to print all items by referring to their index number.
thisList=["java","SQL","C","Reactnative","javascript","Python"]
i=0
while i<len(thisList):
    print(thisList[i])
    i=i+1

# 8. Write a Python program to sort the list alphanumerically.
thisList=["java","SQL","C","Reactnative","javascript","Python"]
for e in sorted(thisList):
    print(e,end=' ')

# 9. Write a Python script to create a list of city names taken from the user.
list=[]
noOfCity=int(input("Enter how many city add the list:"))
i=0
while i<noOfCity:
    list.append(input("Enter a city name:"))
    print(list[i])
    i+=1
for e in list:
    print(e,end=' ')

# 10. Write a Python script to create a list where each element of the list is a digit of a given number.
num=int(input("Enter a number to store digit in a list:"))
list=[]
temp=num
while temp!=0:
    list.append(temp%10)
    temp=temp//10
for e in list:
    print(e) 

