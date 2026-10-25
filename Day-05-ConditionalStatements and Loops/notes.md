# Day 05 – Conditional Statements and Loops in Python

## 1. Revision of Conditional Statements

Conditional statements are used to make decisions in a program. They allow Python to execute different blocks of code depending on whether a condition is `True` or `False`.

### Types of Conditional Statements

- **`if` statement:** Executes a block when the condition is true.
- **`if-else` statement:** Selects between two possible blocks depending on the condition.
- **`if-elif-else` statement:** Checks multiple conditions in sequence and executes the block associated with the first true condition.
- **Nested `if` statement:** An `if` statement placed inside another conditional statement.

### Important Rules

- A condition evaluates to either `True` or `False`.
- A colon (`:`) is written after the condition.
- Indentation defines the block of statements belonging to a condition.
- In an `if-elif-else` structure, conditions are checked from top to bottom.
- The `else` block executes when none of the preceding conditions is true.
- A nested conditional is useful when a second decision depends on the first decision.

## 2. Introduction to Loops

A loop is a control structure that repeatedly executes a block of statements.

Loops are useful when the same task needs to be performed multiple times. They reduce code repetition and make programs easier to maintain.

### Why Are Loops Needed?

- To repeat instructions efficiently.
- To process multiple values.
- To perform calculations repeatedly.
- To iterate through a sequence of items.
- To continue performing a task until a condition changes.

## 3. Types of Loops in Python

Python provides two main types of loops:

### A. `for` Loop

A `for` loop is used to iterate over a sequence or other iterable object, such as a string, list, or range of numbers.

**Main characteristics:**

- It processes items one by one.
- It is commonly used when iterating over a sequence.
- The `range()` function is often used when a sequence of integers is needed.
- The loop variable takes the value of each item during iteration.

### B. `while` Loop

A `while` loop repeatedly executes a block of statements as long as its condition remains true.

**Main characteristics:**

- It is controlled by a condition.
- The condition is checked before each iteration.
- The loop may execute zero times if its condition is initially false.
- The condition must eventually become false when the loop is intended to terminate normally.

## 4. The `range()` Function

The `range()` function produces a sequence of integers commonly used with a `for` loop.

It can be used with:

- A stop value.
- A start value and a stop value.
- A start value, stop value, and step value.

**Important rules:**

- The stop value is excluded from the sequence.
- The start value is included when specified.
- The step determines the interval between successive values.
- The step can be positive or negative, but it cannot be zero.

## 5. Loop Control Statements

Python provides statements that change the normal flow of a loop.

### A. `break`

The `break` statement immediately terminates the nearest enclosing loop.

### B. `continue`

The `continue` statement skips the remaining statements in the current iteration and proceeds to the next iteration.

### C. `pass`

The `pass` statement performs no action. It acts as a placeholder where a statement is syntactically required.

## 6. Nested Loops

A nested loop is a loop placed inside another loop.

- The inner loop executes as part of the outer loop.
- Each iteration of the outer loop can trigger a complete execution of the inner loop.
- Nested loops are useful for working with rows and columns, tables, and combinations of values.

## 7. Infinite Loops

An infinite loop is a loop that continues indefinitely because its termination condition is never reached or never becomes false.

- An incorrectly designed `while` loop can become infinite.
- Updating variables involved in a loop condition is often necessary.
- A loop can also be intentionally infinite and terminated using a control statement.

## 8. Difference Between `for` and `while` Loops

| `for` Loop | `while` Loop |
|---|---|
| Iterates over an iterable or sequence. | Repeats while a condition is true. |
| Commonly used to process items or a range of values. | Commonly used when repetition depends on a condition. |
| Often used when the iterable defines the items to process. | Requires attention to the condition and how it changes. |

## 9. Conditional Statements vs Loops

| Conditional Statements | Loops |
|---|---|
| Used to make decisions. | Used to repeat statements. |
| Execute a block based on a condition. | Execute a block over multiple iterations. |
| Include `if`, `elif`, and `else`. | Include `for` and `while`. |

## 10. Quick Revision

- Conditional statements control decision-making.
- `if`, `if-else`, `if-elif-else`, and nested `if` handle different decision structures.
- Loops repeat a block of statements.
- Python has `for` and `while` loops.
- `range()` generates a sequence of integers.
- `break` terminates a loop.
- `continue` skips to the next iteration.
- `pass` acts as a placeholder.
- Nested loops contain one loop inside another.
- Correct loop conditions and updates help prevent unintended infinite loops.
