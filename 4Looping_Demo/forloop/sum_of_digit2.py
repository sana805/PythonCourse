num=int(input("enter a number"))
sum=0
for i in range(len(str(num))):
 digit=num%10
 sum+=digit
 num=num//10
 print("sum of digits :",sum)
    