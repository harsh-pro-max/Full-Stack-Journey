# Python Assignments: Dictionary Manipulation

# 1. Write a Python program to create and print a dictionary which stores your information 
#    (name, age, gender, etc.).
d1={"name" : "harsh","age":20,"gender":"male"}
print(type(d1))
print(d1)

# 2. Write a Python program to access the items of a dictionary by referring to its key name.
d1={"name" : "harsh","age":20,"gender":"male"}
for e in d1:
    print(e,"=",d1[e])

# 3. Write a Python program to get a list of the values from a dictionary.

d1={"name":"harsh","age":18,"gender":"male"}
l1=[]
for e in d1:
    l1.append(d1[e])
print(l1)
# 4. Write a Python program to change the value of a specific item by referring to its key name.

d1={"name":"harsh","age":18,"gender":"male"}
d1["name"]="prince"
print(d1)

# 5. Write a Python program to print all key names in the dictionary, one by one.
d1={"name":"harsh","age":18,"gender":"male"}
for e in d1:
    print(e)

# 6. Write a Python program to create a dictionary that contains three dictionaries (nested dictionary).
student_data={
    "student1":{"name":"harsh","age":20,"subject":["science","math"]},
    "student2":{"name":"prince","age":20,"subject":["che","maths"]},
    "student3":{"name":"ritesh","age":20,"subject":["hindi","physices"]}
}
for e in student_data:
    print(student_data[e])


# 7. Write a Python program to create three dictionaries, then create one dictionary that will 
#    contain the other three dictionaries.

d1={"name":"harsh","age":20,"roll_no":1}
d2={"name":"prince","age":21,"roll_no":2}
d3={"name":"harsh","age":22,"roll_no":3}
d4={"first": d1,"second": d2,"third": d3}
for key in d4:
    for subkey in d4[key]:
        print(key,subkey,d4[key][subkey])

# 8. Write a Python program to convert two lists into a dictionary in a way that items from 
#    list1 are keys and items from list2 are values.# Step 1: Define two lists

keys = [1, 2, 3, 4, 5]  # First list (keys)
values = ["apple", "pineapple", "guava", "orange", "banana"]  # Second list (values)

# Step 2: Use zip() to pair elements of both lists
paired = zip(keys, values)  # zip() creates tuples of (key, value)

# Step 3: Convert zipped pairs into dictionary
dictionary = dict(paired)  # dict() converts zipped object into dictionary

# Step 4: Print the final dictionary
print(dictionary)


# 9. Write a Python program to merge two Python dictionaries into one dictionary.


d1={"name":"harsh","age":20,"roll_no":1}
d2={"name":"prince","age":21,"roll_no":2}


# 10. Write a Python program to get the key of the lowest value from the dictionary.
d1={21:"a",22:"b",31:"c",42:"d",32:"e"}
print(max(d1))
