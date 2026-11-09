
```sql
````
# Chapter 8 – Introduction to Structured Query Language (SQL)
# Exercise Questions and Answers

**Class:** XI – Informatics Practices  
**Topic:** SQL and MySQL

---

# Q1. Match the following clauses with their respective functions.

| SQL Clause | Correct Function |
|---|---|
| ALTER | Change the name/structure of a column |
| UPDATE | Update existing information in a table |
| DELETE | Delete an existing row from a table |
| INSERT INTO | Insert values in a table |
| CONSTRAINTS | Restrictions on columns |
| DESC | Display table definition |
| CREATE | Create a database |

---

# Q2. Choose the appropriate answer with respect to the following code snippet.

Consider the following SQL statement:

```sql
CREATE TABLE student (
    name CHAR(30),
    student_id INT,
    gender CHAR(1),
    PRIMARY KEY (student_id)
);
````

### (a) What will be the degree of the student table?

Options:

1. 30
2. 1
3. 3
4. 4

Answer: Option 3 – 3

Explanation:

Degree means the total number of columns (attributes) in a table.

The student table has three columns:

- name
- student_id
- gender

Therefore, degree = 3.

### (b) What does `name` represent in the above code snippet?

Options:

1. A table
2. A row
3. A column
4. A database

Answer: Option 3 – A column

Explanation:

Name is an attribute of the student table. An attribute represents a column.

### (c) What is true about the following SQL statement?

```
SelecT * fROM student;
```

Options:

1. Displays contents of table student.
2. Displays column names and contents of table student.
3. Results in error as improper case has been used.
4. Displays only the column names of table student.

Answer: Option 2 – Displays column names and contents of the student table.

Explanation:

- SQL is case-insensitive.
- SELECT and SelecT are treated the same.
- The `*` symbol retrieves all columns.
- The output includes column headings and records.

### (d) What will be the output of the following query?

```
INSERT INTO student
VALUES ("Suhana",109,'F'),
VALUES ("Rivaan",102,'M'),
VALUES ("Atharv",103,'M'),
VALUES ("Rishika",105,'F'),
VALUES ("Garvit",104,'M'),
VALUES ("Shaurya",109,'M');
```

Options:

1. Error
2. No Error
3. Depends on compiler
4. Successful completion of the query

Answer: Option 1 – Error

Explanation:

The query has incorrect INSERT syntax because `VALUES` is repeated before each record.

Also, student_id is a primary key, so duplicate values are not allowed.

The correct multi-row INSERT syntax is:

```
INSERT INTO student
VALUES
('Suhana', 109, 'F'),
('Rivaan', 102, 'M'),
('Atharv', 103, 'M'),
('Rishika', 105, 'F'),
('Garvit', 104, 'M'),
('Shaurya', 109, 'M');
```

However, this corrected query will still produce an error because student_id 109 is repeated.

### (e) In the following query, how many rows will be deleted?

```
DELETE FROM student
WHERE student_id = 109;
```

Options:

1. 1 row
2. All rows where student_id is equal to 109
3. No row will be deleted
4. 2 rows

Answer: Option 4 – 2 rows

Explanation:

The condition matches both records having student_id 109.

Therefore, both matching rows would be deleted if they existed in the table.

# Q3. Fill in the blanks.

### (a) \_\_\_\_\_\_\_\_\_\_ declares that an index in one table is related to that in another table.

Options:

1. Primary Key
2. Foreign Key
3. Composite Key
4. Secondary Key

Answer: Option 2 – Foreign Key

Explanation:

A foreign key is used to establish a relationship between two tables. It refers to the primary key of another table.

### (b) The symbol Asterisk (\*) in a SELECT query retrieves \_\_\_\_\_\_\_\_\_\_.

Options:

1. All data from the table
2. Data of primary key only
3. NULL data
4. None of the mentioned

Answer: Option 1 – All data from the table

Explanation:

The `*` symbol is used to retrieve all columns from a table.

Example:

```
SELECT *
FROM STUDENT;
```

