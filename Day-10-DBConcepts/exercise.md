# Chapter 7 – Database Concepts
## Exercise Questions and Answers

---

## Q1. Give the terms for each of the following:

### a) Collection of logically related records.

**Answer:** Database

A database is an organised collection of logically related data.

### b) DBMS creates a file that contains description about the data stored in the database.

**Answer:** Data Dictionary (Database Catalog)

It stores information about the database, such as table names, attributes and constraints. This information is also called metadata.

### c) Attribute that can uniquely identify the tuples in a relation.

**Answer:** Candidate Key

A candidate key is an attribute or a set of attributes that can uniquely identify each record in a table.

### d) Special value that is stored when actual data value is unknown for an attribute.

**Answer:** NULL

NULL represents a missing, unknown or unavailable value.

### e) An attribute which can uniquely identify tuples of the table but is not defined as primary key of the table.

**Answer:** Alternate Key

An alternate key is a candidate key that has not been selected as the primary key.

### f) Software that is used to create, manipulate and maintain a relational database.

**Answer:** Relational Database Management System (RDBMS)

Examples: MySQL, Oracle and PostgreSQL.

---

## Q2. Why are foreign keys allowed to have NULL values? Explain with an example.

**Answer:**

A foreign key is allowed to have a NULL value because sometimes a record may not have a relationship with another table.

A foreign key is used to connect two tables. However, every record does not necessarily need to refer to a record in another table.

**Example:**

Consider two tables:

**STUDENT Table**

| RollNo (Primary Key) | Name | GuardianID (Foreign Key) |
|---|---|---|
| 1 | Aman | G101 |
| 2 | Riya | G102 |
| 3 | Rahul | NULL |

Here, Rahul's GuardianID is NULL because the guardian information is not available.

Therefore, a foreign key can contain NULL values if it is not a part of the primary key.

---

## Q3. Differentiate between:

### a) Database State and Database Schema

| Database State | Database Schema |
|---|---|
| It represents the actual data stored in a database at a particular time. | It represents the design or structure of a database. |
| It changes whenever data is inserted, deleted or updated. | It generally remains unchanged unless the database structure is modified. |
| It is also called a database instance. | It defines tables, attributes and constraints. |
| Example: Records currently stored in a STUDENT table. | Example: STUDENT(RollNo, Name, Class). |

### b) Primary Key and Foreign Key

| Primary Key | Foreign Key |
|---|---|
| It uniquely identifies each record in a table. | It is used to establish a relationship between two tables. |
| It cannot contain duplicate values. | It can contain duplicate values. |
| It cannot contain NULL values. | It can contain NULL values if it is not part of a primary key. |
| A table has only one primary key. | A table can have multiple foreign keys. |
| Example: RollNo in STUDENT. | Example: GuardianID in STUDENT referring to GUARDIAN. |

### c) Degree and Cardinality of a Relation

| Degree | Cardinality |
|---|---|
| Degree is the total number of attributes (columns) in a table. | Cardinality is the total number of tuples (rows) in a table. |
| It represents the columns. | It represents the rows. |
| Example: A table with 4 columns has degree 4. | Example: A table with 10 records has cardinality 10. |

---

## Q4. Compared to a file system, how does a Database Management System avoid redundancy in data through a database?

**Answer:**

A DBMS avoids data redundancy by storing data in separate but related tables instead of repeating the same information in multiple files.

Tables are connected using common attributes and keys such as primary keys and foreign keys.

**Example:**

Suppose a school maintains student and guardian information.

Instead of storing guardian details repeatedly for every student, the school can create two tables.

**STUDENT Table**

| RollNo | Name | GUID |
|---|---|---|
| 1 | Aman | G101 |
| 2 | Riya | G101 |
| 3 | Rahul | G102 |

**GUARDIAN Table**

| GUID | GuardianName |
|---|---|
| G101 | Rajesh |
| G102 | Suresh |

Here, guardian details are stored only once in the GUARDIAN table.

The GUID connects the two tables.

Thus, DBMS reduces data redundancy and saves storage space.

