num=int(input("enter a number:"))
temp=num
rev=0
for i in range(len(str(num))):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if rev==temp:
    print(f"{temp} is a pallindrome")
else:
    print(f"{temp} is not a pallindrome")