This displays all columns and records from the STUDENT table.

# Q4. Consider the following MOVIE database and answer the SQL queries based on it.

### Given MOVIE Table

| MovieID | MovieName     | Category  | ReleaseDate | ProductionCost | BusinessCost |
| ------- | ------------- | --------- | ----------- | -------------- | ------------ |
| 001     | Hindi_Movie   | Musical   | 2018-04-23  | 124500         | 130000       |
| 002     | Tamil_Movie   | Action    | 2016-05-17  | 112000         | 118000       |
| 003     | English_Movie | Horror    | 2017-08-06  | 245000         | 360000       |
| 004     | Bengali_Movie | Adventure | 2017-01-04  | 72000          | 100000       |
| 005     | Telugu_Movie  | Action    | NULL        | 100000         | NULL         |
| 006     | Punjabi_Movie | Comedy    | NULL        | 30500          | NULL         |

Note: A dash (-) in the given table represents NULL.

### (a) Retrieve movies information without mentioning their column names.

Answer:

We use `SELECT *` to retrieve all columns.

```
SELECT *
FROM MOVIE;
```

Explanation:

The asterisk (\*) retrieves all columns from the MOVIE table.

### (b) List business done by the movies showing only MovieID, MovieName and BusinessCost.

Answer:

```
SELECT MovieID, MovieName, BusinessCost
FROM MOVIE;
```

Explanation:

Only the three specified columns will be displayed.

### (c) List the different categories of movies.

Answer:

We use DISTINCT to display unique categories.

```
SELECT DISTINCT Category
FROM MOVIE;
```

Output:

| Category  |
| --------- |
| Musical   |
| Action    |
| Horror    |
| Adventure |
| Comedy    |

Explanation:

Action appears more than once in the original table. DISTINCT displays it only once.

### (d) Find the net profit of each movie showing its ID, Name and Net Profit.

Hint:

Net Profit = BusinessCost – ProductionCost

The new column should be labelled as NetProfit.

Answer:

```
SELECT MovieID,
       MovieName,
       BusinessCost - ProductionCost AS NetProfit
FROM MOVIE;
```

Explanation:

Net profit is calculated by subtracting ProductionCost from BusinessCost.

| MovieName     | Calculation     | NetProfit |
| ------------- | --------------- | --------- |
| Hindi_Movie   | 130000 - 124500 | 5500      |
| Tamil_Movie   | 118000 - 112000 | 6000      |
| English_Movie | 360000 - 245000 | 115000    |
| Bengali_Movie | 100000 - 72000  | 28000     |
| Telugu_Movie  | NULL - 100000   | NULL      |
| Punjabi_Movie | NULL - 30500    | NULL      |

Additional Questions:

1\. Is NetProfit now a part of the MOVIE relation?

Answer: No. NetProfit is only a calculated or derived column displayed in the query output. It is not permanently added to the MOVIE table.

2\. What name is given to such columns?

Answer: Derived columns or calculated columns.

3\. What can you say about the profit of a movie which has not yet been released?

Answer: Its BusinessCost is NULL because the movie has not been released and its business information is unavailable.

4\. Does the query show profit as zero?

Answer: No. The result is NULL, not zero, because arithmetic operations involving NULL produce NULL.

### (e) List all movies with ProductionCost greater than 80,000 and less than 1,25,000 showing ID, Name and ProductionCost.

Answer:

```
SELECT MovieID, MovieName, ProductionCost
FROM MOVIE
WHERE ProductionCost > 80000
AND ProductionCost < 125000;
```

Output:

| MovieID | MovieName    | ProductionCost |
| ------- | ------------ | -------------- |
| 001     | Hindi_Movie  | 124500         |
| 002     | Tamil_Movie  | 112000         |
| 005     | Telugu_Movie | 100000         |

Explanation:

Both conditions must be satisfied.

- ProductionCost must be greater than 80000.
- ProductionCost must be less than 125000.

### (f) List all movies which fall in the category of Comedy or Action.

