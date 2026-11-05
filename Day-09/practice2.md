# DBMS – Practice Worksheet
## Topics: Primary Key, Candidate Key, Alternate Key, Foreign Key, Composite Primary Key, Degree and Cardinality

**Instructions:**
- Attempt all questions.
- Write proper explanations wherever required.
- Do not look at answers while solving.
- Identify keys carefully from the given tables.

---

## Section A – Primary Key and Candidate Key

### Q1. Student Database

Consider the following table:

| Student_ID | Roll_No | Name | Email |
|---|---|---|---|
| 101 | 21 | Rahul | rahul@gmail.com |
| 102 | 22 | Aman | aman@gmail.com |
| 103 | 23 | Priya | priya@gmail.com |
| 104 | 24 | Riya | riya@gmail.com |

Assume Student_ID, Roll_No and Email are unique.

Answer:
1. Identify all candidate keys.
2. If Student_ID is selected as the primary key, identify the alternate keys.
3. Can Name be a candidate key? Give a reason.

### Q2. Employee Database

| Employee_ID | PAN_No | Name | Department |
|---|---|---|---|
| 201 | PAN101 | Amit | HR |
| 202 | PAN102 | Neha | IT |
| 203 | PAN103 | Ravi | Sales |
| 204 | PAN104 | Priya | IT |

Assume Employee_ID and PAN_No are unique.

1. Identify all candidate keys.
2. If PAN_No is selected as the primary key, identify the alternate key.
3. Can Department be a primary key? Why?

### Q3. Library Database

| Book_ID | ISBN | Book_Name | Author |
|---|---|---|---|
| 1 | ISBN101 | Python Basics | John |
| 2 | ISBN102 | Java Basics | Peter |
| 3 | ISBN103 | DBMS | David |
| 4 | ISBN104 | C++ Basics | John |

Assume Book_ID and ISBN are unique.

1. Identify candidate keys.
2. If Book_ID is the primary key, identify the alternate key.
3. Can Author be a candidate key?

### Q4.
A table contains three candidate keys: A, B and C.

1. If A is selected as the primary key, what are the alternate keys?
2. Can B and C still uniquely identify records?
3. How many primary keys can the table have?

### Q5.
A STUDENT table contains Student_ID, Name, Email and Phone.

Assume Student_ID and Email are unique, but Phone may contain duplicate values.

1. Identify the candidate keys.
2. If Student_ID is the primary key, identify the alternate key.
3. Can Phone be a candidate key? Explain.

---

## Section B – Alternate Keys and Primary Key Properties

### Q6.
A table has four candidate keys: A, B, C and D. If B is selected as the primary key:

1. Identify all alternate keys.
2. How many alternate keys are present?
3. Can A still uniquely identify records?

### Q7.
Consider the following STUDENT table:

| Roll_No | Name | Age |
|---|---|---|
| 1 | Rahul | 16 |
| 2 | Aman | 17 |
| 3 | Priya | 16 |
| 4 | Riya | 17 |

1. Which column can be selected as the primary key?
2. Can Name be the primary key?
3. Can Age be the primary key?
4. Give reasons for your answers.

### Q8.
A school maintains student records using Admission_No, Roll_No, Name and Email. Admission_No, Roll_No and Email are unique.

If Roll_No is selected as the primary key:

1. Identify the candidate keys.
2. Identify the primary key.
3. Identify the alternate keys.

### Q9.
Can a primary key contain:
1. Duplicate values?
2. NULL values?
3. Both duplicate and NULL values?

Give reasons.

### Q10.
Differentiate between:
1. Primary Key and Candidate Key.
2. Candidate Key and Alternate Key.

---

## Section C – Foreign Key

### Q11. Department and Student Tables

**DEPARTMENT**

| Dept_ID | Dept_Name |
|---|---|
| D01 | CSE |
| D02 | Mechanical |
| D03 | Civil |

**STUDENT**

| Student_ID | Name | Dept_ID |
|---|---|---|
| 101 | Rahul | D01 |
| 102 | Aman | D02 |
| 103 | Priya | D01 |
| 104 | Riya | D03 |

1. Identify the primary key of both tables.
2. Identify the foreign key.
3. Why does Dept_ID appear multiple times in STUDENT?
4. Which table is the referenced table?

### Q12. Customer and Orders Tables

**CUSTOMER**

| Customer_ID | Customer_Name |
|---|---|
| 1 | Rahul |
| 2 | Aman |
| 3 | Priya |

**ORDERS**

| Order_ID | Customer_ID | Amount |
|---|---|---|
| 101 | 1 | 500 |
| 102 | 2 | 700 |
| 103 | 1 | 300 |
| 104 | 3 | 900 |

1. Identify the primary keys.
2. Identify the foreign key.
3. Can Customer_ID repeat in ORDERS?
4. Which table contains the foreign key?