---

## Q5. What are the limitations of a file system that can be overcome by a relational DBMS?

**Answer:**

The limitations of a file system are:

1. **Difficulty in Access:** Finding specific information from large files is difficult. DBMS allows users to retrieve data using queries.

2. **Data Redundancy:** The same data may be stored in multiple files. DBMS reduces duplication by storing data in related tables.

3. **Data Inconsistency:** When duplicate data is updated in one file but not another, information becomes inconsistent. DBMS helps maintain consistency.

4. **Data Isolation:** Data may be stored in different files and formats, making it difficult to combine. DBMS stores related data in an organised manner.

5. **Data Dependence:** Changes in file structure may require changes in application programs. DBMS provides data independence.

6. **Controlled Data Sharing:** Sharing data among multiple users is difficult in a file system. DBMS provides controlled access to multiple users.

---

## Q6. A school has a rule that each student must participate in a sports activity. So each one should give only one preference for sports activity.

The class representative has prepared the following table:

| Roll_no | Preference |
|---|---|
| 9 | Cricket |
| 13 | Football |
| 17 | Badminton |
| 17 | Football |
| 21 | Hockey |
| 24 | NULL |
| NULL | Kabaddi |

### a) Roll no 24 may not be interested in sports. Can a NULL value be assigned to that student's preference field?

**Answer:**

No, according to the given school rule, every student must participate in a sports activity.

Therefore, every student must provide a sports preference.

A NULL value cannot be accepted for Roll No. 24 because the student is required to select a sport.

### b) Roll no 17 has given two sports preferences. Which property of relational DBMS is violated here? Can we use any constraint or key in the relational DBMS to check against such violation?

**Answer:**

The rule that each student can give only one sports preference is violated.

Roll No. 17 appears twice with two different preferences.

This violates the uniqueness requirement of the Roll_no attribute.

We can define Roll_no as the **Primary Key** of the table.

A primary key does not allow duplicate or NULL values. Therefore, the same student cannot be entered twice.

### c) Kabaddi was not chosen by any student. Is it possible to have this tuple in the Sports Preferences relation?

**Answer:**

No.

The tuple containing NULL as Roll_no cannot be inserted because Roll_no is the primary key.

A primary key cannot contain NULL values.

---

## Q7. In another class having 2 sections, the two respective class representatives have prepared two separate Sports Preferences tables.

**Section 1 Table**

| Roll_no | Sports |
|---|---|
| 9 | Cricket |
| 13 | Football |
| 17 | Badminton |
| 21 | Hockey |
| 24 | Cricket |

**Section 2 Table**

| Sports | Roll_no |
|---|---|
| Badminton | 17 |
| Cricket | 9 |
| Cricket | 24 |
| Football | 13 |
| Hockey | 21 |

**Question:** Are the states of both the relations equivalent? Justify.

**Answer:**

Yes, both relations have equivalent states.

Although the order of columns and rows is different, both tables contain exactly the same data.

In a relational database:

- The order of rows does not matter.
- The order of columns does not matter.
- The same set of tuples represents the same relation state.

Therefore, both relations are equivalent.

---

## Q8. The school canteen wants to maintain records of items available in the school canteen and generate bills when students purchase any item.

Design a database by answering the following questions.

### a) To store each item name along with its price, what relation should be used? Decide appropriate attribute names along with their data type. Each item and its price should be stored only once. What restriction should be used while defining the relation?

**Answer:**

We should create a relation named **ITEM**.

The table can have the following structure:

**ITEM Table**

| Attribute | Data Type | Constraint |
|---|---|---|
| ItemID | INT | Primary Key |
| ItemName | VARCHAR(30) | NOT NULL |
| Price | DECIMAL(8,2) | NOT NULL |

Example:

| ItemID | ItemName | Price |
|---|---|---|
| 101 | Sandwich | 50.00 |
| 102 | Burger | 80.00 |
| 103 | Juice | 40.00 |

**Explanation:**

- ItemID uniquely identifies every item.
- ItemName stores the name of the item.
- Price stores the price of the item.
- The primary key prevents duplicate ItemID values.
- Each item should be stored only once.

