while True:
    ask=input('Do you want to take out percentage? (yes/no):')
    if ask=='yes':
        part=float(input("Enter part value:"))
        whole=float(input("Enter Whole numbers:"))
        percentage=(part/whole)*100
        print('percentage=',percentage,'%')
    elif ask=='no':
        A=int(input("Enter First number:"))
        B=int(input("Enetr second number:"))
        C=input("Enter your operations:")
        if C=='+':
          print(A+B) 
        elif C=='-':
            print(A-B) 
        elif C=='*':
            print(A*B) 
        elif C=='/':
            print(A/B)
        else:
            print("Something went wrong.....")
    else:print("Please type yes or no..")
    cont=input('Do you want to continue?(yes/no)').lower()
    if cont=='no':
        print("Existing from calculator..")
          
        