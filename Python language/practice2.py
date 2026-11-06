pin = 12345

name = "saeed"
for i in range(1, 10):
    print("**************Login System*************")
    print("1 Options = toyota supra")
    print("2 Options = civic 2021 model")
    print("3 Options = mahran 2022")
    print("4 Options = Exit")
    

    pin = int(input("Enter your Pin: "))

    name = input("Enter your name: ")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You purchased car name toyota supra")
        print("Price is 45 lakha")

    elif choice == "2":
        print("You purchased car name civic 2021 model")
        print("Price is 80 lakha")

    elif choice == "1":
        print("You purchased car name mahran")
        print("Price is 10 lakha")


    elif choice == "4" or choice.lower() == "exit":
        print("Thank you for using the bank system!")
        break

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
    
print("Program ended.")