# Python Practice – Questions 1, 2 and 3

## Question 1: Identify Valid and Invalid Identifiers

Identify the invalid identifiers and explain why.

| Identifier | Valid/Invalid | Reason |
|---|---|---|
| `Serial_no.` | Invalid | Contains a dot (`.`). |
| `1st_Room` | Invalid | Starts with a digit. |
| `Hundred$` | Invalid | Contains a special character (`$`). |
| `Total Marks` | Invalid | Contains a space. |
| `Total_Marks` | Valid | Uses letters and an underscore. |
| `total-Marks` | Invalid | Contains a hyphen (`-`). |
| `_Percentage` | Valid | An identifier can start with an underscore. |
| `True` | Invalid | `True` is a reserved Boolean constant in Python. |

## Question 2: Python Assignment Statements

### (a) Assign 10 to `length` and 20 to `breadth`.

```python
length = 10
breadth = 20
```

### (b) Assign the average of `length` and `breadth` to a variable named `sum`.

```python
sum = (length + breadth) / 2
```

### (c) Assign a list containing the strings 'Paper', 'Gel Pen', and 'Eraser' to `stationery`.

```python
stationery = ['Paper', 'Gel Pen', 'Eraser']
```

### (d) Assign 'Mohandas', 'Karamchand', and 'Gandhi' to `first`, `middle`, and `last`.

```python
first = 'Mohandas'
middle = 'Karamchand'
last = 'Gandhi'
```

### (e) Concatenate the three strings with appropriate spaces and assign the result to `fullname`.

```python
fullname = first + ' ' + middle + ' ' + last
print(fullname)
```

**Output:**

```text
Mohandas Karamchand Gandhi
```

## Question 3: Choose the Appropriate Data Type

| Part | Data Value | Data Type | Reason |
|---|---|---|---|
| (a) | Number of months in a year | `int` | Represents a whole number (12). |
| (b) | Resident of Delhi or not | `bool` | Represents `True` or `False`. |
| (c) | Mobile number | `str` | An identifier that may contain a leading zero or country code. |
| (d) | Pocket money | `float` | Can contain decimal values. |
| (e) | Volume of a sphere | `float` | Can contain fractional values. |
| (f) | Perimeter of a square | `float` | Can contain fractional values. |
| (g) | Name of the student | `str` | Contains characters. |
| (h) | Address of the student | `str` | Contains text, numbers, spaces, and possibly special characters. |

## Complete Practical Program

```python
# Question 2: Assignment Statements

length = 10
breadth = 20
sum = (length + breadth) / 2

stationery = ['Paper', 'Gel Pen', 'Eraser']

first = 'Mohandas'
middle = 'Karamchand'
last = 'Gandhi'

fullname = first + ' ' + middle + ' ' + last

print("Average:", sum)
print("Stationery:", stationery)
print("Full Name:", fullname)

# Question 3: Data Types

months = 12
is_resident = True
mobile_number = "09876543210"
pocket_money = 250.50
volume = 125.75
perimeter = 20.5
student_name = "Rahul"
address = "House 12, Bengaluru"

print(type(months))
print(type(is_resident))
print(type(mobile_number))
print(type(pocket_money))
print(type(student_name))
print(type(address))
```