### b) In order to generate a bill, we should know the quantity of an item purchased. Should this information be in a new relation or a part of the previous relation?

**Answer:**

This information should be stored in a new relation because the quantity purchased can be different for every order.

We can create a new relation named **ORDER_DETAILS**.

**ORDER_DETAILS Table**

| Attribute | Data Type | Constraint |
|---|---|---|
| BillNo | INT | Primary Key (part of composite key) |
| ItemID | INT | Foreign Key |
| Quantity | INT | NOT NULL |

A suitable primary key is the combination of BillNo and ItemID.

**Composite Primary Key: (BillNo, ItemID)**

**Foreign Key: ItemID**

It refers to ItemID in the ITEM table.

**Restrictions:**

i) The same bill cannot be generated for different orders.

BillNo identifies a bill. The combination of BillNo and ItemID uniquely identifies each item entry in a bill.

ii) Bill can be generated only for available items in the canteen.

ItemID is defined as a foreign key referencing the ITEM table. Therefore, an order can refer only to an item present in the ITEM table.

### c) The school wants to find out how many calories students intake when they order an item. In which relation should the attribute 'calories' be stored?

**Answer:**

The attribute Calories should be stored in the **ITEM** relation.

Calories are a property of an item and do not depend on the quantity purchased.

For example:

| ItemID | ItemName | Price | Calories |
|---|---|---|---|
| 101 | Sandwich | 50.00 | 250 |
| 102 | Burger | 80.00 | 400 |
| 103 | Juice | 40.00 | 120 |

---

## Q9. An organisation wants to create a database EMP-DEPENDENT to maintain the following details:

EMPLOYEE(AadharNumber, Name, Address, Department, EmployeeID)

DEPENDENT(EmployeeID, DependentName, Relationship)

### a) Name the attributes of EMPLOYEE, which can be used as candidate keys.

**Answer:**

The candidate keys are:

1. AadharNumber
2. EmployeeID

**Reason:**

Both attributes can uniquely identify an employee.

Therefore, both can be considered candidate keys.

### b) The company wants to retrieve details of dependent of a particular employee. Name the tables and the key which are required to retrieve this detail.

**Answer:**

The required tables are:

1. EMPLOYEE
2. DEPENDENT

The common attribute is EmployeeID.

- EmployeeID is the primary key in the EMPLOYEE table.
- EmployeeID is the foreign key in the DEPENDENT table.

Using EmployeeID, the organisation can connect both tables and retrieve the dependent details of a particular employee.

### c) What is the degree of EMPLOYEE and DEPENDENT relation?

**Answer:**

Degree means the total number of attributes (columns) in a relation.

EMPLOYEE:

AadharNumber, Name, Address, Department, EmployeeID

Total attributes = **5**

DEPENDENT:

EmployeeID, DependentName, Relationship

Total attributes = **3**

Therefore:

- Degree of EMPLOYEE = 5
- Degree of DEPENDENT = 3

---

## Q10. School uniform is available at M/s Sheetal Private Limited. They have maintained SCHOOL_UNIFORM Database with two relations viz. UNIFORM and COST.

### Given UNIFORM relation

| UCode | UName | UColor |
|---|---|---|
| 1 | Shirt | White |
| 2 | Pant | Grey |
| 3 | Skirt | Grey |
| 4 | Tie | Blue |
| 5 | Socks | Blue |
| 6 | Belt | Blue |

Constraints:

- UCode – Primary Key
- UName – NOT NULL
- UColor – No constraint specified

### Given COST relation

| UCode | Size | Price |
|---|---|---|
| 1 | M | 500 |
| 1 | L | 580 |
| 1 | XL | 620 |
| 2 | M | 810 |
| 2 | L | 890 |
| 2 | XL | 940 |
| 3 | M | 770 |
| 3 | L | 830 |
| 3 | XL | 910 |
| 4 | S | 150 |
| 4 | L | 170 |
| 5 | S | 180 |
| 5 | L | 210 |
| 6 | M | 110 |
| 6 | L | 140 |
| 6 | XL | 160 |

