# Day 06: Python Lists

## 1. Introduction to Lists

A **list** is a Python data type used to store multiple elements in a single variable.

Lists are:
- **Ordered:** Elements maintain their order.
- **Mutable:** Elements can be changed after creation.
- **Indexed:** Every element has an index.
- **Flexible:** They can store different data types.
- **Allow duplicates:** The same element can appear multiple times.

### Syntax

```python
list_name = [element1, element2, element3]
```

### Examples

```python
# List of integers
numbers = [2, 4, 6, 8, 10]

# List of strings
vowels = ['a', 'e', 'i', 'o', 'u']

# List of mixed data types
mixed = [100, 23.5, "Hello"]

# Empty list
empty = []

print(numbers)
print(vowels)
print(mixed)
print(empty)
```

## 2. Accessing Elements in a List

Each element in a list is accessed using its **index**.

Python indexing starts from `0`.

```python
numbers = [2, 4, 6, 8, 10, 12]

print(numbers[0])  # First element
print(numbers[3])  # Fourth element
print(numbers[5])  # Sixth element
```

Output:

```text
2
8
12
```

### Negative Indexing

Negative indexing accesses elements from the right side of the list.

```python
numbers = [2, 4, 6, 8, 10, 12]

print(numbers[-1])  # Last element
print(numbers[-2])  # Second-last element
print(numbers[-6])  # First element
```

Output:

```text
12
10
2
```

### Using `len()`

The `len()` function returns the total number of elements in a list.

```python
numbers = [2, 4, 6, 8, 10, 12]

n = len(numbers)

print(n)
print(numbers[n - 1])
```

Output:

```text
6
12
```

**Important:** Accessing an index that does not exist raises an `IndexError`.

## 3. Lists Are Mutable

Lists are mutable, which means their elements can be changed after the list is created.

```python
colours = ['Red', 'Green', 'Blue', 'Orange']

colours[3] = 'Black'

print(colours)
```

Output:

```text
['Red', 'Green', 'Blue', 'Black']
```

Here, the element at index `3` changes from `'Orange'` to `'Black'`.

## 4. List Operations

### 4.1 Concatenation (`+`)

Concatenation joins two or more lists.

```python
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

list3 = list1 + list2

print(list3)
```

Output:

```text
[1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
```

The original lists remain unchanged unless the result is assigned to a variable.

**Note:** The `+` operator joins lists with other lists, not directly with strings or integers.

### 4.2 Repetition (`*`)

The repetition operator repeats the elements of a list.

```python
list1 = ['Hello']

print(list1 * 4)
```

Output:

```text
['Hello', 'Hello', 'Hello', 'Hello']
```

### 4.3 Membership (`in` and `not in`)

The `in` operator checks whether an element exists in a list.

The `not in` operator checks whether an element is absent.

```python
colours = ['Red', 'Green', 'Blue']

print('Green' in colours)
print('Cyan' in colours)
print('Cyan' not in colours)
```

Output:

```text
True
False
True
```

### 4.4 Slicing

Slicing creates a new list containing selected elements from an existing list.

### Syntax

```python
list_name[start:stop:step]
```

- `start`: Index where slicing begins.
- `stop`: Index where slicing stops; this index is excluded.
- `step`: Number of positions to move between selected elements.

Example:

```python
colours = ['Red', 'Green', 'Blue', 'Cyan',
           'Magenta', 'Yellow', 'Black']

print(colours[2:6])
print(colours[:5])
print(colours[0:6:2])
print(colours[-6:-2])
print(colours[::2])
print(colours[::-1])
```

Output:

```text
['Blue', 'Cyan', 'Magenta', 'Yellow']
['Red', 'Green', 'Blue', 'Cyan', 'Magenta']
['Red', 'Blue', 'Magenta']
['Green', 'Blue', 'Cyan', 'Magenta']
['Red', 'Blue', 'Magenta', 'Black']
['Black', 'Yellow', 'Magenta', 'Cyan', 'Blue', 'Green', 'Red']
```

**Remember:**
- `list_name[:3]` selects elements from the beginning up to index `2`.
- `list_name[2:]` selects elements from index `2` to the end.
- `list_name[::2]` selects every second element.
- `list_name[::-1]` returns the elements in reverse order.

## 5. Traversing a List

**Traversing** means accessing each element of a list one by one.

### 5.1 Using a `for` Loop

```python
colours = ['Red', 'Green', 'Blue', 'Yellow', 'Black']

for colour in colours:
    print(colour)
```

Output:

```text
Red
Green
Blue
Yellow
Black
```

### 5.2 Using `range()` and `len()`

```python
colours = ['Red', 'Green', 'Blue', 'Yellow', 'Black']

for i in range(len(colours)):
    print(colours[i])
```

Here:
- `len(colours)` returns the number of elements.
- `range(len(colours))` generates indexes from `0` to one less than the length.

### 5.3 Using a `while` Loop

```python
numbers = [10, 20, 30]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1
```

## 6. List Methods and Built-in Functions

### 6.1 `len()`

