# SQL Practice Worksheet – UPDATE and DELETE
## Class 11 – Informatics Practices

### Topics Covered
- UPDATE command
- SET clause
- WHERE clause
- DELETE command
- Updating multiple columns
- Deleting records based on conditions

### Instructions
Write the correct SQL query for each question. Do not write the answers.

---

## Table 1: STUDENT

| RollNo | Name   | Class | Marks | City       |
|--------|--------|-------|-------|------------|
| 1      | Aanya  | 11    | 85    | Delhi      |
| 2      | Rohan  | 12    | 72    | Mumbai     |
| 3      | Meera  | 11    | 90    | Chandigarh |
| 4      | Karan  | 12    | 65    | Delhi      |
| 5      | Simran | 11    | 78    | Ludhiana   |

## Table 2: EMPLOYEE

| EmpID | EmpName | Department | Salary |
|-------|---------|------------|--------|
| 101   | Aman    | IT         | 35000  |
| 102   | Riya    | HR         | 28000  |
| 103   | Arjun   | Sales      | 30000  |
| 104   | Priya   | IT         | 42000  |
| 105   | Karan   | Finance    | 25000  |

---

# Section A: UPDATE Command (Q1–Q8)

**Q1.** Change the marks of the student whose RollNo is 2 to 88.

**Q2.** Change the city of Aanya to Mumbai.

**Q3.** Increase the salary of employee Aman to 40000.

**Q4.** Change the department of employee with EmpID 103 to Marketing.

**Q5.** Change the marks of all students in Class 11 to 95.

**Q6.** Increase the salary of all employees in the IT department to 50000.

**Q7.** Change both the name and city of the student whose RollNo is 4 to Rahul and Jaipur, respectively.

**Q8.** Change the department of employees earning less than 30000 to Administration.

---

# Section B: DELETE Command (Q9–Q15)

**Q9.** Delete the student record whose RollNo is 5.

**Q10.** Delete all students who belong to Class 12.

**Q11.** Delete the employee record whose EmpID is 105.

**Q12.** Delete all employees who work in the Sales department.

**Q13.** Delete students who have scored less than 70 marks.

**Q14.** Delete all employees whose salary is greater than 40000.

**Q15.** Delete all records from the STUDENT table without deleting the table structure.

---

# Quick Revision

| Command | Purpose |
|---------|---------|
| UPDATE | Modifies existing records |
| SET | Specifies the new column values |
| WHERE | Selects the records to be modified or deleted |
| DELETE | Removes records from a table |

## Important Syntax

### UPDATE
```sql
UPDATE table_name
SET column_name = value
WHERE condition;
