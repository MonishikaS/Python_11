Here are **30 unique practice questions for Class 11** based on the **SELECT statement** shown in your textbook page. The worksheet has 15 output-prediction questions and 15 query-writing questions.

It covers `SELECT`, `FROM`, selecting specific columns, `SELECT *`, and basic `WHERE` conditions. **UPDATE and DELETE are not included.**

````
# SQL – SELECT Statement Practice Worksheet
## Class 11 – Informatics Practices

### Topics Covered
- SELECT statement
- FROM clause
- Selecting specific columns
- SELECT *
- WHERE clause
- Conditions using comparison operators

---

# Section A: Predict the Output (Q1–Q15)

Use the following STUDENT table to answer Questions 1–15.

### STUDENT Table

| RollNumber | SName         | Class | Marks | City      |
|------------|---------------|-------|-------|-----------|
| 1          | Atharv Ahuja  | 11    | 92    | Delhi     |
| 2          | Riya Sharma   | 11    | 85    | Mumbai    |
| 3          | Kabir Singh   | 12    | 76    | Chandigarh|
| 4          | Meera Gupta   | 11    | 95    | Delhi     |
| 5          | Arjun Verma   | 12    | 68    | Jaipur    |
| 6          | Simran Kaur   | 11    | 88    | Ludhiana  |

**Instructions:** Write the output that will be displayed for each SQL query.

### Q1.
```sql
SELECT * FROM STUDENT;
````

### **Q2.**

```
SELECT SName FROM STUDENT;
```

### **Q3.**

```
SELECT RollNumber, Marks FROM STUDENT;
```

### **Q4.**

```
SELECT SName, City
FROM STUDENT
WHERE RollNumber = 4;
```

### **Q5.**

```
SELECT SName, Marks
FROM STUDENT
WHERE Marks > 85;
```

### **Q6.**

```
SELECT SName, Class
FROM STUDENT
WHERE Class = 12;
```

### **Q7.**

```
SELECT SName, City
FROM STUDENT
WHERE City = 'Delhi';
```

### **Q8.**

```
SELECT RollNumber, SName, Marks
FROM STUDENT
WHERE Marks < 80;
```

### **Q9.**

```
SELECT SName
FROM STUDENT
WHERE RollNumber = 2;
```

### **Q10.**

```
SELECT SName, Marks
FROM STUDENT
WHERE Marks >= 90;
```

### **Q11.**

```
SELECT SName, City
FROM STUDENT
WHERE Class = 11;
```

### **Q12.**

```
SELECT RollNumber, SName
FROM STUDENT
WHERE Marks <= 85;
```

### **Q13.**

```
SELECT SName, Marks
FROM STUDENT
WHERE City = 'Jaipur';
```

### **Q14.**

```
SELECT SName, Class, Marks
FROM STUDENT
WHERE RollNumber > 3;
```

### **Q15.**

```
SELECT SName, City
FROM STUDENT
WHERE RollNumber = 10;
```

# **Section B: Write SQL Queries (Q16–Q30)**

**Instructions:** Write the correct SQL query for each question.

Use the following table structures wherever mentioned.

### **Table 1: EMPLOYEE**

| Column Name | Data Type   |
| ----------- | ----------- |
| EmpID       | INT         |
| EmpName     | VARCHAR(30) |
| Department  | VARCHAR(20) |
| Salary      | INT         |
| City        | VARCHAR(20) |

### **Table 2: BOOK**

| Column Name | Data Type   |
| ----------- | ----------- |
| BookID      | INT         |
| BookName    | VARCHAR(40) |
| Author      | VARCHAR(30) |
| Price       | INT         |
| Publisher   | VARCHAR(30) |

### **Table 3: PRODUCT**

| Column Name | Data Type   |
| ----------- | ----------- |
| ProductID   | INT         |
| ProductName | VARCHAR(30) |
| Category    | VARCHAR(20) |
| Price       | INT         |
| Quantity    | INT         |

### **Q16.**

Write a query to display all the records and columns from the EMPLOYEE table.

### **Q17.**

Write a query to display only the names of all employees.

### **Q18.**

Write a query to display the EmpID, EmpName and Salary of all employees.

### **Q19.**

Write a query to display the details of employees who belong to the 'IT' department.

### **Q20.**

Write a query to display the names and salaries of employees whose salary is greater than 40,000.

### **Q21.**

Write a query to display the names of employees who live in 'Chandigarh'.

### **Q22.**

Write a query to display the details of employees whose EmpID is 105.

### **Q23.**

Write a query to display the names and departments of employees whose salary is less than 30,000.

### **Q24.**

Write a query to display all the details of books from the BOOK table.

### **Q25.**

Write a query to display only the BookName and Author of all books.

### **Q26.**

Write a query to display the names and prices of books whose price is greater than 500.

### **Q27.**

Write a query to display the details of books published by 'Penguin'.

### **Q28.**

Write a query to display ProductName and Quantity from the PRODUCT table.

### **Q29.**

Write a query to display the names of products whose quantity is less than 10.

### **Q30.**

Write a query to display ProductName, Category and Price of products whose price is equal to 1,000.

## **Important Revision**

| SQL Keyword | Purpose                              |
| ----------- | ------------------------------------ |
| SELECT      | Retrieves data from a table          |
| FROM        | Specifies the table name             |
| WHERE       | Filters records based on a condition |
| \*          | Selects all columns                  |

### **Remember**

1. Every SELECT query must contain the FROM clause.
2. Use `*` to display all columns.
3. Use column names to display specific columns.
4. WHERE is optional.
5. Text values must be written inside single quotes.
6. Numeric values are generally written without quotes.
7. SELECT retrieves data; it does not modify or delete records.

```
```
