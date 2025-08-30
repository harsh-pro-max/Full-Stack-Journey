#                   Assignment-27,Set-Manupulation Date:14/08/2025

# 1. Write a Python program to store all the programming languages known to you using a set.
lang={"C","C++","JavaScript","html","CSS","Python","SQL","Java"}
for e in lang:
    print(e,end=' ')

# 2. Write a Python program to store your own information(name,age,gender,etc),using a set.
info={"name:Harsh kushwah","age:20","gender:male","graduation:BCA"}
for e in info:
    print(e)

# 3. Write a Python script to get the data type of a set.
data={23,52,52}
print(type(data))

# 4. Write a Python program to find if "Python" is present in the given set.
lang={"C","C++","JavaScript","html","CSS","Python","SQL","Java"}
if "Python" in lang:
    print("Python is available in dict ")
else:
    print("not available")

# 5. Write a Python program to add items from another set to the current set.
firstSet={5,2,56,3,5,6}
secondSet={9,2,5,9,3}

for e in secondSet:
    firstSet.add(e)
for e in firstSet:
    print(e)

# 6. Write a Python program to add elements of a list to a set.
l1=["harsh","prince","kumar",True,False]
s1=set(l1)
for e in s1:
    print(e)

# 7. Write a Python program to remove the last items of the given set.
s2={89,92,"harsh",90,53}
s2.remove(53)
for e in s2:
    print(e)

# 8. Write a Python program to delete the set completely.
s2={89,92,"harsh",90,53}
s2.clear()
for e in s2:
    print(e)

# 9. Write a Python program to loop through the set add print values.
loop={"harsh","prince","manjeet","bihar","shrada","aman"}
for e in loop:
    print(e)

# 10. Write a Python program to find the maximum and minimum values in a set.
set1={523,52,3,1,2,9757,432,}
print(min(set1))
print(max(set1))
print(sum(set1))
