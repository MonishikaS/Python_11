# Day 03: Python Fundamentals
# Variables, Data Types, Mutability and Operators

# ==================================================
# Example 1: Variables and Reassignment
# ==================================================

name = "Rahul"
age = 16

print("Name:", name)
print("Age:", age)

age = 17
print("Updated age:", age)


# ==================================================
# Example 2: Multiple Assignment
# ==================================================

a, b, c = 10, 20, 30

print("a =", a)
print("b =", b)
print("c =", c)

# Assigning the same value to multiple variables
x = y = z = 100

print(x, y, z)


# ==================================================
# Example 3: Swapping Two Variables
# ==================================================

first = 10
second = 20

print("Before swapping:", first, second)

first, second = second, first

print("After swapping:", first, second)


# ==================================================
# Example 4: Basic Data Types
# ==================================================

integer_value = 25
float_value = 3.14
string_value = "Python"
boolean_value = True

print(integer_value, type(integer_value))
print(float_value, type(float_value))
print(string_value, type(string_value))
print(boolean_value, type(boolean_value))


# ==================================================
# Example 5: Collection Data Types
# ==================================================

# List: ordered and mutable
my_list = [10, 20, 30]

# Tuple: ordered and immutable
my_tuple = (10, 20, 30)

# Set: unique elements and mutable
my_set = {10, 20, 30}

# Dictionary: key-value pairs and mutable
my_dict = {"name": "Rahul", "age": 16}

print(my_list, type(my_list))
print(my_tuple, type(my_tuple))
print(my_set, type(my_set))
print(my_dict, type(my_dict))


# ==================================================
# Example 6: Mutable List
# ==================================================

numbers = [10, 20, 30]

print("Original list:", numbers)

numbers[0] = 100

print("Modified list:", numbers)


# ==================================================
# Example 7: Shared Reference to a Mutable Object
# ==================================================

a = [1, 2, 3]
b = a

b[0] = 100

print("a:", a)
print("b:", b)

# Both variables refer to the same list.


# ==================================================
# Example 8: Immutable String
# ==================================================

language = "Python"

language = language + " Programming"

print(language)

# A new string is created and assigned to language.


# ==================================================
# Example 9: Immutable Integer
# ==================================================

a = 10
b = a

b = 50

print("a:", a)
print("b:", b)

# Reassigning b does not change the value of a.


# ==================================================
# Example 10: Arithmetic Operators
# ==================================================

a = 17
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Remainder:", a % b)
print("Exponentiation:", a ** b)


# ==================================================
# Example 11: Comparison Operators
# ==================================================

x = 10
y = 20

print("Equal:", x == y)
print("Not equal:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal:", x >= y)
print("Less than or equal:", x <= y)


# ==================================================
# Example 12: Assignment Operators
# ==================================================

score = 10

score += 5
print("After += 5:", score)

score -= 3
print("After -= 3:", score)

score *= 2
print("After *= 2:", score)

score //= 3
print("After //= 3:", score)


# ==================================================
# Example 13: Logical Operators
# ==================================================

age = 17
has_permission = True

print("AND:", age >= 18 and has_permission)
print("OR:", age >= 18 or has_permission)
print("NOT:", not has_permission)


# ==================================================
# Example 14: Membership Operators
# ==================================================

fruits = ["apple", "banana", "mango"]

print("apple in fruits:", "apple" in fruits)
print("grapes in fruits:", "grapes" in fruits)
print("grapes not in fruits:", "grapes" not in fruits)


# ==================================================
# Example 15: Identity vs Equality
# ==================================================

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print("a is b:", list_a is list_b)
print("a is c:", list_a is list_c)
print("a == c:", list_a == list_c)


# ==================================================
# Example 16: Type Conversion
# ==================================================

age_text = "16"

age_number = int(age_text)

print("Age:", age_number)
print("Type:", type(age_number))

price = 99
price_text = str(price)

print("Price as text:", price_text)
print("Type:", type(price_text))


# ==================================================
# Example 17: Student Marks Calculator
# ==================================================

student_name = "Rahul"

maths = 85
science = 90
english = 80

total = maths + science + english
average = total / 3

print("Student:", student_name)
print("Total marks:", total)
print("Average marks:", average)


# ==================================================
# Example 18: Shopping Discount Calculator
# ==================================================

price = 2000
discount_percentage = 15

discount = price * discount_percentage / 100
final_price = price - discount

print("Original price: Rs.", price)
print("Discount: Rs.", discount)
print("Final price: Rs.", final_price)
