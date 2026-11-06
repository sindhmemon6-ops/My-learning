# class Employee:
#     languaage = "Python"  #this is a class attributes
#     Salary = 1200000

#     def __init__(self):
#         print("i am a consector an objests: ")

#     def saeed(self):
#         print(f"the language is {self.languaage}, the salary is {self.Salary}")



# saeed = Employee()
# saeed.languaage = "Flutter Expert" # this is a instance atrributes
# print(saeed.languaage, saeed.Salary)

# Q 01

# class programmer:
#      company = "Microsoft"
#      def __init__(self, name, salary, pin):
#           self.name = name
#           self.salary = salary
#           self.pin = pin

# p = programmer("saeed", 1200000, 78601)
# print(p.name, p.salary, p.company)


# Q 02

# class calculator:
#     def __init__(self, n):
#         self.n = n

#         def square(self):
#             print(f"The squre is {self.n*self.n}")

# a = calculator(8)
# a.square()
        
# Q 03
class Demo:
    a = 4

o = Demo()
print(o.a)

o.a = 0
print(o.a)

print(Demo.a)
