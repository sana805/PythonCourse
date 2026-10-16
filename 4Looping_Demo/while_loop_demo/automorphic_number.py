def auto(num):
    square=num*num
    while num>0:
        if num%10 != square%10:
            print("not an automorphic number")
            return
        num=num//10
        square=square//10
    print(" automorphic number")
num=int(input("enter a number:"))
auto(num)