# Day 06: Python Lists
# Run each example in Spyder.

# Example 1: Creating lists
numbers = [10, 20, 30, 40]
fruits = ["apple", "mango", "banana"]
mixed = [100, 23.5, "Hello"]

print(numbers)
print(fruits)
print(mixed)


# Example 2: Positive indexing
colours = ["Red", "Green", "Blue", "Yellow"]

print(colours[0])
print(colours[1])
print(colours[3])


# Example 3: Negative indexing
numbers = [10, 20, 30, 40, 50]

print(numbers[-1])
print(numbers[-2])
print(numbers[-5])


# Example 4: Length of a list
subjects = ["English", "Maths", "IP", "Physics"]

print("Total subjects:", len(subjects))


# Example 5: Modifying a list
colours = ["Red", "Green", "Blue"]

colours[1] = "Black"

print(colours)


# Example 6: Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2

print(list3)


# Example 7: Repetition
items = ["Python"]

print(items * 3)


# Example 8: Membership operators
fruits = ["Apple", "Mango", "Banana"]

print("Mango" in fruits)
print("Grapes" in fruits)
print("Grapes" not in fruits)


# Example 9: Slicing
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])
print(numbers[::-1])


# Example 10: Traversing using a for loop
fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)


# Example 11: Traversing using indexes
numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])


# Example 12: Traversing using a while loop
numbers = [5, 10, 15]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1


# Example 13: append()
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)


# Example 14: extend()
numbers = [10, 20, 30]

numbers.extend([40, 50])

print(numbers)


# Example 15: insert()
numbers = [10, 20, 30, 40]

numbers.insert(2, 25)

print(numbers)


# Example 16: Difference between append() and extend()
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)

list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)


# Example 17: count() and index()
numbers = [10, 20, 10, 30, 10]

print("Count of 10:", numbers.count(10))
print("Index of 30:", numbers.index(30))


# Example 18: remove()
numbers = [10, 20, 30, 20, 40]

numbers.remove(20)

print(numbers)


# Example 19: pop()
numbers = [10, 20, 30, 40]

removed = numbers.pop()

print("Removed element:", removed)
print("Updated list:", numbers)


# Example 20: reverse()
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)


# Example 21: sort()
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)


# Example 22: Descending order
numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)


# Example 23: sorted()
numbers = [40, 10, 30, 20]

new_numbers = sorted(numbers)

print("Original list:", numbers)
print("Sorted list:", new_numbers)


# Example 24: min(), max(), and sum()
marks = [78, 85, 92, 67, 88]

print("Minimum:", min(marks))
print("Maximum:", max(marks))
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))


# Example 25: Print only even numbers using a list and loop
numbers = [11, 24, 7, 18, 30, 9, 42]

for number in numbers:
    if number % 2 == 0:
        print(number)
