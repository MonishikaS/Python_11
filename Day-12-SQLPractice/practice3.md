You're right—the previous worksheet missed several important SELECT topics. Here is the revised **30-question Class 11 worksheet**, including:

- `SELECT` and `WHERE`
- Membership operators: `IN`, `NOT IN`
- `DISTINCT`
- `ORDER BY` (`ASC`, `DESC`)
- `LIKE` with `%` and `_`
- Column aliases using `AS`
- Output prediction and query writing

UPDATE and DELETE are excluded.


````
# SQL – SELECT Statement Practice Worksheet
## Class 11 – Informatics Practices

### Topics Covered
1. SELECT and WHERE
2. DISTINCT
3. Membership Operators – IN, NOT IN
4. ORDER BY – ASC, DESC
5. LIKE Operator – %, _
6. Alias Names using AS

---

# Section A: Predict the Output (Q1–Q15)

Use the following STUDENT table for all questions in this section.

### STUDENT Table

| RollNo | Name     | Class | Marks | City       |
|--------|----------|-------|-------|------------|
| 1      | Aanya    | 11    | 92    | Delhi      |
| 2      | Rohan    | 12    | 78    | Mumbai     |
| 3      | Meera    | 11    | 85    | Delhi      |
| 4      | Karan    | 12    | 67    | Chandigarh |
| 5      | Simran   | 11    | 92    | Mumbai     |
| 6      | Arjun    | 11    | 74    | Ludhiana   |
| 7      | Priya    | 12    | 88    | Delhi      |
| 8      | Aman     | 11    | 81    | Chandigarh |

**Predict the exact output of each query.**

### Q1. 
```sql
SELECT DISTINCT City FROM STUDENT;
````

### **Q2.**

```
SELECT Name, Marks
FROM STUDENT
ORDER BY Marks ASC;
```

### **Q3.**

```
SELECT Name, Marks
FROM STUDENT
ORDER BY Marks DESC;
```

### **Q4.**

```
SELECT Name, City
FROM STUDENT
WHERE City IN ('Delhi', 'Mumbai');
```

### **Q5.**

```
SELECT Name, City
FROM STUDENT
WHERE City NOT IN ('Delhi', 'Mumbai');
```

### **Q6.**

```
SELECT Name
FROM STUDENT
WHERE Name LIKE 'A%';
```

### **Q7.**

```
SELECT Name
FROM STUDENT
WHERE Name LIKE '%a';
```

### **Q8.**

```
SELECT Name
FROM STUDENT
WHERE Name LIKE '_a%';
```

### **Q9.**

```
SELECT Name AS StudentName, Marks AS Score
FROM STUDENT;
```

### **Q10.**

```
SELECT DISTINCT Marks
FROM STUDENT
ORDER BY Marks DESC;
```

### **Q11.**

```
SELECT Name, Marks
FROM STUDENT
WHERE Marks BETWEEN 80 AND 90;
```

### **Q12.**

```
SELECT Name, Class
FROM STUDENT
WHERE Class IN (11, 12)
ORDER BY Name ASC;
```

### **Q13.**

```
SELECT Name
FROM STUDENT
WHERE Name LIKE '%an%';
```

### **Q14.**

```
SELECT City AS StudentCity
FROM STUDENT
ORDER BY City ASC;
```

### **Q15.**

```
SELECT DISTINCT Class, City
FROM STUDENT
ORDER BY Class DESC;
```

# **Section B: Write SQL Queries (Q16–Q30)**

Write SQL queries for the following questions.

Use the following tables and their structures.

## **Table 1: EMPLOYEE**

| Column Name | Data Type   |
| ----------- | ----------- |
| EmpID       | INT         |
| EmpName     | VARCHAR(30) |
| Department  | VARCHAR(20) |
| Salary      | INT         |
| City        | VARCHAR(20) |

## **Table 2: BOOK**

| Column Name | Data Type   |
| ----------- | ----------- |
| BookID      | INT         |
| BookName    | VARCHAR(40) |
| Author      | VARCHAR(30) |
| Price       | INT         |
| Publisher   | VARCHAR(30) |

## **Table 3: PRODUCT**

| Column Name | Data Type   |
| ----------- | ----------- |
| ProductID   | INT         |
| ProductName | VARCHAR(30) |
| Category    | VARCHAR(20) |
| Price       | INT         |
| Quantity    | INT         |

### **Q16. SELECT**

Display all columns and records from the EMPLOYEE table.

### **Q17. WHERE**

Display the names and salaries of employees whose salary is greater than 35,000.

### **Q18. DISTINCT**

Display all unique departments from the EMPLOYEE table.

### **Q19. IN Operator**

Display the details of employees who work in either the 'HR', 'IT' or 'Sales' department.

### **Q20. NOT IN Operator**

Display the names of employees who do not belong to the 'Finance' or 'Marketing' department.

### **Q21. ORDER BY ASC**

Display employee names and salaries in ascending order of salary.

### **Q22. ORDER BY DESC**

Display all employee details in descending order of EmpID.

### **Q23. LIKE Operator (%)**

Display the names of employees whose names start with the letter 'S'.

### **Q24. LIKE Operator (%)**

Display the names of employees whose names end with 'a'.

### **Q25. LIKE Operator (\_)**

Display the names of employees whose names have 'a' as their second character.

### **Q26. Alias Name**

Display EmpName as Employee_Name and Salary as Monthly_Salary.

### **Q27. DISTINCT with ORDER BY**

Display unique cities from the EMPLOYEE table in alphabetical order.

### **Q28. BOOK Table**

Display BookName and Price of books whose price is between 200 and 600, in descending order of price.

### **Q29. BOOK Table**

Display the names of books published by either 'Penguin' or 'Oxford'.

### **Q30. PRODUCT Table**

Display ProductName as Item_Name and Quantity as Stock. Show only products whose names start with 'M', arranging them alphabetically.

# **Quick Revision – SQL Commands**

| Command / Operator | Purpose                                  |
| ------------------ | ---------------------------------------- |
| SELECT \*          | Displays all columns                     |
| SELECT column      | Displays selected columns                |
| WHERE              | Filters records                          |
| DISTINCT           | Removes duplicate rows                   |
| IN                 | Matches any value in a given list        |
| NOT IN             | Excludes values in a given list          |
| ORDER BY           | Sorts records                            |
| ASC                | Sorts in ascending order                 |
| DESC               | Sorts in descending order                |
| LIKE               | Searches for a matching pattern          |
| %                  | Represents zero or more characters       |
| \_                 | Represents exactly one character         |
| AS                 | Gives a temporary alias name             |
| BETWEEN            | Checks whether a value is within a range |

## **Important Points**

1. DISTINCT is written immediately after SELECT.
2. IN is used when checking multiple possible values.
3. NOT IN excludes the specified values.
4. ORDER BY ASC sorts from smallest to largest or A to Z.
5. ORDER BY DESC sorts from largest to smallest or Z to A.
6. LIKE 'A%' finds values starting with A.
7. LIKE '%a' finds values ending with a.
8. LIKE '\_a%' finds values having a as the second character.
9. AS gives a temporary name to a column in the output.
10. WHERE is used to filter records before displaying them.

## **Remember**

- SELECT retrieves records.
- DISTINCT removes duplicate combinations of selected columns.
- ORDER BY sorts the result.
- LIKE searches for patterns.
- IN checks multiple values.
- AS changes the displayed column heading, not the actual table structure.

