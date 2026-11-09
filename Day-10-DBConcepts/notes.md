# Chapter 7 – Database Concepts
## Class 11 – Informatics Practices

---

# 1. Introduction

Data is important in schools, banks, hospitals, shops and many other places.

Data needs to be stored in an organised manner so that it can be easily:
- Accessed
- Updated
- Deleted
- Searched
- Shared

### Example: School Database

A school maintains information about:
- Students
- Teachers
- Parents
- Attendance
- Examination results
- Fees

Maintaining all this information manually in registers becomes difficult.

### Problems with Manual Record Keeping

1. Repeated writing of the same information.
2. Chances of spelling mistakes.
3. Difficulty in finding information.
4. Registers may get lost or damaged.
5. Updating information takes time.
6. Calculations may contain errors.

Therefore, computers are used to store and manage data.

---

# 2. File System

A **File** is a container used to store data on a computer.

A file may contain:
- Text
- Images
- Videos
- Audio
- Program code
- CSV data

A **File System** stores information in separate files.

### Example

A school may maintain two files:

**STUDENT File**

| RollNumber | SName | SDateofBirth | GName | GPhone |
|---|---|---|---|---|
| 1 | Atharv | 2003-05-15 | Amit | 9876543210 |
| 2 | Daizy | 2002-02-28 | Rahul | 9876543211 |

**ATTENDANCE File**

| AttendanceDate | RollNumber | SName | AttendanceStatus |
|---|---|---|---|
| 2026-11-01 | 1 | Atharv | P |
| 2026-11-01 | 2 | Daizy | A |
| 2026-11-02 | 1 | Atharv | P |

P = Present  
A = Absent

## 2.1 Limitations of File System

### 1. Difficulty in Access

Retrieving required information from files can be difficult.

An application program may be required to search for particular information.

**Example:** Finding all students who were absent on a particular date.

### 2. Data Redundancy

Data redundancy means storing the same information multiple times in different files.

**Example:** Student name is stored in both STUDENT and ATTENDANCE files.

**Disadvantages:**
- Wastes storage space.
- Makes data management difficult.
- Can cause data inconsistency.

### 3. Data Inconsistency

Data inconsistency occurs when the same information stored in different files does not match.

**Example:**

If a student's name is updated in the STUDENT file but not in the ATTENDANCE file, both files will contain different names.

### 4. Data Isolation

Data isolation means related information is stored in different files without proper connections.

**Example:** STUDENT and ATTENDANCE files contain related information but are maintained separately.

### 5. Data Dependence

Data dependence occurs when application programs depend on the structure or format of files.

If the file structure changes, the application programs may also need modifications.

**Example:** Changing column names may cause an existing application program to stop working.

### 6. Controlled Data Sharing

Different users should have different permissions to access data.

**Example:**
- Teachers can update attendance.
- Parents can only view attendance.
- Administrators can access student information.

Providing controlled access is difficult in an ordinary file system.

### Summary: Limitations of File System

| Limitation | Meaning |
|---|---|
| Difficulty in Access | Searching and retrieving data is difficult. |
| Data Redundancy | Same information is stored repeatedly. |
| Data Inconsistency | Different copies of data do not match. |
| Data Isolation | Related data is stored separately. |
| Data Dependence | Programs depend on file structure. |
| Controlled Data Sharing | Managing user permissions is difficult. |

---

# 3. Database Management System (DBMS)

A **Database** is an organised collection of logically related data.

A **Database Management System (DBMS)** is software used to create, store, retrieve and manage databases.

### Functions of DBMS

1. Creating databases.
2. Storing information.
3. Retrieving information.
4. Inserting new records.
5. Updating existing records.
6. Deleting records.

### Examples of DBMS

- MySQL
- Oracle
- PostgreSQL
- Microsoft Access
- SQL Server
- MongoDB

### Role of DBMS

A DBMS acts as an interface between the database and the user or application program.

### Querying a Database

Querying means requesting information from a database.

**Example:** Finding the names of students who were present on a particular date.

## 3.1 Applications of Database

