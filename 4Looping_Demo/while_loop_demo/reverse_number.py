def reverse(num):
    temp=num
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    if rev==temp:
            print("pallindrome number")
    else:
            print("not a pallindrome number")
    return rev
num=int(input("enter a number:"))
reverse(num)