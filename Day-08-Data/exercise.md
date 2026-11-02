# Exercise – Understanding Data

## Q1. Identify data required to be maintained to perform the following services:

### (a) Declare exam results and print e-certificates

**Answer:**

The following data is required:
1. Student name and roll number.
2. Class and subject details.
3. Marks obtained in each subject.
4. Total marks and percentage.
5. Result status (Pass/Fail).
6. Certificate details.

### (b) Register participants in an exhibition and issue biometric ID cards

**Answer:**

The following data is required:
1. Participant name.
2. Age and gender.
3. Address and contact number.
4. Email ID.
5. Photograph.
6. Biometric details such as fingerprint.
7. Registration ID.

### (c) To search for an image by a search engine

**Answer:**

The following data is required:
1. Image name or keywords.
2. Image format and size.
3. Image dimensions and resolution.
4. Image URL or location.
5. Tags and description.
6. Metadata associated with the image.

### (d) To book an OPD appointment with a hospital in a specific department

**Answer:**

The following data is required:
1. Patient name and age.
2. Contact details.
3. Patient ID.
4. Hospital department.
5. Doctor's name.
6. Appointment date and time.
7. Medical history, if required.

---

## Q2. A school having 500 students wants to identify beneficiaries of the merit-cum-means scholarship, achieving more than 75% for two consecutive years and having family income less than 5 lakh per annum. Briefly describe the data processing steps to be taken to prepare the list of students.

**Answer:**

The school needs to follow these data processing steps:

**1. Input (Data Collection):**

Collect the following data from all 500 students:
- Student name and roll number.
- Marks obtained in the previous year.
- Marks obtained in the current year.
- Annual family income.

**2. Processing:**

- Check whether each student has scored more than 75% in both consecutive years.
- Check whether the student's annual family income is less than ₹5 lakh.
- Select students who satisfy all three conditions.
- Verify the collected information.

**3. Output:**

Prepare a final list containing the names and details of all eligible students who can receive the scholarship.

---

## Q3. A bank 'XYZ' wants to know about its popularity among the residents of a city 'ABC' on the basis of number of bank accounts each family has and the average monthly account balance of each person. Briefly describe the steps to be taken for collecting data and what results can be checked through processing of the collected data.

**Answer:**

**1. Data Collection:**

The bank should collect data from families residing in city ABC through surveys, questionnaires or existing bank records.

The following information should be collected:
- Family details and number of family members.
- Number of bank accounts each family has.
- Account holder details.
- Average monthly account balance of each person.

**2. Data Processing:**

- Organise the collected data in a spreadsheet or database.
- Calculate the number of accounts held by each family.
- Calculate the average monthly account balance.
- Compare the number of accounts and average balances across families.

**3. Results/Output:**

The bank can identify:
- Number of families having accounts in the bank.
- Average number of accounts per family.
- Average monthly account balance.
- Families having multiple accounts.
- Overall popularity of the bank among city residents.

---

## Q4. Identify the type of data being collected/generated in the following scenarios:

### (a) Recording a video

**Answer:** Unstructured data, because a video does not follow a fixed row-and-column structure.

### (b) Marking attendance by teacher

**Answer:** Structured data, because attendance is generally recorded in a fixed format containing student names, roll numbers and attendance status.

### (c) Writing tweets

**Answer:** Unstructured data, because tweets may contain text, images, videos and other content without a fixed tabular structure.

### (d) Filling an application form online

**Answer:** Structured data, because information is entered into predefined fields such as name, age, address and contact number.

---

## Q5. Consider the temperature (in Celsius) of 7 days of a week as 34, 34, 27, 28, 27, 34, 34. Identify the appropriate statistical technique to be used to calculate the following:

Given data:

34, 34, 27, 28, 27, 34, 34

### (a) Find the average temperature.

**Statistical technique: Mean**

Formula:

Mean = Sum of all values / Number of values

Mean = (34 + 34 + 27 + 28 + 27 + 34 + 34) / 7

Mean = 218 / 7

**Mean = 31.14°C**

### (b) Find the temperature Range of that week.

**Statistical technique: Range**

Formula:

Range = Maximum value − Minimum value

Range = 34 − 27

**Range = 7°C**

### (c) Find the standard deviation temperature.

**Statistical technique: Standard Deviation**

Mean = 31.14 (approximately)