| Application | Information Stored |
|---|---|
| Banking | Customer and account details |
| Schools | Student and teacher details |
| Hospitals | Patient and doctor details |
| Online Shopping | Products and customer details |
| Organisations | Employee and salary details |
| Inventory | Products and stock details |

## 3.2 Converting File System into Database

Consider the school example.

Initially, the school maintains separate STUDENT and ATTENDANCE files.

To improve the system, we can divide information into three tables.

### 1. STUDENT Table

| RollNumber | SName | SDateofBirth | GUID |
|---|---|---|---|

### 2. GUARDIAN Table

| GUID | GName | GPhone | GAddress |
|---|---|---|---|

### 3. ATTENDANCE Table

| AttendanceDate | RollNumber | AttendanceStatus |
|---|---|---|

### Why are three tables created?

1. Student names need not be repeated in the attendance table.
2. Guardian information can be stored separately.
3. GUID uniquely identifies a guardian.
4. Related tables can be connected using common fields.

### Advantages

- Reduces data redundancy.
- Improves data consistency.
- Makes data management easier.
- Helps connect related information.

### Costs of Using DBMS

1. Purchasing hardware and software.
2. Training users.
3. Regular backup and recovery expenses.

---

# 4. Important DBMS Concepts

## 4.1 Database Schema

A **Database Schema** is the design or structure of a database.

It defines:
- Table names.
- Column names.
- Data types.
- Constraints.
- Relationships between tables.

**Example:**

A STUDENT table may contain:

- RollNumber
- SName
- SDateofBirth
- GUID

Remember: Schema means the structure of a database.

## 4.2 Data Constraint

A **Data Constraint** is a rule or restriction applied to data entered into a database.

Examples:
- Roll number must be unique.
- Roll number cannot be NULL.
- Mobile number must contain 10 digits.

Constraints help maintain accurate data.

## 4.3 Metadata / Data Dictionary

Metadata means **Data About Data**.

It describes the structure and properties of information stored in a database.

Example:

Information that:
- RollNumber is an integer.
- SName is a character field.
- RollNumber must be unique.

This information is metadata.

## 4.4 Database Instance

A **Database Instance** is the state or snapshot of a database at a particular time.

It changes whenever records are:
- Inserted
- Updated
- Deleted

### Schema vs Instance

| Schema | Instance |
|---|---|
| Structure of database | Actual database state |
| Defines tables and columns | Contains actual records |
| Changes less frequently | Changes frequently |

## 4.5 Query

A **Query** is a request made to a database to retrieve information.

Example:

Finding all students who were present on a particular date.

## 4.6 Data Manipulation

Data manipulation means changing the information stored in a database.

Three basic operations:

### 1. Insertion

Adding new records to a database.

Example: Adding a new student's details.

### 2. Deletion

Removing existing records.

Example: Deleting a student's record.

### 3. Update

Modifying existing information.

Example: Updating a guardian's phone number.

## 4.7 Database Engine

A **Database Engine** is the underlying component of a DBMS that handles database creation, retrieval and manipulation of data.

## 4.8 Limitations of DBMS

1. **Increased Complexity:** Managing security, consistency and data sharing makes the system complex.
2. **Increased Data Vulnerability:** Hardware or software failures may affect centrally stored information.

---

# 5. Relational Data Model

A **Data Model** describes how data is organised and represented in a database.

The Relational Data Model is one of the most commonly used data models.

In this model, data is stored in tables.

### Important Terms

| Database Term | Meaning |
|---|---|
| Relation | Table |
| Tuple | Row |
| Attribute | Column |
| Domain | Set of allowed values |

### Other Data Models

1. Object-Oriented Data Model
2. Entity-Relationship Data Model
3. Document Model
4. Hierarchical Data Model

## 5.1 Terminology of Relational Data Model

### 1. Relation

A relation is a table containing data arranged in rows and columns.

Example: STUDENT table.

### 2. Attribute

An attribute is a column or field in a table.

Example:

In STUDENT:

- RollNumber
- SName
- Age
- Class

These are attributes.

### 3. Tuple

A tuple is a row or record in a table.

Example:

| RollNumber | Name | Age |
|---|---|---|
| 101 | Rahul | 16 |

The complete row represents one tuple.

