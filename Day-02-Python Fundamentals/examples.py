# Day 02 — Python Fundamentals
# Practical Examples

# Example 1: Python Character Set
# Alphabets, digits, and special symbols

student_name = "Rahul"
age = 16
total = 10 + 20

print(student_name)
print(age)
print(total)


# Example 2: Python Is Case-Sensitive

name = "Rahul"
Name = "Aman"

print(name)
print(Name)


# Example 3: Identifiers

student_name = "Riya"
student_age = 17
marks1 = 90
_total = 100

print(student_name)
print(student_age)
print(marks1)
print(_total)


# Example 4: Different Types of Literals

integer_value = 25
float_value = 3.14
string_value = "Python"
boolean_value = True
empty_value = None

print(integer_value)
print(float_value)
print(string_value)
print(boolean_value)
print(empty_value)


# Example 5: Arithmetic Operators

a = 17
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Exponentiation:", a ** b)


# Example 6: Comparison Operators

x = 20
y = 10

print("Greater than:", x > y)
print("Less than:", x < y)
print("Equal to:", x == y)
print("Not equal to:", x != y)
print("Greater than or equal:", x >= y)
print("Less than or equal:", x <= y)


# Example 7: Assignment Operators

score = 10
print("Initial score:", score)

score += 5
print("After adding 5:", score)

score -= 3
print("After subtracting 3:", score)

score *= 2
print("After multiplying by 2:", score)


# Example 8: Logical Operators

age = 17
has_id = True

print("AND:", age >= 18 and has_id)
print("OR:", age >= 18 or has_id)
print("NOT:", not has_id)


# Example 9: Identifying Tokens

marks = 90

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# Example 10: Simple Calculator

number1 = 20
number2 = 4

print("Sum:", number1 + number2)
print("Difference:", number1 - number2)
print("Product:", number1 * number2)
print("Quotient:", number1 / number2)


# Example 11: Student Result

student_marks = 75

if student_marks >= 40:
    print("Congratulations! You passed.")
else:
    print("Keep practising!")


# Example 12: Discount Calculator

price = 1000
discount_percentage = 10

discount = price * discount_percentage / 100
final_price = price - discount

print("Original price:", price)
print("Discount:", discount)
print("Final price:", final_price)
