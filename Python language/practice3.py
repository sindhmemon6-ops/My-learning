# for i in range(1, 10):
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = int(input("Enter third number: "))


#     if a >= b and a >= c:
#         print("Largest:", a)

#     elif b >= a and b >= c:
#         print("Largest:", b)

#     else:
#         print("Largest:", c)


# a = "10"

# b = "10"

# print(a + b)

correct_password = "1234"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access Granted")
        break

    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)

if attempts == 0:
    print("try again later")