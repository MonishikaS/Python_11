# Unit 5: Data Literacy – Data Collection to Data Analysis

## 1. Introduction to Data Literacy

### What is Data?

**Definition:** Data is a representation of facts or instructions about an entity (such as students, schools, sports, businesses or animals) that can be processed or communicated by humans or machines.

**Examples:**
- Students' marks
- Names and ages of people
- Weather reports
- Sales records of a shop

AI systems depend on data to learn patterns, make predictions and provide useful results.

### What is Data Literacy?

**Definition:** Data literacy means being able to find and use data effectively.

It includes the ability to:
1. Collect data.
2. Organize data.
3. Check the quality of data.
4. Analyse data.
5. Understand the results.
6. Use data ethically.

**Example:** A teacher collects students' marks, organizes them in a table, calculates the average and identifies students who need extra help. This is an example of using data literacy.

### Importance of Data Literacy in AI

- Helps AI systems learn from data.
- Helps identify patterns and trends.
- Supports better decision-making.
- Helps check whether the input data is correct and useful.
- Helps convert raw data into meaningful information.

### Types of Data Based on Structure

1. **Structured Data:** Data arranged in a fixed format, usually rows and columns.

   Example: A student database containing roll numbers, names and marks.

2. **Semi-Structured Data:** Data that does not follow a strict table format but contains some organization using tags or labels.

   Example: JSON and XML files.

3. **Unstructured Data:** Data that does not have a fixed structure or format.

   Example: Images, videos, audio recordings and text documents.

---

## 2. Data Collection

### What is Data Collection?

**Definition:** Data collection is the process of gathering data from different sources so that it can be analysed and used to find patterns, trends and useful information.

**Example:** A school collects students' marks, attendance and feedback to understand their academic performance.

### Importance of Data Collection in AI

- Data is the main ingredient of an AI project.
- It helps machine learning models identify patterns.
- It helps build models that can make predictions.
- Good-quality data improves the usefulness of predictions.

### Quantity and Diversity of Data

The amount of data required depends on:
- Number of features in the dataset.
- Complexity of the AI model.
- Type of problem being solved.

**Data Diversity:** Data should cover different situations and scenarios in which the AI model will be used.

Example:
- A simple number plate detection project may work with a smaller dataset.
- A medical AI project may require a much larger and more diverse dataset.

**Important:** Collecting diverse data is important because it helps an AI model handle different real-world situations.

### Sources of Data Collection

There are two main sources:

1. Primary Data Sources
2. Secondary Data Sources

### A. Primary Data Sources

**Definition:** Primary data is collected directly for a specific purpose or analysis.

| Method | Description | Example |
|---|---|---|
| Survey | Collecting information from people using forms or questionnaires. | Asking students about their favourite subjects. |
| Interview | Direct communication with individuals or groups to collect information. | Interviewing employees about job satisfaction. |
| Observation | Watching and recording people's behaviour or events. | Observing children's activities in a playground. |
| Experiment | Changing one or more variables to study their effects. | Testing different fertilizers on plants. |
| Marketing Campaign (using data) | Using customer data to understand behaviour and improve marketing. | Sending product offers based on previous purchases. |
| Questionnaire | A list of questions designed to collect information from respondents. | Asking customers to rate a service from 1 to 5. |

**Remember:** A questionnaire is a specific tool used within surveys.

### B. Secondary Data Sources

**Definition:** Secondary data is data that has already been collected and stored by someone else and is available for reuse.

| Method | Description | Example |
|---|---|---|
| Social Media Data Tracking | Collecting information from social media posts, comments and interactions. | Analysing comments about a new product. |
| Web Scraping | Using automated tools to extract information from websites. | Collecting product prices from shopping websites. |
| Satellite Data Tracking | Collecting information about Earth using satellite images. | Monitoring weather and environmental changes. |
| Online Data Platforms | Using already available datasets from online platforms. | Kaggle and GitHub datasets. |

### Difference Between Primary and Secondary Data

| Primary Data | Secondary Data |
|---|---|
| Collected directly for a specific purpose. | Already collected and stored. |
| Usually collected by the researcher. | Collected by another person or organization. |
| Example: Survey and interview. | Example: Books, websites and Kaggle datasets. |