### 4. Domain

A domain is the set of valid values that an attribute can contain.

Examples:

- Age → Integer values.
- Name → Character values.
- DateOfBirth → Date values.

### 5. Degree

Degree means the total number of columns or attributes in a relation.

Example:

| RollNumber | Name | Age | Class |
|---|---|---|---|

Degree = 4

### 6. Cardinality

Cardinality means the total number of rows or tuples in a relation.

Example:

| RollNumber | Name |
|---|---|
| 1 | Rahul |
| 2 | Aman |
| 3 | Priya |

Cardinality = 3

### Degree vs Cardinality

| Degree | Cardinality |
|---|---|
| Number of columns | Number of rows |
| Number of attributes | Number of tuples |
| Also called width | Also called number of records |

**Remember:**
- Degree = Columns
- Cardinality = Rows

## 5.2 Flat File

A relation is called a flat file when:

1. Each column contains a single value in a row.
2. Every record has the same number of columns.

---

# 6. Properties of a Relation

There are three important properties of a relation.

## Property 1: Attributes (Columns)

- Every attribute must have a unique name.
- The order of columns does not matter.

## Property 2: Tuples (Rows)

- Every tuple must be distinct.
- The order of rows does not matter.

## Property 3: Data Values

- All values in an attribute must belong to the same domain.
- Every value must be atomic.
- One attribute cannot contain multiple values in a single tuple.
- NULL can be used when a value is unknown or not applicable.

## 6.1 NULL Value

NULL is a special value used when the actual value is unknown or not applicable.

Example:

If a guardian has not provided a phone number, GPhone may contain NULL.

**Important:**

NULL is different from:
- Zero (0)
- Empty string ("")
- The word "NULL"

---

# 7. Keys in Relational Database

A **Key** is an attribute or combination of attributes used to identify records or establish relationships between tables.

Keys help identify records uniquely and connect related tables.

There are five important types of keys.

## 7.1 Candidate Key

A **Candidate Key** is an attribute or combination of attributes that can uniquely identify every row in a table.

A table can have multiple candidate keys.

Example:

In the GUARDIAN table:

| GUID | GName | GPhone |
|---|---|---|
| G01 | Amit | 9876543210 |
| G02 | Rahul | 9876543211 |

If both GUID and GPhone are unique, both can be candidate keys.

## 7.2 Primary Key

A **Primary Key** is the candidate key selected to uniquely identify every record in a table.

### Properties of Primary Key

1. Must contain unique values.
2. Cannot contain duplicate values.
3. Cannot contain NULL values.
4. Only one primary key is selected for a table.
5. It can consist of one or more attributes.

Example:

In STUDENT:

| RollNumber (PK) | Name |
|---|---|
| 101 | Rahul |
| 102 | Aman |
| 103 | Priya |

RollNumber is the primary key.

## 7.3 Alternate Key

An **Alternate Key** is a candidate key that is not selected as the primary key.

Example:

Suppose GUID and GPhone are both candidate keys.

If GUID is selected as the primary key, GPhone becomes the alternate key.

## 7.4 Composite Primary Key

A **Composite Primary Key** is a primary key made by combining two or more attributes.

It is used when a single attribute cannot uniquely identify every record.

Example: ATTENDANCE Table

| AttendanceDate | RollNumber | Status |
|---|---|---|
| 01-11-2026 | 101 | P |
| 01-11-2026 | 102 | A |
| 02-11-2026 | 101 | P |

Here:

- AttendanceDate alone is not unique.
- RollNumber alone is not unique.
- Both together uniquely identify an attendance record.

Therefore:

**Composite Primary Key = AttendanceDate + RollNumber**

## 7.5 Foreign Key

A **Foreign Key** is an attribute in one table that refers to the primary key of another table.

It is used to establish relationships between tables.

Example:

### GUARDIAN Table

| GUID (Primary Key) | GName |
|---|---|
| G01 | Amit |
| G02 | Rahul |

### STUDENT Table

| RollNumber (PK) | SName | GUID (FK) |
|---|---|---|
| 101 | Aman | G01 |
| 102 | Priya | G02 |

Here:

