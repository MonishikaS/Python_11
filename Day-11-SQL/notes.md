# Chapter 8 – Introduction to Structured Query Language (SQL)

## Class 11 – Informatics Practices

---

# 1. Introduction

In the previous chapter, we learned about Database Management Systems (DBMS) and Relational Database Management Systems (RDBMS).

We know that an RDBMS stores data in the form of tables.

But how do we create these tables?
How do we insert records?
How do we update existing information?
How do we retrieve particular records from a database?

For performing all these operations, we use a language called **SQL**.

### What is SQL?

SQL stands for **Structured Query Language**.

It is a standard language used to communicate with a relational database.

SQL allows us to:

1. Create databases.
2. Create tables.
3. Insert records into tables.
4. Retrieve information from tables.
5. Update existing records.
6. Delete records.
7. Modify the structure of tables.
8. Apply constraints to tables.

### Examples of RDBMS that use SQL

- MySQL
- Oracle
- Microsoft SQL Server
- PostgreSQL

### Example

Suppose a school wants to store student information.

We can create a database called `School` and a table called `STUDENT`.

| RollNumber | Name | Class |
|---|---|---|
| 1 | Aman | XI |
| 2 | Riya | XI |
| 3 | Rahul | XI |

We can use SQL commands to insert, retrieve, update and delete these records.

---

# 2. Structured Query Language (SQL)

SQL is a query language used to access and manage data stored in a database.

### Features of SQL

1. **Easy to Learn:** SQL commands use simple English-like words.
2. **Case Insensitive:** SQL keywords can be written in uppercase or lowercase.
3. **Standard Language:** It is used by many relational database systems.
4. **Data Retrieval:** It helps retrieve specific information from tables.
5. **Data Manipulation:** It allows insertion, updation and deletion of records.
6. **Database Creation:** It allows us to create databases and tables.
7. **Constraint Management:** It allows us to apply restrictions to data.

### Important Rules for Writing SQL Statements

1. SQL is case insensitive.

   `SELECT` and `select` mean the same thing.

2. Every SQL statement should end with a semicolon (`;`).

3. SQL statements can be written in multiple lines.

4. When a statement continues on another line in the MySQL command line, the prompt changes from `mysql>` to `->`.

### Example
Yes. Here is the content starting from Data Types onwards, in proper GitHub-compatible Markdown. Copy and paste the entire block directly into your `notes.md` file. No extra formatting or special code-block attributes.

````
# 4. Data Types in MySQL

## What is a Data Type?

A data type specifies the type of value that can be stored in a particular column of a table.

For example:
- A student's name contains characters.
- A student's age contains an integer.
- A date of birth contains a date.
- A percentage may contain a decimal value.

Therefore, different columns require different data types.

## Commonly Used MySQL Data Types

| Data Type | Meaning | Example |
|---|---|---|
| CHAR(n) | Fixed-length character string | CHAR(10) |
| VARCHAR(n) | Variable-length character string | VARCHAR(30) |
| INT | Stores integer values | 100 |
| FLOAT | Stores decimal values | 85.5 |
| DATE | Stores date values | '2005-08-15' |

### 4.1 CHAR(n)

CHAR is used to store fixed-length character data.

- It reserves space for the specified number of characters.
- Its length can be from 0 to 255 characters.
- If the entered value is shorter, the remaining space is padded with spaces.

**Example:**

