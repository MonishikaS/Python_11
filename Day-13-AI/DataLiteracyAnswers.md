# Unit 5: Data Literacy – Data Collection to Data Analysis
## Exercise Questions with Answers

---

# A. Multiple-Choice Questions (MCQs)

### 1. Which of the following best defines data literacy?

- A) The ability to read and write data
- B) The ability to find and use data effectively
- C) The ability to analyse data using AI
- D) The ability to collect and store data securely

**Answer: B) The ability to find and use data effectively**

**Explanation:** Data literacy means the ability to understand, interpret, analyse, and use data effectively.

### 2. What is the purpose of data preprocessing?

- A) To make data more complex
- B) To make data less accessible
- C) To clean and prepare data for analysis
- D) To increase the size of the dataset

**Answer: C) To clean and prepare data for analysis**

**Explanation:** Data preprocessing removes errors, handles missing values, and prepares data for analysis or machine learning.

### 3. How can missing data be handled in a dataset?

- A) By ignoring it
- B) By replacing missing values with estimates
- C) By deleting rows or columns with missing values
- D) By converting missing values into text

**Answer: B and C) By replacing missing values with estimates or deleting rows or columns**

**Explanation:** Missing data can be handled by filling it with suitable values (such as the mean or median) or by removing rows or columns when appropriate.

### 4. Which statement about the quantity of data needed for machine learning projects is true?

- A) More data is always better for good predictions.
- B) Small batches of data are sufficient for complex models.
- C) Data quantity depends solely on the number of features.
- D) Data diversity is not essential for model performance.

**Answer: A is the closest option, but it is not completely correct.**

**Correct concept:** The amount of data required depends on the problem and model. Sufficient, relevant, and diverse data generally helps improve model performance. More data is not automatically better if it is poor quality or biased.

### 5. Which of the following is an example of a primary source of data collection?

- A) Web scraping
- B) Social media data tracking
- C) Surveys
- D) Kaggle datasets

**Answer: C) Surveys**

**Explanation:** Surveys collect information directly from people, making them a primary source of data.

### 6. What method of data collection involves direct communication with individuals or groups to gather information?

- A) Observations
- B) Experiments
- C) Interviews
- D) Marketing campaigns

**Answer: C) Interviews**

**Explanation:** Interviews involve asking questions directly to individuals to collect information.

### 7. Which of the following is an example of ratio scale data?

- A) Grading students' exam papers as A, B, C, D, and F
- B) Measuring temperature in Celsius
- C) Rating a meal as unpalatable, unappetizing, just okay, tasty, and delicious
- D) Recording the weight of a person in kilograms

**Answer: D) Recording the weight of a person in kilograms**

**Explanation:** Weight has a true zero point. A person weighing 60 kg is twice as heavy as someone weighing 30 kg.

### 8. What is the distinguishing feature of ratio scale data?

- A) It involves categories without a specific order.
- B) It has a zero point and allows for ratios to be calculated.
- C) It involves categories with a strict order but no measurable differences.
- D) It has a definite order, but the differences between categories cannot be measured.

**Answer: B) It has a zero point and allows for ratios to be calculated.**

**Explanation:** Ratio data has equal intervals and a true zero, which makes multiplication and division meaningful.

### 9. Which statistical measure is most suitable for datasets with evenly spread values and no exceptionally high or low values?

- A) Mean
- B) Median
- C) Mode
- D) Variance

**Answer: A) Mean**

**Explanation:** Mean is suitable when values are fairly evenly distributed and there are no extreme values.

### 10. What is the term used to describe the graphical or pictorial representation of data?

- A) Statistical summary
- B) Data organization
- C) Data visualization
- D) Data interpretation

**Answer: C) Data visualization**

**Explanation:** Data visualization represents information using graphs, charts, and diagrams.

---

# B. Short Answer Questions

### 1. Explain the concept of data literacy and its importance in today's digital age.

**Answer:**

Data literacy is the ability to read, understand, interpret, analyse, and use data effectively.

**Importance:**
1. Helps in making better decisions.
2. Helps identify patterns and trends.
3. Improves problem-solving skills.
4. Helps understand information presented through charts and graphs.
5. Supports the development of AI and machine learning systems.

**Example:** A school can analyse students' marks to identify subjects in which students need extra support.

### 2. What is data preprocessing?

**Answer:**

Data preprocessing is the process of cleaning and transforming raw data into a suitable format before analysing it or using it in machine learning.

