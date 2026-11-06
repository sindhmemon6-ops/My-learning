# Q 01
# function definition
# def avg(): 
#     a = int(input("Enter a  number: "))
#     b = int(input("Enter a  number: "))
#     c = int(input("Enter a  number: "))

#     average = (a + b + c)/3
#     print(average)

# # function call
# avg() 

# Q 02

# def name(name):
#     print(f"Good day today!: {name}")

# name("Saeed")

# Q 03


# def greatest(a, b, c,):
#     if(a>b and a>c):
#         return a
#     elif (b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
#     else:
#         print("Thank All equals")
# a = 6
# b = 8
# c = 3
# print(greatest(a,b,c))


# Q 04

# def f_to_c(f):
#     return 5 *(f-32)/9

# f = int(input("Enter temperature in f: "))
# print(f_to_c(f))  


# Q 05

# def muliply(n):
#     for i in range(1, 11):
#         print(f"{n} X {i} = {n*i}")

# muliply(5)


# project create gun snake game

computer = -1
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
you = youdict[youstr]

if (computer == -1 and you == 1):
    print("You Win!")

elif (computer == -1 and you == 0):
    print("You Loss!")

elif (computer == 1 and you == -1):
    print("You Loss!")

elif (computer == 1 and you == 0):
    print("You Win!")

elif (computer == 0 and you == 1):
    print("You Win!")

elif (computer == 0 and you == -1):
    print("You Loss!")

else:
    print("Your not win!")