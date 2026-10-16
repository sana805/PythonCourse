# Color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

expenses = []

while True:

    print(CYAN + "\n================================" + RESET)
    print(BLUE + "        💰 EXPENSE TRACKER" + RESET)
    print(CYAN + "================================" + RESET)

    print(YELLOW + "1. Add Expense" + RESET)
    print(YELLOW + "2. View Expenses" + RESET)
    print(YELLOW + "3. Total Expense" + RESET)
    print(YELLOW + "4. Clear Expenses" + RESET)
    print(YELLOW + "5. Exit" + RESET)

    choice = input("\nEnter your choice: ")

    # Add Expense
    if choice == "1":

        name = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))

        expenses.append([name, amount])

        print(GREEN + "✓ Expense added successfully!" + RESET)

    # View Expenses
    elif choice == "2":

        if len(expenses) == 0:
            print(RED + "No expenses found!" + RESET)

        else:
            print(BLUE + "\n------ YOUR EXPENSES ------" + RESET)

            for expense in expenses:
                print(
                    GREEN + expense[0] +
                    RESET + " : ₹" +
                    YELLOW + str(expense[1]) +
                    RESET
                )

    # Total Expense
    elif choice == "3":

        total = 0

        for expense in expenses:
            total = total + expense[1]

        print(
            CYAN +
            "\n💵 Total Expense: ₹" +
            str(total) +
            RESET
        )

    # Clear Expenses
    elif choice == "4":

        expenses.clear()

        print(RED + "✓ All expenses cleared!" + RESET)

    # Exit
    elif choice == "5":

        print(GREEN + "\nThank you for using Expense Tracker! 😊" + RESET)
        break

    else:

        print(RED + "Invalid choice! Please try again." + RESET)