year=int(input("enter a year:"))
for i in range(1):
    if year%4==0:
       print(f"{year} is a leap year")
    else:
       print(f"{year} is not a leap year")