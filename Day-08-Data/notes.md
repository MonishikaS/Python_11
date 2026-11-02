# Chapter 5 – Understanding Data
## Class 11 – Informatics Practices

# 1. Introduction to Data

### What is Data?

Data refers to a collection of raw facts and figures that can be processed to generate meaningful information.

**Examples:**
- Marks obtained by students.
- Names and ages of people.
- Temperature recorded every day.
- Sales details of a shop.

### What is Information?

Information is processed data that has meaning and can help us make decisions.

**Example:**

- Data: 70, 80, 90, 60, 100
- Information: The average marks of the student is 80.

### Difference between Data and Information

| Data | Information |
|---|---|
| Data consists of raw facts. | Information is processed data. |
| It may not have a meaningful form. | It has a meaningful form. |
| Example: 50, 60, 70. | Example: Average marks are 60. |

### Why is Data Important?

Data helps us:
1. Make better decisions.
2. Understand people's needs.
3. Identify patterns and trends.
4. Improve products and services.
5. Predict future situations.
6. Solve real-life problems.

**Real-life examples:**
- A school uses students' marks to analyse academic performance.
- A shopping mall analyses sales data to understand customer preferences.
- Weather departments analyse data to predict rainfall and cyclones.
- Banks maintain account data to manage transactions.

### What is Census?

Census is the systematic process of collecting and recording information about the population of a country or a particular area.

**Example:** The government collects information about people's age, education, occupation and other details during a population census.

---

# 2. Types of Data

Data can mainly be classified into two types:

## A. Structured Data

Structured data is data that is organised in a fixed format, usually in rows and columns.

It is easy to store, search and process using tables and databases.

**Example: Student Record**

| Roll No. | Name | Class | Marks |
|---|---|---|---|
| 1 | Aman | XI | 85 |
| 2 | Riya | XI | 90 |
| 3 | Rahul | XI | 78 |

Here:
- Each row represents one student's record.
- Each column represents a particular attribute.

**Other examples:**
- Attendance records.
- Bank account details.
- Employee records.
- Student registration forms.

## B. Unstructured Data

Unstructured data is data that does not follow a fixed format or traditional row-and-column structure.

It may contain text, images, audio, videos and other multimedia content.

**Examples:**
- Photographs.
- Videos.
- Emails.
- Social media posts.
- Newspaper articles.
- Audio recordings.

### Difference between Structured and Unstructured Data

| Structured Data | Unstructured Data |
|---|---|
| Follows a fixed format. | Does not follow a fixed format. |
| Organised in rows and columns. | Not organised in traditional rows and columns. |
| Easier to search and process using tables. | Requires different methods for processing. |
| Example: Student database. | Example: Video or photograph. |

## Important Terms Related to Structured Data

### 1. Row

A row represents one complete record in a table.

**Example:** All the details of one student form a row.

### 2. Column

A column represents a particular characteristic or property of the data.

**Example:** Name, age and marks are columns in a student table.

### 3. Attribute

An attribute is a property or characteristic of an entity.

**Example:** For a student, name, roll number, age and marks are attributes.

### 4. Observation

An observation is a single record or set of values collected for an individual entity.

**Example:** The complete details of one student in a table form an observation.

### 5. Metadata

Metadata means **data about data**.

It provides additional information that helps describe or understand a particular data item.

**Examples:**

For an image:
- Image size.
- Image format (JPEG, PNG).
- Image resolution.

For an email:
- Subject.
- Recipient.
- Main body.
- Attachments.

---

# 3. Data Collection

### What is Data Collection?

Data collection is the process of identifying already available data or gathering data from appropriate sources for further processing.

Before processing data, we need to collect it.

### Three Situations of Data Collection

Consider a grocery shop that wants to maintain its sales records.

**Situation 1: Data is available in a physical register**

- The shopkeeper has recorded sales in a notebook.
- We need to enter the information into a digital format, such as a spreadsheet.

