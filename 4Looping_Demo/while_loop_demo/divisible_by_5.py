#print numbers divisible by 5 using function and while loop
def divisible():
    num=1
    while num<=100:
        if num%5==0:
            print(num)
        num+=1
divisible()

print()


 #check wheather enterd number is divisible by 5 or not

def div(num):
   while num>0:
    if num%5==0:
         print(f"{num} is divisible by 5")
    else:
       print(f"{num} is not divisible by 5")
       break
num=int(input("enter a number:"))
div(num)
         