- GUID is the primary key in GUARDIAN.
- GUID is the foreign key in STUDENT.
- STUDENT refers to GUARDIAN using GUID.

### Important Terms

**Referencing Relation:**
The table containing the foreign key.

**Referenced Relation:**
The table whose primary key is referred to by another table.

### Another Example

- RollNumber is the primary key in STUDENT.
- RollNumber is the foreign key in ATTENDANCE.

This connects the attendance records with the student records.

## 7.6 Comparison of All Keys

| Key | Definition |
|---|---|
| Candidate Key | Attribute(s) that can uniquely identify a record |
| Primary Key | Selected candidate key |
| Alternate Key | Candidate key not selected as primary key |
| Composite Primary Key | Primary key consisting of multiple attributes |
| Foreign Key | Attribute referring to another table's primary key |

---

# 8. RDBMS and SQL

## RDBMS

RDBMS stands for **Relational Database Management System**.

It is a database management system that stores data in related tables.

### Features of RDBMS

1. Stores data in tables.
2. Tables contain rows and columns.
3. Tables can be connected using keys.
4. Helps maintain data integrity.
5. Supports data retrieval and manipulation.

### SQL

SQL stands for **Structured Query Language**.

It is used to communicate with relational databases.

SQL is used to:
- Create tables.
- Insert records.
- Retrieve information.
- Update records.
- Delete records.

Examples of relational database systems:

- MySQL
- Oracle
- PostgreSQL
- SQL Server

---

# 9. Important Differences for Exams

## Database vs DBMS

| Database | DBMS |
|---|---|
| Organised collection of data | Software used to manage databases |
| Contains actual information | Provides operations to manage information |
| Example: Student database | Example: MySQL |

## File System vs DBMS

| File System | DBMS |
|---|---|
| Stores data in separate files | Stores related data in a database |
| Data redundancy is common | Database design can reduce redundancy |
| Data inconsistency may occur | Helps maintain consistency |
| Related files are not automatically linked | Tables can be connected using keys |
| Access control is difficult | Provides user access management |
| Programs depend on file structure | Provides organised data management |

## Schema vs Instance

| Schema | Instance |
|---|---|
| Database structure | Database state |
| Defines tables and columns | Contains actual records |
| Changes less frequently | Changes frequently |

## Degree vs Cardinality

| Degree | Cardinality |
|---|---|
| Number of columns | Number of rows |
| Attributes | Tuples |

## Primary Key vs Foreign Key

| Primary Key | Foreign Key |
|---|---|
| Uniquely identifies records | Connects related tables |
| Cannot contain duplicate values | Duplicate values are allowed |
| Cannot contain NULL | May contain NULL if not part of its own primary key |
| One selected primary key per table | A table may contain multiple foreign keys |

---

# 10. Quick Revision – One-Line Definitions

1. **File:** A container used to store data on a computer.
2. **Database:** An organised collection of logically related data.
3. **DBMS:** Software used to create and manage databases.
4. **Query:** A request made to a database to obtain information.
5. **Database Schema:** The structure or design of a database.
6. **Database Instance:** The state of a database at a particular time.
7. **Constraint:** A rule or restriction applied to data.
8. **Metadata:** Data about data.
9. **Database Engine:** Component that handles database operations.
10. **Relation:** A table in the relational data model.
11. **Attribute:** A column in a relation.
12. **Tuple:** A row in a relation.
13. **Domain:** Set of valid values for an attribute.
14. **Degree:** Number of columns in a relation.
15. **Cardinality:** Number of rows in a relation.
16. **Candidate Key:** Attribute(s) that can uniquely identify a row.
17. **Primary Key:** Selected candidate key.
18. **Alternate Key:** Candidate key not selected as primary key.
19. **Composite Primary Key:** Primary key consisting of two or more attributes.
20. **Foreign Key:** Attribute referring to the primary key of another table.
21. **NULL:** Special value representing unknown or non-applicable data.
22. **Data Redundancy:** Unnecessary duplication of data.
23. **Data Inconsistency:** Different copies of the same data do not match.
24. **Data Isolation:** Related data stored separately without proper links.
25. **Data Dependence:** Programs depend on the structure of files.

---