It includes:
- Removing duplicate records.
- Handling missing values.
- Correcting errors.
- Removing or treating outliers.
- Converting data into a suitable format.

**Example:** If a student's age is missing in a dataset, we can fill it using an appropriate estimated value.

### 3. What is data visualization and why is it important?

**Answer:**

Data visualization is the graphical representation of data using charts, graphs, and diagrams.

**Importance:**
1. Makes complex data easier to understand.
2. Helps identify patterns and trends.
3. Makes comparisons easier.
4. Helps in decision-making.
5. Presents information clearly.

**Example:** A bar graph can compare the marks obtained by students in different subjects.

### 4. How does a line graph differ from a bar graph?

**Answer:**

| Line Graph | Bar Graph |
|---|---|
| Uses points connected by lines. | Uses rectangular bars. |
| Shows changes and trends over time. | Compares different categories. |
| Useful for continuous data. | Useful for categorical data. |
| Example: Temperature changes over a week. | Example: Books sold in different genres. |

### 5. When would you use a scatter plot?

**Answer:**

A scatter plot is used to show the relationship or correlation between two numerical variables.

It helps identify whether two variables are positively related, negatively related, or have no clear relationship.

**Example:** A scatter plot can show the relationship between students' study hours and examination marks.

### 6. What is data?

**Answer:**

Data is a collection of raw facts, figures, observations, or information that can be processed to obtain meaningful results.

**Examples:**
- Students' marks.
- People's ages.
- Daily temperatures.
- Product prices.

### 7. What do you mean by web scraping?

**Answer:**

Web scraping is the process of automatically collecting information from websites using software or computer programs.

**Example:** Collecting product names and prices from an online shopping website for price comparison.

### 8. If a matrix has 6 elements, what are the possible orders it can have?

**Answer:**

The order of a matrix is represented by:

**Number of rows × Number of columns**

Since the total number of elements is 6:

Possible orders are:

1. 1 × 6
2. 2 × 3
3. 3 × 2
4. 6 × 1

Therefore, a matrix containing 6 elements can have **four possible orders**.

### 9. Construct a 3 × 2 matrix where each element is given by aᵢⱼ = i × j.

**Answer:**

Given:

- Number of rows = 3
- Number of columns = 2
- Formula: aᵢⱼ = i × j

Calculate each element:

| Element | Calculation | Value |
|---|---|---|
| a₁₁ | 1 × 1 | 1 |
| a₁₂ | 1 × 2 | 2 |
| a₂₁ | 2 × 1 | 2 |
| a₂₂ | 2 × 2 | 4 |
| a₃₁ | 3 × 1 | 3 |
| a₃₂ | 3 × 2 | 6 |

Therefore, the required matrix is:

\[
A =
\begin{bmatrix}
1 & 2\\
2 & 4\\
3 & 6
\end{bmatrix}
\]

### 10. Find the transpose of the matrix B.

Given:

\[
B =
\begin{bmatrix}
5 & -1 & 4\\
2 & 3 & 6
\end{bmatrix}
\]

**Answer:**

The transpose of a matrix is obtained by changing its rows into columns and columns into rows.

Therefore:

\[
B^T =
\begin{bmatrix}
5 & 2\\
-1 & 3\\
4 & 6
\end{bmatrix}
\]

The original matrix is of order 2 × 3, and its transpose is of order 3 × 2.

---

# C. Long Answer Questions

### 1. Discuss the advantages and limitations of using a pie chart in data visualization. Provide examples.

**Answer:**

A pie chart is a circular graph divided into slices. Each slice represents a category's proportion or percentage of the total data.

**Example:** A city's transportation usage:

- Car: 40%
- Public Transit: 30%
- Walking: 20%
- Bicycle: 10%

**Advantages of Pie Charts:**

1. **Easy to understand:** Information is presented visually.
2. **Shows proportions:** Clearly displays the percentage of each category.
3. **Easy comparison:** Helps compare the contribution of different categories.
4. **Attractive presentation:** Makes reports and presentations more engaging.

**Limitations of Pie Charts:**

1. **Too many categories:** Becomes difficult to read when there are many slices.
2. **Similar values:** Small differences between categories are difficult to identify.
3. **Not suitable for trends:** Cannot effectively show changes over time.
4. **Requires a meaningful total:** Categories should represent parts of the same whole.

**Example:** A pie chart is suitable for showing the percentage of students using different modes of transportation to reach school.

### 2. Explain the terms mean, median and mode.