**Situation 2: Data is already available digitally**

- The shopkeeper has sales data in a CSV file.
- We can directly use the existing digital data.

**Situation 3: Data has not been recorded anywhere**

- The shopkeeper has not maintained any records.
- We can develop software using a programming language such as Python.
- The software can store and retrieve data using files or a database management system such as MySQL.

### Sources of Data Collection

Data can be collected from:
1. Surveys and questionnaires.
2. Interviews.
3. Existing records and registers.
4. Digital files.
5. Websites and online platforms.
6. Sensors and devices.
7. Applications and software.

### Real-Life Applications of Data Collection

- Hospitals collect patient details.
- Schools collect student information.
- Shopping malls collect purchase details.
- Banks collect customer and account information.

---

# 4. Data Storage

### What is Data Storage?

Data storage is the process of storing data on storage devices so that it can be retrieved and used later.

We store data because it may be required for future use.

### Common Digital Storage Devices

| Storage Device | Description |
|---|---|
| HDD (Hard Disk Drive) | Stores large amounts of data using magnetic storage. |
| SSD (Solid State Drive) | Stores data electronically and is generally faster than HDD. |
| CD/DVD | Optical storage devices used to store data. |
| Pen Drive | Small portable device used to transfer and store data. |
| Memory Card | Small storage device commonly used in phones and cameras. |
| Tape Drive | Used for storing large amounts of data, often for backup. |

### What are Files?

A file is a collection of related data stored together on a computer.

**Examples:**
- Images.
- Documents.
- Audio files.
- Video files.
- Spreadsheet files.

We can add, modify or delete data in files.

### What is File Processing?

File processing means performing operations such as adding, modifying, deleting and retrieving data stored in files.

### What is DBMS?

DBMS stands for **Database Management System**.

It is software used to create, store, organise, manage and retrieve data from databases.

**Example:** MySQL.

DBMS helps manage large amounts of data efficiently.

---

# 5. Data Processing

### What is Data Processing?

Data processing is the process of converting raw data into meaningful information by performing different operations on it.

A large amount of raw data cannot directly help us make decisions. We need to process it to obtain useful results.

### Data Processing Cycle

The data processing cycle consists of three main stages:

1. Input
2. Processing
3. Output

## A. Input

Input refers to collecting and entering raw data into a system.

It includes three main activities:

**1. Data Collection**

Gathering data from different sources.

Example: Collecting student details during admission.

**2. Data Preparation**

Checking and organising collected data before entering it into the system.

Example: Checking whether all student forms contain the required information.

**3. Data Entry**

Entering the prepared data into a computer system.

Example: Entering student details into a school database.

## B. Processing

Processing means performing operations on the collected data to obtain useful results.

It includes:

**1. Store:** Saving data for future use.

**2. Retrieve:** Getting previously stored data.

**3. Classify:** Grouping data into different categories.

**4. Update:** Modifying existing data whenever required.

## C. Output

Output is the meaningful result obtained after processing the data.

It can be represented in the form of:
- Reports.
- Tables.
- Charts.
- Results.
- Certificates.

### Example 1: Online Examination Registration

| Stage | Description |
|---|---|
| Input | Student name, address, marks, photograph and payment details. |
| Processing | Checking details, verifying eligibility and generating roll number. |
| Output | Examination admit card. |

### Example 2: ATM Cash Withdrawal

| Stage | Description |
|---|---|
| Input | ATM PIN, account number and withdrawal amount. |
| Processing | Checking PIN, verifying account balance and deducting the amount. |
| Output | Cash and transaction receipt. |

### Example 3: Train Ticket Booking

| Stage | Description |
|---|---|
| Input | Source, destination, date, passenger details and payment information. |
| Processing | Checking seat availability and verifying payment. |
| Output | Confirmed ticket or waiting list ticket. |

---

# 6. Statistical Techniques for Data Processing

### What are Statistical Techniques?

Statistical techniques are mathematical methods used to summarise, analyse and understand data.

