#               Assignment-28 Dictonary Manipuation Date:

# 1. Write a Python program to create and print a dicionary which stores your information (name,age,gender,etc)
stuData={"name":"harsh kushwaha","gender":"male","age":20}
for k,v in stuData.items():
    print(k,v)

# 2. Write a Python program to access the items of a dictionary by referring to its key name.
info={"vill":"saraiya","po":"umapur","ps":"Bhagwanpur","dist":"kaimur","pin-code":821102}
for e in info.keys():
    print(e)

# 3.Write a Python program to get a list values from a dictionary.
add={"vill":"saraiya","po":"umapur","ps":"Bhagwanpur","dist":"kaimur","pin-code":821102}
for e in info.values():
    print(e)

# 4.Write a Python program to change the vlaue of a specific item by referring to its key name.
info={"vill":"saraiya","po":"umapur","ps":"Bhagwanpur","dist":"kaimur","pin-code":821102}
info["ps"]="bhabua"
for k,v in info.items():
    print(k,v) 

# 5. Write a Python program to print all key names in the dictionary, one by one.
info={"vill":"saraiya","po":"umapur","ps":"Bhagwanpur","dist":"kaimur","pin-code":821102}
for e in info:
    print(e)

# 6. Write a Python program to create a dictionary that contains three dictionaries(nested dictonary).
userInfo = {
    "personal": {"name": "harsh", "age": 20, "marks": 80},
    "address": {"vill": "saraiya", "po": "umapur", "ps": "bhagwanpur"},
    "subjects": {"eng": 60, "math": 80, "phy": 75}
}

print(userInfo["personal"]["name"])  # Output: harsh

# 7. Write a Python program to create three dictionaris,then create one dictionary that will contain the other three dictionaries.
bigDict={
    "allInfo":{
        "personal": {"name": "harsh", "age": 20, "marks": 80},
        "address": {"vill": "saraiya", "po": "umapur", "ps": "bhagwanpur"},
        "subjects": {"eng": 60, "math": 80, "phy": 75}
    }
}
print(bigDict["allInfo"]["personal"])

# 8. Write a Python program to convert two lists into a dictionary in a way that items from list1 are keys and items from lits2 are values.
l1=[52,99,55,23,51]
l2=[77,91,43,24,52]
d1={}
for k in l1:
    for v in l2:
        d1[k]=v
for k,v in d1.items():
    print(k,v)

# 9. Write a Python program to merge two Python dictionaries into one dictionary.
d1={1:"A",2:"B",3:"C",4:"D"}
d2={"a":1,"b":2,"c":3,"d":4}
for k,v in d2.items():
    d1[k]=v
for k,v in d1.items():
    print(k,v)

# 10.Write a Python program to get the key of the lowest value from the dictionay.
d1={1:"A",2:"B",3:"C",4:"D"}
print(min(d1))