---

## 3. Exploring Data

### What is Exploring Data?

**Definition:** Exploring data means understanding the values in a dataset and identifying whether they are typical, unusual, spread out or extreme.

It also helps identify and correct problems in data before analysis.

**Example:** A teacher examines students' marks to identify the highest mark, lowest mark and average mark.

### Levels of Measurement

**Definition:** The level of measurement describes the way data is measured or classified.

There are two main categories:

1. Qualitative Data
2. Quantitative Data

### A. Qualitative Data

Qualitative data describes categories or qualities. It is generally non-numerical.

It is divided into:

#### 1. Nominal Level

**Definition:** Nominal data consists of categories or names that do not have any specific order or ranking.

**Examples:**
- Eye colours: Brown, Black, Blue.
- Car brands: Mercedes, BMW, Audi.
- Seasons: Summer, Winter, Spring.
- Yes or No responses.

**Important Points:**
- No ranking or order exists.
- Categories cannot be meaningfully added or subtracted.
- Numbers used only as labels are also nominal.

Example: A cricket player's jersey number is nominal because it identifies the player rather than measuring anything.

#### 2. Ordinal Level

**Definition:** Ordinal data consists of categories that follow a specific order or ranking, but the differences between the categories cannot be measured.

**Examples:**
- Food ratings: Unpalatable, Unappetizing, Just Okay, Tasty, Delicious.
- Grades: A, B, C, D.
- Hotel ratings: Excellent, Good, Satisfactory, Unsatisfactory.

**Important Points:**
- Data has a meaningful order.
- Differences between ranks cannot be measured exactly.
- It is generally not suitable for ordinary arithmetic calculations.

### B. Quantitative Data

Quantitative data represents numerical values.

It is divided into:

#### 3. Interval Level

**Definition:** Interval data has a definite order, and the differences between values can be measured, but it does not have an absolute zero point.

**Examples:**
- Temperature in Celsius.
- Temperature in Fahrenheit.

**Important Points:**
- Values can be arranged in order.
- Differences can be calculated.
- Zero does not mean the complete absence of the quantity.
- Ratios are not meaningful.

Example: 40°C is not twice as hot as 20°C.

#### 4. Ratio Level

**Definition:** Ratio data has a definite order, measurable differences and a true zero point. Ratios can also be calculated.

**Examples:**
- Weight of a person.
- Height of a person.
- Distance travelled.
- Age.

**Important Points:**
- Has an absolute zero.
- Addition, subtraction, multiplication and division are meaningful.
- Ratios can be calculated.

Example: A person weighing 80 kg weighs twice as much as a person weighing 40 kg.

### Difference Between Four Levels of Measurement

| Level | Order | Difference Measurable | True Zero | Example |
|---|---|---|---|---|
| Nominal | No | No | No | Eye colour |
| Ordinal | Yes | No | No | Grades |
| Interval | Yes | Yes | No | Temperature in Celsius |
| Ratio | Yes | Yes | Yes | Weight |

### Quantitative Data: Discrete and Continuous

**Discrete Data:** Data that can be counted and usually takes separate, countable values.

Examples:
- Number of students in a class.
- Number of books.
- Number of cars.

**Continuous Data:** Data that can be measured and can take any value within a given range.

Examples:
- Height.
- Weight.
- Temperature.
- Time.

---

## 4. Statistical Analysis of Data

### What is Statistics?

**Definition:** Statistics is the science of data. It uses mathematical techniques to collect, organize, analyse, interpret and present data.

In AI, statistics helps convert observations into meaningful information.

### Measure of Central Tendency

**Definition:** Central tendency is a single value that represents the centre or typical value of a dataset.

The three important measures of central tendency are:

1. Mean
2. Median
3. Mode

### A. Mean

**Definition:** Mean is the average of all the values in a dataset.

**Formula:**

Mean = Sum of all values / Total number of values

**Example:**

Data = 5, 10, 15, 20, 30

Mean = (5 + 10 + 15 + 20 + 30) / 5

Mean = 80 / 5 = **16**

**Python Program:**

```python
import statistics

data = [5, 10, 15, 20, 30]

print("Mean:", statistics.mean(data))
```