Returns the number of elements in a list.

```python
numbers = [10, 20, 30, 40, 50]

print(len(numbers))
```

Output: `5`

### 6.2 `list()`

Creates an empty list or converts a sequence into a list.

```python
list1 = list()
list2 = list('aeiou')

print(list1)
print(list2)
```

Output:

```text
[]
['a', 'e', 'i', 'o', 'u']
```

### 6.3 `append()`

Adds a single element at the end of the list.

```python
numbers = [10, 20, 30, 40]

numbers.append(50)

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

A list can also be appended as one element.

```python
numbers = [10, 20, 30, 40]

numbers.append([50, 60])

print(numbers)
```

Output:

```text
[10, 20, 30, 40, [50, 60]]
```

### 6.4 `extend()`

Adds each element of another iterable to the end of the list.

```python
numbers = [10, 20, 30]

numbers.extend([40, 50])

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

**Difference:**

- `append()` adds its argument as one element.
- `extend()` adds the elements individually.

### 6.5 `insert()`

Inserts an element at a specified index.

```python
numbers = [10, 20, 30, 40, 50]

numbers.insert(2, 25)

print(numbers)
```

Output:

```text
[10, 20, 25, 30, 40, 50]
```

### 6.6 `count()`

Returns the number of times a specified element appears.

```python
numbers = [10, 20, 30, 10, 40, 10]

print(numbers.count(10))
print(numbers.count(90))
```

Output:

```text
3
0
```

### 6.7 `index()`

Returns the index of the first occurrence of an element.

```python
numbers = [10, 20, 30, 20, 40, 10]

print(numbers.index(20))
```

Output:

```text
1
```

If the element does not exist, `index()` raises a `ValueError`.

### 6.8 `remove()`

Removes the first occurrence of a specified value.

```python
numbers = [10, 20, 30, 40, 50, 30]

numbers.remove(30)

print(numbers)
```

Output:

```text
[10, 20, 40, 50, 30]
```

If the value is absent, `remove()` raises a `ValueError`.

### 6.9 `pop()`

Removes and returns an element at a specified index. If no index is supplied, it removes the last element.

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers.pop(3))
print(numbers)
```

Output:

```text
40
[10, 20, 30, 50, 60]
```

Without an index:

```python
numbers = [10, 20, 30, 40]

print(numbers.pop())
print(numbers)
```

Output:

```text
40
[10, 20, 30]
```

### 6.10 `reverse()`

Reverses the order of elements in the original list.

```python
numbers = [34, 66, 12, 89, 28, 99]

numbers.reverse()

print(numbers)
```

Output:

```text
[99, 28, 89, 12, 66, 34]
```

### 6.11 `sort()`

Sorts the original list in ascending order by default.

```python
numbers = [34, 66, 12, 89, 28, 99]

numbers.sort()

print(numbers)
```

Output:

```text
[12, 28, 34, 66, 89, 99]
```

For descending order:

```python
numbers.sort(reverse=True)

print(numbers)
```

Output:

```text
[99, 89, 66, 34, 28, 12]
```

### 6.12 `sorted()`

Returns a new list containing the elements in sorted order. The original list remains unchanged.

```python
numbers = [23, 45, 11, 67, 85, 56]

new_numbers = sorted(numbers)

print(numbers)
print(new_numbers)
```

Output:

```text
[23, 45, 11, 67, 85, 56]
[11, 23, 45, 56, 67, 85]
```

**Difference:**
- `sort()` modifies the original list.
- `sorted()` creates a new sorted list.

### 6.13 `min()`, `max()` and `sum()`

These built-in functions work with lists of compatible numeric values.

```python
numbers = [34, 12, 63, 39, 92, 44]

print(min(numbers))
print(max(numbers))
print(sum(numbers))
```

Output:

```text
12
92
284
```

## 7. Important Differences

| Operation | Purpose |
|---|---|
| `append(x)` | Adds one element at the end |
| `extend(iterable)` | Adds elements individually |
| `insert(i, x)` | Inserts an element at an index |
| `remove(x)` | Removes the first matching value |
| `pop(i)` | Removes and returns an element by index |
| `count(x)` | Counts occurrences of a value |
| `index(x)` | Finds the first index of a value |
| `reverse()` | Reverses the original list |
| `sort()` | Sorts the original list |
| `sorted(list)` | Returns a new sorted list |
| `len(list)` | Returns the number of elements |
| `min(list)` | Returns the smallest element |
| `max(list)` | Returns the largest element |
| `sum(list)` | Returns the sum of numeric elements |

## 8. Quick Revision

1. Lists store multiple elements in one variable.
2. List elements are enclosed in square brackets `[]`.
3. Indexing starts from `0`.
4. Negative indexing accesses elements from the end.
5. Lists are mutable, so elements can be modified.
6. `+` joins lists, while `*` repeats list elements.
7. `in` and `not in` check membership.
8. Slicing extracts a portion of a list.
9. `for` and `while` loops can traverse lists.
10. List methods help us add, insert, remove, count, reverse and sort elements.
