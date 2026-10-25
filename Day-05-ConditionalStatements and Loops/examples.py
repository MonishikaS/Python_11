```python
# Day 05: Conditional Statements and Loops in Python

# PART A: CONDITIONAL STATEMENTS

# Example 1: Simple if statement
age = 18

if age >= 18:
    print("You are eligible to vote.")


# Example 2: if-else statement
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Example 3: if-elif-else statement
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Needs improvement")


# Example 4: Nested if statement
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry not allowed")


# PART B: FOR LOOP

# Example 5: Print numbers from 1 to 5
for i in range(1, 6):
    print(i)


# Example 6: Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)


# Example 7: Multiplication table
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# Example 8: Sum of numbers from 1 to 5
total = 0

for i in range(1, 6):
    total = total + i

print("Sum =", total)


# PART C: WHILE LOOP

# Example 9: Print numbers from 1 to 5
i = 1

while i <= 5:
    print(i)
    i = i + 1


# Example 10: Countdown
count = 5

while count >= 1:
    print(count)
    count = count - 1

print("Go!")


# PART D: LOOP CONTROL STATEMENTS

# Example 11: break
for i in range(1, 11):
    if i == 5:
        break
    print(i)


# Example 12: continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# Example 13: pass
for i in range(1, 4):
    if i == 2:
        pass
    print(i)


# PART E: NESTED LOOPS

# Example 14: Print a small pattern
for i in range(3):
    for j in range(2):
        print("*", end=" ")
    print()
```