### Q13. Teacher and Subject Tables

**TEACHER**

| Teacher_ID | Teacher_Name |
|---|---|
| T01 | Amit |
| T02 | Neha |
| T03 | Ravi |

**SUBJECT**

| Subject_ID | Subject_Name | Teacher_ID |
|---|---|---|
| S01 | Python | T01 |
| S02 | Java | T02 |
| S03 | SQL | T01 |
| S04 | C++ | T03 |

1. Identify the primary keys.
2. Identify the foreign key.
3. Can Teacher_ID repeat in SUBJECT?
4. Explain the relationship.

### Q14.
What is a foreign key? Explain with an example of two related tables.

### Q15.
Answer the following about foreign keys:

1. Can a foreign key contain duplicate values?
2. Can a foreign key contain NULL values?
3. Can a foreign key contain a value that does not exist in the referenced table?
4. Can a table have multiple foreign keys?

---

## Section D – Composite Primary Key

### Q16. Attendance Table

| Roll_No | Date | Status |
|---|---|---|
| 21 | 01-11-2026 | Present |
| 21 | 02-11-2026 | Absent |
| 22 | 01-11-2026 | Present |
| 22 | 02-11-2026 | Present |
| 23 | 01-11-2026 | Absent |

1. Can Roll_No alone be the primary key?
2. Can Date alone be the primary key?
3. Identify the composite primary key.
4. Explain why.

### Q17. Student and Course Enrollment

| Student_ID | Course_ID | Marks |
|---|---|---|
| 101 | C01 | 85 |
| 101 | C02 | 90 |
| 102 | C01 | 78 |
| 102 | C03 | 88 |
| 103 | C02 | 92 |

1. Identify the composite primary key.
2. Why can't Student_ID alone be the primary key?
3. Why can't Course_ID alone be the primary key?

### Q18. Railway Reservation Table

| Train_ID | Passenger_ID | Seat_No |
|---|---|---|
| T01 | P101 | 10 |
| T01 | P102 | 11 |
| T02 | P101 | 15 |
| T02 | P103 | 16 |

1. Identify a suitable composite primary key.
2. Can Train_ID alone identify every record?
3. Can Passenger_ID alone identify every record?

### Q19.
A RESULT table contains Student_ID, Subject_ID, Exam_Type and Marks.

A student can appear for multiple subjects and multiple exam types.

1. Suggest a suitable composite primary key.
2. Why is Student_ID alone insufficient?
3. Why is Subject_ID alone insufficient?

### Q20.
Differentiate between a simple primary key and a composite primary key with examples.

---

## Section E – Degree and Cardinality

### Q21. Calculate Degree and Cardinality.

| Student_ID | Name | Age | City |
|---|---|---|---|
| 101 | Rahul | 16 | Delhi |
| 102 | Aman | 17 | Mumbai |
| 103 | Priya | 16 | Pune |

Find:
1. Degree.
2. Cardinality.

### Q22. Calculate Degree and Cardinality.

| Emp_ID | Name | Salary | Department | City |
|---|---|---|---|---|
| 1 | Amit | 30000 | HR | Delhi |
| 2 | Neha | 40000 | IT | Pune |
| 3 | Ravi | 35000 | Sales | Mumbai |
| 4 | Priya | 45000 | IT | Bengaluru |
| 5 | Aman | 32000 | HR | Jaipur |

Find:
1. Degree.
2. Cardinality.

### Q23.
A table contains 8 columns and 15 records.

Find:
1. Degree.
2. Cardinality.

### Q24.
A database table has a degree of 6 and a cardinality of 12.

1. How many columns are present?
2. How many rows are present?

### Q25.
A STUDENT table has 10 rows and 7 columns. Two more students are inserted.

Find:
1. New cardinality.
2. New degree.

### Q26.
A table has 5 columns and 20 records. One column is deleted and three new records are inserted.

Find:
1. New degree.
2. New cardinality.

### Q27.
A table has 12 columns but contains no records.

Find:
1. Degree.
2. Cardinality.

### Q28.
A table has 15 records and 9 attributes. If five records are deleted:

1. What is the new cardinality?
2. What is the degree?

### Q29.
Two tables have the same degree but different cardinalities. Is this possible? Explain with an example.

### Q30.
A table has 6 columns and 8 rows. Another table has 8 columns and 6 rows.

1. Find the degree of both tables.
2. Find the cardinality of both tables.
3. Do both tables have the same degree?
4. Do both tables have the same cardinality?

---

## Section F – Mixed and Application-Based Questions

### Q31. Doctor Database

| Doctor_ID | Registration_No | Name | Email |
|---|---|---|---|
| 1 | R101 | Amit | amit@gmail.com |
| 2 | R102 | Neha | neha@gmail.com |
| 3 | R103 | Ravi | ravi@gmail.com |