Answer:

```
SELECT *
FROM MOVIE
WHERE Category = 'Comedy'
OR Category = 'Action';
```

Output:

| MovieID | MovieName     | Category |
| ------- | ------------- | -------- |
| 002     | Tamil_Movie   | Action   |
| 005     | Telugu_Movie  | Action   |
| 006     | Punjabi_Movie | Comedy   |

Explanation:

OR is used because we want movies belonging to either Comedy or Action.

### (g) List the movies which have not been released yet.

Answer:

```
SELECT *
FROM MOVIE
WHERE ReleaseDate IS NULL;
```

Output:

| MovieID | MovieName     |
| ------- | ------------- |
| 005     | Telugu_Movie  |
| 006     | Punjabi_Movie |

Explanation:

IS NULL is used to retrieve records where ReleaseDate is missing.

# Q5. School Sports Database

Suppose your school management has decided to conduct cricket matches between students of Class XI and Class XII.

Students can join any one of the following four teams:

1. Team Titan
2. Team Rockers
3. Team Magnet
4. Team Hurricane

Answer the following questions.

### (a) Create a database named SPORTS.

Answer:

```
CREATE DATABASE Sports;
```

To select the database:

```
USE Sports;
```

### (b) Create a table TEAM with the following considerations:

- TeamID should store integer values between 1 and 9.
- TeamID should uniquely identify a team.
- TeamName should store a string of at least 10 characters.

Answer:

```
CREATE TABLE TEAM (
    TeamID INT,
    TeamName VARCHAR(30),
    CHECK (TeamID BETWEEN 1 AND 9),
    CHECK (CHAR_LENGTH(TeamName) >= 10)
);
```

Explanation:

- TeamID is an integer.
- TeamName stores team names.
- CHECK ensures that TeamID is between 1 and 9.
- CHAR_LENGTH ensures that TeamName contains at least 10 characters.

### (c) Using table-level constraint, make TeamID the primary key.

Answer:

```
ALTER TABLE TEAM
ADD PRIMARY KEY (TeamID);
```

Explanation:

TeamID becomes the primary key and uniquely identifies every team.

### (d) Show the structure of the TEAM table using an SQL command.

Answer:

```
DESC TEAM;
```

OR

```
DESCRIBE TEAM;
```

### (e) Insert the following four rows into the TEAM table.

| TeamID | TeamName       |
| ------ | -------------- |
| 1      | Team Titan     |
| 2      | Team Rockers   |
| 3      | Team Magnet    |
| 4      | Team Hurricane |

Answer:

```
INSERT INTO TEAM
VALUES
(1, 'Team Titan'),
(2, 'Team Rockers'),
(3, 'Team Magnet'),
(4, 'Team Hurricane');
```

### (f) Show the contents of the TEAM table.

Answer:

```
SELECT *
FROM TEAM;
```

Output:

| TeamID | TeamName       |
| ------ | -------------- |
| 1      | Team Titan     |
| 2      | Team Rockers   |
| 3      | Team Magnet    |
| 4      | Team Hurricane |

### (g) Create another table MATCH_DETAILS and insert the following data.

Given table:

| MatchID | MatchDate  | FirstTeamID | SecondTeamID | FirstTeamScore | SecondTeamScore |
| ------- | ---------- | ----------- | ------------ | -------------- | --------------- |
| M1      | 2018-07-17 | 1           | 2            | 90             | 86              |
| M2      | 2018-07-18 | 3           | 4            | 45             | 48              |
| M3      | 2018-07-19 | 1           | 3            | 78             | 56              |
| M4      | 2018-07-19 | 2           | 4            | 56             | 67              |
| M5      | 2018-07-20 | 1           | 4            | 32             | 87              |
| M6      | 2018-07-21 | 2           | 3            | 67             | 51              |

Answer:

```
CREATE TABLE MATCH_DETAILS (
    MatchID CHAR(2) PRIMARY KEY,
    MatchDate DATE,
    FirstTeamID INT,
    SecondTeamID INT,
    FirstTeamScore INT,
    SecondTeamScore INT
);
```

