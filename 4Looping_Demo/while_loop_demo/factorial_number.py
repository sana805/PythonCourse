def factorial(num):
    fact=1
    while num>0:
        fact*=num
        num-=1
    return fact
n=int(input("enter a number to find its factorial:"))
print(factorial(n))