Assume Doctor_ID, Registration_No and Email are unique.

If Doctor_ID is selected as the primary key, identify:

1. All candidate keys.
2. Primary key.
3. Alternate keys.
4. Degree.
5. Cardinality.

### Q32. Product Database

| Product_ID | Product_Name | Price | Quantity | Category | Manufacturer |
|---|---|---|---|---|---|
| 101 | Laptop | 50000 | 5 | Electronics | Dell |
| 102 | Mouse | 500 | 20 | Accessories | HP |
| 103 | Keyboard | 1000 | 15 | Accessories | Logitech |
| 104 | Monitor | 12000 | 8 | Electronics | Samsung |
| 105 | Printer | 8000 | 3 | Electronics | Canon |
| 106 | Speaker | 2000 | 10 | Electronics | Sony |

Answer:
1. Identify a suitable primary key.
2. Find the degree.
3. Find the cardinality.

### Q33. School Database

**STUDENT**

| Student_ID | Name | Class_ID | Email |
|---|---|---|---|
| 101 | Rahul | C01 | rahul@gmail.com |
| 102 | Aman | C02 | aman@gmail.com |
| 103 | Priya | C01 | priya@gmail.com |

**CLASS**

| Class_ID | Class_Name | Class_Teacher |
|---|---|---|
| C01 | XI-A | Mr. Sharma |
| C02 | XI-B | Mrs. Gupta |

Assume Student_ID and Email are unique.

Answer:
1. Identify candidate keys in STUDENT.
2. If Student_ID is the primary key, identify the alternate key.
3. Identify the primary key of CLASS.
4. Identify the foreign key.
5. Find the degree and cardinality of both tables.

### Q34.
A college database has three tables: STUDENT, SUBJECT and EXAM.

- STUDENT contains Student_ID, Name and Class.
- SUBJECT contains Subject_ID, Subject_Name and Teacher.
- EXAM contains Student_ID, Subject_ID and Marks.

Answer:
1. Identify the primary key of STUDENT.
2. Identify the primary key of SUBJECT.
3. Identify the foreign keys in EXAM.
4. Suggest a suitable primary key for EXAM.
5. Identify the degree of each table.

### Q35.
A library maintains two tables:

**BOOK**

Book_ID, Book_Name, Author, Publisher

**ISSUE**

Issue_ID, Book_ID, Student_ID, Issue_Date, Return_Date

Answer:
1. Identify the primary key of BOOK.
2. Identify the primary key of ISSUE.
3. Identify the foreign key in ISSUE.
4. If Student_ID refers to a STUDENT table, identify its key type.
5. Find the degree of both tables.

### Q36.
A table has Student_ID, Roll_No, Email and Phone. Assume all four attributes are unique.

If Email is selected as the primary key:

1. Identify all candidate keys.
2. Identify the primary key.
3. Identify all alternate keys.
4. How many alternate keys are present?

### Q37.
An ENROLLMENT table contains Student_ID, Course_ID and Semester.

A student can enrol in different courses in the same semester and can enrol in the same course in different semesters.

1. Suggest a suitable composite primary key.
2. Why is Student_ID alone not sufficient?
3. Why is Course_ID alone not sufficient?
4. How many columns are present in this table?

### Q38.
A company maintains EMPLOYEE and PROJECT tables.

**EMPLOYEE:** Employee_ID, Name, Department

**PROJECT:** Project_ID, Project_Name, Employee_ID

One employee can work on multiple projects.

Answer:
1. Identify the primary key of EMPLOYEE.
2. Identify the primary key of PROJECT.
3. Identify the foreign key.
4. Can Employee_ID repeat in PROJECT?
5. Find the degree of both tables.

### Q39.
A table contains 7 attributes and 25 tuples.

1. Find the degree.
2. Find the cardinality.
3. If 5 tuples are added, calculate the new cardinality.
4. If 2 attributes are added, calculate the new degree.

### Q40. Final Challenge

A college maintains a database with the following tables:

**STUDENT**

Student_ID, Roll_No, Name, Email, Department_ID

**DEPARTMENT**

Department_ID, Department_Name, HOD

**COURSE**

Course_ID, Course_Name, Credits

**ENROLLMENT**

Student_ID, Course_ID, Semester, Marks

Assume Student_ID, Roll_No and Email are unique in STUDENT.

Answer:
1. Identify all candidate keys in STUDENT.
2. If Student_ID is selected as the primary key, identify alternate keys.
3. Identify the primary key of DEPARTMENT.
4. Identify the primary key of COURSE.
5. Identify all foreign keys in the database.
6. Suggest a suitable composite primary key for ENROLLMENT.
7. Find the degree of STUDENT.
8. Find the degree of DEPARTMENT.
9. Find the degree of COURSE.
10. Find the degree of ENROLLMENT.
