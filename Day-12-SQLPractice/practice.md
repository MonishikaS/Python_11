# Chapter 8 – SQL Practice Questions
## Class 11 – Informatics Practices

# Section A – Predict the Output (Q1–Q15)

**Instructions:** Read each SQL query carefully and predict its output or identify the error. Assume that the required database and tables exist wherever necessary.

### Q1. Predict the output.

```sql
CREATE DATABASE SCHOOL;
SHOW DATABASES;
```

What will be displayed after executing these commands?

### Q2. Predict the result of the following commands.

```sql
CREATE DATABASE LIBRARY;
USE LIBRARY;
CREATE TABLE BOOK (
    BookID INT,
    BookName VARCHAR(30)
);
SHOW TABLES;
```

Which table name will be displayed?

### Q3. Identify the error, if any.

```sql
CREATE TABLE STUDENT (
    RollNo INT,
    Name VARCHAR(30),
    Age INT
);

CREATE TABLE STUDENT (
    StudentID INT,
    City VARCHAR(20)
);
```

Can two tables with the same name be created in the same database?

### Q4. Predict the output of the following query.

Consider a table named EMPLOYEE:

| EmpID | EmpName | Salary |
|---|---|---:|
| 101 | Aman | 25000 |
| 102 | Riya | 30000 |
| 103 | Karan | 28000 |

```sql
SELECT * FROM EMPLOYEE;
```

How many columns and rows will be displayed?

### Q5. Predict the output.

Using the same EMPLOYEE table:

```sql
SELECT EmpName, Salary
FROM EMPLOYEE;
```

Which columns will appear in the result?

### Q6. Identify the error in the following SQL statement.

```sql
CREATE TABLE PRODUCT (
    ProductID INT,
    ProductName VARCHAR(40),
    Price FLOAT,
);
```

Is the trailing comma after the last column valid in this CREATE TABLE statement?

### Q7. Predict the result of the following commands.

```sql
CREATE DATABASE COLLEGE;
USE COLLEGE;

CREATE TABLE COURSE (
    CourseID INT,
    CourseName VARCHAR(30)
);

DESC COURSE;
```

What information will DESC display?

### Q8. Predict the result.

```sql
CREATE DATABASE COMPANY;
USE COMPANY;

CREATE TABLE DEPARTMENT (
    DeptID INT,
    DeptName VARCHAR(30)
);

INSERT INTO DEPARTMENT
VALUES (1, 'HR');

SELECT * FROM DEPARTMENT;
```

Which record will be displayed?

### Q9. Identify the error.

```sql
CREATE DATABASE SHOP;
USE SHOP;

CREATE TABLE CUSTOMER (
    CustomerID INT,
    CustomerName VARCHAR(30)
);

INSERT INTO CUSTOMER
VALUES (101);
```

Why will this INSERT statement fail?

### Q10. Predict the result.

Assume a table named MOBILE has the following records:

| MobileID | Brand | Price |
|---|---|---:|
| 1 | Samsung | 25000 |
| 2 | Apple | 60000 |
| 3 | Vivo | 18000 |

```sql
SELECT Brand
FROM MOBILE;
```

How many columns and records will be displayed?

### Q11. What happens after executing the following commands?

```sql
ALTER TABLE STUDENT
ADD Email VARCHAR(50);

DESC STUDENT;
```

What change will be visible in the table structure?

### Q12. Predict the result of the following commands.

```sql
CREATE DATABASE OFFICE;
USE OFFICE;

CREATE TABLE STAFF (
    StaffID INT,
    StaffName VARCHAR(30)
);

ALTER TABLE STAFF
ADD Salary INT;
```

How many columns will STAFF contain after ALTER TABLE?

### Q13. Identify the problem in the following command.

```sql
DROP TABLE EMPLOYEE;
SELECT * FROM EMPLOYEE;
```

What happens when the SELECT statement is executed after dropping the table?

### Q14. Predict the result.

```sql
CREATE DATABASE HOTEL;
USE HOTEL;

CREATE TABLE ROOM (
    RoomNo INT,
    RoomType VARCHAR(20)
);

INSERT INTO ROOM
VALUES
(101, 'Deluxe'),
(102, 'Single'),
(103, 'Suite');

SELECT RoomNo
FROM ROOM;
```

