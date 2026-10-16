#check whether enterd number is perfect or not
def perfect(num):
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i+=1
    if sum==num:
        print(f"{num} is perfect  number")
    else:
        print(f"{num} is not perfect number")
num=int(input("enter a number:"))
perfect(num)