```sql
Name CHAR(10);
````

If we insert `'Riya'`, the column reserves space for 10 characters.

Uses: Fixed-length values such as codes or identifiers.

### 4.2 VARCHAR(n)

VARCHAR is used to store variable-length character data.

- It stores strings of different lengths.
- It uses space according to the actual length of the entered string.
- Its maximum length in the textbook is 65,535 characters.

Example:

```
Name VARCHAR(30);
```

We can store:

- Aman
- Riya Sharma
- Monishika

The maximum allowed length is 30 characters.

Uses: Student names, addresses and email addresses.

### 4.3 INT

INT is used to store whole numbers without decimal points.

- It occupies 4 bytes.
- Range: -2147483648 to 2147483647.

Example:

```
Age INT;
```

Values:

- 15
- 18
- 25
- 100

### 4.4 FLOAT

FLOAT is used to store numbers containing decimal points.

It occupies 4 bytes.

Example:

```
Percentage FLOAT;
```

Values:

- 85.5
- 92.75
- 76.25

### 4.5 DATE

DATE is used to store date values.

The format is:

`YYYY-MM-DD`

Where:

- YYYY = Four-digit year
- MM = Two-digit month
- DD = Two-digit day

Example:

```
DateOfBirth DATE;
```

Valid example:

```
'2005-08-15'
```

The supported range mentioned in the textbook is:

`1000-01-01` to `9999-12-31`

### Difference Between CHAR and VARCHAR

| CHAR                              | VARCHAR                                           |
| --------------------------------- | ------------------------------------------------- |
| Fixed-length data type.           | Variable-length data type.                        |
| Reserves the specified length.    | Uses space according to the actual string length. |
| Suitable for fixed-length values. | Suitable for values with different lengths.       |
| Example: CHAR(10)                 | Example: VARCHAR(30)                              |

### Difference Between INT and FLOAT

| INT                               | FLOAT                        |
| --------------------------------- | ---------------------------- |
| Stores whole numbers.             | Stores decimal numbers.      |
| Does not store fractional values. | Can store fractional values. |
| Example: 25                       | Example: 25.75               |

# 5. Constraints in MySQL

## What are Constraints?

Constraints are restrictions applied to the values of columns in a table.

They help maintain the accuracy and reliability of data.

For example:

- A student must have a unique roll number.
- A student's name should not be empty.
- A phone number should not be repeated.
- A student record may refer to an existing guardian.

MySQL provides different constraints to enforce these rules.

## 5.1 NOT NULL Constraint

The NOT NULL constraint ensures that a column cannot contain NULL values.

Example:

```
CREATE TABLE STUDENT (
    RollNo INT,
    Name VARCHAR(30) NOT NULL
);
```

Here, the Name column cannot contain NULL.

## 5.2 UNIQUE Constraint

The UNIQUE constraint ensures that all values in a column are different.

It does not allow duplicate values.

Example:

```
CREATE TABLE STUDENT (
    RollNo INT,
    Email VARCHAR(50) UNIQUE
);
```

Here, two students cannot have the same email address.

## 5.3 DEFAULT Constraint

The DEFAULT constraint assigns a predefined value to a column when no value is provided during insertion.

Example:

```
CREATE TABLE STUDENT (
    RollNo INT,
    City VARCHAR(30) DEFAULT 'Delhi'
);
```

If we insert a student without providing the city, the default value Delhi is assigned.

## 5.4 PRIMARY KEY Constraint

A Primary Key uniquely identifies every record in a table.

Important properties:

1. It must contain unique values.
2. It cannot contain NULL values.
3. A table can have only one primary key.
4. A primary key can consist of one or more columns.

Example:

```
CREATE TABLE STUDENT (
    RollNo INT PRIMARY KEY,
    Name VARCHAR(30)
);
```

Here, RollNo is the primary key.

No two students can have the same RollNo.

## 5.5 FOREIGN KEY Constraint

A Foreign Key is a column that refers to the primary key of another table.

It is used to establish relationships between tables.

Example:

GUARDIAN Table:

| GUID | GuardianName |
| ---- | ------------ |
| 101  | Rajesh       |
| 102  | Suresh       |

STUDENT Table:

| RollNo | Name | GUID |
| ------ | ---- | ---- |
| 1      | Aman | 101  |
| 2      | Riya | 102  |

Here:

- GUID in GUARDIAN is the Primary Key.
- GUID in STUDENT is the Foreign Key.

The foreign key connects the two tables.

### Comparison of Constraints

| Constraint  | Purpose                          |
| ----------- | -------------------------------- |
| NOT NULL    | Does not allow NULL values.      |
| UNIQUE      | Does not allow duplicate values. |
| DEFAULT     | Assigns a default value.         |
| PRIMARY KEY | Uniquely identifies each record. |
| FOREIGN KEY | Connects two tables.             |

Important Question: Which two constraints together produce a Primary Key constraint?

Answer: UNIQUE and NOT NULL.

A primary key must have unique values and cannot contain NULL values.

# 6. SQL for Data Definition

## What is Data Definition?

Data Definition means defining or changing the structure of a database.

For example:

- Creating databases.
- Creating tables.
- Adding columns.
- Removing columns.
- Changing data types.
- Adding constraints.

These operations are performed using Data Definition Language (DDL) commands.

### Important DDL Commands

| Command | Purpose                                     |
| ------- | ------------------------------------------- |
| CREATE  | Creates a database or table.                |
| ALTER   | Changes the structure of an existing table. |
| DROP    | Permanently removes a table or database.    |

# 7. CREATE DATABASE Command

The CREATE DATABASE command is used to create a new database.

### Syntax

```
CREATE DATABASE database_name;
```

Example:

```
CREATE DATABASE StudentAttendance;
```

## 7.1 USE Command

After creating a database, we must select it before creating tables inside it.

The USE command selects the database that we want to work with.

### Syntax

```
USE database_name;
```

Example:

```
USE StudentAttendance;
```

## 7.2 SHOW DATABASES Command

This command displays the databases available in MySQL.

Syntax:

```
SHOW DATABASES;
```

## 7.3 SHOW TABLES Command

This command displays all the tables present in the currently selected database.

Syntax:

```
SHOW TABLES;
```

# 8. CREATE TABLE Command

## What is a Table?

A table is a collection of rows and columns used to store related information.

The CREATE TABLE command is used to create a new table in a database.

### Syntax

```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype
);
```

Every column must have:

1. A column name.
2. A data type.
3. An optional constraint.

Example:

```
CREATE TABLE STUDENT (
    RollNumber INT,
    SName VARCHAR(20),
    SDateofBirth DATE,
    GUID CHAR(12),
    PRIMARY KEY (RollNumber)
);
```

### Explanation

| Column       | Data Type   | Purpose                            |
| ------------ | ----------- | ---------------------------------- |
| RollNumber   | INT         | Stores the student's roll number.  |
| SName        | VARCHAR(20) | Stores the student's name.         |
| SDateofBirth | DATE        | Stores date of birth.              |
| GUID         | CHAR(12)    | Stores the guardian's 12-digit ID. |

Here, RollNumber is the Primary Key.

### Important Points

1. CREATE TABLE creates the structure of a table.
2. It does not automatically insert records.
3. Each column must have a name and data type.
4. Commas separate column definitions.
5. The statement ends with a semicolon.
6. The degree of a table is the number of columns.

# 9. DESCRIBE TABLE Command

The DESCRIBE command is used to display the structure of an existing table.

It shows:

- Column names.
- Data types.
- Whether NULL values are allowed.
- Key information.
- Default values.

### Syntax

```
DESCRIBE table_name;
```

OR

```
DESC table_name;
```

Example:

```
DESC STUDENT;
```

### Difference Between SHOW TABLES and DESC

| SHOW TABLES                                            | DESC                                          |
| ------------------------------------------------------ | --------------------------------------------- |
| Displays the names of tables in the selected database. | Displays the structure of a particular table. |
| Does not show column details.                          | Shows columns, data types and constraints.    |
| Example: SHOW TABLES;                                  | Example: DESC STUDENT;                        |

# 10. ALTER TABLE Command

## What is ALTER?

The ALTER TABLE command is used to modify the structure of an existing table.

We use ALTER when we want to:

1. Add a new column.
2. Remove an existing column.
3. Change the data type of a column.
4. Add a primary key.
5. Add a foreign key.
6. Add a UNIQUE constraint.
7. Add a DEFAULT value.
8. Modify constraints.

### General Syntax

```
ALTER TABLE table_name
ADD / MODIFY / DROP ...;
```

## 10.1 Adding a Primary Key

Suppose we have created the GUARDIAN table without a primary key.

Now we want to add GUID as the primary key.

### Syntax

```
ALTER TABLE table_name
ADD PRIMARY KEY (column_name);
```

Example:

```
ALTER TABLE GUARDIAN
ADD PRIMARY KEY (GUID);
```

Now GUID becomes the primary key of the GUARDIAN table.

### Adding a Composite Primary Key

A composite primary key consists of two or more columns.

Example: In the ATTENDANCE table, the combination of AttendanceDate and RollNumber uniquely identifies each attendance record.

```
ALTER TABLE ATTENDANCE
ADD PRIMARY KEY (AttendanceDate, RollNumber);
```

Here, both columns together form the primary key.

## 10.2 Adding a Foreign Key

A foreign key is used to connect two tables.

Before adding a foreign key:

1. The referenced table must already exist.
2. The referenced column must be a primary key in the referenced table.
3. The data types and sizes of both columns must match.

### Syntax

```
ALTER TABLE table_name
ADD FOREIGN KEY (column_name)
REFERENCES referenced_table_name (column_name);
```

Example:

```
ALTER TABLE STUDENT
ADD FOREIGN KEY (GUID)
REFERENCES GUARDIAN (GUID);
```

Now STUDENT is connected to GUARDIAN through GUID.

## 10.3 Adding UNIQUE Constraint

The UNIQUE constraint prevents duplicate values in a column.

### Syntax

```
ALTER TABLE table_name
ADD UNIQUE (column_name);
```

Example:

```
ALTER TABLE GUARDIAN
ADD UNIQUE (GPhone);
```

Now no two guardians can have the same phone number.

## 10.4 Adding a New Column

The ADD keyword is used to add a new column to an existing table.

### Syntax

```
ALTER TABLE table_name
ADD column_name datatype;
```

Example:

```
ALTER TABLE GUARDIAN
ADD income INT;
```

Now the GUARDIAN table contains an additional column named income.

## 10.5 Modifying Data Type of a Column

The MODIFY keyword is used to change the data type or size of an existing column.

### Syntax

```
ALTER TABLE table_name
MODIFY column_name new_datatype;
```

Example:

```
ALTER TABLE GUARDIAN
MODIFY GAddress VARCHAR(40);
```

Now GAddress can store up to 40 characters.

## 10.6 Adding NOT NULL Constraint

We can modify an existing column to prevent NULL values.

### Syntax

```
ALTER TABLE table_name
MODIFY column_name datatype NOT NULL;
```

Example:

```
ALTER TABLE STUDENT
MODIFY SName VARCHAR(20) NOT NULL;
```

Now the SName column cannot contain NULL values.

## 10.7 Adding DEFAULT Constraint

The DEFAULT keyword assigns a predefined value when a value is not provided.

### Syntax

```
ALTER TABLE table_name
MODIFY column_name datatype DEFAULT default_value;
```

Example:

```
ALTER TABLE STUDENT
MODIFY SDateofBirth DATE DEFAULT '2000-05-15';
```

If a date is not provided during insertion, the default date is assigned.

## 10.8 Removing a Column

The DROP keyword can be used with ALTER TABLE to remove a column.

### Syntax

```
ALTER TABLE table_name
DROP column_name;
```

Example:

```
ALTER TABLE GUARDIAN
DROP income;
```

The income column is permanently removed from the GUARDIAN table.

## 10.9 Removing a Primary Key

We can remove the existing primary key using DROP PRIMARY KEY.

### Syntax

```
ALTER TABLE table_name
DROP PRIMARY KEY;
```

Example:

```
ALTER TABLE GUARDIAN
DROP PRIMARY KEY;
```

The primary key constraint is removed from GUARDIAN.

### Summary of ALTER Commands

| Operation          | SQL Command                         |
| ------------------ | ----------------------------------- |
| Add a column       | ALTER TABLE ... ADD                 |
| Add primary key    | ALTER TABLE ... ADD PRIMARY KEY     |
| Add foreign key    | ALTER TABLE ... ADD FOREIGN KEY     |
| Add UNIQUE         | ALTER TABLE ... ADD UNIQUE          |
| Change data type   | ALTER TABLE ... MODIFY              |
| Add NOT NULL       | ALTER TABLE ... MODIFY ... NOT NULL |
| Add DEFAULT        | ALTER TABLE ... MODIFY ... DEFAULT  |
| Remove a column    | ALTER TABLE ... DROP column         |
| Remove primary key | ALTER TABLE ... DROP PRIMARY KEY    |

# 11. DROP Statement

## What is DROP?

The DROP command is used to permanently remove a database or table.

It removes the structure as well as the data stored inside it.

### 11.1 Drop a Table

Syntax:

```
DROP TABLE table_name;
```

Example:

```
DROP TABLE STUDENT;
```

The STUDENT table is permanently removed.

### 11.2 Drop a Database

Syntax:

```
DROP DATABASE database_name;
```

Example:

```
DROP DATABASE StudentAttendance;
```

The entire StudentAttendance database is removed, including all its tables.

### Important Points

1. DROP permanently removes a table or database.
2. It cannot be undone using a simple SQL command.
3. Dropping a database also removes all tables inside it.
4. Use DROP carefully.

# 12. SQL for Data Manipulation

## What is Data Manipulation?

Data Manipulation means working with the actual records stored inside a table.

It includes:

1. Inserting new records.
2. Retrieving existing records.
3. Updating existing records.
4. Deleting records.

### Important Commands

| Command | Purpose                    |
| ------- | -------------------------- |
| INSERT  | Adds new records.          |
| SELECT  | Retrieves records.         |
| UPDATE  | Modifies existing records. |
| DELETE  | Removes records.           |

# 13. INSERT INTO Command

The INSERT INTO command is used to insert new records into a table.

### Syntax 1: Inserting Values into All Columns

```
INSERT INTO table_name
VALUES (value1, value2, value3);
```

The values must be provided in the same order as the columns were defined in the table.

Example:

```
INSERT INTO STUDENT
VALUES (2, 'Riya', 'XI');
```

### Syntax 2: Inserting Values into Selected Columns

Sometimes we do not want to insert values into every column.

In that case, we specify the column names.

```
INSERT INTO table_name (column1, column2)
VALUES (value1, value2);
```

Example:

```
INSERT INTO STUDENT (RollNo, Name)
VALUES (3, 'Rahul');
```

If the Class column allows NULL and does not have a different default value, it will receive NULL.

### Important Points

1. Values must be entered in the correct order.
2. Text values must be enclosed in single quotes.
3. Date values must be enclosed in single quotes.
4. Numeric values are generally written without quotes.
5. When column names are not specified, values for all columns must be provided in the correct order.
6. When column names are specified, values must match the order of the listed columns.
7. When inserting a foreign key value, the referenced record must already exist in the parent table.

# 14. SQL for Data Query – SELECT Statement

## What is SELECT?

The SELECT statement is used to retrieve information from a database table.

It is also called a query statement.

It does not modify the original data.

### Syntax

```
SELECT column1, column2
FROM table_name
WHERE condition;
```

### Explanation

- SELECT: Specifies which columns we want.
- FROM: Specifies the table from which data is retrieved.
- WHERE: Specifies the condition for selecting records.
- WHERE is optional.

## 14.1 Display All Columns

The asterisk (\*) is used to retrieve all columns from a table.

```
SELECT *
FROM table_name;
```

Example:

```
SELECT *
FROM STUDENT;
```

This displays all columns and records from STUDENT.

## 14.2 Display Selected Columns

We can display only the columns that we need.

Example:

```
SELECT Name, Class
FROM STUDENT;
```

Only Name and Class are displayed.

## 14.3 Renaming Columns Using AS

Sometimes we want to display a column with a different name without changing the actual table structure.

We use the AS keyword.

This is called an alias.

### Syntax

```
SELECT column_name AS alias_name
FROM table_name;
```

Example:

```
SELECT EName AS Name
FROM EMPLOYEE;
```

The output column will be displayed as Name instead of EName.

### Renaming a Calculated Column

Suppose we want to calculate the annual salary of employees.

Annual Salary = Monthly Salary × 12

```
SELECT EName AS Name,
       Salary * 12 AS 'Annual Salary'
