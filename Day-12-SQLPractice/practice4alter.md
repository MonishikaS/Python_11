# SQL Practice Worksheet – ALTER TABLE
## Class 11 – Informatics Practices

### Instructions
Write the SQL query for each question. Do not write the output.

Use the following table structures.

## Table 1: STUDENT

| Column Name | Data Type |
|---|---|
| RollNo | INT |
| Name | VARCHAR(30) |
| Class | INT |
| Marks | INT |

## Table 2: EMPLOYEE

| Column Name | Data Type |
|---|---|
| EmpID | INT |
| EmpName | VARCHAR(30) |
| Department | VARCHAR(20) |
| Salary | INT |

## Table 3: PRODUCT

| Column Name | Data Type |
|---|---|
| ProductID | INT |
| ProductName | VARCHAR(30) |
| Price | INT |
| Quantity | INT |

---

## Section A: Add a Column

**Q1.** Add a new column named `City` with datatype `VARCHAR(25)` to the STUDENT table.

**Q2.** Add a column named `Email` with datatype `VARCHAR(50)` to the EMPLOYEE table.

**Q3.** Add a column named `ManufacturingDate` with datatype `DATE` to the PRODUCT table.

**Q4.** Add a column named `PhoneNumber` with datatype `VARCHAR(15)` to the STUDENT table.

**Q5.** Add a column named `Bonus` with datatype `INT` to the EMPLOYEE table.

---

## Section B: Modify a Column

**Q6.** Change the size of the `Name` column in the STUDENT table from `VARCHAR(30)` to `VARCHAR(50)`.

**Q7.** Change the datatype of the `Salary` column in the EMPLOYEE table to `DECIMAL(10,2)`.

**Q8.** Increase the size of the `ProductName` column in the PRODUCT table to `VARCHAR(60)`.

**Q9.** Change the datatype of the `Marks` column in the STUDENT table to `DECIMAL(5,2)`.

---

## Section C: Drop a Column

**Q10.** Remove the `PhoneNumber` column from the STUDENT table.

**Q11.** Remove the `Bonus` column from the EMPLOYEE table.

**Q12.** Delete the `ManufacturingDate` column from the PRODUCT table.

---

## Section D: Rename a Column

**Q13.** Rename the `Name` column of the STUDENT table to `StudentName`.

**Q14.** Rename the `EmpName` column of the EMPLOYEE table to `EmployeeName`.

---

## Section E: Add a Constraint

**Q15.** Add a UNIQUE constraint to the `Email` column of the EMPLOYEE table.

---

# Quick Revision – ALTER TABLE

| Operation | Syntax |
|---|---|
| Add column | `ALTER TABLE table_name ADD column_name datatype;` |
| Modify column | `ALTER TABLE table_name MODIFY column_name new_datatype;` |
| Drop column | `ALTER TABLE table_name DROP COLUMN column_name;` |
| Rename column | `ALTER TABLE table_name RENAME COLUMN old_name TO new_name;` |
| Add UNIQUE | `ALTER TABLE table_name ADD CONSTRAINT constraint_name UNIQUE (column_name);` |

**Note:** These queries use MySQL syntax. `RENAME COLUMN` is supported in MySQL 8.0 and later.
