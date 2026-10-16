def calculator():
    while True:
        print("simple calculator menu:")
        print("1.add")
        print("2.substract")
        print("3.multiply")
        print("4.division")
        print("5.exit")

        choice=input("enter your choice(1-5):")
        if choice=='5':
            print("exiting the calculator. Goodbye")
            break
        num1=float(input("enter the first number:"))
        num2=float(input("enter the second number:"))

        if choice=='1':
            result=num1+num2
            print(f"the result of {num1}+{num2} is:{result}")
        elif choice=='2':
            result=num1-num2
            print(f"the result of {num1}-{num2} is:{result}")
        elif choice=='3':
            result=num1*num2
            print(f"the result of {num1}*{num2} is:{result}")
        elif choice=='4':
            if num2!=0:
                result=num1/num2
            print(f"the result of {num1}/{num2} is:{result}")
      #  else:
#print("Error: cannot divide by zero.")
        else:
            print("invalid choice. please select a valid option.")
calculator()