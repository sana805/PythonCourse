#print leap year using while loop upto 14 20
def year():
    year=14
    while year<=20:
        if(year%4==0):
            print(year)
        year+=1
year()

print()


#to check wheather entered year is leap or not
def year1():
    i=1
    while i<=1:
        if(year%4==0):
            print("leap year")
        else:
            print("not leap year")
        i+=1
year=int(input("enter a  year:"))
year1()