FROM EMPLOYEE;
```

Here:

- EName is displayed as Name.
- Salary \* 12 is displayed as Annual Salary.

# 15. DISTINCT Clause

The DISTINCT keyword is used to remove duplicate values from the query output.

It displays only unique values.

### Syntax

```
SELECT DISTINCT column_name
FROM table_name;
```

Example:

Suppose the EMPLOYEE table contains:

| EmpNo | EName    | DeptId |
| ----- | -------- | ------ |
| 101   | Aaliya   | D01    |
| 102   | Kritika  | D02    |
| 103   | Shabbir  | D01    |
| 104   | Gurpreet | D03    |
| 105   | Joseph   | D02    |

Query:

```
SELECT DISTINCT DeptId
FROM EMPLOYEE;
```

Output:

| DeptId |
| ------ |
| D01    |
| D02    |
| D03    |

### Difference Between SELECT and SELECT DISTINCT

| SELECT                         | SELECT DISTINCT                               |
| ------------------------------ | --------------------------------------------- |
| Displays all matching values.  | Displays only unique values.                  |
| Duplicate values are included. | Duplicate values are removed from the output. |

# 16. WHERE Clause

The WHERE clause is used to retrieve only those records that satisfy a particular condition.

### Syntax

```
SELECT column_name
FROM table_name
WHERE condition;
```

Example:

Display employees whose department is D01.

```
SELECT *
FROM EMPLOYEE
WHERE DeptId = 'D01';
```

## 16.1 Relational Operators

Relational operators are used to compare two values.

| Operator | Meaning                  | Example        |
| -------- | ------------------------ | -------------- |
| =        | Equal to                 | Salary = 5000  |
| >        | Greater than             | Salary > 5000  |
| <        | Less than                | Salary < 5000  |
| >=       | Greater than or equal to | Salary >= 5000 |

\|  30000;

````

This displays employees earning more than 30000.

---

# 17. Logical Operators – AND, OR, NOT

Logical operators are used to combine multiple conditions in a WHERE clause.

## 17.1 AND Operator

AND returns TRUE only when all conditions are TRUE.

**Example:**

```sql
SELECT *
FROM EMPLOYEE
WHERE Salary > 5000 AND DeptId = 'D04';
````

