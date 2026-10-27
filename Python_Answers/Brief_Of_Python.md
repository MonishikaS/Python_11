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

## 4. Give the output of the following

Given: `num1 = 4`, `num2 = 3`, `num3 = 2`

**a) `num1 += num2 + num3`**

```python
num1 = 4
num2 = 3
num3 = 2
num1 += num2 + num3
```

Output/value: `num1 = 9`

**b) `print(num1)`**

Output:
```text
9
```

**c) `num1 = num1 ** (num2 + num3)`**

Calculation: `9 ** (3 + 2) = 9 ** 5`

Value: `59049`

**d) `print(num1)`**

Output:
```text
59049
```

**e) `num1 **= num2 + c`**

**Error:** `NameError`, because variable `c` has not been defined.

**f) `num1 = '5' + '5'`**

**g) `print(num1)`**

Output:
```text
55
```

Explanation: Both values are strings, so `+` joins them instead of adding them numerically.

**h) `print(4.00/(2.0+2.0))`**

Output:
```text
1.0
```

**i) `num1 = 2+9*((3*12)-8)/10`**

Calculation:

- `3 * 12 = 36`
- `36 - 8 = 28`
- `9 * 28 = 252`
- `252 / 10 = 25.2`
- `2 + 25.2 = 27.2`

**j) `print(num1)`**

Output:
```text
27.2
```

**k) `num1 = float(10)`**

**l) `print(num1)`**

Output:
```text
10.0
```

**m) `num1 = int('3.14')`**

**Error:** `ValueError`, because the string `'3.14'` cannot be directly converted into an integer using `int()`.

**n) `print(num1)`**

This statement is not executed if the previous statement raises an error and the program is not handling it.

**o) `print(10 != 9 and 20 >= 20)`**

Output:
```text
True
```

Explanation: Both conditions are true.

**p) `print(5 % 10 + 10 < 50 and 29 <= 29)`**

Output:
```text
True
```

Explanation:

- `5 % 10 = 5`
- `5 + 10 = 15`
- `15 < 50` is `True`
- `29 <= 29` is `True`
- `True and True` gives `True`

**Note:** The questions are treated as separate code snippets where appropriate. If all statements are executed sequentially in one program, earlier errors will stop execution unless handled.

---

## 5. Categorise the following errors

### a) `25 / 0`

**Answer:** Runtime error (`ZeroDivisionError`).

Explanation: Division by zero is not allowed in Python.

### b) `num1 = 25; num2 = 0; num1/num2`

**Answer:** Runtime error (`ZeroDivisionError`).

Explanation: The variables are assigned correctly, but dividing `num1` by `num2` causes an error because `num2` is zero.

---

## 6. Program to calculate simple interest and amount payable

```python
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time in years: "))

SI = (P * R * T) / 100
amount = P + SI

print("Simple Interest =", SI)
print("Amount Payable =", amount)
```

**Formula:**

- Simple Interest = (P × R × T) / 100
- Amount Payable = Principal + Simple Interest

---

## 7. Program to repeat "GOOD MORNING" n times

```python
n = int(input("Enter the number of times: "))

print("GOOD MORNING " * n)
```

**Example output:**

```text
Enter the number of times: 3
GOOD MORNING GOOD MORNING GOOD MORNING
```

---

## 8. Program to find the average of three numbers

```python
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

average = (a + b + c) / 3

print("Average =", average)
```

---

## 9. Program to find the year in which the user turns 100

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = 2026
year = current_year + (100 - age)

print(name, "will turn 100 years old in", year)
```

**Example output:**

```text
Enter your name: Rahul
Enter your age: 16
Rahul will turn 100 years old in 2110
```

**Note:** This solution assumes the user's age is their current age in 2026. The exact year may depend on whether their birthday has already occurred this year.

---

## 10. Difference between `else` and `elif`

| `else` | `elif` |
|---|---|
| Means "otherwise". | Means "else if". |
| Does not contain a condition. | Contains a condition. |
| Executes when all preceding `if` and `elif` conditions are false. | Checks another condition if the preceding conditions are false. |
| Only one `else` is allowed in an `if` statement chain. | Multiple `elif` blocks can be used. |

**Example:**

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

Output:
```text
Grade B
```

---

## 11. Find the output of the following program segments

### a)

```python
for i in range(20, 30, 2):
    print(i)
```

**Output:**

```text
20
22
24
26
28
```

Explanation: The loop starts at 20, increases by 2, and stops before 30.

### b)

```python
country = 'INDIA'

for i in country:
    print(i)
```

**Output:**

```text
I
N
D
I
A
```

Explanation: The loop accesses and prints each character of the string individually.

### c)

```python
i = 0
sum = 0

while i < 9:
    if i % 4 == 0:
        sum = sum + i
    i = i + 2

print(sum)
```

**Output:**

```text
12
```

**Explanation:**

The values of `i` are `0, 2, 4, 6, 8`.

The condition `i % 4 == 0` is true for `0`, `4`, and `8`.

Therefore:

`sum = 0 + 4 + 8 = 12`

Final output: `12`



