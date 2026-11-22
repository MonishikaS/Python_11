# CLASS 11 – INFORMATICS PRACTICES
## Python (Lists & Dictionaries) + SQL – Assessment Test

**Time:** 1 Hour  
**Maximum Marks:** 50

# SECTION A – MULTIPLE CHOICE QUESTIONS (10 Marks)

**Q1. Choose the correct answer. (1 × 10 = 10)**

**1.** Which of the following creates an empty list in Python?

a) `L = {}`  
b) `L = []`  
c) `L = ()`  
d) `L = <>`

**2.** What will be the output?

```python
L = [10, 20, 30, 40]
print(L[-1])
```

a) 10  
b) 20  
c) 30  
d) 40

**3.** Which method is used to add an element at the end of a list as one single element?

a) `add()`  
b) `append()`  
c) `insert()`  
d) `extend()`

**4.** Which of the following is a mutable data type?

a) Tuple  
b) String  
c) List  
d) Integer

**5.** What is the output?

```python
D = {"A": 10, "B": 20}
print(D["B"])
```

a) A  
b) 10  
c) 20  
d) B

**6.** Which method returns all the keys of a dictionary?

a) `values()`  
b) `keys()`  
c) `items()`  
d) `getkeys()`

**7.** Which SQL command is used to remove all records from a table along with its structure?

a) DELETE  
b) UPDATE  
c) DROP  
d) ALTER

**8.** Which SQL operator is used to check whether a value belongs to a specified set?

a) LIKE  
b) IN  
c) DISTINCT  
d) BETWEEN

**9.** Which SQL command is used to modify the structure of an existing table?

a) UPDATE  
b) ALTER  
c) INSERT  
d) SELECT

**10.** Which SQL clause is used to arrange records in descending order?

a) GROUP BY  
b) DISTINCT  
c) ORDER BY DESC  
d) WHERE

---

# SECTION B – PREDICT THE OUTPUT (10 Marks)

**Q2. Write the exact output of the following Python programs. (2 × 3 = 6)**

**a.**

```python
L = [5, 10, 15, 20]
L.append(25)
L.insert(1, 8)
L.remove(15)
print(L)
```

**b.**

```python
L = [10, 20, 30, 40, 50]
print(L[1:4])
print(L[-2])
```

**c.**

```python
D = {"Maths": 90, "English": 85}
D["Science"] = 95
D["Maths"] = 98

print(D)
print(D.keys())
```

**Q3. Predict the output of the following SQL queries. (2 × 2 = 4)**

Consider the following table:

**STUDENT**

| RollNo | Name | Marks | City |
|---|---|---:|---|
| 1 | Aman | 85 | Delhi |
| 2 | Riya | 92 | Mumbai |
| 3 | Karan | 75 | Delhi |
| 4 | Neha | 92 | Pune |
| 5 | Arjun | 60 | Mumbai |

**a.**

```sql
SELECT DISTINCT City
FROM STUDENT;
```

Write the resulting values.

**b.**

```sql
SELECT Name, Marks
FROM STUDENT
WHERE Marks >= 85
ORDER BY Marks DESC;
```

Write the resulting table.

---

# SECTION C – PYTHON PROGRAMMING (10 Marks)

**Q4. Answer the following questions. (5 × 2 = 10)**

**a. List Operations**

Write a Python program to:
- Create a list containing 5 numbers entered by the user.
- Display the original list.
- Find and display the largest element.
- Display the list in reverse order.

**b. Dictionary Operations**

Write a Python program to:
- Create a dictionary containing the names of 3 students as keys and their marks as values.
- Display all the keys and values.
- Add a new student with marks.
- Update the marks of an existing student.
- Display the final dictionary.

---

# SECTION D – SQL (20 Marks)

**Q5. Answer the following MCQs. (1 × 4 = 4)**

**1.** Which command is used to display the structure of a table?

a) SHOW TABLE  
b) DESC  
c) DISPLAY  
d) SELECT

**2.** Which constraint prevents duplicate values in a column and does not allow NULL values?

a) DEFAULT  
b) FOREIGN KEY  
c) PRIMARY KEY  
d) CHECK

**3.** What does the following query display?

```sql
SELECT * FROM STUDENT
WHERE Name LIKE 'A%';
```

a) Names ending with A  
b) Names starting with A  
c) Names containing A anywhere  
d) All names

**4.** Which command is used to change existing values in a table?

a) ALTER  
b) UPDATE  
c) INSERT  
d) DROP

**Q6. Write SQL queries for the following. (1 × 6 = 6)**

Consider the following table:

**EMPLOYEE**

| EmpID | EmpName | Department | Salary | City |
|---|---|---|---:|---|
| 101 | Aman | IT | 45000 | Delhi |
| 102 | Riya | HR | 35000 | Mumbai |
| 103 | Karan | IT | 55000 | Delhi |
| 104 | Neha | Sales | 40000 | Pune |
| 105 | Arjun | HR | 30000 | Mumbai |

Write SQL queries to:

a) Display the names and salaries of all employees.

b) Display employees whose salary is greater than 40000.

c) Display unique department names.

d) Display all employees in descending order of salary.

e) Display employees whose names start with 'A'.

**Q7. Write SQL commands for the following tasks. (2 × 3 = 6)**

a) Create a database named `SCHOOL`.

b) Create a table named `STUDENT` with the following columns:

- RollNo – Integer and Primary Key
- Name – VARCHAR(30)
- Class – Integer
- City – VARCHAR(20) with default value 'Delhi'

c) Insert the following two records into the STUDENT table:

| RollNo | Name | Class | City |
|---|---|---:|---|
| 1 | Rahul | 11 | Delhi |
| 2 | Priya | 11 | Mumbai |

**Q8. Answer the following SQL questions. (2 × 2 = 4)**

a) Write SQL commands to:

- Add a column named `Phone` of type VARCHAR(15) to the EMPLOYEE table.
- Change the datatype of the `Phone` column to VARCHAR(20).

b) Write SQL queries to:

- Increase the salary of employee with EmpID 103 to 60000.
- Delete the record of employee with EmpID 105.

---

## END OF QUESTION PAPER

**Check before submitting:**
- Have you attempted all questions?
- Have you checked Python indentation?
- Have you checked SQL spelling and semicolons?
- Have you written the complete queries?
