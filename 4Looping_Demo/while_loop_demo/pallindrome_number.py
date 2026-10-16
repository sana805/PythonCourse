def pallindrome(num):
    temp=num
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    if rev==temp:
        print("number is pallindrome")
    else:
        print("number is not pallindrome")
num=int(input("enter a number:"))
pallindrome(num)