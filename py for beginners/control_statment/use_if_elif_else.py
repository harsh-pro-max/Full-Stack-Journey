# write a program to print grade optained in a test. take masrks obtained from user and display the grade.
marks=int(input("Enter your marks:"))
if marks >90 and marks <= 100:
    print("grade A")
elif marks>80 and marks<90:
    print("grade B")
elif marks>70 and marks<=80:
    print("grade C")
elif marks>60 and marks<=70:
    print("grade D")
elif marks>50 and marks<=60:
    print("grade E")
elif marks<50:
    print("below 50")