How many rows will be displayed, and which column will appear?

### Q15. Predict the result of the following commands.

```sql
CREATE DATABASE SPORTS;
DROP DATABASE SPORTS;
SHOW DATABASES;
```

Will SPORTS appear in the list of databases after executing all three commands? Explain why.

---

# Section B – Practical SQL Query Writing (Q16–Q30)

**Instructions:** Write the required SQL commands for each question. Create the database and tables wherever required. Insert the given records and execute the SELECT queries.

## Q16. School Database

Create a database named `SCHOOL_DB`.

Create a table named `STUDENT` with the following columns:

| Column Name | Data Type |
|---|---|
| RollNo | INT |
| StudentName | VARCHAR(30) |
| Class | INT |
| Section | CHAR(1) |

Perform the following tasks:

1. Create the database.
2. Select the database.
3. Create the STUDENT table.
4. Display all databases.
5. Display all tables in the selected database.
6. Display the structure of STUDENT.

## Q17. Book Store Database

Create a database named `BOOK_STORE`.

Create a table `BOOKS` with the following columns:

| Column Name | Data Type |
|---|---|
| BookID | INT |
| BookName | VARCHAR(40) |
| Author | VARCHAR(30) |
| Price | FLOAT |

Insert the following records:

| BookID | BookName | Author | Price |
|---|---|---|---:|
| 1 | Python Basics | R Sharma | 350 |
| 2 | SQL for Beginners | A Verma | 420 |
| 3 | Computer Networks | S Kumar | 500 |
| 4 | Learn Java | P Singh | 450 |

Write queries to:

1. Create the database and table.
2. Insert all four records.
3. Display all records.
4. Display only BookName and Author.
5. Display only BookID and Price.

## Q18. Employee Database

Create a database named `EMP_DB`.

Create a table `EMPLOYEE` with:

| Column Name | Data Type |
|---|---|
| EmpID | INT |
| EmpName | VARCHAR(30) |
| Department | VARCHAR(20) |
| Salary | FLOAT |

Insert these records:

| EmpID | EmpName | Department | Salary |
|---|---|---|---:|
| 101 | Aman | HR | 25000 |
| 102 | Riya | IT | 35000 |
| 103 | Karan | Sales | 28000 |

Write SQL queries to:

1. Create the database and table.
2. Insert all records.
3. Display the complete EMPLOYEE table.
4. Display only employee names.
5. Display employee names and departments.

## Q19. Hospital Database

Create a database named `HOSPITAL`.

Create a table `PATIENT` with:

| Column Name | Data Type |
|---|---|
| PatientID | INT |
| PatientName | VARCHAR(30) |
| Age | INT |
| Disease | VARCHAR(40) |

Insert the following records:

| PatientID | PatientName | Age | Disease |
|---|---|---:|---|
| 1 | Meera | 25 | Fever |
| 2 | Rahul | 40 | Diabetes |
| 3 | Simran | 32 | Allergy |
| 4 | Arjun | 28 | Cold |

Write queries to:

1. Create the database.
2. Create the PATIENT table.
3. Insert all four records.
4. Display all records.
5. Display only PatientName and Disease.

## Q20. Online Shopping Database

Create a database named `SHOPPING`.

Create a table `PRODUCT` with:

| Column Name | Data Type |
|---|---|
| ProductID | INT |
| ProductName | VARCHAR(40) |
| Category | VARCHAR(20) |
| Price | FLOAT |
| Quantity | INT |

Insert the following records:

| ProductID | ProductName | Category | Price | Quantity |
|---|---|---|---:|---:|
| 1 | Laptop | Electronics | 55000 | 5 |
| 2 | Chair | Furniture | 2500 | 10 |
| 3 | Headphones | Electronics | 1500 | 20 |
| 4 | Table | Furniture | 4500 | 8 |

Write queries to:

1. Create the database and table.
2. Insert all records.
3. Display the complete PRODUCT table.
4. Display only ProductName and Price.
5. Display only ProductID, Category and Quantity.

## Q21. College Database – ALTER TABLE

Create a database named `COLLEGE_DB`.

Create a table `STUDENT` with:

| Column Name | Data Type |
|---|---|
| StudentID | INT |
| StudentName | VARCHAR(30) |
| Course | VARCHAR(20) |

Insert these records:

