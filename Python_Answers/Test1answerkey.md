# Class 11 – Informatics Practices
## Answer Key: Python (Lists & Dictionaries) + SQL

**Maximum Marks:** 50  
**Time:** 1 Hour

---

# SECTION A – MULTIPLE CHOICE QUESTIONS (10 Marks)

| Q.No. | Correct Answer |
|---|---|
| 1 | b) `L = []` |
| 2 | d) 40 |
| 3 | b) `append()` |
| 4 | c) List |
| 5 | c) 20 |
| 6 | b) `keys()` |
| 7 | c) DROP |
| 8 | b) IN |
| 9 | b) ALTER |
| 10 | c) ORDER BY DESC |

**Important Concept:**
- `append()` adds an element as one single element at the end of a list.
- `extend()` adds individual elements of an iterable to a list.

---

# SECTION B – PREDICT THE OUTPUT (10 Marks)

## Q2. Python Output (6 Marks)

### a. Answer

```python
L = [5, 10, 15, 20]
L.append(25)
L.insert(1, 8)
L.remove(15)
print(L)
```

**Output:**

```python
[5, 8, 10, 20, 25]
```

**Explanation:**
1. `append(25)` adds 25 at the end.
2. `insert(1, 8)` inserts 8 at index 1.
3. `remove(15)` removes the element 15.

### b. Answer

```python
L = [10, 20, 30, 40, 50]
print(L[1:4])
print(L[-2])
```

**Output:**

```python
[20, 30, 40]
40
```

**Explanation:**
- `L[1:4]` returns elements from index 1 to index 3.
- `L[-2]` returns the second-last element.

### c. Answer

```python
D = {"Maths": 90, "English": 85}
D["Science"] = 95
D["Maths"] = 98

print(D)
print(D.keys())
```

**Output:**

```python
{'Maths': 98, 'English': 85, 'Science': 95}
dict_keys(['Maths', 'English', 'Science'])
```

**Explanation:**
- Science is added as a new key.
- Maths marks are updated from 90 to 98.
- `keys()` displays all dictionary keys.

## Q3. SQL Output (4 Marks)

Given STUDENT table:

| RollNo | Name | Marks | City |
|---|---|---|---|
| 1 | Aman | 85 | Delhi |
| 2 | Riya | 92 | Mumbai |
| 3 | Karan | 75 | Delhi |
| 4 | Neha | 92 | Pune |
| 5 | Arjun | 60 | Mumbai |

### a. Answer

```sql
SELECT DISTINCT City
FROM STUDENT;
```

**Output:**

| City |
|---|
| Delhi |
| Mumbai |
| Pune |

**Explanation:** `DISTINCT` removes duplicate values and displays only unique cities.

### b. Answer

```sql
SELECT Name, Marks
FROM STUDENT
WHERE Marks >= 85
ORDER BY Marks DESC;
```

**Output:**

| Name | Marks |
|---|---:|
| Riya | 92 |
| Neha | 92 |
| Aman | 85 |

**Explanation:**
- `WHERE Marks >= 85` selects students scoring 85 or above.
- `ORDER BY Marks DESC` sorts marks from highest to lowest.
- Riya and Neha can appear in either order because both have 92 marks.

---

# SECTION C – PYTHON PROGRAMMING (10 Marks)

## Q4 (a). List Operations (5 Marks)

**Program:**

```python
L = []

for i in range(5):
    n = int(input("Enter a number: "))
    L.append(n)

print("Original List:", L)

print("Largest Element:", max(L))

print("Reverse List:", L[::-1])
```

**Sample Output:**

```text
Enter a number: 10
Enter a number: 20
Enter a number: 5
Enter a number: 40
Enter a number: 30

Original List: [10, 20, 5, 40, 30]
Largest Element: 40
Reverse List: [30, 40, 5, 20, 10]
```

**Explanation:**
- `L = []` creates an empty list.
- `append()` adds elements to the list.
- `max(L)` finds the largest element.
- `L[::-1]` displays the list in reverse order.

