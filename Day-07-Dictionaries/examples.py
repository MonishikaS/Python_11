```python
# Python Dictionaries - Examples

# Example 1: Creating a dictionary
student = {"name": "Rahul", "age": 16, "class": 11}
print(student)

# Example 2: Accessing values
student = {"name": "Rahul", "age": 16, "class": 11}
print(student["name"])
print(student["age"])

# Example 3: Using get()
student = {"name": "Rahul", "age": 16}
print(student.get("name"))
print(student.get("marks", "Not Available"))

# Example 4: Adding an element
student = {"name": "Rahul", "age": 16}
student["city"] = "Bengaluru"
print(student)

# Example 5: Modifying an element
student = {"name": "Rahul", "age": 16}
student["age"] = 17
print(student)

# Example 6: Deleting an element
student = {"name": "Rahul", "age": 16, "city": "Delhi"}
del student["city"]
print(student)

# Example 7: Finding dictionary length
marks = {"Maths": 90, "English": 85, "Python": 95}
print(len(marks))

# Example 8: Checking whether a key exists
student = {"name": "Rahul", "age": 16}
print("name" in student)
print("marks" in student)

# Example 9: Checking whether a value exists
marks = {"Maths": 90, "English": 85}
print(90 in marks.values())
print(75 in marks.values())

# Example 10: Displaying all keys
student = {"name": "Rahul", "age": 16, "city": "Delhi"}
print(student.keys())

# Example 11: Displaying all values
student = {"name": "Rahul", "age": 16, "city": "Delhi"}
print(student.values())

# Example 12: Displaying key-value pairs
student = {"name": "Rahul", "age": 16}
print(student.items())

# Example 13: Traversing dictionary keys
marks = {"Maths": 90, "English": 85, "Python": 95}
for subject in marks:
    print(subject)

# Example 14: Traversing dictionary values
marks = {"Maths": 90, "English": 85, "Python": 95}
for mark in marks.values():
    print(mark)

# Example 15: Traversing keys and values
marks = {"Maths": 90, "English": 85, "Python": 95}
for subject, mark in marks.items():
    print(subject, mark)

# Example 16: Updating a dictionary
student = {"name": "Rahul", "age": 16}
student.update({"age": 17, "city": "Delhi"})
print(student)

# Example 17: Using pop()
student = {"name": "Rahul", "age": 16, "city": "Delhi"}
removed = student.pop("age")
print(removed)
print(student)

# Example 18: Using popitem()
student = {"name": "Rahul", "age": 16, "city": "Delhi"}
print(student.popitem())
print(student)

# Example 19: Clearing a dictionary
student = {"name": "Rahul", "age": 16}
student.clear()
print(student)

# Example 20: Calculating total marks
marks = {"Maths": 90, "English": 85, "Python": 95}
total = sum(marks.values())
print("Total marks:", total)

# Example 21: Calculating average marks
marks = {"Maths": 90, "English": 85, "Python": 95}
average = sum(marks.values()) / len(marks)
print("Average:", average)

# Example 22: Counting subjects with marks >= 80
marks = {"Maths": 90, "English": 75, "Python": 95, "Science": 82}
count = 0

for mark in marks.values():
    if mark >= 80:
        count += 1

print("Subjects with marks >= 80:", count)

# Example 23: Nested dictionary
students = {
    "student1": {"name": "Aman", "marks": 90},
    "student2": {"name": "Priya", "marks": 95}
}

print(students["student1"]["name"])
print(students["student2"]["marks"])

# Example 24: Counting character frequency
word = "banana"
frequency = {}

for character in word:
    frequency[character] = frequency.get(character, 0) + 1

print(frequency)

# Example 25: Creating a dictionary using input
student = {}

student["name"] = input("Enter student name: ")
student["age"] = int(input("Enter age: "))

print(student)
```