**When is Mean Used?**

- When values are relatively evenly distributed.
- When there are no exceptionally high or low values.

### B. Median

**Definition:** Median is the middle value of a dataset when the values are arranged in ascending or descending order.

**Steps to Find Median:**
1. Arrange the values in ascending order.
2. Find the middle value.
3. If there are two middle values, calculate their average.

**Example 1: Odd Number of Values**

Data = 10, 20, 30, 40, 50

Median = **30**

**Example 2: Even Number of Values**

Data = 10, 20, 30, 40

Median = (20 + 30) / 2 = **25**

**Python Program:**

```python
import statistics

data = [10, 20, 30, 40, 50]

print("Median:", statistics.median(data))
```

**When is Median Used?**

- When data contains exceptionally high or low values.
- When the middle position is more useful than the average.

### C. Mode

**Definition:** Mode is the value that occurs most frequently in a dataset.

**Example:**

Data = 10, 20, 20, 30, 40, 20, 50

Mode = **20**

Because 20 appears three times.

**Python Program:**

```python
import statistics

data = [10, 20, 20, 30, 40, 20, 50]

print("Mode:", statistics.mode(data))
```

**When is Mode Used?**

- To find the most frequently occurring value.
- To identify the most popular item or category.

### Difference Between Mean, Median and Mode

| Mean | Median | Mode |
|---|---|---|
| Average of all values. | Middle value. | Most frequent value. |
| Uses all values. | Depends on the position of values. | Depends on frequency. |
| Can be affected by extreme values. | Less affected by extreme values. | Shows the most common value. |

**Real-Life Example:**

A shopkeeper wants to know which shoe size is sold most often. The shopkeeper can use Mode to identify the most popular shoe size.

### Python Statistics Library

Python provides a built-in library called `statistics` for statistical calculations.

```python
import statistics
```

| Function | Purpose |
|---|---|
| `statistics.mean()` | Returns the mean. |
| `statistics.median()` | Returns the median. |
| `statistics.mode()` | Returns the mode. |
| `statistics.variance()` | Returns the variance. |
| `statistics.stdev()` | Returns the standard deviation. |

### D. Variance

**Definition:** Variance is a measure that tells us how far the data values are spread out from the mean.

In simple words, variance tells us how spread out the values are.

**Important Points:**
- Small variance means values are close to the mean.
- High variance means values are spread far from the mean.

### E. Standard Deviation

**Definition:** Standard deviation measures how much the data values differ or spread out from the mean.

**Formula:**

Standard Deviation = Square Root of Variance

**Important Points:**
- Low standard deviation means values are close to the mean.
- High standard deviation means values are widely spread out.

**Example:**

Consider the heights of five dogs:

600, 470, 170, 430, 300

Mean = (600 + 470 + 170 + 430 + 300) / 5

Mean = 1970 / 5 = 394 mm

Variance = 21704

Standard Deviation = √21704 = **147.32 mm**

### Difference Between Variance and Standard Deviation

| Variance | Standard Deviation |
|---|---|
| Measures the spread of data around the mean. | Measures the spread of data around the mean. |
| Expressed in squared units. | Expressed in the original unit of data. |
| It is the average squared deviation from the mean in the population formula. | It is the square root of variance. |

---

## 5. Representation of Data

### What is Data Representation?

**Definition:** Data representation is the process of presenting data in a compact and meaningful format so that it can be easily understood and interpreted.

It helps people understand large amounts of information quickly.

### Types of Data Representation

There are two main types:

### A. Non-Graphical Representation

Data is represented without using graphs or charts.

Examples:
- Tables.
- Case-based representation.

**Example:**

| Student | Marks |
|---|---:|
| Aditi | 85 |
| Rahul | 90 |
| Aman | 78 |

### B. Graphical Representation

Data is represented visually using graphs, charts and diagrams.

It makes large and complex datasets easier to understand.

### What is Data Visualization?

**Definition:** Data visualization is the graphical or pictorial representation of data using graphs, charts and other visual formats.

**Examples:**
- Bar graph.
- Line graph.
- Pie chart.
- Histogram.
- Scatter plot.