| StudentID | StudentName | Course |
|---|---|---|
| 1 | Aditi | CSE |
| 2 | Rohan | ECE |
| 3 | Neha | CSE |

Now perform the following operations:

1. Add a column `Age` of type INT.
2. Add a column `Email` of type VARCHAR(50).
3. Display the updated table structure.
4. Display all records after altering the table.

## Q22. Library Database – MODIFY Column

Create a database named `LIBRARY_DB`.

Create a table `BOOK` with:

| Column Name | Data Type |
|---|---|
| BookID | INT |
| BookName | VARCHAR(20) |
| Author | VARCHAR(20) |

Insert the following records:

| BookID | BookName | Author |
|---|---|---|
| 1 | Python | Sharma |
| 2 | SQL | Verma |
| 3 | Java | Kumar |

Perform the following operations:

1. Increase the size of BookName from VARCHAR(20) to VARCHAR(50).
2. Change the size of Author from VARCHAR(20) to VARCHAR(40).
3. Display the updated structure using DESC.
4. Display all records.

## Q23. Restaurant Database – ADD and DROP COLUMN

Create a database named `RESTAURANT_DB`.

Create a table `MENU` with:

| Column Name | Data Type |
|---|---|
| ItemID | INT |
| ItemName | VARCHAR(30) |
| Price | FLOAT |

Insert:

| ItemID | ItemName | Price |
|---|---|---:|
| 1 | Pizza | 250 |
| 2 | Burger | 120 |
| 3 | Pasta | 180 |

Perform the following operations:

1. Add a column `Category` of type VARCHAR(20).
2. Add a column `Availability` of type CHAR(1).
3. Remove the column `Availability`.
4. Display the final structure of MENU.
5. Display all records.

## Q24. Banking Database – DEFAULT Constraint

Create a database named `BANK_DB`.

Create a table `ACCOUNT` with:

| Column Name | Data Type |
|---|---|
| AccountNo | INT |
| HolderName | VARCHAR(30) |
| Balance | FLOAT |
| Branch | VARCHAR(30) |

Apply a DEFAULT value of `'Main Branch'` to the Branch column.

Insert the following records:

| AccountNo | HolderName | Balance |
|---|---|---:|
| 101 | Ananya | 15000 |
| 102 | Varun | 25000 |
| 103 | Priya | 18000 |

Perform the following tasks:

1. Create the database and table with the DEFAULT constraint.
2. Insert the three records without specifying Branch.
3. Display all records.
4. Display the table structure.

## Q25. University Database – UNIQUE Constraint

Create a database named `UNIVERSITY_DB`.

Create a table `FACULTY` with:

| Column Name | Data Type |
|---|---|
| FacultyID | INT |
| FacultyName | VARCHAR(30) |
| Email | VARCHAR(50) |
| Department | VARCHAR(20) |

Apply a UNIQUE constraint on Email.

Insert the following records:

| FacultyID | FacultyName | Email | Department |
|---|---|---|---|
| 1 | Rakesh | rakesh@gmail.com | CSE |
| 2 | Neelam | neelam@gmail.com | ECE |
| 3 | Amit | amit@gmail.com | IT |

Perform the following tasks:

1. Create the database and table.
2. Insert all three records.
3. Display all records.
4. Try inserting another faculty member using the email `rakesh@gmail.com`.
5. Observe what happens and explain why.

## Q26. Transport Database – RENAME TABLE

Create a database named `TRANSPORT_DB`.

Create a table `VEHICLE` with:

| Column Name | Data Type |
|---|---|
| VehicleID | INT |
| VehicleName | VARCHAR(30) |
| VehicleType | VARCHAR(20) |

Insert the following records:

| VehicleID | VehicleName | VehicleType |
|---|---|---|
| 1 | Swift | Car |
| 2 | Activa | Scooter |
| 3 | Creta | Car |

Perform the following operations:

1. Create the database and table.
2. Insert all records.
3. Rename the table VEHICLE to TRANSPORT.
4. Display all tables in the database.
5. Display the structure of TRANSPORT.
6. Retrieve all records from TRANSPORT.

## Q27. Sports Database – Multiple Tables

Create a database named `SPORTS_DB`.

Create the following two tables:

**Table 1: PLAYER**