They help us identify important characteristics of data and make better decisions.

For example, a teacher can use statistical techniques to calculate the average marks of a class.

The five important statistical techniques discussed in this chapter are:

1. Mean
2. Median
3. Mode
4. Range
5. Standard Deviation

These techniques are divided into two categories.

| Measures of Central Tendency | Measures of Variability |
|---|---|
| Mean | Range |
| Median | Standard Deviation |
| Mode | |

## 6.1 Measures of Central Tendency

Measures of central tendency help us identify the central or typical value of a dataset.

### A. Mean

**Definition:** Mean is the average of all the given values.

It is calculated by adding all values and dividing the sum by the total number of values.

**Formula:**

Mean = Sum of all values / Number of values

**Example:**

Marks of five students:

10, 20, 30, 40, 50

Mean = (10 + 20 + 30 + 40 + 50) / 5

Mean = 150 / 5

**Mean = 30**

**Applications:**
- Finding the average marks of students.
- Calculating average monthly expenses.
- Finding average temperature.
- Calculating average salary.

### B. Median

**Definition:** Median is the middle value of a dataset when the values are arranged in ascending or descending order.

There are two situations:

**1. When the number of values is odd**

The middle value is the median.

Example:

10, 20, 30, 40, 50

There are five values.

Median = **30**

**2. When the number of values is even**

The median is the average of the two middle values.

Example:

10, 20, 30, 40

The two middle values are 20 and 30.

Median = (20 + 30) / 2

Median = **25**

**Important:** Always arrange the values before calculating the median.

**Applications:**
- Finding the middle salary of employees.
- Analysing house prices.
- Finding the typical income of a group.
- Understanding the middle value in examination marks.

### C. Mode

**Definition:** Mode is the value that appears the most number of times in a given dataset.

In simple words, mode is the most frequently occurring value.

**Example:**

Data:

10, 20, 20, 30, 40, 20, 50

Here, 20 occurs three times.

Therefore, Mode = **20**

**Important points:**
- A dataset may have one mode.
- A dataset may have more than one mode if multiple values have the same highest frequency.
- A dataset may have no mode if every value occurs only once.
- Mode can be used for both numerical and non-numerical data.

**Applications:**
- Finding the most popular clothing size.
- Finding the most popular car colour.
- Identifying the most frequently chosen product.
- Finding the most common division secured by students.

---

## 6.2 Measures of Variability

Measures of variability tell us how much the values in a dataset differ or spread out from one another.

They are also called **measures of dispersion**.

For example, two classes may have the same average marks, but the marks of students in one class may be more spread out than those in the other class.

The two common measures of variability are Range and Standard Deviation.

### A. Range

**Definition:** Range is the difference between the maximum and minimum values in a dataset.

**Formula:**

Range = Maximum Value − Minimum Value

**Example:**

Data:

10, 20, 30, 40, 50

Maximum value = 50

Minimum value = 10

Range = 50 − 10

**Range = 40**

**Applications:**
- Finding the difference between the highest and lowest salaries.
- Comparing temperature variations.
- Comparing price differences.
- Finding the spread between the highest and lowest marks.

### B. Standard Deviation

**Definition:** Standard deviation is the positive square root of the average of the squared differences of each value from the mean.

In simple words, standard deviation tells us how far the values are spread out from their average.

**Important points:**
- Low standard deviation means values are close to the mean.
- High standard deviation means values are spread far away from the mean.
- It is used to measure the variation or consistency of data.

**Formula:**

\[
SD = \sqrt{\frac{\sum (x_i-\bar{x})^2}{n}}
\]

Where:

- \(SD\) = Standard Deviation
- \(x_i\) = Each individual value
- \(\bar{x}\) = Mean of the values
- \(n\) = Total number of values
- \(\sum\) = Sum of all values

### Steps to Calculate Standard Deviation

