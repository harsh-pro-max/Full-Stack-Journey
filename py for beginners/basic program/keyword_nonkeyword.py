# use of non keyword argument

def f1(*t):#tuple
    print(t)
def f2(*t):
    return sum(t)/len(t)
t1=(4,52,33,52)
avg=f2(*t1)
print(avg)
# f1(*t1)#print t1 call of non keyword argument
#using *pass value 1 by 1
# f1(t1)# this time t1 as pass tuple variable 
# use of keyword argument
d={'a':56,'b':78,'c':88,'d':92}
def keyword(**d):#dict
    for k,v in d.items():
        print(k,'-',v)
keyword(**d)# call of keyword argument
