import random
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'
        ,'R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h'
        ,'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
        'x','y','z']
number=['1','2','3','4','5','6','7','8','9','0']
schar=['!','@','#','$','%','^','&','*','(',')','/',
       '?','>','<','{','}','|']
password=[]
l1=int(input("How many letter you want in your password:"))
n1=int(input("How many digit you want in your password:"))
sc=int(input("How many special character you want in your passwors: "))
for i in range(l1):
    i=random.choice(letter)
    password+=i

for i in range(n1):
    i=random.choice(number)
    password+=i
for i in range(sc):
    i=random.choice(schar)
    password+=i

random.shuffle(password)
final_pass=""
for i in password:
    final_pass+=i

print("Your Password=",final_pass)