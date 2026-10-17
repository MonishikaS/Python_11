# Day 03 — Assignment
## Variables, Data Types, Mutability and Operators

### Learning Objectives

- Practise variables and assignment statements.
- Identify Python data types.
- Understand mutable and immutable objects.
- Apply Python operators.
- Predict program outputs without running the code.

---

## Part A: Theory Questions

1. What is a variable in Python?
2. Explain assignment and reassignment with examples.
3. What is multiple assignment? Give an example.
4. What is dynamic typing?
5. What is the purpose of the `type()` function?
6. Differentiate between `int`, `float`, `str`, and `bool`.
7. What is the difference between a list and a tuple?
8. Explain mutable and immutable objects with two examples of each.
9. What is the difference between `=` and `==`?
10. Differentiate between `==` and `is`.
11. What are membership operators? Give examples.
12. Explain arithmetic, comparison, logical, and assignment operators.

## Part B: Identify Data Types

Write the data type of each value.

1. `25`
2. `3.14`
3. `"Hello"`
4. `False`
5. `[10, 20, 30]`
6. `(10, 20, 30)`
7. `{1, 2, 3}`
8. `{"name": "Rahul"}`
9. `None`

## Part C: Predict the Output

**Instructions:** Predict the output before executing each program.

### Question 1: Reassignment

```python
x = 5
x = 15
x += 5

print(x)
```

### Question 2: Multiple Assignment

```python
a, b, c = 2, 4, 6

print(a + b + c)
```

### Question 3: Arithmetic Operators

```python
a = 17
b = 5

print(a // b)
print(a % b)
print(a ** 2)
```

### Question 4: Assignment Operators

```python
x = 10
x += 5
x *= 2
x -= 4

print(x)
```

### Question 5: Comparison Operators

```python
a = 10
b = 20

print(a < b)
print(a == b)
print(a != b)
```

### Question 6: Mutable List

```python
a = [1, 2, 3]
b = a

b[1] = 50

print(a)
print(b)
```

### Question 7: Immutable Integer

```python
a = 10
b = a

b = 50

print(a)
print(b)
```

### Question 8: Logical Operators

```python
a = True
b = False

print(a and b)
print(a or b)
print(not a)
```

### Question 9: Membership Operators

```python
numbers = [10, 20, 30]

print(20 in numbers)
print(40 not in numbers)
```

### Question 10: Identity and Equality

```python
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
print(a == c)
```

---

## Part D: Coding Exercises

### Exercise 1: Personal Information

Create variables for your name, age, class, and favourite subject. Print each value and its data type.

### Exercise 2: Swap Two Variables

Create two variables:

- `a = 50`
- `b = 100`

Swap their values without creating a third variable.

### Exercise 3: Data Type Explorer

Create variables containing an integer, float, string, Boolean, list, tuple, set, and dictionary. Print each variable's value and type.

### Exercise 4: Mutable List

Create a list containing five numbers. Change the second element and print the modified list.

### Exercise 5: Student Marks Calculator

Store marks for five subjects. Calculate and display:

- Total marks
- Average marks
- Whether the average is at least 40

### Exercise 6: Arithmetic Calculator

Store two numbers and display their sum, difference, product, quotient, floor division, remainder, and exponentiation.

### Exercise 7: Shopping Discount

A product costs ₹2,000. Calculate the discount amount and final price after a 15% discount.

### Exercise 8: Membership Checker

Create a list of five favourite games. Check whether a particular game is present using `in` and `not in`.

### Exercise 9: Type Conversion

Create a variable containing `"25"` as a string. Convert it to an integer, add 10, and print the result.

### Exercise 10: Mutable vs. Immutable

1. Create a list and assign it to another variable.
2. Modify the list using the second variable.
3. Print both variables.
4. Repeat the experiment using an integer.
5. Explain why the outputs differ.

---

## Part E: Challenge Questions

### Challenge 1: Output Detective

Predict the output and explain why.

```python
x = 5
y = x

x = x + 10
y = y + 20

print(x)
print(y)
```

### Challenge 2: Operator Puzzle

Predict the output.

```python
a = 2
b = 3
c = 4

print(a + b * c)
print((a + b) * c)
```

### Challenge 3: List References

Predict the output and explain the relationship between the variables.

```python
first = [10, 20]
second = first

first.append(30)

print(first)
print(second)
```

### Challenge 4: Student Report Mini Project

Write a program that:

1. Stores a student's name and marks in three subjects.
2. Calculates total and average marks.
3. Displays the student's details.
4. Checks whether the average is at least 40.
5. Prints an appropriate result message.

### Challenge 5: Shopping Bill Mini Project

Write a program that stores the prices of three products, calculates the total, applies a 10% discount, and displays the final bill.

---

## Submission Instructions

1. Answer all theory questions.
2. Predict the output before running the programs.
3. Write and test the coding exercises in Spyder.
4. Save your answers in `solutions.py`.
5. Upload your completed work to GitHub.

**Important:** Do not copy the examples directly. Try to solve each question independently and explain the reasoning behind your output.