Insert records:

```
INSERT INTO MATCH_DETAILS
VALUES
('M1', '2018-07-17', 1, 2, 90, 86),
('M2', '2018-07-18', 3, 4, 45, 48),
('M3', '2018-07-19', 1, 3, 78, 56),
('M4', '2018-07-19', 2, 4, 56, 67),
('M5', '2018-07-20', 1, 4, 32, 87),
('M6', '2018-07-21', 2, 3, 67, 51);
```

### (h) Use the foreign key constraint in MATCH_DETAILS with reference to TEAM so that MATCH_DETAILS records scores of teams existing in TEAM only.

Answer:

```
ALTER TABLE MATCH_DETAILS
ADD CONSTRAINT fk_first_team
FOREIGN KEY (FirstTeamID)
REFERENCES TEAM(TeamID);
```

```
ALTER TABLE MATCH_DETAILS
ADD CONSTRAINT fk_second_team
FOREIGN KEY (SecondTeamID)
REFERENCES TEAM(TeamID);
```

Explanation:

- FirstTeamID refers to TeamID in TEAM.
- SecondTeamID also refers to TeamID in TEAM.
- Only existing team IDs can be entered in these columns.

# Q6. Using the SPORTS database containing two relations (TEAM, MATCH_DETAILS), answer the following relational algebra queries.

### Given MATCH_DETAILS Table

| MatchID | MatchDate  | FirstTeamID | SecondTeamID | FirstTeamScore | SecondTeamScore |
| ------- | ---------- | ----------- | ------------ | -------------- | --------------- |
| M1      | 2018-07-17 | 1           | 2            | 90             | 86              |
| M2      | 2018-07-18 | 3           | 4            | 45             | 48              |
| M3      | 2018-07-19 | 1           | 3            | 78             | 56              |
| M4      | 2018-07-19 | 2           | 4            | 56             | 67              |
| M5      | 2018-07-20 | 1           | 4            | 32             | 87              |
| M6      | 2018-07-21 | 2           | 3            | 67             | 51              |

### (a) Retrieve the MatchID of all matches where both teams have scored more than 70.

Answer – Relational Algebra:

```
π MatchID (σ FirstTeamScore > 70 AND SecondTeamScore > 70 (MATCH_DETAILS))
```

SQL Query:

```
SELECT MatchID
FROM MATCH_DETAILS
WHERE FirstTeamScore > 70
AND SecondTeamScore > 70;
```

Output:

| MatchID |
| ------- |
| M1      |

Explanation:

Only M1 has both team scores greater than 70.

### (b) Retrieve the MatchID of all matches where FirstTeam has scored less than 70 but SecondTeam has scored more than 70.

Answer – Relational Algebra:

```
π MatchID (σ FirstTeamScore < 70 AND SecondTeamScore > 70 (MATCH_DETAILS))
```

SQL Query:

```
SELECT MatchID
FROM MATCH_DETAILS
WHERE FirstTeamScore < 70
AND SecondTeamScore > 70;
```

Output:

| MatchID |
| ------- |
| M4      |
| M5      |

### (c) Find out the MatchID and date of matches played by Team 1 and won by it.

Answer – Relational Algebra:

```
π MatchID, MatchDate
(σ FirstTeamID = 1 AND FirstTeamScore > SecondTeamScore
(MATCH_DETAILS))
```

SQL Query:

```
SELECT MatchID, MatchDate
FROM MATCH_DETAILS
WHERE FirstTeamID = 1
AND FirstTeamScore > SecondTeamScore;
```

Output:

| MatchID | MatchDate  |
| ------- | ---------- |
| M1      | 2018-07-17 |
| M3      | 2018-07-19 |

Explanation:

Team 1 played matches M1, M3 and M5.

It won M1 and M3 because its score was greater than the opponent's score.

### (d) Find out the MatchID of matches played by Team 2 and not won by it.