Constraints:

- UCode and Size – Composite Primary Key
- Price – Greater than 0

### a) Can they insert the following tuples into the UNIFORM relation? Give reasons.

#### i) (7, Handkerchief, NULL)

**Answer: YES**

Reason:

- UCode 7 is unique and is not NULL.
- UName is Handkerchief and is not NULL.
- UColor has no constraint specified, so NULL is allowed.

Therefore, the tuple can be inserted.

#### ii) (4, Ribbon, Red)

**Answer: NO**

Reason:

UCode 4 already exists in the UNIFORM table.

UCode is the primary key, and a primary key cannot contain duplicate values.

Therefore, the tuple cannot be inserted.

#### iii) (8, NULL, White)

**Answer: NO**

Reason:

The UName attribute has a NOT NULL constraint.

The given tuple contains NULL in UName.

Therefore, the tuple cannot be inserted.

### b) Can they insert the following tuples into the COST relation? Give reasons.

#### i) (7, S, 0)

**Answer: NO**

Reason:

The Price attribute has a constraint that its value must be greater than 0.

Here, Price = 0.

Therefore, the tuple cannot be inserted.

#### ii) (9, XL, 100)

**Answer: YES, according to the constraints explicitly shown in the question.**

Reason:

- The combination (9, XL) is not already present in the COST table.
- Price = 100, which is greater than 0.

Therefore, it satisfies the displayed composite primary key and price constraints.

---

## Q11. In a multiplex, movies are screened in different auditoriums. One movie can be shown in more than one auditorium.

The database contains two relations:

MOVIE(Movie_ID, MovieName, ReleaseDate)

AUDI(AudiNo, Movie_ID, Seats, ScreenType, TicketPrice)

### a) Is it correct to assign Movie_ID as the primary key in the MOVIE relation? If no, then suggest an appropriate primary key.

**Answer:**

Yes.

Movie_ID can be the primary key of the MOVIE relation because it uniquely identifies each movie.

One movie can be screened in multiple auditoriums, but its details are stored only once in the MOVIE table.

### b) Is it correct to assign AudiNo as the primary key in the AUDI relation? If no, then suggest an appropriate primary key.

**Answer:**

No.

AudiNo alone may not uniquely identify a record because an auditorium can screen different movies.

Therefore, we should use a composite primary key:

**(AudiNo, Movie_ID)**

The combination of AudiNo and Movie_ID can uniquely identify a movie screening in an auditorium.

### c) Is there any foreign key in any of these relations?

**Answer:**

Yes.

Movie_ID in the AUDI relation is a foreign key.

It refers to Movie_ID, the primary key of the MOVIE relation.

This connects the AUDI table with the MOVIE table.

---

## Q12. For the above given database STUDENT-PROJECT, answer the following:

### STUDENT Table

| Roll No | Name | Class | Section | Registration_ID |
|---|---|---|---|---|
| 11 | Mohan | XI | 1 | IP-101-15 |
| 12 | Sohan | XI | 2 | IP-104-15 |
| 21 | John | XII | 1 | CS-103-14 |
| 22 | Meena | XII | 2 | CS-101-14 |
| 23 | Juhi | XII | 2 | CS-101-10 |

### PROJECT Table

| ProjectNo | PName | SubmissionDate |
|---|---|---|
| 101 | Airline Database | 12/01/2018 |
| 102 | Library Database | 12/01/2018 |
| 103 | Employee Database | 15/01/2018 |
| 104 | Student Database | 12/01/2018 |
| 105 | Inventory Database | 15/01/2018 |
| 106 | Railway Database | 15/01/2018 |

### PROJECT-ASSIGNED Table

| Registration_ID | ProjectNo |
|---|---|
| IP-101-15 | 101 |
| IP-104-15 | 103 |
| CS-103-14 | 102 |
| CS-101-14 | 105 |
| CS-101-10 | 104 |

### a) Name the primary key of each table.

**Answer:**

