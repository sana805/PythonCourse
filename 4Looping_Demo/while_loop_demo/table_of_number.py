#To print a table of a number
def table(num):
    i=1
    while i<=10:
        print(num,"*",i,"=",num*i)
        i+=1
num=int(input("enter a number:"))
table(num)