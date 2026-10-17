# Day 03 — Variables, Data Types, Mutability and Operators

## Learning Objectives

By the end of this lesson, you should be able to:

- Understand variables and assignment statements.
- Identify Python's basic data types.
- Explain mutable and immutable objects.
- Use arithmetic, comparison, logical, assignment, membership, and identity operators.
- Predict the output of simple Python programs.

---

## 1. Variables and Assignments

### What is a variable?

A variable is a name that refers to a value in a Python program.

```python
name = "Rahul"
age = 16
marks = 92.5
```

Here, `name`, `age`, and `marks` are variable names.

### Assignment operator (`=`)

The `=` operator assigns a value to a variable.

```python
x = 10
print(x)
```

Output:

```text
10
```

### Reassigning a variable

A variable can refer to a new value later.

```python
x = 10
x = 25

print(x)
```

Output:

```text
25
```

### Multiple assignment

Different values can be assigned to multiple variables in one statement.

```python
a, b, c = 10, 20, 30
print(a, b, c)
```

Output:

```text
10 20 30
```

The same value can also be assigned to multiple variables.

```python
x = y = z = 100
print(x, y, z)
```

Output:

```text
100 100 100
```

### Swapping variables

Python allows two values to be swapped without a temporary variable.

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

---

## 2. Python Data Types

A data type describes the kind of value an object represents.

The built-in `type()` function helps identify a value's type.

### 2.1 Integer (`int`)

Integers are whole numbers without a decimal point.

Examples: `10`, `-5`, `0`

```python
age = 16
print(age)
print(type(age))
```

Output:

```text
16
<class 'int'>
```

### 2.2 Floating-point (`float`)

Floating-point numbers represent numbers with a decimal component.

Examples: `3.14`, `99.5`, `-2.5`

```python
price = 99.5
print(type(price))
```

Output:

```text
<class 'float'>
```

### 2.3 String (`str`)

A string is a sequence of characters enclosed in quotes.

```python
name = "Python"
print(name)
print(type(name))
```

Output:

```text
Python
<class 'str'>
```

Both single quotes and double quotes can be used to create strings.

### 2.4 Boolean (`bool`)

Boolean values represent truth values: `True` and `False`.

```python
is_student = True
is_adult = False

print(type(is_student))
```

Output:

```text
<class 'bool'>
```

Remember that Python uses capital letters in `True` and `False`.

### 2.5 List (`list`)

A list stores multiple items in a single ordered collection.

```python
marks = [80, 90, 95]
print(marks)
print(type(marks))
```

Output:

```text
[80, 90, 95]
<class 'list'>
```

### 2.6 Tuple (`tuple`)

A tuple stores multiple items in an ordered collection.

```python
coordinates = (10, 20)
print(coordinates)
print(type(coordinates))
```

Output:

```text
(10, 20)
<class 'tuple'>
```

### 2.7 Set (`set`)

A set stores unique elements. It does not guarantee a particular display order.

```python
numbers = {1, 2, 3, 3}
print(numbers)
print(type(numbers))
```

Output contains each unique value once:

```text
{1, 2, 3}
```

### 2.8 Dictionary (`dict`)

A dictionary stores data as key-value pairs.

```python
student = {
    "name": "Rahul",
    "age": 16
}

print(student["name"])
print(type(student))
```

Output:

```text
Rahul
<class 'dict'>
```

### 2.9 None (`NoneType`)

`None` represents the absence of a value.

```python
result = None
print(result)
print(type(result))
```

Output:

```text
None
<class 'NoneType'>
```

### Data types at a glance

| Data type | Example | Mutable? |
|---|---|---|
| `int` | `10` | No |
| `float` | `3.14` | No |
| `str` | `"Hello"` | No |
| `bool` | `True` | No |
| `list` | `[1, 2, 3]` | Yes |
| `tuple` | `(1, 2, 3)` | No |
| `set` | `{1, 2, 3}` | Yes |
| `dict` | `{"a": 1}` | Yes |

---

## 3. Mutable and Immutable Objects

This is an important Python concept.

### What does mutable mean?

A mutable object can be changed after it is created.

Examples include lists, dictionaries, and sets.

