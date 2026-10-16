def sum_digit(num):
    sum=0
    while num>0:
        digit=num%10
        sum+=digit
        num//=10
    return sum
num=int(input("enter a number:"))
print("sum of digits are=",sum_digit(num))