### Data Visualization Using Python

Python provides a library called **Matplotlib** for creating graphs and charts.

**Installation:**

```bash
pip install matplotlib
```

**Importing the Library:**

```python
import matplotlib.pyplot as plt
```

### Important Matplotlib Functions

| Function | Purpose |
|---|---|
| `title()` | Adds a title to the graph. |
| `xlabel()` | Sets the label of the X-axis. |
| `ylabel()` | Sets the label of the Y-axis. |
| `xlim()` | Sets the limits of the X-axis. |
| `ylim()` | Sets the limits of the Y-axis. |
| `xticks()` | Sets the tick marks on the X-axis. |
| `yticks()` | Sets the tick marks on the Y-axis. |
| `show()` | Displays the graph. |
| `savefig()` | Saves the graph to a specified location. |
| `figure()` | Sets the size of the figure. |

### 1. Line Graph

**Definition:** A line graph represents continuous data using points connected by lines. It is useful for showing changes and trends over time.

**Example:** A student's marks in five consecutive tests.

| Test | Marks |
|---|---:|
| Test 1 | 25 |
| Test 2 | 34 |
| Test 3 | 49 |
| Test 4 | 40 |
| Test 5 | 48 |

**Real-Life Uses:**
- Monthly rainfall.
- Temperature changes.
- Stock market trends.
- Student performance over time.

**Python Function:** `plot()`

**Example Program:**

```python
import matplotlib.pyplot as plt

tests = ["Test 1", "Test 2", "Test 3", "Test 4", "Test 5"]
marks = [25, 34, 49, 40, 48]

plt.plot(tests, marks, marker="o")
plt.title("Student Performance")
plt.xlabel("Tests")
plt.ylabel("Marks")
plt.show()
```

**Important Attributes of `plot()`:**

| Attribute | Purpose |
|---|---|
| `linewidth` | Sets the width of the line. |
| `linestyle` | Sets the line style, such as solid or dashed. |
| `marker` | Sets the shape of the data point marker. |
| `markersize` | Sets the size of markers. |
| `markeredgecolor` | Sets the edge colour of markers. |

### 2. Bar Graph

**Definition:** A bar graph represents categorical data using rectangular bars. The height or length of each bar is proportional to its value.

It is mainly used to compare different categories.

**Example:** Number of students from different schools attending a seminar.

| School | Students |
|---|---:|
| Oxford Public School | 123 |
| Delhi Public School | 87 |
| Jyothis Central School | 105 |
| Sanskriti School | 146 |
| Bombay Public School | 34 |

**Real-Life Uses:**
- Comparing students' marks.
- Comparing sales of different products.
- Comparing population of different cities.

**Python Function:** `bar()`

**Example Program:**

```python
import matplotlib.pyplot as plt

schools = ["Oxford", "DPS", "Jyothis", "Sanskriti", "Bombay"]
students = [123, 87, 105, 146, 34]

plt.bar(schools, students)
plt.title("Students Attending Seminar")
plt.xlabel("Schools")
plt.ylabel("Number of Students")
plt.show()
```

**Important Attributes of `bar()`:**

| Attribute | Purpose |
|---|---|
| `color` | Sets the colour of the bars. |
| `edgecolor` | Sets the colour of the bar edges. |
| `width` | Sets the width of the bars. |

### 3. Histogram

**Definition:** A histogram is a graphical representation of the frequency distribution of numerical data. It uses vertical rectangles to show how many values fall within different intervals or ranges.

These intervals are also called **bins**.

**Example:** Heights of students can be grouped into intervals:

| Height Range (cm) | Number of Students |
|---|---:|
| 140–145 | 5 |
| 145–150 | 8 |
| 150–155 | 6 |

**Real-Life Uses:**
- Distribution of students' heights.
- Distribution of exam marks.
- Age distribution of people.

**Python Function:** `hist()`

**Example Program:**

```python
import matplotlib.pyplot as plt

heights = [141, 145, 142, 147, 144, 148, 141, 142, 149, 144]

plt.hist(heights, bins=5)
plt.title("Distribution of Heights")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.show()
```

### 4. Scatter Plot

**Definition:** A scatter plot represents the relationship between two numerical variables using individual data points plotted on the X-axis and Y-axis.

