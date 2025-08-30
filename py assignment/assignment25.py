# Python Assignments: List Manipulation

# 1. Write a Python script to create a list of first N natural numbers.
N=int(input("how many store natural no:"))
r1=range(1,N+1)
l1=[]
for e in r1:
    l1.append(int(e))
print(l1)
# using extend methord direct store
l1.extend(r1)
print(l1)
# 2. Write a Python script to create a list of first N odd natural numbers.
N=int(input("how many store odd no:"))
l1=[]
i=1
while N:
    l1.append(i)
    i=i+2
    N=N-1
print(l1)
# second methord
N = int(input("How many odd numbers to store: "))
l1 = [i for i in range(1, 2*N, 2)]
print(l1)

# 3. Write a Python script to create a list of first N even natural numbers.
N = int(input("How many even numbers to store: "))
l1=[i for i in range(2,2*N+1,2)]
print(l1)

# 4. Write a Python script to find the greatest number in a given list of numbers.

print(max(l1))

# 5. Write a Python script to find the smallest number in a given list of numbers.
print(min(l1))

# 6. Write a Python script to calculate the sum of elements in a given list of numbers.
l2=[4,5,2,3,6,3,6]
print("sum of list",sum(l2))


# 7. Write a Python script to remove all non-int values from a list.
l1=[2,5,3,5.5,"harsh","pk"]
r1=[]
for e in l1:
    if(type(e)==int):
        r1.append(e)
l1.clear()
l1.extend(r1)
print(l1)        

# second methord comprehension
r1 = [i for i in l1 if isinstance(i, int)]

# 8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
mylist = [2, 3, 2, 4, 3, 5, 3, 6, 2]
s1=set()
s1={i for i in mylist}

for i in s1:
    print(i,"appears",mylist.count(i),"times")


# 9. Write a Python script to print indices of all occurrences of a given element in a given list.
mylist = [2, 3, 2, 4, 3, 5, 3, 6, 2]
element=3
print("Element 3 found at indices: [")
i=0
l=len(mylist)
while l:
    if mylist[i]==3:
        print(i,end=',')
    l=l-1
    i=i+1
print("]")    

# 10. Write a Python script to sort a list.
l1=[2,4,2,1,63,21,23,632]
print(sorted(l1))