Answer – Relational Algebra:

```
π MatchID
(σ (FirstTeamID = 2 AND FirstTeamScore <= SecondTeamScore)
OR
(SecondTeamID = 2 AND SecondTeamScore <= FirstTeamScore)
(MATCH_DETAILS))
```

SQL Query:

```
SELECT MatchID
FROM MATCH_DETAILS
WHERE
(FirstTeamID = 2 AND FirstTeamScore <= SecondTeamScore)
OR
(SecondTeamID = 2 AND SecondTeamScore <= FirstTeamScore);
```

Output:

| MatchID |
| ------- |
| M4      |
| M6      |

Explanation:

- Team 2 played M1, M4 and M6.
- It won M1.
- It lost M4 and M6.

Therefore, M4 and M6 are the required matches.

### (e) In the TEAM relation, change the name of the relation to T_DATA. Also change the attributes TeamID and TeamName to T_ID and T_NAME respectively.

Answer:

Rename the table:

```
RENAME TABLE TEAM TO T_DATA;
```

Rename TeamID:

```
ALTER TABLE T_DATA
RENAME COLUMN TeamID TO T_ID;
```

Rename TeamName:

```
ALTER TABLE T_DATA
RENAME COLUMN TeamName TO T_NAME;
```

Explanation:

- TEAM is renamed to T_DATA.
- TeamID is renamed to T_ID.
- TeamName is renamed to T_NAME.

# Q7. Differentiate between the following commands.

### (a) ALTER and UPDATE

| ALTER                                           | UPDATE                                             |
| ----------------------------------------------- | -------------------------------------------------- |
| ALTER is a DDL command.                         | UPDATE is a DML command.                           |
| It changes the structure of a table.            | It changes the data stored in a table.             |
| Used to add, remove or modify columns.          | Used to modify existing records.                   |
| Does not directly update the values of records. | Updates the values of selected records.            |
| Example: ALTER TABLE STUDENT ADD Age INT;       | Example: UPDATE STUDENT SET Age=17 WHERE RollNo=1; |

### (b) DELETE and DROP

| DELETE                                        | DROP                                    |
| --------------------------------------------- | --------------------------------------- |
| DELETE is a DML command.                      | DROP is a DDL command.                  |
| It removes records from a table.              | It removes an entire table or database. |
| Table structure remains unchanged.            | Table structure is also removed.        |
| WHERE can be used to delete selected records. | WHERE cannot be used with DROP.         |
| Example: DELETE FROM STUDENT WHERE RollNo=1;  | Example: DROP TABLE STUDENT;            |

# Q8. Create a database called STUDENT_PROJECT having the following tables. Choose appropriate data types and apply necessary constraints.

The database contains three tables:

1. STUDENT
2. PROJECT_ASSIGNED
3. PROJECT

### STUDENT Table

| RollNo | Name  | Stream     | Section | RegistrationID |
| ------ | ----- | ---------- | ------- | -------------- |
| 1      | Aman  | Science    | I       | R101           |
| 2      | Riya  | Commerce   | II      | R102           |
| 3      | Rahul | Humanities | I       | R103           |

Conditions:

- Stream can be Science, Commerce or Humanities.
- Section can be I or II.

### PROJECT_ASSIGNED Table

| RegistrationID | ProjectID | AssignDate |
| -------------- | --------- | ---------- |
| R101           | P01       | 2026-01-10 |
| R102           | P02       | 2026-01-11 |
| R103           | P03       | 2026-01-12 |

### PROJECT Table

| ProjectID | ProjectName      | SubmissionDate | TeamSize | GuideTeacher |
| --------- | ---------------- | -------------- | -------- | ------------ |
| P01       | AI Project       | 2026-03-10     | 3        | Mr Sharma    |
| P02       | Web Development  | 2026-03-15     | 4        | Mrs Gupta    |
| P03       | Database Project | 2026-03-20     | 2        | Mr Verma     |

## Answer

### Step 1: Create Database

```
CREATE DATABASE STUDENT_PROJECT;
```

