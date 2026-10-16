num=int(input("enter a number:"))
temp=num
sum=0
for i in range(len(str(num))):
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if sum==num:
        print(f"{num} is an armstrong number")
else:
        print(f"{num}is not an armstrong number")