```python
numbers = [10, 20, 30]
numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

The existing list was modified.

### What does immutable mean?

An immutable object cannot be changed after it is created. An operation that appears to change its value creates a new value or object instead.

Examples include integers, floats, strings, booleans, and tuples.

```python
name = "Python"
name = name + " Programming"

print(name)
```

Output:

```text
Python Programming
```

The original string was not modified in place. The variable was assigned a new string.

### Example: Mutable list

```python
a = [1, 2, 3]
b = a

b[0] = 100

print(a)
print(b)
```

Output:

```text
[100, 2, 3]
[100, 2, 3]
```

Why? Both `a` and `b` refer to the same list object.

### Example: Immutable integer

```python
a = 10
b = a

b = 20

print(a)
print(b)
```

Output:

```text
10
20
```

Why? Assigning `20` to `b` does not change the value referred to by `a`.

**Important:** Mutable and immutable describe objects, not simply whether a variable name can be reassigned. A variable can be reassigned whether it refers to a mutable or immutable object.

---

## 4. Python Operators

Operators perform operations on values and variables.

### 4.1 Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | Approximately `3.333` |
| `//` | Floor division | `10 // 3` | `3` |
| `%` | Remainder | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### 4.2 Comparison operators

Comparison operators compare values and return `True` or `False`.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Example:

```python
a = 10
b = 20

print(a < b)
print(a == b)
print(a != b)
```

Output:

```text
True
False
True
```

### 4.3 Assignment operators

Assignment operators assign or update variable values.

| Operator | Example | Equivalent expression |
|---|---|---|
| `=` | `x = 10` | Assign 10 to `x` |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 2` | `x = x * 2` |
| `/=` | `x /= 2` | `x = x / 2` |
| `//=` | `x //= 2` | `x = x // 2` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 2` | `x = x ** 2` |

### 4.4 Logical operators

Logical operators combine or reverse conditions.

- `and`: True when both conditions are true.
- `or`: True when at least one condition is true.
- `not`: Reverses a truth value.

```python
age = 17
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)
```

Output:

```text
False
True
False
```

### 4.5 Membership operators

Membership operators check whether an item exists in a collection or sequence.

- `in`
- `not in`

```python
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("grapes" not in fruits)
```

Output:

```text
True
True
```

### 4.6 Identity operators

Identity operators check whether two references point to the same object.

- `is`
- `is not`

```python
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
print(a == c)
```

Output:

```text
True
False
True
```

Explanation:

- `a is b` is `True` because both refer to the same list object.
- `a is c` is `False` because `c` is a separate list object.
- `a == c` is `True` because their contents are equal.

**Remember:** `==` compares values for equality, while `is` checks object identity. Use `is None` when checking whether a value is `None`.

---

## 5. Type Conversion

Type conversion changes a value from one data type to another when the conversion is supported.

```python
age = "16"

age = int(age)

print(age)
print(type(age))
```

Output:

```text
16
<class 'int'>
```

Common conversion functions:

- `int()` — converts a compatible value to an integer.
- `float()` — converts a compatible value to a float.
- `str()` — converts a value to a string.
- `bool()` — converts a value to a Boolean.

Example:

```python
number = 10
text = str(number)

print(text)
print(type(text))
```

Output:

```text
10
<class 'str'>
```

Note: Not every conversion is valid. For example, `int("hello")` raises a `ValueError`.

---

## 6. Quick Revision

1. A variable is a name that refers to a value.
2. `=` is the assignment operator.
3. `type()` identifies the type of an object.
4. Lists, dictionaries, and sets are mutable.
5. Integers, floats, strings, booleans, and tuples are immutable.
6. Arithmetic operators perform mathematical calculations.
7. Comparison operators return Boolean results.
8. Logical operators combine or reverse conditions.
9. Membership operators check for an item's presence.
10. Identity operators check whether references point to the same object.

## 7. Mini Project: Student Marks Calculator

```python
name = "Rahul"
maths = 85
science = 90
english = 80

total = maths + science + english
average = total / 3

print("Student:", name)
print("Total marks:", total)
print("Average marks:", average)
```

Output:

```text
Student: Rahul
Total marks: 255
Average marks: 85.0
```
