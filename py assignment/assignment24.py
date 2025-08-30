# Python Assignments: Lists and Data Handling

# 1. Write a Python script to store multiple items in a single variable 
#    (Items are “Java”, “Python”, “SQL”, “C”) using a list.
l1=["Java","Python","SQL","C"]
print(type(l1))
print(l1)
# 2. Write a Python script to get the data type of a list.
l2=[1,2,3]
print(type(l2))
# 3. Write a Python script to get the last item of the list 
#    (mylist = ["Java", "C", "Python"]).
mylist=["Java","C","Python"]
print("last elment of list:",mylist[-1])
# or 
print("last elment of list:",mylist[2])
# 4. Write a Python script to change the values "SQL" and "Reactnative" with the 
#    values "NoSQL" and "Flutter". 
#    (List: thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]).
List=["Jave","SQL","C","Reactnative","Javascript","Python"]
List[1]="NoSQL"
List[3]="Flutter"
print(List)
# 5. Write a Python script to add an item to the end of the list 
#    (Item: “Python”, List: mylist = ["Java", "SQL", "C", "Reactnative"]).
mylist=["Jave","SQL","C","Reactnative",]
mylist.append("Python")
print(mylist)
mylist.extend(["harsh","prince"])
print(mylist)

# 6. Write a Python program to append elements from another list to the current list. 
#    (firstlist = ["Java", "Python", "SQL"], secondlist = ["C", "Cpp", "NoSQL"]).

firstlist=["Java","Python","SQL"]
secondlist=['C','Cpp',"NoSQL"]
# firstlist.extend(secondlist)
for e in secondlist:
    firstlist.append(e)
print(firstlist)

# 7. Write a Python program to print all items by referring to their index number.
#    (List: thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]).

thislist=["Jave","SQL","C","Reactnative","Javascript","Python"]
i=0
l=len(thislist)
while l:
    print(thislist[i])
    i=i+1
    l-=1
# 8. Write a Python program to sort the list alphanumerically.
#    (List: thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]).
thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
print(sorted(thislist))

# 9. Write a Python script to create a list of city names taken from the user.
l1=[]
print(type(l1))
n=int(input("how many input city name:"))
i=0
while n:
    l1.append(str(input("enter city name")))
    n-=1
    i+=1 
print(l1)
# 10. Write a Python script to create a list where each element of the list 
#     is a digit of a given number.
num=int(input("enter a bigger number:"))
l1=[]
while num:
    mod=num%10
    l1.insert(0,int(mod))
    num=num//10
print(l1)