Both conditions must be satisfied.

## 17.2 OR Operator

OR returns TRUE when at least one condition is TRUE.

Example:

```
SELECT *
FROM EMPLOYEE
WHERE DeptId = 'D01' OR DeptId = 'D02';
```

An employee will be displayed if either condition is satisfied.

## 17.3 NOT Operator

NOT reverses the result of a condition.

Example:

```
SELECT *
FROM EMPLOYEE
WHERE NOT EName = 'Aaliya';
```

This displays all employees except Aaliya.

### Difference Between AND and OR

| AND                                           | OR                                           |
| --------------------------------------------- | -------------------------------------------- |
| All conditions must be true.                  | At least one condition must be true.         |
| Used when all requirements must be satisfied. | Used when any one requirement is sufficient. |

### Truth Table

| Condition 1 | Condition 2 | AND   | OR    |
| ----------- | ----------- | ----- | ----- |
| TRUE        | TRUE        | TRUE  | TRUE  |
| TRUE        | FALSE       | FALSE | TRUE  |
| FALSE       | TRUE        | FALSE | TRUE  |
| FALSE       | FALSE       | FALSE | FALSE |

# 18. BETWEEN Operator

The BETWEEN operator is used to retrieve values within a specified range.

It includes both boundary values.

### Syntax