Select the database:

```
USE STUDENT_PROJECT;
```

### Step 2: Create STUDENT Table

```
CREATE TABLE STUDENT (
    RollNo INT UNIQUE,
    Name VARCHAR(30) NOT NULL,
    Stream VARCHAR(20),
    Section CHAR(1),
    RegistrationID VARCHAR(10) PRIMARY KEY,
    CHECK (Stream IN ('Science', 'Commerce', 'Humanities')),
    CHECK (Section IN ('I', 'II'))
);
```

Explanation:

- RegistrationID is the primary key.
- RollNo is also kept unique.
- Name cannot be NULL.
- Stream accepts only Science, Commerce or Humanities.
- Section accepts only I or II.

### Step 3: Create PROJECT Table

```
CREATE TABLE PROJECT (
    ProjectID VARCHAR(10) PRIMARY KEY,
    ProjectName VARCHAR(50) NOT NULL,
    SubmissionDate DATE,
    TeamSize INT,
    GuideTeacher VARCHAR(30)
);
```

Explanation:

ProjectID is the primary key because it uniquely identifies each project.

### Step 4: Create PROJECT_ASSIGNED Table

```
CREATE TABLE PROJECT_ASSIGNED (
    RegistrationID VARCHAR(10),
    ProjectID VARCHAR(10),
    AssignDate DATE,
    PRIMARY KEY (RegistrationID, ProjectID),
    FOREIGN KEY (RegistrationID)
        REFERENCES STUDENT(RegistrationID),
    FOREIGN KEY (ProjectID)
        REFERENCES PROJECT(ProjectID)
);
```

Explanation:

- RegistrationID is a foreign key referencing STUDENT.
- ProjectID is a foreign key referencing PROJECT.
- Both columns together form a composite primary key.

### (a) Populate these tables with appropriate data.

Insert records into STUDENT:

```
INSERT INTO STUDENT
VALUES
(1, 'Aman', 'Science', 'I', 'R101'),
(2, 'Riya', 'Commerce', 'II', 'R102'),
(3, 'Rahul', 'Humanities', 'I', 'R103'),
(4, 'Meena', 'Commerce', 'I', 'R104');
```

Insert records into PROJECT:

```
INSERT INTO PROJECT
VALUES
('P01', 'AI Project', '2026-03-10', 3, 'Mr Sharma'),
('P02', 'Web Development', '2026-03-15', 4, 'Mrs Gupta'),
('P03', 'Database Project', '2026-03-20', 2, 'Mr Verma');
```

Insert records into PROJECT_ASSIGNED:

```
INSERT INTO PROJECT_ASSIGNED
VALUES
('R101', 'P01', '2026-01-10'),
('R102', 'P02', '2026-01-11'),
('R103', 'P03', '2026-01-12'),
('R104', 'P02', '2026-01-13');
```

### (b) Write SQL queries for the following.

The queries are given in the next subquestions.

### (c) Find the names of students in Science Stream.

Answer:

```
SELECT Name
FROM STUDENT
WHERE Stream = 'Science';
```

Output:

| Name |
| ---- |
| Aman |

Explanation:

The WHERE clause selects only students belonging to Science Stream.

### (d) What will be the primary keys of the three tables?

Answer:

| Table            | Primary Key               |
| ---------------- | ------------------------- |
| STUDENT          | RegistrationID            |
| PROJECT          | ProjectID                 |
| PROJECT_ASSIGNED | RegistrationID, ProjectID |

Explanation:

PROJECT_ASSIGNED has a composite primary key consisting of two columns.

### (e) What are the foreign keys of the three relations?

Answer:

| Table            | Foreign Key               |
| ---------------- | ------------------------- |
| STUDENT          | None                      |
| PROJECT          | None                      |
| PROJECT_ASSIGNED | RegistrationID, ProjectID |

Explanation:

- RegistrationID in PROJECT_ASSIGNED references RegistrationID in STUDENT.
- ProjectID in PROJECT_ASSIGNED references ProjectID in PROJECT.