It helps identify positive, negative or no correlation between variables.

**Example:** Relationship between the number of hours students study and their mathematics marks.

- X-axis: Study hours (independent variable).
- Y-axis: Mathematics marks (dependent variable).

**Real-Life Uses:**
- Study hours and exam marks.
- Height and weight.
- Advertising expenses and sales.

**Python Function:** `scatter()`

**Example Program:**

```python
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5]
marks = [35, 45, 55, 70, 85]

plt.scatter(study_hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
```

### 5. Pie Chart

**Definition:** A pie chart is a circular graph divided into different sections or slices. Each slice represents a proportion or percentage of the total data.

**Example:** Periods allotted to different subjects in a week.

| Subject | Periods |
|---|---:|
| English | 6 |
| Maths | 8 |
| Science | 8 |
| Social Science | 7 |
| AI | 3 |
| PE | 2 |

**Real-Life Uses:**
- Monthly household expenses.
- Time spent on different subjects.
- Percentage of sales of different products.

**Python Function:** `pie()`

**Example Program:**

```python
import matplotlib.pyplot as plt

subjects = ["English", "Maths", "Science", "Social Science", "AI", "PE"]
periods = [6, 8, 8, 7, 3, 2]

plt.pie(periods, labels=subjects, autopct="%1.1f%%")
plt.title("Periods Allotted to Subjects")
plt.show()
```

**Important Points About Pie Charts:**
- Shows parts of a whole.
- Best used for a small number of categories.
- The textbook recommends limiting categories to seven for clarity.
- Zero values cannot be shown.
- Not suitable for showing changes over time.

### Difference Between Different Graphs

| Graph | Main Purpose | Example |
|---|---|---|
| Line Graph | Shows changes and trends over time. | Monthly temperature. |
| Bar Graph | Compares different categories. | Students in different schools. |
| Histogram | Shows frequency distribution of numerical data. | Students' heights. |
| Scatter Plot | Shows the relationship between two numerical variables. | Study hours and marks. |
| Pie Chart | Shows parts of a whole. | Monthly expenses. |

---

## 6. Introduction to Matrices

### What is a Matrix?

**Definition:** A matrix is a rectangular arrangement of numbers arranged in rows and columns.

The plural of matrix is **matrices**.

Matrices are widely used in mathematics and Artificial Intelligence, especially in computer vision and image processing.

**Example:**

A shop records the number of pencils and erasers purchased by three students.

| Student | Pencils | Erasers |
|---|---:|---:|
| Aditi | 25 | 5 |
| Adit | 10 | 2 |
| Manu | 5 | 1 |

This information can be represented as a matrix:

```text
      [25  5]
A =   [10  2]
      [ 5  1]
```

This matrix has 3 rows and 2 columns.

### Order of a Matrix

**Definition:** The order of a matrix is represented by the number of rows multiplied by the number of columns.

Order = m × n

Where:
- m = Number of rows.
- n = Number of columns.

**Example:**

```text
A = [ 2  4 ]
    [ 5  6 ]
    [ 7  8 ]
```

Number of rows = 3

Number of columns = 2

Order = **3 × 2**

Total number of elements = 3 × 2 = **6**

### Elements of a Matrix

Each element in a matrix is represented by `aij`.

Where:
- `i` represents the row number.
- `j` represents the column number.

Example:

```text
A = [ 5  8 ]
    [ 2  9 ]
```

- a11 = 5
- a12 = 8
- a21 = 2
- a22 = 9

### Operations on Matrices

#### 1. Addition of Matrices

**Definition:** Matrix addition is performed by adding the corresponding elements of two matrices.

**Condition:** Both matrices must have the same order.

**Example:**

```text
A = [3   2]       B = [6   3]
    [4  -1]           [5   9]

A + B = [3+6   2+3]
        [4+5  -1+9]

      = [9   5]
        [9   8]
```

#### 2. Subtraction of Matrices

**Definition:** Matrix subtraction is performed by subtracting the corresponding elements of one matrix from another.

**Condition:** Both matrices must have the same order.

**Example:**