**Answer:**

Mean, median, and mode are the three commonly used measures of central tendency. They help us understand the centre or typical value of a dataset.

**1. Mean**

Mean is the average of all the values in a dataset.

Formula:

Mean = Sum of all observations / Total number of observations

**Example:**

Data: 10, 20, 30, 40, 50

Mean = (10 + 20 + 30 + 40 + 50) / 5

Mean = 150 / 5 = **30**

**2. Median**

Median is the middle value when the data is arranged in ascending or descending order.

**Example 1 (Odd number of values):**

Data: 10, 20, 30, 40, 50

Median = **30**

**Example 2 (Even number of values):**

Data: 10, 20, 30, 40

Median = (20 + 30) / 2

Median = **25**

**3. Mode**

Mode is the value that occurs most frequently in a dataset.

**Example:**

Data: 10, 20, 20, 30, 40

Mode = **20**

**Difference between Mean, Median and Mode:**

| Mean | Median | Mode |
|---|---|---|
| Average of values. | Middle value. | Most frequently occurring value. |
| Uses all observations. | Depends on the middle position. | Depends on frequency. |
| Affected by extreme values. | Less affected by extreme values. | Useful for finding the most common value. |

### 3. Explain the four levels of measurement.

**Answer:**

Levels of measurement describe how data is classified and measured. There are four main levels:

**1. Nominal Scale**

- Used to classify data into categories.
- There is no particular order among categories.
- Example: Gender categories, blood groups, or colours.

**2. Ordinal Scale**

- Data is divided into categories that have a meaningful order.
- The exact difference between categories cannot be measured.
- Example: Customer satisfaction ratings such as Poor, Average, Good, and Excellent.

**3. Interval Scale**

- Data has a definite order.
- Differences between values are equal and meaningful.
- It does not have a true zero point.
- Example: Temperature measured in Celsius.

**4. Ratio Scale**

- Has all the properties of an interval scale.
- Contains a true zero point.
- Ratios can be calculated.
- Example: Height, weight, age, and distance.

**Difference between the Four Levels:**

| Level | Order | Equal Intervals | True Zero | Example |
|---|---|---|---|---|
| Nominal | No | No | No | Blood group |
| Ordinal | Yes | No | No | Satisfaction rating |
| Interval | Yes | Yes | No | Temperature in Celsius |
| Ratio | Yes | Yes | Yes | Weight in kg |

### 4. Given the matrices A and B, calculate A + B and B – A.

**Answer:**

The numerical values of matrices A and B are not included in the provided question.

**Rules to remember:**

**Matrix Addition (A + B):**

Add the corresponding elements of both matrices.

If:

\[
A =
\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix}
,\quad
B =
\begin{bmatrix}
5 & 6\\
7 & 8
\end{bmatrix}
\]

Then:

\[
A+B =
\begin{bmatrix}
1+5 & 2+6\\
3+7 & 4+8
\end{bmatrix}
=
\begin{bmatrix}
6 & 8\\
10 & 12
\end{bmatrix}
\]

**Matrix Subtraction (B – A):**

Subtract the corresponding elements of A from B.

\[
B-A =
\begin{bmatrix}
5-1 & 6-2\\
7-3 & 8-4
\end{bmatrix}
=
\begin{bmatrix}
4 & 4\\
4 & 4
\end{bmatrix}
\]

**Important:** Two matrices can be added or subtracted only when they have the same order.

---

# D. Python Programs

## 1. Calculate Mean, Median and Mode

**Question:**

The ages of a group of people are:

25, 28, 30, 35, 40, 45, 50, 55, 60, 65.

Write a Python program to calculate the mean, median, and mode.

**Program:**

```python
import statistics

# List of ages
ages = [25, 28, 30, 35, 40, 45, 50, 55, 60, 65]

# Calculate mean
mean = statistics.mean(ages)

# Calculate median
median = statistics.median(ages)

# Calculate mode
modes = statistics.multimode(ages)

# Display results
print("Mean:", mean)
print("Median:", median)

# Check whether a mode exists
if len(modes) == len(ages):
    print("Mode: No mode (all values occur once)")
else:
    print("Mode:", modes)
```

**Output:**

```text
Mean: 43.3
Median: 42.5
Mode: No mode (all values occur once)
```

**Explanation:**

- `statistics.mean()` calculates the average.
- `statistics.median()` finds the middle value.
- `statistics.multimode()` returns all values having the highest frequency.
- Since every age occurs only once, there is no unique mode.

