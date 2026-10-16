a=int(input("enter first number:"))
b=int(input("enter second number:"))
for i in range(1):
    temp=a
    a=b
    b=temp
    print("first number is:",a)
    print("second number is:",b)