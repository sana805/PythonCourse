#To print how many days in all month

def month(num):
    while num!=0:
        if num==1 or num==3 or num ==5 or num==7 or  num==8 or num ==10 or num==12:
            print("31 days")
        elif num==4 or num==6 or num==9 or num==10 or num==11:
            print("30 days:")
        elif num==2:
            print("28 or 29 days")
        else:
            print("invalid month")
        num=0
num=int(input("enter a month:"))
month(num)