```text
A = [5  8]       B = [2  3]
    [7  6]           [1  4]

A - B = [5-2  8-3]
        [7-1  6-4]

      = [3  5]
        [6  2]
```

#### 3. Transpose of a Matrix

**Definition:** Transpose of a matrix is obtained by interchanging its rows and columns.

It is represented by Aᵀ or A'.

**Example:**

```text
A = [8  7]
    [2  5]
    [4  6]

Aᵀ = [8  2  4]
     [7  5  6]
```

Original order = 3 × 2

Transpose order = 2 × 3

### Applications of Matrices in AI

1. **Image Processing:** Digital images are represented using matrices. Each pixel has a numerical value representing its intensity.

   - In a grayscale image, pixel values range from 0 to 255.
   - Values closer to 0 represent darker shades.
   - Values closer to 255 represent lighter shades.

2. **Recommendation Systems:** Matrices help represent relationships between users and the products they purchase or view.

3. **Natural Language Processing (NLP):** Vectors represent the distribution of words in documents. A vector is a one-dimensional matrix.

---

## 7. Data Preprocessing

### What is Data Preprocessing?

**Definition:** Data preprocessing is the process of cleaning and preparing raw data so that it becomes suitable for machine learning models.

It helps improve the quality and usefulness of data before it is given to an AI model.

### Steps of Data Preprocessing

The textbook discusses the following processes:

### 1. Data Cleaning

Data cleaning means identifying and correcting errors or problems in a dataset.

It includes:

**a. Missing Data**

Missing data occurs when some values are absent from a dataset.

Ways to handle missing data:
- Delete rows or columns containing missing values.
- Replace missing values with estimated values.
- Use algorithms that can handle missing data.

Example:

| Name | Marks |
|---|---:|
| Aditi | 85 |
| Rahul | Missing |
| Aman | 90 |

Rahul's missing marks need to be handled before analysis.

**b. Outliers**

Outliers are data points that are significantly different from the other values in a dataset.

Example:

Marks = 70, 72, 75, 74, 98, 10

If most marks are around 70–75, the value 10 may be an outlier that needs investigation.

Ways to handle outliers:
- Identify and remove them when appropriate.
- Transform the data.
- Use statistical methods that reduce their impact.

**c. Inconsistent Data**

Inconsistent data contains errors such as spelling mistakes, different formats or incorrect data types.

Example:

- "Delhi"
- "delhi"
- "DELHI"

These values may need to be standardized.

**d. Duplicate Data**

Duplicate data means the same record appears more than once.

Example: The same student's record is entered twice.

Duplicate records should be identified and removed to maintain data accuracy.

### 2. Data Transformation

**Definition:** Data transformation is the process of converting data into a suitable format for analysis or machine learning.

It includes:
- Converting categorical variables into numerical variables.
- Identifying new features.
- Modifying existing features when required.

Example:

```text
Yes → 1
No  → 0
```

### 3. Data Reduction

**Definition:** Data reduction means reducing the size or number of features in a dataset while retaining useful information.

It includes:
- Reducing the number of features.
- Applying sampling techniques when the dataset is too large.

Example: Removing unnecessary columns from a student dataset.

### 4. Data Integration and Normalization

**Data Integration:** Combining data from different sources or formats into one dataset.

Example: Combining student attendance data and marks data.

**Data Normalization:** Adjusting the scale of data features so that they have a similar scale and distribution.

Example: Converting different numerical features into a common scale.

### 5. Feature Selection

**Definition:** Feature selection is the process of selecting the most relevant features that contribute to predicting the target variable and removing irrelevant features.

Example:

To predict students' marks, useful features may include:
- Study hours.
- Attendance.
- Previous marks.

An unrelated feature, such as favourite colour, may be removed.

### Summary of Data Preprocessing

| Process | Meaning | Example |
|---|---|---|
| Data Cleaning | Correcting errors in data. | Handling missing marks. |
| Data Transformation | Converting data into a suitable format. | Yes/No into 1/0. |
| Data Reduction | Reducing unnecessary data or features. | Removing irrelevant columns. |
| Data Integration | Combining data from multiple sources. | Combining attendance and marks. |
| Normalization | Bringing features to a similar scale. | Scaling marks and age. |
| Feature Selection | Selecting important features. | Keeping study hours to predict marks. |

