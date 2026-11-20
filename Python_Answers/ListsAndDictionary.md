# Python Class 11 – Lists and Dictionaries

## Revision Worksheet (NCERT)

**Total Questions:** 40\
**Lists:** 20 Questions\
**Dictionaries:** 20 Questions

---

# PART A – LISTS (20 Questions)

## Section 1: Predict the Output (Q1–Q10)

**Q1.** Predict the output.

```
L = [10, 20, 30, 40, 50]
print(L[2])
print(L[-1])
```

**Q2.** Predict the output.

```
L = [2, 4, 6, 8, 10]
print(L[1:4])
print(L[:3])
```

**Q3.** Predict the output.

```
L = [5, 10, 15]
L.append(20)
print(L)
```

**Q4.** Predict the output.

```
L = [10, 20, 30]
L.insert(1, 15)
print(L)
```

**Q5.** Predict the output.

```
L = [1, 2, 3, 4, 5]
L.remove(3)
print(L)
```

**Q6.** Predict the output.

```
L = [10, 20, 30, 40]
x = L.pop()
print(x)
print(L)
```

**Q7.** Predict the output.

```
L = [4, 2, 8, 1, 6]
L.sort()
print(L)
```

**Q8.** Predict the output.

```
L = [1, 2, 3, 4]
L.reverse()
print(L)
```

**Q9.** Predict the output.

```
L = [10, 20, 10, 30, 10]
print(L.count(10))
print(L.index(30))
```

**Q10.** Predict the output.

```
L = [2, 4, 6]
L.extend([8, 10])
print(L)
print(len(L))
```

## Section 2: Conceptual Questions (Q11–Q15)

**Q11.** What is a list in Python? Give one example.

**Q12.** Differentiate between `append()` and `extend()` with an example.

**Q13.** What is the difference between `remove()` and `pop()`?

**Q14.** Write the output of the following code and explain why.

```
L = [10, 20, 30]
L[1] = 50
print(L)
```

**Q15.** Identify the error in the following code.

```
L = [10, 20, 30]
L.append(40, 50)
print(L)
```

## Section 3: Write Python Programs (Q16–Q20)

**Q16.** Write a Python program to create a list of five numbers and display all elements using a `for` loop.

**Q17.** Write a Python program to find the largest element in a list.

**Q18.** Write a Python program to count the number of even numbers in a list.

**Q19.** Write a Python program to search for an element in a list. Display "Found" if the element exists; otherwise display "Not Found".

**Q20.** Write a Python program to create a list of numbers and calculate the sum and average of its elements.

---

# PART B – DICTIONARIES (20 Questions)

## Section 1: Predict the Output (Q21–Q30)

**Q21.** Predict the output.

```
student = {"name": "Rahul", "age": 16, "class": 11}
print(student["name"])
print(student["age"])
```

**Q22.** Predict the output.

```
D = {"A": 10, "B": 20, "C": 30}
print(D.keys())
```

**Q23.** Predict the output.

```
D = {"A": 10, "B": 20}
print(D.values())
```

**Q24.** Predict the output.

```
D = {"name": "Riya", "age": 17}
D["age"] = 18
print(D)
```

**Q25.** Predict the output.

```
D = {"Maths": 90, "Science": 85}
D["English"] = 88
print(D)
```

**Q26.** Predict the output.

```
D = {"A": 10, "B": 20, "C": 30}
D.pop("B")
print(D)
```

**Q27.** Predict the output.

```
D = {"x": 5, "y": 10, "z": 15}
print(len(D))
print("y" in D)
```

**Q28.** Predict the output.

```
D = {"A": 1, "B": 2, "C": 3}
print(D.get("B"))
print(D.get("D", 0))
```

**Q29.** Predict the output.

```
D = {"apple": 10, "mango": 20}
for k in D:
    print(k)
```

**Q30.** Predict the output.

```
D = {"A": 10, "B": 20}
for k, v in D.items():
    print(k, v)
```

## Section 2: Conceptual Questions (Q31–Q35)

**Q31.** What is a dictionary in Python? Give one example.

**Q32.** What is the difference between a list and a dictionary?

**Q33.** What are keys and values in a dictionary? Explain with an example.

**Q34.** What is the difference between `keys()`, `values()` and `items()` methods?

**Q35.** Identify the error in the following code.

```
D = {"name": "Aman", "age": 17}
print(D[0])
```

Explain why the error occurs.

## Section 3: Write Python Programs (Q36–Q40)

**Q36.** Write a Python program to create a dictionary containing the names and marks of three students. Display the dictionary.

**Q37.** Write a Python program to display all keys and values of a dictionary using a `for` loop.

**Q38.** Write a Python program to create a dictionary of five subjects and their marks. Calculate and display the total marks.

**Q39.** Write a Python program to search for a particular key in a dictionary. Display "Key Found" if it exists; otherwise display "Key Not Found".

**Q40.** Write a Python program to create a dictionary of five numbers and find the largest value in the dictionary.

---

# ANSWER KEY

# PART A – LISTS ANSWERS

## Section 1: Output Answers

