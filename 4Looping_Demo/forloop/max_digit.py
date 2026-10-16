num=int(input("enter a number"))
sum=0
max=0
for i in range(len(str(num))):
 digit=num%10
 if digit>max:
  max=digit
 sum+=digit
 num=num//10
# print("sum of digits :",sum)
 print("max digit=",max)