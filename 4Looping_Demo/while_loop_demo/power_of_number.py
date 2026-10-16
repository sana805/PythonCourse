#print power of number using while loop

def power(base,expo):
    result=1
    i=1
    while i<=expo:
        result=result*base
        i+=1
    print("power=",result)
base=int(input("enter a base:"))
expo=int(input("enter a exponent:"))
power(base,expo)