**A1.**

```
30
50
```

**A2.**

```
[4, 6, 8]
[2, 4, 6]
```

**A3.**

```
[5, 10, 15, 20]
```

**A4.**

```
[10, 15, 20, 30]
```

**A5.**

```
[1, 2, 4, 5]
```

**A6.**

```
40
[10, 20, 30]
```

**A7.**

```
[1, 2, 4, 6, 8]
```

**A8.**

```
[4, 3, 2, 1]
```

**A9.**

```
3
3
```

**A10.**

```
[2, 4, 6, 8, 10]
5
```

## Section 2: Conceptual Answers

**A11.** A list is an ordered and mutable collection of elements. It can store different data types.

Example:

```
L = [10, 20, 30, "Hello"]
```

**A12.**

- `append()` adds one element at the end.
- `extend()` adds multiple elements from another iterable.

```
L = [1, 2]
L.append([3, 4])
print(L)
# [1, 2, [3, 4]]

L = [1, 2]
L.extend([3, 4])
print(L)
# [1, 2, 3, 4]
```

**A13.**

- `remove()` deletes an element by its value.
- `pop()` deletes an element by its index and returns the deleted element. By default, it removes the last element.

**A14.**

```
[10, 50, 30]
```

The element at index 1 is replaced with 50.

**A15.**

Error: `append()` accepts only one argument.

Correct code:

```
L = [10, 20, 30]
L.append(40)
L.append(50)
print(L)
```

## Section 3: Programming Answers

**A16. Display all elements**

```
L = [10, 20, 30, 40, 50]

for i in L:
    print(i)
```

**A17. Find the largest element**

```
L = [10, 45, 20, 80, 30]

largest = L[0]

for i in L:
    if i > largest:
        largest = i

print("Largest:", largest)
```

**A18. Count even numbers**

```
L = [2, 5, 8, 11, 14, 17]

count = 0

for i in L:
    if i % 2 == 0:
        count += 1

print("Even numbers:", count)
```

**A19. Search an element**

```
L = [10, 20, 30, 40, 50]

n = int(input("Enter number: "))

if n in L:
    print("Found")
else:
    print("Not Found")
```

**A20. Calculate sum and average**

```
L = [10, 20, 30, 40, 50]

total = sum(L)
average = total / len(L)

print("Sum:", total)
print("Average:", average)
```

---

# PART B – DICTIONARIES ANSWERS

## Section 1: Output Answers

**A21.**

```
Rahul
16
```

**A22.**

```
dict_keys(['A', 'B', 'C'])
```

**A23.**

```
dict_values([10, 20])
```

**A24.**

```
{'name': 'Riya', 'age': 18}
```

**A25.**

```
{'Maths': 90, 'Science': 85, 'English': 88}
```

**A26.**

```
{'A': 10, 'C': 30}
```

**A27.**

```
3
True
```

**A28.**

```
20
0
```

**A29.**

```
apple
mango
```

**A30.**

```
A 10
B 20
```

## Section 2: Conceptual Answers

**A31.** A dictionary is a mutable collection of data stored in key-value pairs. Each key must be unique and hashable.

Example:

```
student = {"name": "Rahul", "age": 16}
```

**A32.**

| List                           | Dictionary             |
| ------------------------------ | ---------------------- |
| Stores elements                | Stores key-value pairs |
| Accessed using index           | Accessed using keys    |
| Created using `[]`             | Created using `{}`     |
| Duplicate elements are allowed | Keys must be unique    |

**A33.**

- Key: Used to identify or access a value.
- Value: Data associated with a key.

Example:

```
student = {"name": "Aman", "age": 17}
```

Here, `name` and `age` are keys, while `Aman` and `17` are values.

**A34.**

- `keys()` returns all dictionary keys.
- `values()` returns all dictionary values.
- `items()` returns all key-value pairs as tuples.

**A35.**

Error: `KeyError: 0`

Reason: Dictionary elements are accessed using their keys, not numerical indexes.

Correct code:

```
D = {"name": "Aman", "age": 17}
print(D["name"])
```

## Section 3: Programming Answers

**A36. Create a student dictionary**

```
D = {
    "Rahul": 85,
    "Priya": 90,
    "Aman": 78
}

print(D)
```

**A37. Display all keys and values**

```
D = {"A": 10, "B": 20, "C": 30}

for k, v in D.items():
    print(k, v)
```

**A38. Calculate total marks**

```
D = {
    "Maths": 90,
    "English": 85,
    "Science": 95,
    "Computer": 88,
    "Hindi": 80
}

total = 0

for marks in D.values():
    total += marks

print("Total Marks:", total)
```

**A39. Search for a key**

```
D = {"name": "Rahul", "age": 16, "class": 11}

key = input("Enter key: ")

if key in D:
    print("Key Found")
else:
    print("Key Not Found")
```

**A40. Find the largest dictionary value**

```
D = {
    "A": 45,
    "B": 78,
    "C": 92,
    "D": 56,
    "E": 88
}

largest = max(D.values())

print("Largest Value:", largest)
```

---