---

## 8. Data in Modelling and Evaluation

After data preprocessing, the dataset is used to build and evaluate a machine learning model.

### Training Dataset

**Definition:** A training dataset is the portion of data used to train a machine learning model.

The model learns patterns and relationships from this data.

### Testing Dataset

**Definition:** A testing dataset is the portion of data used to evaluate the performance of a trained machine learning model.

It checks how well the model works on data it has not used during training.

### Difference Between Training and Testing Data

| Training Dataset | Testing Dataset |
|---|---|
| Used to train the model. | Used to evaluate the model. |
| Helps the model learn patterns. | Checks how well the model performs. |
| Used during the learning process. | Used after training for evaluation. |

### Steps in Modelling and Evaluation

1. Collect the data.
2. Preprocess and clean the data.
3. Divide the dataset into training and testing sets.
4. Select an appropriate machine learning algorithm.
5. Train the model using training data.
6. Evaluate the model using testing data.
7. Analyse errors and improve the model if required.

### Machine Learning Algorithms

The algorithm is selected based on the nature of the problem.

Examples:
- Classification.
- Regression.
- Clustering.

### Model Evaluation Techniques

**1. Train-Test Split**

The dataset is divided into training and testing parts. The training data is used to train the model, and testing data is used to evaluate it.

**2. Cross-Validation**

Cross-validation checks whether the model performs consistently across different subsets of the dataset.

**3. Error Analysis**

Error analysis helps identify the mistakes made by a model and understand where improvements are required.

### Evaluation Metrics

Different evaluation techniques are used depending on the type of machine learning problem.

**For Classification Problems:**
- Accuracy
- Precision
- Recall
- F1-score
- ROC Curve

**For Regression Problems:**
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R-squared

---

## Quick Revision

| Term | Meaning |
|---|---|
| Data | Facts or information about an entity. |
| Data Literacy | Ability to find and use data effectively. |
| Data Collection | Gathering data from different sources. |
| Primary Data | Data collected directly for a specific purpose. |
| Secondary Data | Already collected data available for reuse. |
| Web Scraping | Extracting information from websites using automated tools. |
| Data Exploration | Understanding and examining a dataset. |
| Nominal | Categories without order. |
| Ordinal | Ordered categories without measurable differences. |
| Interval | Ordered data with measurable differences but no true zero. |
| Ratio | Data with measurable differences and a true zero. |
| Mean | Average of values. |
| Median | Middle value. |
| Mode | Most frequently occurring value. |
| Variance | Measure of spread around the mean. |
| Standard Deviation | Square root of variance. |
| Data Visualization | Graphical representation of data. |
| Matrix | Rectangular arrangement of numbers in rows and columns. |
| Transpose | Interchanging rows and columns. |
| Data Preprocessing | Cleaning and preparing data for machine learning. |
| Outlier | A value significantly different from other values. |
| Feature Selection | Selecting relevant features for a model. |
| Training Data | Data used to train a model. |
| Testing Data | Data used to evaluate a trained model. |
| Cross-Validation | Evaluating model consistency across different subsets. |

## Important Points to Remember

1. AI is data-driven.
2. Data literacy includes collecting, organizing, analysing and using data ethically.
3. The two main data collection sources are Primary and Secondary.
4. The four levels of measurement are Nominal, Ordinal, Interval and Ratio.
5. Mean, Median and Mode are measures of central tendency.
6. Variance and Standard Deviation measure the spread of data.
7. Matplotlib is a Python library used for data visualization.
8. `plot()` is used for line graphs.
9. `bar()` is used for bar graphs.
10. `hist()` is used for histograms.
11. `scatter()` is used for scatter plots.
12. `pie()` is used for pie charts.
13. A matrix is an arrangement of numbers in rows and columns.
14. Matrix addition and subtraction require matrices of the same order.
15. Transpose interchanges rows and columns.
16. Data preprocessing prepares raw data for machine learning.
17. Training data trains the model, while testing data evaluates it.
18. Cross-validation checks model performance across different subsets.

---

**End of Unit 5: Data Literacy – Data Collection to Data Analysis**
