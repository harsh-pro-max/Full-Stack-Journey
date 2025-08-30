
s=lambda a,b: a+b# using reference id to print or call 
print(s(2,3))# call of lambda expression
s=(lambda a,b:a*b)(8,3)
# in s holdes the value of lambda expression
print(s)
# call of lambda expression

# use of lambda expression in recursion
f=lambda a: 1 if a==0 else a*f(a-1)
print(f(7))