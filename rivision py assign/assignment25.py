#                   Assignment-25 : List Manipulation Date: 07/08/2025

# 1. Write a Python script to create a list of first N natural numbers.
N=int(input("Enter a Natural numbers to add in list"))
r1=range(1,N+1,1) #1 to N range is in r1.
l1=[]

for e in r1:
    l1.append(e)
for e in l1:
    print(e,end=' ')

# 2. Write a python script to create a list of first N odd natural numbers.
N=int(input("Enter a Natural numbers to add odd number from 1 to N:"))
r1=range(1,N*2+1,2)
l1=[]
for e in r1:
    l1.append(e)
for e in l1:
    print(e,end=' ')

# 3. Write a python script to create a list of first N even natural numbers.
N=int(input("Enter a Natural numbers to add even number from 1 to N:"))
r1=range(2,N*2+1,2)
l1=[]
for e in r1:
    l1.append(e)
for e in l1:
    print(e,end=' ')


# 4. Write a python script to find the greatest number in a given list of numbers.
l1=[4,52,21,63,73,14,333,62]
lmax=max(l1)
print("gratest of this list is:",lmax)

# 5. Write a python script to find the smallest number in a given list of numbers.
l1=[4,52,21,63,73,14,333,62]
lsmall=min(l1)
print("smallest of given list is:",lsmall)

# 6. Write a python script to calculate the sum of elements in a given list of numbers.
l1=[4,52,21,63,73,14,333,62]
listSum=sum(l1)
print("Sum of list is:",listSum)

# 7. Write a python script to remove all non-int values from a list.
mixed_list = [
    42,
    3.14,
    "Hello, Harsh!",
    True,
    None,
    2 + 3j,
    [1, 2, 3],
    {"key": "value"}
]

# Filter only int values
int_only_list = [e for e in mixed_list if type(e) == int]

print(int_only_list)

# 8. Write a python script to print distinct elements along with their frequencies of occurrence in the list.
my_list = [1, 2, 2, 3, 1, 4, 2, 3]

# Step 1: Create an empty list to store elements already counted
counted = []

# Step 2: Loop through each element
for i in range(len(my_list)):
    element = my_list[i]
    
    # Check if element is already counted
    if element not in counted:
        # Count frequency manually
        count = 0
        for j in range(len(my_list)):
            if my_list[j] == element:
                count += 1
        
        # Print result
        print(f"{element} occurs {count} times")
        
        # Mark this element as counted
        counted.append(element)
    
# 9. Write a Python script to print indices of all occurrences of a given element in a given list.
num=10
i=0
my_list = [10, 20, 10, 30, 10, 40]
listLen=len(my_list)
# first method
i=0
while i<listLen:
    if num==my_list[i]:
        print("%d found at index %d"%(num,i))
    i+=1
# second method
for c,e in my_list:
    if num==e:
        print("%d found at index %d"%(num,c))

# 10.Write a python script to sort a list.
my_list = [10, 20, 10, 30, 10, 40]
print(sorted(my_list))