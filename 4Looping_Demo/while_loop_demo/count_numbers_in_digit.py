def count(num):
    count=0
    while num!=0:
        num=num//10
        count=count+1
    print("number of digits=",count)
num=int(input("enter digits :"))
count(num)


