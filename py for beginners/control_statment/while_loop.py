# write a program to print mySirG five times.
n=0
while n!=5:
    print("MySirG")
    n=n+1
# write a program to print first 10 natural number
i=1
while i<=10:
    print(i,end=' ')
    i+=1

# write a program to print first 10 natural numbers in reverse order
print()
i=10
while i>=1:
    print(i,end=' ')
    i-=1
print()
# write a program to print first N even natural numbers.
i=1
ev=2
while i<=10:
    print(ev,end=' ')
    ev=ev+2
    i+=1
print()
# Write a program where the user gets three attempts to input an even number. If the user enters an even number, they win the game; otherwise, after three wrong attempts, they lose the game
count=1
while count <=3:
    ev=int(input("Input an Even number:"))
    if ev%2==0 :
        print("you won the game")
        break
    else:
        print("this no not a even no")
        
    if count==3:
        print("you lose the game:")
        break
    count=count+1
    