| Temperature (x) | x − Mean | (x − Mean)² |
|---:|---:|---:|
| 34 | 2.86 | 8.18 |
| 34 | 2.86 | 8.18 |
| 27 | -4.14 | 17.14 |
| 28 | -3.14 | 9.86 |
| 27 | -4.14 | 17.14 |
| 34 | 2.86 | 8.18 |
| 34 | 2.86 | 8.18 |
| **Total** | | **76.86** |

Formula:

SD = √[Sum of (x − Mean)² / n]

SD = √(76.86 / 7)

SD = √10.98

**Standard Deviation ≈ 3.31°C**

---

## Q6. A school teacher wants to analyse results. Identify the appropriate statistical technique to be used along with its justification for the following cases:

### (a) Teacher wants to compare performance in terms of division secured by students in Class XII A and Class XII B where each class strength is same.

**Answer: Mode**

**Justification:** Division is a categorical value. Mode helps identify the most frequently secured division in each class. Since both classes have equal strength, their most common divisions can be compared.

### (b) Teacher has conducted five unit tests for that class in months July to November and wants to compare the class performance in these five months.

**Answer: Mean**

**Justification:** Mean helps calculate the average marks obtained by the class in each unit test. The average marks of the five months can be compared to understand the overall class performance.

---

## Q7. Suppose annual day of your school is to be celebrated. The school has decided to felicitate those parents of the students studying in classes XI and XII, who are the alumni of the same school. In this context, answer the following questions:

### (a) Which statistical technique should be used to find out the number of students whose both parents are alumni of this school?

**Answer: Mode**

**Justification:** The alumni status of parents can be recorded as categories. Mode helps identify the most frequently occurring category. The school should also count the records in which both parents are alumni to obtain the exact number of students.

### (b) How varied are the age of parents of the students of that school?

**Answer: Standard Deviation**

**Justification:** Standard deviation measures the variation or spread of parents' ages around their mean age. A higher standard deviation indicates greater variation in ages.

---

## Q8. For the annual day celebrations, the teacher is looking for an anchor in a class of 42 students. The teacher would make selection of an anchor on the basis of singing skill, writing skill, as well as monitoring skill.

### (a) Which mode of data collection should be used?

**Answer:**

The teacher should use direct data collection through practical activities, auditions and observation.

### (b) How would you represent the skill of students as data?

**Answer:**

The skills can be represented in a structured tabular format.

Example:

| Roll No. | Singing Skill | Writing Skill | Monitoring Skill |
|---|---|---|---|
| 1 | Good | Average | Good |
| 2 | Average | Good | Excellent |
| 3 | Excellent | Good | Average |

The teacher can assign ratings or marks to each skill and compare the performance of students to select a suitable anchor.

---

## Q9. Differentiate between structured and unstructured data giving one example.

**Answer:**

| Structured Data | Unstructured Data |
|---|---|
| Data arranged in a fixed format. | Data that does not follow a fixed format. |
| Usually organised in rows and columns. | Does not follow a traditional row-and-column structure. |
| Easy to store and process using tables and databases. | Requires different methods and tools for processing. |
| Example: Student attendance record. | Example: Video or photograph. |

---

## Q10. The principal of a school wants to do the following analysis on the basis of food items procured and sold in the canteen:

### (a) Compare the purchase and sale price of fruit juice and biscuits.

**Answer:**

Create a dataset containing the purchase price and selling price of fruit juice and biscuits. Compare the prices to identify the profit earned on each item.

### (b) Compare sales of fruit juice, biscuits and samosa.

**Answer:**

Record the quantity of fruit juice, biscuits and samosa sold over a given period. Compare their total sales quantities to identify which item sells more. Mean can also be used to calculate the average quantity sold per day.

### (c) Variation in sale price of fruit juices of different companies for same quantity (in ml).

**Answer:**

Use Range or Standard Deviation to measure the variation in selling prices of fruit juices of different companies for the same quantity.

**Sample dataset:**

| Food Item | Purchase Price (₹) | Sale Price (₹) |
|---|---:|---:|
| Fruit Juice | 20 | 30 |
| Biscuits | 10 | 15 |
| Samosa | 12 | 20 |

**Profit = Selling Price − Purchase Price**

| Food Item | Profit (₹) |
|---|---:|
| Fruit Juice | 10 |
| Biscuits | 5 |
| Samosa | 8 |

For fruit juice price variation, consider three companies selling the same 200 ml quantity:

| Company | Selling Price (₹) |
|---|---:|
| A | 30 |
| B | 35 |
| C | 40 |

Range = Maximum Price − Minimum Price

Range = 40 − 30

**Range = ₹10**

---

# End of Exercise – Chapter 5
