def armstrong(num):
    temp=num
    digits=len(str(num))
    sum=0
    while num>0:
        digit=num%10
        sum=sum+(digit**digits)
        num=num//10
    if sum==temp:
        print("armstrong number")
    else:
        print("not armstrong number")
num=int(input("enter a number:"))
armstrong(num)