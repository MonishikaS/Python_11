# Day 05 – Assignment
## Conditional Statements and Loops in Python

### Q1. Conditional Statements

Write Python programs for the following:

1. Check whether a number is positive, negative, or zero.
2. Check whether a number is even or odd.
3. Accept a person's age and check whether they are eligible to vote.
4. Accept marks and display a grade using `if-elif-else`.
5. Find the greater of two numbers.
6. Find the greatest of three numbers.
7. Check whether a year is a leap year.
8. Accept a username and password and check whether both match predefined values.
9. Check whether a number is divisible by both 3 and 5.
10. Use a nested `if` statement to check age eligibility and whether the person has an ID card.

### Q2. Predict the Output

Write the output without running the programs.

**1.**
```python
x = 8

if x > 5:
    print("A")
else:
    print("B")
```

**2.**
```python
for i in range(1, 5):
    print(i)
```

**3.**
```python
for i in range(2, 11, 2):
    print(i)
```

**4.**
```python
i = 1

while i <= 3:
    print(i)
    i += 1
```

**5.**
```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

**6.**
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### Q3. For Loop Practice

Write programs to:

1. Print numbers from 1 to 20.
2. Print numbers from 20 to 1.
3. Print all even numbers from 1 to 50.
4. Print all odd numbers from 1 to 30.
5. Display the multiplication table of a number entered by the user.
6. Calculate the sum of numbers from 1 to 100.
7. Calculate the factorial of a positive integer.
8. Count how many numbers from 1 to 100 are divisible by 7.

### Q4. While Loop Practice

Write programs to:

1. Print numbers from 1 to 10 using a `while` loop.
2. Print numbers from 10 to 1.
3. Calculate the sum of the first `n` natural numbers.
4. Keep asking the user to enter a number until they enter 0.
5. Count the number of digits in a positive integer.
6. Reverse the digits of a positive integer.

### Q5. Understand Loop Control

1. Explain the difference between `break` and `continue`.
2. What is the purpose of the `pass` statement?
3. Write a program that stops printing when the loop reaches 6.
4. Write a program that prints numbers from 1 to 10 but skips 5.
5. Explain what an infinite loop is and how it can occur.

### Q6. Challenge Questions

1. Print this pattern using nested loops:
   ```text
   *
   * *
   * * *
   * * * *
   * * * * *
   ```

2. Print all numbers between 1 and 100 that are divisible by both 3 and 5.

3. Create a number-guessing program that keeps asking the user to guess a fixed number until they guess correctly.

4. Create a simple menu-driven calculator that performs addition, subtraction, multiplication, or division based on the user's choice.

### Instructions

- Write each program in a Python file.
- Predict the output before executing each program.
- Use proper indentation.
- For loop questions, identify the starting value, stopping condition, and update where applicable.