```
SELECT *
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

Example:

```
SELECT *
FROM EMPLOYEE
WHERE Salary BETWEEN 20000 AND 50000;
```

This includes employees earning:

- 20000
- 30000
- 40000
- 50000

The boundary values 20000 and 50000 are also included.

BETWEEN is inclusive.

It is equivalent to:

```
WHERE Salary >= 20000 AND Salary <= 50000;
```

# 19. IN Operator

The IN operator checks whether a value matches any value in a given list.

### Syntax

```
SELECT *
FROM table_name
WHERE column_name IN (value1, value2, value3);
```

Example:

```
SELECT *
FROM EMPLOYEE
WHERE DeptId IN ('D01', 'D02', 'D04');
```

This displays employees belonging to any one of these three departments.

### Using NOT IN

NOT IN is used to exclude the values specified in a list.

Example:

```
SELECT *
FROM EMPLOYEE
WHERE DeptId NOT IN ('D01', 'D02');
```

This displays employees who do not belong to departments D01 or D02.

### Difference Between IN and OR

| IN                                                                      | OR                                    |
| ----------------------------------------------------------------------- | ------------------------------------- |
| Checks whether a value belongs to a list.                               | Combines multiple conditions.         |
| Makes queries shorter when checking multiple values of the same column. | Can be used for different conditions. |

# 20. ORDER BY Clause

ORDER BY is used to arrange the records in ascending or descending order.

By default, records are arranged in ascending order.

### Syntax

```
SELECT *
FROM table_name
ORDER BY column_name;
```

## 20.1 Ascending Order

Ascending order means arranging values from smallest to largest.

For text, it generally means alphabetical order.

```
SELECT *
FROM EMPLOYEE
ORDER BY Salary ASC;
```

The employees will be displayed from the lowest salary to the highest salary.

ASC is optional because ascending order is the default.

## 20.2 Descending Order

Descending order means arranging values from largest to smallest.

```
SELECT *
FROM EMPLOYEE
ORDER BY Salary DESC;
```

The employees will be displayed from the highest salary to the lowest salary.

## ORDER BY Using Multiple Columns

We can also arrange records using more than one column.

Example:

```
SELECT *
FROM EMPLOYEE
ORDER BY Salary, Bonus;
```

First, records are arranged by Salary. When salary values are equal, Bonus is used for further ordering.

### Difference Between ASC and DESC

| ASC                  | DESC                             |
| -------------------- | -------------------------------- |
| Ascending order.     | Descending order.                |
| Smallest to largest. | Largest to smallest.             |
| A to Z for text.     | Z to A for text.                 |
| Default order.       | Must be specified when required. |

# 21. Handling NULL Values

## What is NULL?

NULL is a special value used to represent missing, unknown or unavailable data.

Example:

| EmpNo | EName   | Bonus |
| ----- | ------- | ----- |
| 101   | Aaliya  | 500   |
| 102   | Kritika | NULL  |
| 103   | Shabbir | 700   |

Here, the bonus of Kritika is unknown or not available.

Therefore, NULL is stored.

### Important Properties of NULL

1. NULL represents missing or unknown information.
2. NULL is different from zero.
3. NULL is different from an empty string.
4. Arithmetic operations involving NULL generally produce NULL.
5. We use IS NULL to check for NULL values.
6. We use IS NOT NULL to check for values that are not NULL.

## 21.1 IS NULL

Used to retrieve records where a column contains NULL.

### Syntax

```
SELECT *
FROM table_name
WHERE column_name IS NULL;
```

Example:

```
SELECT *
FROM EMPLOYEE
WHERE Bonus IS NULL;
```

This displays employees who have no available bonus value.

## 21.2 IS NOT NULL

Used to retrieve records where a column does not contain NULL.

### Syntax

```
SELECT *
FROM table_name
WHERE column_name IS NOT NULL;
```

Example:

```
SELECT *
FROM EMPLOYEE
WHERE Bonus IS NOT NULL;
```

This displays employees whose bonus value is available.

### Difference Between NULL and 0

| NULL                                       | 0                                  |
| ------------------------------------------ | ---------------------------------- |
| Represents missing or unknown information. | Represents the numeric value zero. |
| It is not a numeric value.                 | It is a numeric value.             |
| NULL + 5 results in NULL.                  | 0 + 5 results in 5.                |
| Checked using IS NULL.                     | Checked using = 0.                 |

Important: We should not write `Bonus = NULL` to check for NULL values. Use `Bonus IS NULL`.

# 22. Substring Pattern Matching – LIKE Operator

## What is Pattern Matching?

Sometimes we do not know the complete value of a record.

We may only know a few characters.

For example:

- Find names starting with A.
- Find names ending with a.
- Find names containing the word 'an'.
- Find names having exactly five characters.

For these situations, SQL provides the LIKE operator.

## What is LIKE?

LIKE is used with WHERE to search for a specified pattern in a column.

### Syntax

```
SELECT *
FROM table_name
WHERE column_name LIKE 'pattern';
```

LIKE uses two wildcard characters.

## 22.1 Percentage Symbol (%)

The percentage symbol represents zero, one or multiple characters.

| Pattern | Meaning                        |
| ------- | ------------------------------ |
| 'A%'    | Starts with A.                 |
| '%a'    | Ends with a.                   |
| '%an%'  | Contains an anywhere.          |
| 'M%n'   | Starts with M and ends with n. |

Example: Names Starting With K

```
SELECT *
FROM EMPLOYEE
WHERE EName LIKE 'K%';
```

Example: Names Ending With a

```
SELECT *
FROM EMPLOYEE
WHERE EName LIKE '%a';
```

Example: Names Containing 'se'

```
SELECT EName
FROM EMPLOYEE
WHERE EName LIKE '%se%';
```

## 22.2 Underscore Symbol (\_)

The underscore represents exactly one character.

| Pattern    | Meaning                                                |
| ---------- | ------------------------------------------------------ |
| '\_a%'     | Second character must be a.                            |
| 'A\_'      | Starts with A and contains exactly one more character. |
| '\_\_\_\_' | Exactly four characters.                               |
| '\_ANYA'   | Exactly five characters, ending with ANYA.             |

Example: Second Character is a

```
SELECT EName
FROM EMPLOYEE
WHERE EName LIKE '_a%';
```

Example: Exactly Five Characters Ending With ANYA

```
SELECT EName
FROM EMPLOYEE
WHERE EName LIKE '_ANYA';
```

### Difference Between % and \_

| %                                             | \_                                |
| --------------------------------------------- | --------------------------------- |
| Represents zero or more characters.           | Represents exactly one character. |
| Can represent a complete group of characters. | Represents only one character.    |
| Example: 'A%'                                 | Example: 'A\_'                    |

# 23. Data Updation

## What is UPDATE?

The UPDATE statement is used to modify existing records in a table.

For example:

- Changing a student's address.
- Correcting a student's name.
- Updating a phone number.
- Changing an employee's salary.

### Syntax

```
UPDATE table_name
SET column_name = new_value
WHERE condition;
```

Example:

```
UPDATE STUDENT
SET GUID = '101010101010'
WHERE RollNumber = 3;
```

Only the record having RollNumber 3 will be updated.

## Updating Multiple Columns

We can update more than one column in a single UPDATE statement.

### Syntax

```
UPDATE table_name
SET column1 = value1,
    column2 = value2
