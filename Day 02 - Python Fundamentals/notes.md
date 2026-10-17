# Day 02 — Python Fundamentals

## 1. Python Character Set

A **character set** is a collection of characters used to write a Python program.

The main categories are:

### 1.1 Alphabets
Python supports uppercase and lowercase letters.

- Uppercase letters: `A–Z`
- Lowercase letters: `a–z`

Example:

```python
name = "Rahul"
print(name)
```

### 1.2 Digits

Python uses digits from `0` to `9` to represent numerical values.

```python
age = 16
print(age)
```

### 1.3 Special Symbols

Special symbols are used to perform operations and organize code.

Examples:

`+`, `-`, `*`, `/`, `=`, `()`, `[]`, `{}`, `:`, `,`, `#`, `_`

Example:

```python
total = 10 + 20
print(total)
```

Output:

```text
30
```

### 1.4 Whitespace Characters

Whitespace characters include spaces, tabs, and newlines. They help separate and organize code.

Example:

```python
name = "Rahul"
age = 16

print(name)
print(age)
```

**Important:** Python is case-sensitive. This means uppercase and lowercase letters are treated differently.

```python
name = "Rahul"
Name = "Aman"

print(name)
print(Name)
```

Output:

```text
Rahul
Aman
```

Here, `name` and `Name` are two different variables.

---

## 2. Python Tokens

A **token** is the smallest meaningful unit of a Python program.

Python tokens are commonly classified into five categories:

1. Keywords
2. Identifiers
3. Literals
4. Operators
5. Punctuators

## 2.1 Keywords

Keywords are reserved words that have predefined meanings in Python. They cannot be used as ordinary variable names.

Examples:

`if`, `else`, `for`, `while`, `True`, `False`, `and`, `or`, `def`

Example:

```python
if 10 > 5:
    print("Ten is greater")
```

Output:

```text
Ten is greater
```

Here, `if` is a keyword.

## 2.2 Identifiers

Identifiers are names given to variables, functions, classes, and other program elements.

Example:

```python
student_name = "Riya"
marks = 95

print(student_name)
print(marks)
```

Here, `student_name` and `marks` are identifiers.

### Rules for Naming Identifiers

- An identifier can contain letters, digits, and underscores.
- It cannot start with a digit.
- It cannot contain spaces.
- It cannot be a Python keyword.
- Identifiers are case-sensitive.

**Valid identifiers:**

```python
name = "Aman"
student_age = 16
marks1 = 90
_total = 100
```

**Invalid identifiers:**

```python
# 1name = "Aman"      # Cannot start with a digit
# student age = 16    # Cannot contain spaces
# for = 10            # Cannot use a keyword
```

The invalid examples are written as comments so that the file remains executable.

## 2.3 Literals

Literals are fixed values written directly in a program.

Example:

```python
age = 16
price = 99.5
language = "Python"
passed = True
```

The literals are `16`, `99.5`, `"Python"`, and `True`.

### Types of Literals

| Type | Examples |
|---|---|
| Integer | `10`, `25`, `-5` |
| Floating-point | `3.14`, `99.5` |
| String | `"Hello"`, `'Python'` |
| Boolean | `True`, `False` |
| Special | `None` |

## 2.4 Operators

Operators are symbols or words used to perform operations on values and variables.

### A. Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `10 + 5` gives `15` |
| `-` | Subtraction | `10 - 5` gives `5` |
| `*` | Multiplication | `10 * 5` gives `50` |
| `/` | Division | `10 / 5` gives `2.0` |
| `//` | Floor division | `17 // 5` gives `3` |
| `%` | Modulus (remainder) | `17 % 5` gives `2` |
| `**` | Exponentiation | `2 ** 3` gives `8` |

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

### B. Comparison Operators

Comparison operators compare two values and return a Boolean result: `True` or `False`.

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
a = 20
b = 10

print(a > b)
print(a == b)
print(a != b)
```

Output:

```text
True
False
True
```

### C. Assignment Operators

Assignment operators assign or update variable values.

| Operator | Example | Equivalent operation |
|---|---|---|
| `=` | `x = 10` | Assign 10 to `x` |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 2` | `x = x * 2` |
| `/=` | `x /= 2` | `x = x / 2` |

Example:

```python
score = 10
score += 5

print(score)
```

Output:

```text
15
```

**Remember:** `=` assigns a value, while `==` compares two values.

### D. Logical Operators

Logical operators combine or reverse conditions.

| Operator | Meaning |
|---|---|
| `and` | True when both conditions are true |
| `or` | True when at least one condition is true |
| `not` | Reverses a Boolean result |

Example:

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

## 2.5 Punctuators

Punctuators are symbols that help separate or organize parts of a Python program.

Examples include:

- `()` — parentheses
- `[]` — square brackets
- `{}` — curly braces
- `:` — colon
- `,` — comma
- `.` — period

Example:

```python
marks = [90, 85, 95]
print(marks)
```

Output:

```text
[90, 85, 95]
```

Here, square brackets enclose the list, and commas separate its elements.

---

## 3. Identifying Tokens in a Python Program

Consider the following program:

```python
marks = 90

if marks >= 40:
    print("Pass")
```

| Token | Category |
|---|---|
| `marks` | Identifier |
| `=` | Assignment operator |
| `90` | Integer literal |
| `if` | Keyword |
| `>=` | Comparison operator |
| `40` | Integer literal |
| `:` | Punctuator |
| `print` | Built-in function name |
| `"Pass"` | String literal |
| `()` | Punctuators |

Output:

```text
Pass
```

**Note:** `print()` is a built-in function, not a keyword.

---

## 4. Quick Revision

- A character set contains characters used to write programs.
- Python is case-sensitive.
- A token is the smallest meaningful unit of a program.
- Keywords have predefined meanings.
- Identifiers are names given to program elements.
- Literals are fixed values written directly in code.
- Operators perform operations on values.
- Punctuators help organize code.

## 5. Key Takeaways

After completing this lesson, a student should be able to:

1. Explain the Python character set.
2. Identify the five categories of Python tokens.
3. Distinguish between keywords, identifiers, literals, operators, and punctuators.
4. Follow the rules for naming identifiers.
5. Recognize arithmetic, comparison, assignment, and logical operators.
6. Identify different tokens in a Python program.

---

**Next Topic:** Section 3.4 — Barebones of a Python Program, followed by Section 3.5 — Variables and Assignments.
