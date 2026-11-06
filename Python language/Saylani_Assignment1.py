# 2. Variables, Data Types, Operators
# python
name = "Saeed"        # str
age = 20              # int
height = 5.9          # float
is_student = True     # bool

print(type(name), type(age), type(height), type(is_student))


a, b = 10, 3
print(a + b, a - b, a * b)    # arithmetic: 13 7 30
print(a / b, a // b, a % b, a ** b)  # 3.33.. 3 1 1000
print(a > b, a == b, a != b)  # comparison: True False True
print(a > 5 and b < 5)        # logical: True


# 3. Conditional Statements

# Example: check a grade from marks

# python
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


#     even or odd

# python
n = int(input("Enter a number: "))
print("Even" if n % 2 == 0 else "Odd")


# Python Data Structures
# python
# List (ordered, changeable)
fruits = ["apple", "banana"]
fruits.append("mango")
fruits.remove("banana")
print(fruits)             # ['apple', 'mango']

# Tuple (ordered, unchangeable)
point = (10, 20)
print(point[0])           # 10

# Dictionary (key: value)
student = {"name": "Ali", "age": 20}
student["city"] = "Karachi"
print(student["name"])

# Set (unique items only)
nums = {1, 2, 2, 3}
print(nums)               # {1, 2, 3}


# String methods (from the assignment title)
# python
s = "  Hello Python  "
print(s.strip())          # "Hello Python"
print(s.upper())          # "  HELLO PYTHON  "
print(s.lower())
print(s.replace("Python", "World"))
print(s.split())          # ['Hello', 'Python']
print(s.strip().startswith("Hello"))  # True
print(s.find("Python"))   # 8
print(len(s))
print("-".join(["a", "b", "c"]))  