## Q4 (b). Dictionary Operations (5 Marks)

**Program:**

```python
D = {
    "Aman": 85,
    "Riya": 90,
    "Karan": 78
}

print("Keys:", D.keys())
print("Values:", D.values())

D["Neha"] = 92

D["Aman"] = 95

print("Final Dictionary:", D)
```

**Output:**

```text
Keys: dict_keys(['Aman', 'Riya', 'Karan'])
Values: dict_values([85, 90, 78])
Final Dictionary: {'Aman': 95, 'Riya': 90, 'Karan': 78, 'Neha': 92}
```

**Explanation:**
- `keys()` displays all dictionary keys.
- `values()` displays all dictionary values.
- `D["Neha"] = 92` adds a new student.
- `D["Aman"] = 95` updates the marks of an existing student.

---

# SECTION D – SQL (20 Marks)

## Q5. SQL MCQs (4 Marks)

| Q.No. | Correct Answer |
|---|---|
| 1 | b) DESC |
| 2 | c) PRIMARY KEY |
| 3 | b) Names starting with A |
| 4 | b) UPDATE |

---

## Q6. Write SQL Queries (6 Marks)

Given EMPLOYEE table:

| EmpID | EmpName | Department | Salary | City |
|---|---|---|---:|---|
| 101 | Aman | IT | 45000 | Delhi |
| 102 | Riya | HR | 35000 | Mumbai |
| 103 | Karan | IT | 55000 | Delhi |
| 104 | Neha | Sales | 40000 | Pune |
| 105 | Arjun | HR | 30000 | Mumbai |

### a. Display the names and salaries of all employees.

```sql
SELECT EmpName, Salary
FROM EMPLOYEE;
```

### b. Display employees whose salary is greater than 40000.

```sql
SELECT *
FROM EMPLOYEE
WHERE Salary > 40000;
```

### c. Display unique department names.

```sql
SELECT DISTINCT Department
FROM EMPLOYEE;
```

### d. Display all employees in descending order of salary.

```sql
SELECT *
FROM EMPLOYEE
ORDER BY Salary DESC;
```

### e. Display employees whose names start with 'A'.

```sql
SELECT *
FROM EMPLOYEE
WHERE EmpName LIKE 'A%';
```

### f. Display employees who belong to either Delhi or Mumbai using IN.

```sql
SELECT *
FROM EMPLOYEE
WHERE City IN ('Delhi', 'Mumbai');
```

**Note:** Question (f) is an additional question to make Q6 worth 6 marks. The original paper contained only five questions.

---

## Q7. SQL Commands (6 Marks)

### a. Create a database named SCHOOL.

```sql
CREATE DATABASE SCHOOL;
```

### b. Create a STUDENT table.

```sql
CREATE TABLE STUDENT (
    RollNo INT PRIMARY KEY,
    Name VARCHAR(30),
    Class INT,
    City VARCHAR(20) DEFAULT 'Delhi'
);
```

### c. Insert two records into STUDENT.

```sql
INSERT INTO STUDENT
VALUES
(1, 'Rahul', 11, 'Delhi'),
(2, 'Priya', 11, 'Mumbai');
```

---

## Q8. SQL Queries (4 Marks)

### a. Add a Phone column of VARCHAR(15) to EMPLOYEE.

```sql
ALTER TABLE EMPLOYEE
ADD Phone VARCHAR(15);
```

**Change the datatype to VARCHAR(20).**

```sql
ALTER TABLE EMPLOYEE
MODIFY Phone VARCHAR(20);
```

### b. Increase the salary of employee 103 to 60000.

```sql
UPDATE EMPLOYEE
SET Salary = 60000
WHERE EmpID = 103;
```

**Delete the record of employee 105.**

```sql
DELETE FROM EMPLOYEE
WHERE EmpID = 105;
```

---


4. SQL queries must have correct table names, column names and conditions.
5. For MySQL, `MODIFY` is the correct syntax for changing a column's datatype.
6. Award partial marks for correct logic even if there is a minor syntax error.