## 2. Calculate Variance and Standard Deviation

**Question:**

A company recorded daily temperatures:

20°C, 22°C, 25°C, 18°C, and 23°C.

Determine the variance and standard deviation.

**Program:**

```python
import statistics

# List of temperatures
temperatures = [20, 22, 25, 18, 23]

# Calculate population variance
variance = statistics.pvariance(temperatures)

# Calculate population standard deviation
std_dev = statistics.pstdev(temperatures)

# Display results
print("Variance:", variance)
print("Standard Deviation:", round(std_dev, 2))
```

**Output:**

```text
Variance: 5.84
Standard Deviation: 2.42
```

**Explanation:**

- Variance measures how far the values are spread from the mean.
- Standard deviation measures the typical spread of values around the mean.
- `statistics.pvariance()` calculates population variance.
- `statistics.pstdev()` calculates population standard deviation.

**Note:** This solution treats the five recorded days as the complete population.

## 3. Plot a Line Chart

**Question:**

Plot a line chart representing weekly customer inquiries:

- Week 1: 150
- Week 2: 170
- Week 3: 180
- Week 4: 200

**Program:**

```python
import matplotlib.pyplot as plt

# Data
weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]
inquiries = [150, 170, 180, 200]

# Create line chart
plt.plot(weeks, inquiries, marker='o')

# Add labels and title
plt.xlabel("Weeks")
plt.ylabel("Number of Inquiries")
plt.title("Weekly Customer Inquiries")

# Display grid
plt.grid(True)

# Display chart
plt.show()
```

**Explanation:**

- `plt.plot()` creates a line graph.
- `marker='o'` displays circular markers at each data point.
- `xlabel()` gives a label to the X-axis.
- `ylabel()` gives a label to the Y-axis.
- `title()` adds a title.
- `show()` displays the graph.

## 4. Plot a Bar Chart

**Question:**

Plot a bar chart representing books sold by different genres:

- Fiction: 120
- Mystery: 90
- Science Fiction: 80
- Romance: 110
- Biography: 70

**Program:**

```python
import matplotlib.pyplot as plt

# Data
genres = ["Fiction", "Mystery", "Science Fiction",
          "Romance", "Biography"]

books_sold = [120, 90, 80, 110, 70]

# Create bar chart
plt.bar(genres, books_sold)

# Add labels and title
plt.xlabel("Book Genres")
plt.ylabel("Number of Books Sold")
plt.title("Books Sold by Genre")

# Display chart
plt.show()
```

**Explanation:**

- `plt.bar()` creates a bar chart.
- `xlabel()` labels the X-axis.
- `ylabel()` labels the Y-axis.
- `title()` adds a heading to the chart.
- `show()` displays the chart.

## 5. Visualize Transportation Data Using a Pie Chart

**Question:**

Represent the different types of transportation used by commuters:

- Car: 40%
- Public Transit: 30%
- Walking: 20%
- Bicycle: 10%

**Program:**

```python
import matplotlib.pyplot as plt

# Data
transport = ["Car", "Public Transit", "Walking", "Bicycle"]
percentage = [40, 30, 20, 10]

# Create pie chart
plt.pie(percentage, labels=transport, autopct='%1.1f%%')

# Add title
plt.title("Transportation Used by Commuters")

# Display chart
plt.show()
```

**Explanation:**

- `plt.pie()` creates a pie chart.
- `labels` displays the names of categories.
- `autopct='%1.1f%%'` displays percentages with one decimal place.
- `title()` adds a title.
- `show()` displays the pie chart.

---

# Quick Revision

| Concept | Meaning |
|---|---|
| Data Literacy | Ability to understand and use data effectively. |
| Data Preprocessing | Cleaning and preparing data. |
| Data Visualization | Graphical representation of data. |
| Web Scraping | Automatically collecting information from websites. |
| Mean | Average of all values. |
| Median | Middle value of arranged data. |
| Mode | Most frequently occurring value. |
| Variance | Measure of data spread. |
| Standard Deviation | Measure of spread around the mean. |
| Matrix | Rectangular arrangement of elements in rows and columns. |
| Transpose | Interchanging rows and columns. |
| Pie Chart | Shows proportions of a whole. |
| Bar Chart | Compares categories. |
| Line Graph | Shows changes or trends. |
| Scatter Plot | Shows the relationship between two numerical variables. |

**End of Unit 5 Exercise Answers**
