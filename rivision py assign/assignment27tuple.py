#           Assignment-27 : tuple Manupuation

 # 🧠 Python Assignments: Tuple Manipulation

# 1. Create a tuple using three different methods
t1=(4,5,2)
t2=tuple([4,2,52])
t3=4,5,2,5
t4=()
print(t1,t2,t3,t4)

# 2. Access the third element from the tuple
t3=4,5,2,5
print(t3[2])

# 3. Slice the tuple to get (3, 4, 5)
t1=(2,5,2,5,5,2)
print(t1[2:5])

# 4. Concatenate two tuples
t5=t1+t2
for e in t5:
    print(e)

# 5. Repeat the tuple three times
t6=(4,5)
print(t6*3)

# 6. Check if element 5 exists in the tuple
t7=(1,2,5,2,1,56,2,2)
for e in t7:
    if e==5:
        print("5 avalable in tuple")
        break


# 7. Count how many times 2 appears in the tuple
t7=(1,2,5,2,1,56,2,2)
count=0
for e in t7:
    if e==2:
        count+=1
print(count)

# 8. Find the index of element 4
t7=(1,2,5,2,1,56,2,4,2)
print(t7.index(4))

# 9. Convert a list into a tuple
l1=[4,5,2,4]
t1=4,5,l1
for e in t1:
    print(e)

# 10. Create a nested tuple and access an inner element
t1=(4,5,2,(4,5,2))
print(t1[3][0])