1. Calculate the mean of the given values.
2. Subtract the mean from each value.
3. Square each difference.
4. Add all the squared differences.
5. Divide the sum by the total number of values.
6. Calculate the square root of the result.

**Example:**

Find the standard deviation of:

2, 4, 6

**Step 1: Calculate Mean**

Mean = (2 + 4 + 6) / 3

Mean = 12 / 3 = 4

**Step 2: Calculate deviations and squares**

| Value (x) | x − Mean | (x − Mean)² |
|---:|---:|---:|
| 2 | -2 | 4 |
| 4 | 0 | 0 |
| 6 | 2 | 4 |
| **Total** | **0** | **8** |

**Step 3: Apply the formula**

\[
SD = \sqrt{\frac{8}{3}}
\]

\[
SD = \sqrt{2.67}
\]

\[
\boxed{SD \approx 1.63}
\]

**Applications:**
- Measuring variation in employee salaries.
- Comparing income levels of two cities.
- Measuring variation in students' marks.
- Comparing temperature variations.
- Understanding how consistent a dataset is.

---

# 7. Difference Between Statistical Techniques

| Technique | Meaning | Used For |
|---|---|---|
| Mean | Average of values. | Finding average marks or salary. |
| Median | Middle value of arranged data. | Finding the central value. |
| Mode | Most frequently occurring value. | Finding the most popular item. |
| Range | Maximum − Minimum. | Finding the difference between extreme values. |
| Standard Deviation | Measures spread around the mean. | Finding variation or consistency. |

### How to Identify the Correct Statistical Technique?

| If the question asks for... | Use |
|---|---|
| Average or average performance | Mean |
| Middle value | Median |
| Most popular or frequently occurring value | Mode |
| Difference between highest and lowest values | Range |
| Disparity, variation or spread | Standard Deviation |

---

# 8. Python and Data Analysis

Python is a programming language that can be used for data processing and analysis.

It has special libraries that help perform calculations and analyse large amounts of data efficiently.

Python can be used to:
- Store and retrieve data.
- Perform mathematical calculations.
- Analyse large datasets.
- Generate meaningful results.
- Create tables and visualisations.

In the following chapters, we will learn about Python libraries used for data processing and analysis.

---

# 9. Quick Revision – Important Definitions

| Term | Definition |
|---|---|
| Data | Raw facts and figures that can be processed to generate information. |
| Information | Processed data that has meaning. |
| Census | Systematic collection and recording of population information. |
| Structured Data | Data organised in a fixed format, usually rows and columns. |
| Unstructured Data | Data that does not follow a fixed format. |
| Metadata | Data about data. |
| Data Collection | Identifying available data or gathering data from appropriate sources. |
| Data Storage | Storing data so that it can be retrieved later. |
| File | A collection of related data stored together. |
| DBMS | Software used to create, store, manage and retrieve data from databases. |
| Data Processing | Converting raw data into meaningful information. |
| Mean | Average of given values. |
| Median | Middle value of arranged data. |
| Mode | Value that appears most frequently. |
| Range | Difference between maximum and minimum values. |
| Standard Deviation | Positive square root of the average of squared differences from the mean. |

---

# 10. Important Points to Remember for Exams

1. Data can be structured or unstructured.
2. Metadata means data about data.
3. Structured data is generally organised in rows and columns.
4. HDD, SSD, CD/DVD, pen drive and memory card are storage devices.
5. DBMS stands for Database Management System.
6. Data processing has three main stages: Input, Processing and Output.
7. Input includes data collection, data preparation and data entry.
8. Processing includes storing, retrieving, classifying and updating data.
9. Mean, Median and Mode are measures of central tendency.
10. Range and Standard Deviation are measures of variability.
11. Median requires data to be arranged in ascending or descending order.
12. Mode can be calculated for numerical as well as non-numerical data.
13. Standard deviation measures how spread out the values are from the mean.
14. A low standard deviation indicates less variation, while a high standard deviation indicates more variation.

**End of Chapter 5 – Understanding Data**
