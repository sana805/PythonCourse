def max(a,b):
    while a>=0 or b>=0:
        if a>b:
            print(f"{a} is maximum number")
        else:
            print(f"{b} is  maximum number")
        break
a=int(input("enter a number:"))
b=int(input("enter a number:"))
max(a,b)