### (f) Find names of all students studying in Commerce Stream and guided by the same teacher, even if they are assigned different projects.

Answer:

```
SELECT DISTINCT S.Name, P.GuideTeacher
FROM STUDENT S
JOIN PROJECT_ASSIGNED PA
    ON S.RegistrationID = PA.RegistrationID
JOIN PROJECT P
    ON PA.ProjectID = P.ProjectID
WHERE S.Stream = 'Commerce';
```

Explanation:

1. STUDENT is joined with PROJECT_ASSIGNED using RegistrationID.
2. PROJECT_ASSIGNED is joined with PROJECT using ProjectID.
3. WHERE selects students from Commerce Stream.
4. DISTINCT prevents duplicate output rows.

Note: The query displays the Commerce students and their guide teachers. If multiple Commerce students are guided by the same teacher, they will appear with the same GuideTeacher value.

# Q9. EMP-DEPENDENT Database

An organization ABC maintains a database named EMP-DEPENDENT to record details about employees and their dependents.

The database contains two relations:

### EMPLOYEE

```
EMPLOYEE(AadhaarNo, Name, Address, Department, EmpID)
```

### DEPENDENT

```
DEPENDENT(EmpID, DependentName, Relationship)
```

Assume EmpID is the primary key of EMPLOYEE and a foreign key in DEPENDENT.

### (a) Find the names of employees with their dependent names.

Answer:

```
SELECT E.Name, D.DependentName
FROM EMPLOYEE E
JOIN DEPENDENT D
ON E.EmpID = D.EmpID;
```

Explanation:

- EMPLOYEE and DEPENDENT are joined using EmpID.
- The query displays employee names with their dependent names.

### (b) Find employee details working in a department, say, PRODUCTION.

Answer:

```
SELECT *
FROM EMPLOYEE
WHERE Department = 'PRODUCTION';
```

Explanation:

The WHERE clause selects employees whose department is PRODUCTION.

### (c) Find employee names having no dependent.

Answer:

```
SELECT E.Name
FROM EMPLOYEE E
LEFT JOIN DEPENDENT D
ON E.EmpID = D.EmpID
WHERE D.EmpID IS NULL;
```

Explanation:

- LEFT JOIN displays all employees.
- If an employee has no dependent, the matching DEPENDENT columns contain NULL.
- IS NULL selects employees without dependents.

### (d) Find names of employees working in SALES and having exactly two dependents.

Answer:

```
SELECT E.Name
FROM EMPLOYEE E
JOIN DEPENDENT D
ON E.EmpID = D.EmpID
WHERE E.Department = 'SALES'
GROUP BY E.EmpID, E.Name
HAVING COUNT(D.DependentName) = 2;
```

Explanation:

- JOIN connects employees with their dependents.
- WHERE selects employees working in SALES.
- GROUP BY groups records employee-wise.
- COUNT counts the dependents.
- HAVING selects employees having exactly two dependents.

# Q10. Wonderful Garments – SCHOOL_UNIFORM Database

A shop called Wonderful Garments sells school uniforms.

It maintains a database named SCHOOL_UNIFORM containing two relations:

1. UNIFORM
2. PRICE

### UNIFORM Table

| UCode | UName | UColor |
| ----- | ----- | ------ |
| 1     | Shirt | White  |
| 2     | Pant  | Grey   |
| 3     | Skirt | Grey   |
| 4     | Tie   | Blue   |
| 5     | Socks | Blue   |
| 6     | Belt  | Blue   |

### PRICE Table

| UCode | Size | Price |
| ----- | ---- | ----- |
| 1     | M    | 500   |
| 1     | L    | 580   |
| 1     | XL   | 620   |
| 2     | M    | 810   |
| 2     | L    | 890   |
| 2     | XL   | 940   |
| 3     | M    | 770   |
| 3     | L    | 830   |
| 3     | XL   | 910   |
| 4     | S    | 150   |
| 4     | L    | 170   |
| 5     | S    | 180   |
| 5     | L    | 210   |
| 6     | M    | 110   |
| 6     | L    | 140   |
| 6     | XL   | 160   |

