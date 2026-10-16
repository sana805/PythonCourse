# to print enter number is prime or not
def prime(num):
    count=0
    i=2
    while i<=num//2:
        if num%i==0:
            count+=1
        i+=1
    if count==0:
         print("prime number")
    else:
        print("not prime number")
prime(10)
            
