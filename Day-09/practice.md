# DBMS – Important Keys and Relational Database Concepts

## 1. Primary Key

### Definition
A **Primary Key** is an attribute (column) or a combination of attributes that uniquely identifies every record (row) in a table.

### Example

**STUDENT Table**

| Student_ID | Name | Age |
|---|---|---|
| 101 | Rahul | 16 |
| 102 | Aman | 17 |
| 103 | Priya | 16 |
| 104 | Riya | 17 |

Here, `Student_ID` is the Primary Key because every student has a different Student_ID.

### Properties of Primary Key
1. Every value must be unique.
2. It cannot contain NULL values.
3. A table can have only one Primary Key.
4. A Primary Key can consist of multiple columns.

---

## 2. Candidate Key

### Definition
A **Candidate Key** is an attribute or a combination of attributes that can uniquely identify every record in a table.

### Example

**STUDENT Table**

| Student_ID | Roll_No | Name | Email |
|---|---|---|---|
| 101 | 21 | Rahul | rahul@gmail.com |
| 102 | 22 | Aman | aman@gmail.com |
| 103 | 23 | Priya | priya@gmail.com |
| 104 | 24 | Riya | riya@gmail.com |

Here, the following columns can uniquely identify students:

- Student_ID
- Roll_No
- Email

Therefore, all three are Candidate Keys.

### Important Points
1. A table can have multiple Candidate Keys.
2. Every Candidate Key must uniquely identify a record.
3. One Candidate Key is selected as the Primary Key.

---

## 3. Alternate Key

### Definition
An **Alternate Key** is a Candidate Key that is not selected as the Primary Key.

### Example

Consider the previous STUDENT table.

Suppose we select `Student_ID` as the Primary Key.

| Key Type | Attribute |
|---|---|
| Primary Key | Student_ID |
| Candidate Keys | Student_ID, Roll_No, Email |
| Alternate Keys | Roll_No, Email |

Roll_No and Email are Alternate Keys because they can also uniquely identify students but were not selected as the Primary Key.

### Remember
**Candidate Keys – Selected Primary Key = Alternate Keys**

---

## 4. Foreign Key

### Definition
A **Foreign Key** is an attribute in one table that refers to the Primary Key of another table.

It is used to establish relationships between two tables.

### Example

**CLASS Table**

| Class_ID (PK) | Class_Name |
|---|---|
| 1 | XI-A |
| 2 | XI-B |

**STUDENT Table**

| Student_ID (PK) | Name | Class_ID (FK) |
|---|---|---|
| 101 | Rahul | 1 |
| 102 | Aman | 2 |
| 103 | Priya | 1 |
| 104 | Riya | 2 |

### Explanation
- Class_ID in CLASS is the Primary Key.
- Class_ID in STUDENT is the Foreign Key.
- The Foreign Key connects students with their respective classes.

### Properties of Foreign Key
1. It refers to the Primary Key or another candidate key with a suitable uniqueness constraint in another table.
2. Duplicate values are allowed.
3. NULL values are allowed if no NOT NULL constraint applies and the column is not part of a Primary Key.
4. A table can have multiple Foreign Keys.

---

## 5. Composite Primary Key

### Definition
A **Composite Primary Key** is a Primary Key formed by combining two or more attributes (columns) to uniquely identify a record.

### Example

A student can enrol in multiple courses.

**ENROLLMENT Table**

| Student_ID | Course_ID | Marks |
|---|---|---|
| 101 | C01 | 85 |
| 101 | C02 | 90 |
| 102 | C01 | 78 |
| 102 | C03 | 88 |
| 103 | C02 | 92 |

### Explanation
- Student_ID alone cannot uniquely identify each record because a student can enrol in multiple courses.
- Course_ID alone cannot uniquely identify each record because multiple students can enrol in the same course.
- But Student_ID and Course_ID together uniquely identify every record.

Therefore:

**Composite Primary Key = (Student_ID, Course_ID)**

### Important Points
1. It contains two or more attributes.
2. The combination must be unique.
3. Each individual attribute may contain duplicate values.
4. The combination cannot contain NULL values because it is a Primary Key.

---

## 6. Degree of a Relation

### Definition
**Degree** is the total number of columns (attributes) present in a table.

### Example

**STUDENT Table**

| Student_ID | Name | Age | City |
|---|---|---|---|
| 101 | Rahul | 16 | Delhi |
| 102 | Aman | 17 | Mumbai |
| 103 | Priya | 16 | Pune |

The table contains four columns:

1. Student_ID
2. Name
3. Age
4. City

Therefore:

**Degree = 4**

### Remember
Degree = Number of Columns (Attributes).

---

## 7. Cardinality of a Relation

### Definition
**Cardinality** is the total number of rows (tuples or records) present in a table.

### Example

**STUDENT Table**

| Student_ID | Name | Age | City |
|---|---|---|---|
| 101 | Rahul | 16 | Delhi |
| 102 | Aman | 17 | Mumbai |
| 103 | Priya | 16 | Pune |
| 104 | Riya | 17 | Bengaluru |
| 105 | Karan | 16 | Chandigarh |

The table contains five records.

Therefore:

**Cardinality = 5**

### Remember
Cardinality = Number of Rows (Tuples).

---

## 8. Difference Between All Keys

| Key | Meaning | Example |
|---|---|---|
| Primary Key | Uniquely identifies each record | Student_ID |
| Candidate Key | All possible attributes that uniquely identify records | Student_ID, Roll_No, Email |
| Alternate Key | Candidate Key not selected as Primary Key | Roll_No, Email |
| Foreign Key | Connects two tables | Class_ID in STUDENT |
| Composite Primary Key | Combination of two or more attributes | Student_ID + Course_ID |

---

## 9. Difference Between Degree and Cardinality

| Degree | Cardinality |
|---|---|
| Number of columns in a table | Number of rows in a table |
| Also called number of attributes | Also called number of tuples |
| Example: 4 columns | Example: 5 rows |

**Easy Trick to Remember:**

- Degree = Columns
- Cardinality = Rows

---

## 10. Quick Revision Examples

### Example 1
A table contains 5 columns and 10 records.

- Degree = 5
- Cardinality = 10

### Example 2
A table has Student_ID, Roll_No and Email, and all three are unique. Student_ID is selected as the Primary Key.

- Candidate Keys = Student_ID, Roll_No, Email
- Primary Key = Student_ID
- Alternate Keys = Roll_No, Email

### Example 3
In a STUDENT table, Class_ID refers to Class_ID in the CLASS table.

- Class_ID in CLASS = Primary Key
- Class_ID in STUDENT = Foreign Key

### Example 4
Student_ID and Course_ID together identify each record in an ENROLLMENT table.

- Composite Primary Key = Student_ID + Course_ID

---

## 11. Important Exam Points

1. A table can have multiple Candidate Keys but only one Primary Key.
2. A Primary Key cannot contain duplicate or NULL values.
3. An Alternate Key is an unselected Candidate Key.
4. A Foreign Key establishes a relationship between tables.
5. Foreign Keys can contain duplicate values.
6. A Composite Primary Key consists of two or more attributes.
7. Degree represents the number of columns.
8. Cardinality represents the number of rows.
9. Two tables can have the same Degree but different Cardinality.
10. The order of rows and columns does not affect the relation.

### Final Memory Trick

| Concept | Remember |
|---|---|
| Primary Key | Main unique identifier |
| Candidate Key | Possible Primary Keys |
| Alternate Key | Remaining Candidate Keys |
| Foreign Key | Connects tables |
| Composite Key | Combination of columns |
| Degree | Columns |
| Cardinality | Rows |
