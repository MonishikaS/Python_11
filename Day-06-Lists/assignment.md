# Day 06 Assignment: Python Lists

## Instructions

- Solve the questions in Spyder.
- For output-prediction questions, predict the output before running the code.
- Do not directly copy the examples.
- Use only the concepts taught in today's lesson.

---

# Part A: Easy Questions (5)

## Q1. Predict the Output

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(len(numbers))
```

## Q2. Predict the Output

```python
fruits = ["Apple", "Mango", "Banana"]

fruits[1] = "Orange"

print(fruits)
```

## Q3. Create a List

Create a list named `hobbies` containing five hobbies.

Print:
1. The complete list.
2. The first element.
3. The last element.
4. The total number of elements.

## Q4. Membership Operators

Given:

```python
subjects = ["English", "Maths", "IP", "Physics"]
```

Write statements to check whether:
1. `"IP"` is present in the list.
2. `"Biology"` is present in the list.
3. `"Chemistry"` is absent from the list.

## Q5. Predict the Output

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
print(numbers[:3])
print(numbers[::2])
print(numbers[::-1])
```

---

# Part B: Medium Questions (5)

## Q6. Difference Between append() and extend()

Predict the output and explain the difference.

```python
a = [1, 2, 3]
a.append([4, 5])
print(a)

b = [1, 2, 3]
b.extend([4, 5])
print(b)
```

## Q7. List Manipulation

Start with:

```python
numbers = [15, 5, 20, 10, 5]
```

Perform the following operations in order:

1. Append `25`.
2. Insert `12` at index `2`.
3. Count the occurrences of `5`.
4. Remove the first occurrence of `5`.
5. Print the final list.

## Q8. Traverse a List

Given:

```python
marks = [45, 82, 67, 90, 76]
```

Use a `for` loop to print only marks greater than or equal to `75`.

## Q9. Calculate Total and Average

Write a program that:

1. Accepts marks for five subjects from the user.
2. Stores the marks in a list.
3. Prints the list.
4. Calculates the total marks.
5. Calculates the average marks.
6. Displays the highest mark.

## Q10. Separate Even and Odd Numbers

Given:

```python
numbers = [11, 24, 7, 18, 30, 9, 42]
```

Create two new lists:
- `even_numbers`
- `odd_numbers`

Store the appropriate numbers in each list using a loop and an `if-else` statement. Print all three lists.

---

# Part C: Hard Questions (5)

## Q11. Predict the Output

```python
numbers = [12, 5, 8, 3]

a = sorted(numbers)
numbers.sort(reverse=True)

print(a)
print(numbers)
print(numbers[1:3])
```

Explain the difference between `sort()` and `sorted()`.

## Q12. Search for an Element

Write a program that:

1. Accepts five integers from the user.
2. Stores them in a list.
3. Asks the user for a number to search for.
4. Prints the index if the number is present.
5. Prints `"Number not found"` otherwise.

**Hint:** Use a loop or the `in` operator.

## Q13. Find the Largest and Smallest

Write a program that accepts six numbers from the user and stores them in a list.

Display:
1. The complete list.
2. The largest number.
3. The smallest number.
4. The sum of all numbers.
5. The average of the numbers.

Use `max()`, `min()`, `sum()` and `len()`.


## Q14. Student Marks Analyser

Write a program that asks the user how many students' marks they want to enter.

Store all the marks in a list and display:

1. All the marks.
2. The highest mark.
3. The lowest mark.
4. The total and average marks.
5. The number of students who scored at least `80`.
6. All the marks in descending order.

Use lists, loops, conditions and built-in functions.





