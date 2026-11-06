balance = 10000
pin = "12345678"
print("Login First")
saeed_pin = input("Enter your pin: ")

if saeed_pin == pin:
    while True:

        
        print("\n\t ATM Machine:")

        print("\n1. Add balance \n 2 Balance inqury \n 3. withdraw amount \n 4. exist")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            amount = float(input("Enter add balance: "))
            balance += amount
            print(f"Add balance succssfully: {balance}")
        
        elif choice == "2":
                print(f"Check balance: {balance}")

        elif choice == "3":
            amount = float(input("Enter withdraw amount: "))
            if  amount <= balance:
                balance -= amount
            print(f"Withdraw amount succssfully: {balance}")


        elif choice == "4":
             print("Thank you for using the ATM")
             break

        else:
             print("invalid choice. try again")

else:
     print("Incorrect PIN")
