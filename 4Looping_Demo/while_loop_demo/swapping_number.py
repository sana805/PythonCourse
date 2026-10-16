#swapping of two number  using third variable.
def swap(a,b):
    while a>=0 or b>=0:
        temp=a
        a=b
        b=temp
        print("after swapping:")
        print("a=",a)
        print("b=",b)
        break
a=int(input("enter number for a:"))
b=int(input("enter number for b:"))
swap(a,b)