1. STUDENT – Roll No
2. PROJECT – ProjectNo
3. PROJECT-ASSIGNED – Combination of Registration_ID and ProjectNo

The PROJECT-ASSIGNED table uses a composite primary key because the combination identifies each student-project assignment.

### b) Find foreign keys in table PROJECT-ASSIGNED.

**Answer:**

There are two foreign keys:

1. Registration_ID – References Registration_ID in STUDENT.
2. ProjectNo – References ProjectNo in PROJECT.

These foreign keys establish relationships between the three tables.

### c) Is there any alternate key in table STUDENT? Give justification for your answer.

**Answer:**

Yes, Registration_ID is an alternate key.

Reason:

- Roll No is selected as the primary key.
- Registration_ID also contains unique values.
- Therefore, Registration_ID can also uniquely identify students.

Since it is not selected as the primary key, it is an alternate key.

### d) Can a user assign duplicate value to the field RollNo of STUDENT table? Justify.

**Answer:**

No.

RollNo is the primary key of the STUDENT table.

A primary key must contain unique values and cannot contain duplicates.

Therefore, duplicate RollNo values cannot be inserted.

---

## Q13. For the above given database STUDENT-PROJECT, can we perform the following operations?

### a) Insert a student record with missing roll number value.

**Answer: NO**

Reason:

RollNo is the primary key of the STUDENT table.

A primary key cannot contain NULL values.

Therefore, a student record with a missing RollNo cannot be inserted.

### b) Insert a student record with missing registration number value.

**Answer: NO**

Reason:

Registration_ID is an alternate key.

It must uniquely identify each student and cannot contain NULL values.

Therefore, a student record with a missing Registration_ID cannot be inserted.

### c) Insert a project detail without submission-date.

**Answer: YES, according to the constraints given in the question.**

Reason:

ProjectNo is the primary key of the PROJECT table.

No NOT NULL constraint is specified for SubmissionDate in the given question.

Therefore, a project record can be inserted with a NULL SubmissionDate.

### d) Insert a record with registration ID IP-101-19 and ProjectNo 206 in table PROJECT-ASSIGNED.

**Answer: NO**

Reason:

PROJECT-ASSIGNED contains two foreign keys:

- Registration_ID refers to the STUDENT table.
- ProjectNo refers to the PROJECT table.

The Registration_ID IP-101-19 does not exist in the STUDENT table.

The ProjectNo 206 does not exist in the PROJECT table.

Therefore, the record cannot be inserted because it violates referential integrity.

---

# Quick Revision – Important Answers

| Question | Important Concept |
|---|---|
| Q1 | Database, Data Dictionary, Candidate Key, NULL, Alternate Key, RDBMS |
| Q2 | Foreign Key and NULL |
| Q3 | Schema, State, Primary Key, Foreign Key, Degree, Cardinality |
| Q4 | Data Redundancy |
| Q5 | Limitations of File System |
| Q6 | Primary Key and NULL constraints |
| Q7 | Properties of Relations |
| Q8 | Database Design, Primary Key, Foreign Key, Composite Key |
| Q9 | Candidate Keys and Degree |
| Q10 | Primary Key, NOT NULL and Value Constraints |
| Q11 | Composite Primary Key and Foreign Key |
| Q12 | Primary Key, Alternate Key and Foreign Key |
| Q13 | Primary Key, Alternate Key and Referential Integrity |

---

## Important Points to Remember

1. A primary key cannot contain duplicate or NULL values.
2. A foreign key connects two tables.
3. A foreign key can contain NULL if it is not part of a primary key.
4. A candidate key uniquely identifies records.
5. An alternate key is a candidate key that was not selected as the primary key.
6. A composite primary key contains more than one attribute.
7. Degree means the number of columns in a table.
8. Cardinality means the number of rows in a table.
9. Database schema represents the structure of a database.
10. Database state represents the data stored at a particular time.
11. A relation is another name for a table.
12. A tuple is another name for a row.
13. An attribute is another name for a column.
14. A foreign key helps maintain referential integrity.
15. The order of rows and columns does not affect the state of a relation.