Given constraints:

- UCode is the primary key of UNIFORM.
- UCode and Size together form a composite primary key of PRICE.

### (a) The PRICE relation has an attribute named Price. In order to avoid confusion, write SQL query to change the name of the relation PRICE to COST.

Answer:

```
RENAME TABLE PRICE TO COST;
```

Explanation:

The table PRICE is renamed to COST.

### (b) M/S Wonderful Garments also keeps handkerchiefs of red color, medium size of ₹100 each. Insert this record in COST table.

Answer:

First, add the handkerchief details to the UNIFORM table:

```
INSERT INTO UNIFORM
VALUES (7, 'Handkerchief', 'Red');
```

Now insert its price details into COST:

```
INSERT INTO COST
VALUES (7, 'M', 100);
```

Explanation:

- UCode 7 represents Handkerchief.
- Size is M.
- Price is 100.

### (c) When you used the above query to insert data, you were able to enter the values for handkerchief without entering its details in the UNIFORM relation. Make a provision so that the data can be entered in COST table only if it is already there in UNIFORM table.

Answer:

We use a FOREIGN KEY constraint.

```
ALTER TABLE COST
ADD FOREIGN KEY (UCode)
REFERENCES UNIFORM(UCode);
```

Explanation:

- UCode in COST becomes a foreign key.
- It references UCode in UNIFORM.
- A record cannot be inserted into COST with a UCode that does not exist in UNIFORM.

### (d) Further, you should be able to assign a new UCode to an item only if it has a valid UName. Write a query to add appropriate constraint to the SCHOOL_UNIFORM database.

Answer:

We use the NOT NULL constraint on UName.

```
ALTER TABLE UNIFORM
MODIFY UName VARCHAR(30) NOT NULL;
```

Explanation:

The NOT NULL constraint ensures that UName cannot contain NULL values.

Every uniform item must have a name.

### (e) ALTER table to add the constraint that price of an item is always greater than zero.

Answer:

We use the CHECK constraint.

```
ALTER TABLE COST
ADD CONSTRAINT chk_price
CHECK (Price > 0);
```

Explanation:

The CHECK constraint ensures that the price of every item must be greater than zero.

For example:

- Price = 100 is valid.
- Price = 500 is valid.
- Price = 0 is invalid.
- Price = -50 is invalid.

# Quick Revision – Important Answers

| Question | Important Concept                                           |
| -------- | ----------------------------------------------------------- |
| Q1       | SQL commands and their functions                            |
| Q2       | Degree, columns, SELECT, INSERT and DELETE                  |
| Q3       | Foreign Key and SELECT \*                                   |
| Q4       | SELECT, DISTINCT, WHERE, AND, OR, IS NULL and aliases       |
| Q5       | CREATE DATABASE, CREATE TABLE, PRIMARY KEY and FOREIGN KEY  |
| Q6       | Relational algebra and SQL queries                          |
| Q7       | Difference between ALTER, UPDATE, DELETE and DROP           |
| Q8       | Multiple tables, constraints, primary keys and foreign keys |
| Q9       | JOIN, LEFT JOIN, GROUP BY, COUNT and HAVING                 |
| Q10      | RENAME TABLE, FOREIGN KEY, NOT NULL and CHECK               |

# Important SQL Concepts to Practise

1. CREATE DATABASE
2. USE
3. CREATE TABLE
4. PRIMARY KEY
5. FOREIGN KEY
6. INSERT INTO
7. SELECT \*
8. SELECT DISTINCT
9. WHERE
10. AND and OR
11. BETWEEN
12. IN
13. ORDER BY
14. IS NULL
15. LIKE
16. UPDATE
17. DELETE
18. ALTER TABLE
19. JOIN
20. GROUP BY and HAVING



```

```
    gender CHAR(1),
    PRIMARY KEY (student_id)
);
