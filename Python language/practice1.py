# Python Bank System Using For Loop, If-Else, and OR

balance = 5000

for i in range(1, 10):
    print("\n===== BANK SYSTEM =====")
    print("1. Check Amount")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your current balance is:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print("Updated balance:", balance)
        else:
            print("Invalid deposit amount!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining balance:", balance)
        else:
            print("Invalid amount or insufficient balance!")

    elif choice == "4" or choice.lower() == "exit":
        print("Thank you for using the bank system!")
        break

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")

print("Program ended.")