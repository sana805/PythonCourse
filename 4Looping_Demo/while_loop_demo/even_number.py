# print all even numbers 1 to n
def even(num):
    i=1
    while i<=num:
        if i%2==0:
            print(i)
        i+=1
num=int(input("enter a number:"))
even(num)
print()

def eve(num):
    while num>0:
        if num%2==0:
            print(f"{num} is even")
    else:
            print(f"{num} is odd")
num=int(input("enter a number:"))
eve(num)