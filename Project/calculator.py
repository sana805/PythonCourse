A=int(input("Enter First Number:"))
B=int(input("Enter Second Number:"))
C=input("Enter Your Operation:")
if C=='+':
    print(A+B)
elif C=='-':
    print(A-B)
elif C=='*':
    print(A*B)
elif C=='/':
    print(A/B)
elif C=='%':
    print(A%B)
else:
    print("Something Went Wrong!")