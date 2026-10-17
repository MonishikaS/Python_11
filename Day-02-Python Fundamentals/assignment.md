# Day 02 — Python Fundamentals Assignment

## Objective

Practise Python character sets, tokens, identifiers, literals, and operators.

## Part A: Theory Questions

1. What is a character set in Python?
2. Name the four main categories of characters used in Python.
3. Why is Python called a case-sensitive language?
4. What is a token? Name its five main categories.
5. What are keywords? Write any five examples.
6. What are identifiers? Explain the rules for naming identifiers.
7. What are literals? Give four examples.
8. What are operators? Explain any four arithmetic operators.
9. Differentiate between `=` and `==`.
10. What are punctuators? Give four examples.

## Part B: Identify Valid and Invalid Identifiers

For each identifier, write **Valid** or **Invalid**. If invalid, explain why.

1. `student_name`
2. `2marks`
3. `total_marks`
4. `student age`
5. `for`
6. `_score`
7. `name1`
8. `my-name`
9. `Age`
10. `class`

## Part C: Predict the Output

Predict the output before running each program.

### Question 1
```python
x = 10
X = 20

print(x)
print(X)
```

### Question 2
```python
a = 17
b = 5

print(a // b)
print(a % b)
```

### Question 3
```python
score = 10
score += 5
score *= 2

print(score)
```

### Question 4
```python
a = 10
b = 20

print(a > b)
print(a == b)
print(a != b)
```

### Question 5
```python
age = 17
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)
```

### Question 6
```python
x = 2
y = 3

print(x ** y)
print(x * y)
```

## Part D: Coding Exercises

### Exercise 1: Student Introduction
Create variables for your name, age, class, and favourite subject. Print all four values.

### Exercise 2: Arithmetic Calculator
Store two numbers in variables and display their:
- Sum
- Difference
- Product
- Quotient
- Floor division
- Remainder

### Exercise 3: Rectangle Calculator
Store the length and breadth of a rectangle. Calculate its area and perimeter.

Formulae:
- Area = length × breadth
- Perimeter = 2 × (length + breadth)

### Exercise 4: Temperature Converter
Store a temperature in Celsius and convert it to Fahrenheit.

Formula:

Fahrenheit = (Celsius × 9/5) + 32

### Exercise 5: Student Marks
Store marks for three subjects. Calculate and print the total and average marks.

### Exercise 6: Discount Calculator
A product costs ₹1,500. Calculate the discount amount and final price after applying a 10% discount.

Formulae:
- Discount = Price × Discount Percentage / 100
- Final Price = Price − Discount

### Exercise 7: Token Identification
Identify the keywords, identifiers, literals, operators, and punctuators in the following program.

```python
marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

## Part E: Challenge Questions

### Challenge 1: Swap Two Variables
Create two variables, `a = 10` and `b = 20`. Swap their values without assigning the numbers again, then print both variables.

### Challenge 2: Shopping Bill
Store the prices of three products. Calculate the total bill, apply a 10% discount, and print the final amount.

### Challenge 3: Output Detective
Without running the code, predict the output and explain why.

```python
a = 5
b = 2

a += b
b *= a

print(a)
print(b)
```

