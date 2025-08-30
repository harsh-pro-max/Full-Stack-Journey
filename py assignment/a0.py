# import a1
# print(a1.a)
# del a1.a
# write a program to check a number is posetive or negative.
a=56
if a>0:
    print("postive")
if a<0:
    print("negative")

# use of single line ef else
print("positive ") if a>0 else print("non positive")

# write a program to print grade obtained in a test. take marks obtained by the user and print the grade .
marks=int(input("enter your marks in % :"))
if marks>90 and marks<=100:
    print("grade A")
elif marks>80 and marks<=90:
    print("grade B")
elif marks>70 and marks<=80:
    print("grade C")
elif marks>60 and marks<=70:
    print("grade d")
elif marks>50 and marks<=60:
    print("grade e")
else:
    print("bellow 50")