| Column Name | Data Type |
|---|---|
| PlayerID | INT |
| PlayerName | VARCHAR(30) |
| Age | INT |

**Table 2: TEAM**

| Column Name | Data Type |
|---|---|
| TeamID | INT |
| TeamName | VARCHAR(30) |
| CoachName | VARCHAR(30) |

Insert the following records.

PLAYER:

| PlayerID | PlayerName | Age |
|---|---|---:|
| 1 | Virat | 35 |
| 2 | Rohit | 38 |
| 3 | Hardik | 32 |

TEAM:

| TeamID | TeamName | CoachName |
|---|---|---|
| 101 | Tigers | Aman |
| 102 | Panthers | Rahul |
| 103 | Warriors | Karan |

Write queries to:

1. Create the database.
2. Create both tables.
3. Insert the records into both tables.
4. Display all tables.
5. Display the structure of both tables.
6. Display all records from PLAYER.
7. Display only TeamName and CoachName from TEAM.

## Q28. Hotel Database – DROP TABLE

Create a database named `HOTEL_DB`.

Create two tables:

**ROOM**

| Column Name | Data Type |
|---|---|
| RoomID | INT |
| RoomType | VARCHAR(30) |
| Price | FLOAT |

**CUSTOMER**

| Column Name | Data Type |
|---|---|
| CustomerID | INT |
| CustomerName | VARCHAR(30) |
| City | VARCHAR(30) |

Insert at least two records into each table.

Perform the following operations:

1. Display all tables.
2. Display all records from both tables.
3. Drop the ROOM table.
4. Display all tables again.
5. Explain what happened to the CUSTOMER table.

## Q29. Examination Database – DROP DATABASE

Create a database named `EXAM_DB`.

Create two tables:

**STUDENT**

| Column Name | Data Type |
|---|---|
| RollNo | INT |
| StudentName | VARCHAR(30) |
| Marks | INT |

**SUBJECT**

| Column Name | Data Type |
|---|---|
| SubjectID | INT |
| SubjectName | VARCHAR(30) |

Perform the following operations:

1. Create the database.
2. Select the database.
3. Create both tables.
4. Insert at least three records into STUDENT.
5. Insert at least three records into SUBJECT.
6. Display all tables.
7. Display all records from STUDENT.
8. Drop the complete EXAM_DB database.
9. Explain what happens to both tables after dropping the database.

## Q30. Complete Database Creation Challenge

A company wants to maintain details of its products and suppliers.

Create a database named `COMPANY_STORE`.

Create the following tables:

**PRODUCT**

| Column Name | Data Type |
|---|---|
| ProductID | INT |
| ProductName | VARCHAR(40) |
| Price | FLOAT |
| Quantity | INT |

**SUPPLIER**

| Column Name | Data Type |
|---|---|
| SupplierID | INT |
| SupplierName | VARCHAR(30) |
| City | VARCHAR(30) |

Insert the following records.

PRODUCT:

| ProductID | ProductName | Price | Quantity |
|---|---|---:|---:|
| 101 | Keyboard | 800 | 15 |
| 102 | Mouse | 450 | 20 |
| 103 | Monitor | 8500 | 5 |
| 104 | Printer | 6500 | 3 |

SUPPLIER:

| SupplierID | SupplierName | City |
|---|---|---|
| 1 | Tech Solutions | Delhi |
| 2 | Digital World | Mumbai |
| 3 | Smart Systems | Bengaluru |

Perform all the following operations:

1. Create the COMPANY_STORE database.
2. Select the database.
3. Create both tables.
4. Insert all records into both tables.
5. Display all databases.
6. Display all tables in COMPANY_STORE.
7. Display the structure of PRODUCT and SUPPLIER.
8. Display all records from PRODUCT.
9. Display only ProductName and Price from PRODUCT.
10. Add a column `Warranty` of type INT to PRODUCT.
11. Add a column `Email` of type VARCHAR(50) to SUPPLIER.
12. Modify the ProductName column to VARCHAR(60).
13. Display the updated table structures.
14. Rename the SUPPLIER table to VENDOR.
15. Display all tables again.
16. Display all records from VENDOR.

---

# End of Practice Worksheet


- [ ] DROP DATABASE

**Practice Rule:** Write every SQL query in MySQL Workbench and verify the result. Do not just read the questions.
