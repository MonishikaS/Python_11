# Day 05 – Predict the Output
## Python: Conditional Statements and Loops

**Instructions:**
- Predict the exact output of each program without running it.
- Show the working or dry run for each question.
- Pay attention to indentation, conditions, and the number of iterations.

---

## Level 1: Easy (5 Questions)

### Q1. Simple `if-else`

```python
x = 5

if x > 3:
    print("Yes")
else:
    print("No")
```

### Q2. `for` Loop

```python
for i in range(1, 5):
    print(i)
```

### Q3. `while` Loop

```python
i = 1

while i <= 3:
    print(i)
    i = i + 1
```

### Q4. Even or Odd

```python
num = 8

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Q5. Adding Numbers

```python
total = 0

for i in range(1, 4):
    total = total + i

print(total)
```

---

## Level 2: Medium (5 Questions)

### Q6. `if-elif-else`

```python
marks = 75

if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")
```

### Q7. `range()` with a Step

```python
for i in range(2, 11, 3):
    print(i)
```

### Q8. Updating a Variable

```python
x = 2

for i in range(3):
    x = x + 2

print(x)
```

### Q9. `while` Loop with a Condition

```python
i = 2

while i < 10:
    print(i)
    i = i + 3
```

### Q10. Nested `if`

```python
age = 20
has_id = False

if age >= 18:
    if has_id:
        print("Allowed")
    else:
        print("ID required")
else:
    print("Not allowed")
```

---

## Level 3: Hard (5 Questions)

### Q11. `break` Statement

```python
for i in range(1, 8):
    if i == 5:
        break
    print(i)
```

### Q12. `continue` Statement

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### Q13. `while` Loop with `if`

```python
i = 0
total = 0

while i < 8:
    if i % 2 == 0:
        total = total + i
    i = i + 2

print(total)
```

### Q14. Nested Loops

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```

### Q15. Combined Conditions and Loops

```python
total = 0

for i in range(1, 6):
    if i % 2 != 0:
        total = total + i
    else:
        total = total - 1

print(total)
```

---
```python
# Day 05 - Python Practice Questions
# Class XI | Spyder 3
# Solve each question independently.

# ==========================================
# PART A: CONDITIONAL STATEMENTS (3 QUESTIONS)
# ==========================================

# Q1. Even or Odd
# Accept an integer from the user.
# Check whether the number is even or odd.
# Display an appropriate message.


# Q2. Greatest of Three Numbers
# Accept three numbers from the user.
# Use if-elif-else to find and display
# the greatest number.


# Q3. Grade Calculator
# Accept marks out of 100.
# Display the grade according to these rules:
# 90 and above  -> Grade A
# 75 to 89      -> Grade B
# 50 to 74      -> Grade C
# Below 50      -> Grade D
# Also display "Invalid marks" if marks are
# below 0 or above 100.


# ==========================================
# PART B: LOOPS (3 QUESTIONS)
# ==========================================

# Q4. Print Numbers
# Use a for loop to print numbers from 1 to 20.


# Q5. Multiplication Table
# Accept a number from the user.
# Use a for loop to print its multiplication
# table from 1 to 10.


# Q6. Sum of Natural Numbers
# Accept a positive integer n from the user.
# Use a while loop to calculate and display
# the sum of numbers from 1 to n.
```