WHERE condition;
```

Example:

```
UPDATE GUARDIAN
SET GAddress = 'Delhi',
    GPhone = '9010810547'
WHERE GUID = '466444466666';
```

The address and phone number will be updated for the guardian matching the given GUID.

### Important Warning

Always be careful while using UPDATE.

If we do not write the WHERE clause, all records in the table may be updated.

Example Without WHERE:

```
UPDATE STUDENT
SET Class = 'XII';
```

This updates the Class of every student to XII.

# 24. Data Deletion

## What is DELETE?

The DELETE statement is used to remove one or more records from a table.

It removes rows but does not remove the table structure.

### Syntax

```
DELETE FROM table_name
WHERE condition;
```

Example:

```
DELETE FROM STUDENT
WHERE RollNumber = 2;
```

Only the matching record will be deleted.

### Deleting All Records

```
DELETE FROM STUDENT;
```

This removes all records from the STUDENT table.

However, the table structure remains.

### Important Warning

If we forget the WHERE clause, all records in the table will be deleted.

Always check the condition before executing DELETE.

# 25. Difference Between Important SQL Commands

## 25.1 CREATE vs ALTER

| CREATE                               | ALTER                                     |
| ------------------------------------ | ----------------------------------------- |
| Creates a new database or table.     | Modifies an existing table structure.     |
| Used when an object does not exist.  | Used when an object already exists.       |
| Example: CREATE TABLE STUDENT (...); | Example: ALTER TABLE STUDENT ADD Age INT; |

## 25.2 ALTER vs UPDATE

| ALTER                                     | UPDATE                              |
| ----------------------------------------- | ----------------------------------- |
| Changes the structure of a table.         | Changes the data stored in a table. |
| Used to add, remove or modify columns.    | Used to modify existing records.    |
| Example: ALTER TABLE STUDENT ADD Age INT; | Example: UPDATE STUDENT SET Age=17; |

## 25.3 DELETE vs DROP

| DELETE                                       | DROP                                   |
| -------------------------------------------- | -------------------------------------- |
| Deletes records from a table.                | Removes the entire table or database.  |
| Table structure remains.                     | Table structure is removed.            |
| Can delete selected rows using WHERE.        | Removes the complete specified object. |
| Example: DELETE FROM STUDENT WHERE RollNo=1; | Example: DROP TABLE STUDENT;           |

## 25.4 DELETE vs UPDATE

| DELETE                                       | UPDATE                                                  |
| -------------------------------------------- | ------------------------------------------------------- |
| Removes records.                             | Modifies existing records.                              |
| Uses DELETE FROM.                            | Uses UPDATE and SET.                                    |
| Example: DELETE FROM STUDENT WHERE RollNo=1; | Example: UPDATE STUDENT SET Name='Riya' WHERE RollNo=1; |

## 25.5 INSERT vs UPDATE

| INSERT                                          | UPDATE                                                  |
| ----------------------------------------------- | ------------------------------------------------------- |
| Adds new records.                               | Modifies existing records.                              |
| Uses INSERT INTO.                               | Uses UPDATE and SET.                                    |
| Example: INSERT INTO STUDENT VALUES (1,'Aman'); | Example: UPDATE STUDENT SET Name='Riya' WHERE RollNo=1; |

## 25.6 DROP vs ALTER

| DROP                                   | ALTER                                      |
| -------------------------------------- | ------------------------------------------ |
| Removes a table or database.           | Modifies the structure of a table.         |
| Removes the specified database object. | Keeps the table but changes its structure. |
| Example: DROP TABLE STUDENT;           | Example: ALTER TABLE STUDENT ADD Age INT;  |

# 26. Important SQL Command Summary

| SQL Command     | Category           | Purpose                                   |
| --------------- | ------------------ | ----------------------------------------- |
| CREATE DATABASE | DDL                | Creates a database.                       |
| USE             | Database selection | Selects a database.                       |
| SHOW DATABASES  | Display            | Displays available databases.             |
| SHOW TABLES     | Display            | Displays tables in the selected database. |
| CREATE TABLE    | DDL                | Creates a table.                          |
| DESC            | Structure display  | Displays the structure of a table.        |
| ALTER TABLE     | DDL                | Changes table structure.                  |
| DROP TABLE      | DDL                | Removes a table.                          |
| DROP DATABASE   | DDL                | Removes a database.                       |
| INSERT INTO     | DML                | Inserts records.                          |
| SELECT          | Data query         | Retrieves records.                        |
| UPDATE          | DML                | Modifies existing records.                |
| DELETE          | DML                | Deletes records.                          |

# 27. Complete SQL Example – Student Database

Let's create a database and perform basic SQL operations.

## Step 1: Create a Database

```
CREATE DATABASE School;
```

## Step 2: Select the Database

```
USE School;
```

## Step 3: Create a STUDENT Table

```
CREATE TABLE STUDENT (
    RollNo INT PRIMARY KEY,
    Name VARCHAR(30) NOT NULL,
    Age INT,
    City VARCHAR(30) DEFAULT 'Delhi'
);
```

## Step 4: Check the Structure

```
DESC STUDENT;
```

## Step 5: Insert Records

```
INSERT INTO STUDENT
VALUES (1, 'Aman', 16, 'Delhi');

