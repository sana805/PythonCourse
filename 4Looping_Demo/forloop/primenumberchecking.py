num=int(input("enter a number:"))
if num<=1:
    print("not a prime number")
else:-
count=0:
for i in range(2,num//2+1):
    if num%i==0:
        count+=1
        print("count:",count)
        if count==0:
            print("")