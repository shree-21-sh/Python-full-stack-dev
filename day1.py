def greet(name):
    return f"Hello, {name}! Welcome to Python."


def add_numbers(a, b):
    return a + b


def find_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"


def square(number):
    return number * number


print(greet("Shree"))
print("Sum:", add_numbers(12, 10))
print("Square:", square(8))

marks = int(input("Enter your marks: "))
print("Your grade is:", find_grade(marks))

name = "shree"
age = 20
marks_value = 99
usn = "1GD24CS140"
college = "GCEM"
passed = True

print(type(name))
print(type(age))
print(type(marks_value))
print(type(usn))
print(type(college))
print(type(passed))

print("Addition:", 12 + 10)
print("Subtraction:", 12 - 10)
print("Multiplication:", 12 * 10)
print("Division:", 12 / 10)
marks=int(input("Enter your marks:"))
print("Your grade is:", find_grade(marks))