INSERT INTO STUDENT
VALUES (2, 'Riya', 17, 'Mumbai');

INSERT INTO STUDENT
VALUES (3, 'Rahul', 16, 'Pune');

INSERT INTO STUDENT
VALUES (4, 'Meena', 17, 'Delhi');
```

## Step 6: Display All Records

```
SELECT *
FROM STUDENT;
```

## Step 7: Display Only Names

```
SELECT Name
FROM STUDENT;
```

## Step 8: Display Students Older Than 16

```
SELECT *
FROM STUDENT
WHERE Age > 16;
```

## Step 9: Display Students From Delhi

```
SELECT *
FROM STUDENT
WHERE City = 'Delhi';
```

## Step 10: Display Unique Cities

```
SELECT DISTINCT City
FROM STUDENT;
```

## Step 11: Arrange Students by Age

```
SELECT *
FROM STUDENT
ORDER BY Age ASC;
```

## Step 12: Update a Student's City

```
UPDATE STUDENT
SET City = 'Chandigarh'
WHERE RollNo = 1;
```

## Step 13: Delete a Student Record

```
DELETE FROM STUDENT
WHERE RollNo = 4;
```

## Step 14: Add a New Column

```
ALTER TABLE STUDENT
ADD Email VARCHAR(50);
```

## Step 15: Display the Final Table

```
SELECT *
FROM STUDENT;
```

# 28. Important Definitions for Exams

| Term        | Definition                                                                  |
| ----------- | --------------------------------------------------------------------------- |
| SQL         | Structured Query Language is used to communicate with relational databases. |
| MySQL       | An open-source Relational Database Management System.                       |
| Data Type   | Specifies the type of value that a column can store.                        |
| Constraint  | A restriction applied to values in a column.                                |
| NOT NULL    | Prevents a column from storing NULL values.                                 |
| UNIQUE      | Ensures that values in a column are distinct.                               |
| DEFAULT     | Assigns a predefined value when no value is supplied.                       |
| Primary Key | Uniquely identifies each record in a table.                                 |
| Foreign Key | A column that refers to a primary key in another table.                     |
| CREATE      | Used to create databases and tables.                                        |
| ALTER       | Used to modify the structure of a table.                                    |
| DROP        | Used to permanently remove a database or table.                             |
| INSERT      | Used to add new records to a table.                                         |
| SELECT      | Used to retrieve records from a table.                                      |
| UPDATE      | Used to modify existing records.                                            |
| DELETE      | Used to remove records from a table.                                        |
| DISTINCT    | Removes duplicate values from query output.                                 |
| WHERE       | Specifies conditions for retrieving records.                                |
| BETWEEN     | Checks whether a value falls within a range, including both boundaries.     |
| IN          | Checks whether a value matches any value in a given list.                   |
| ORDER BY    | Arranges query results in ascending or descending order.                    |
| LIKE        | Searches for a specified pattern in a column.                               |
| NULL        | Represents missing, unknown or unavailable information.                     |
| Alias       | An alternative name given to a column in query output.                      |
| Wildcard    | A special character used for pattern matching.                              |

# 29. Important Points to Remember

1. SQL stands for Structured Query Language.
2. MySQL is an open-source RDBMS.
3. SQL is case insensitive.
4. Every SQL statement should end with a semicolon.
5. CHAR is a fixed-length string data type.
6. VARCHAR is a variable-length string data type.
7. INT stores whole numbers.
8. FLOAT stores decimal values.
9. DATE stores dates in YYYY-MM-DD format.
10. Constraints maintain the accuracy and reliability of data.
11. A primary key cannot contain duplicate or NULL values.
12. A foreign key connects two related tables.
13. CREATE DATABASE creates a new database.
14. USE selects a database.
15. SHOW TABLES displays tables in the selected database.
16. CREATE TABLE creates a table.
17. DESC displays the structure of a table.
18. ALTER TABLE modifies the structure of an existing table.
19. DROP permanently removes a table or database.
20. INSERT INTO adds records to a table.
21. SELECT retrieves records from a table.
22. SELECT \* retrieves all columns.
23. DISTINCT removes duplicate values from query output.
24. WHERE is used to specify conditions.
25. AND requires all conditions to be true.
26. OR requires at least one condition to be true.
27. NOT reverses a condition.
28. BETWEEN includes both boundary values.
29. IN checks values against a list.
30. ORDER BY arranges records.
31. ASC means ascending order.
32. DESC means descending order.
33. IS NULL checks for NULL values.
34. IS NOT NULL checks for non-NULL values.
35. LIKE is used for pattern matching.
36. The % wildcard represents zero or more characters.
37. The \_ wildcard represents exactly one character.
38. UPDATE modifies existing records.
39. DELETE removes records but keeps the table structure.
40. Always use WHERE carefully with UPDATE and DELETE.

# 30. Quick Revision – SQL Syntax

| Operation                | Syntax                                                  |
| ------------------------ | ------------------------------------------------------- |
| Create database          | CREATE DATABASE database_name;                          |
| Select database          | USE database_name;                                      |
| Show databases           | SHOW DATABASES;                                         |
| Show tables              | SHOW TABLES;                                            |
| Create table             | CREATE TABLE table_name (column datatype);              |
| Describe table           | DESC table_name;                                        |
| Insert record            | INSERT INTO table_name VALUES (...);                    |
| Insert selected columns  | INSERT INTO table_name (column1, column2) VALUES (...); |
| Display all columns      | SELECT \* FROM table_name;                              |
| Display selected columns | SELECT column1, column2 FROM table_name;                |
| Apply condition          | SELECT \* FROM table_name WHERE condition;              |
| Remove duplicates        | SELECT DISTINCT column FROM table_name;                 |
| Sort ascending           | SELECT \* FROM table_name ORDER BY column ASC;          |
| Sort descending          | SELECT \* FROM table_name ORDER BY column DESC;         |
| Check range              | SELECT \* FROM table_name WHERE column BETWEEN a AND b; |
| Check list               | SELECT \* FROM table_name WHERE column IN (a,b,c);      |
| Check NULL               | SELECT \* FROM table_name WHERE column IS NULL;         |
| Pattern matching         | SELECT \* FROM table_name WHERE column LIKE 'A%';       |
| Update record            | UPDATE table_name SET column=value WHERE condition;     |
| Delete record            | DELETE FROM table_name WHERE condition;                 |
| Add column               | ALTER TABLE table_name ADD column datatype;             |
| Modify column            | ALTER TABLE table_name MODIFY column datatype;          |
| Remove column            | ALTER TABLE table_name DROP column;                     |
| Drop table               | DROP TABLE table_name;                                  |
| Drop database            | DROP DATABASE database_name;                            |

# 31. Common Mistakes to Avoid

### Mistake 1: Forgetting the Semicolon

Incorrect:

```
CREATE DATABASE School
```

Correct:

```
CREATE DATABASE School;
```

### Mistake 2: Forgetting Quotes Around Text

Incorrect:

```
INSERT INTO STUDENT
VALUES (1, Aman, 16);
```

Correct:

```
INSERT INTO STUDENT
VALUES (1, 'Aman', 16);
```

### Mistake 3: Using = NULL

Incorrect:

```
SELECT *
FROM STUDENT
WHERE City = NULL;
```

Correct:

```
SELECT *
FROM STUDENT
WHERE City IS NULL;
```

### Mistake 4: Forgetting WHERE in UPDATE

Incorrect:

```
UPDATE STUDENT
SET City = 'Delhi';
```

This changes the city of every student.

Correct:

```
UPDATE STUDENT
SET City = 'Delhi'
WHERE RollNo = 1;
```

### Mistake 5: Forgetting WHERE in DELETE

Incorrect:

```
DELETE FROM STUDENT;
```

This deletes all records.

Correct:

```
DELETE FROM STUDENT
WHERE RollNo = 1;
```

### Mistake 6: Confusing DROP and DELETE

- DELETE removes records.
- DROP removes the entire table or database.

### Mistake 7: Confusing ALTER and UPDATE

- ALTER changes table structure.
- UPDATE changes the data inside a table.

```
```

```sql
CREATE DATABASE School;
