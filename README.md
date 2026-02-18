# Marketing campaign data analysis, Affinity-Card-Prediction, Predictive Application and User Interfac

The data set contains 1500 customer records. Each record consists of 19 variables, which includes socio-demographic and product ownership information. Variable 11, AFFINITY_CARD (1 = High-value, 0 = Low-value), is the target variable.
All datasets are in CSV format with the following attributes:
1.	CUST_ID
2.	CUST_GENDER
3.	AGE
4.	CUST_MARITAL_STATUS
5.	COUNTRY_NAME
6.	CUST_INCOME_LEVEL
7.	EDUCATION
8.	OCCUPATION
9.	HOUSEHOLD_SIZE
10.	YRS_RESIDENCE
11.	AFFINITY_CARD
12.	BULK_PACK_DISKETTES
13.	FLAT_PANEL_MONITOR
14.	HOME_THEATER_PACKAGE
15.	BOOKKEEPING_APPLICATION
16.	PRINTER_SUPPLIES
17.	Y_BOX_GAMES
18.	OS_DOC_SET_KANJI
19.	COMMENTS


________________________________________



Requirements Specifications
## 1. Data Understanding
1.1. Produce a metadata table to show the characteristics of each attribute.
The metadata table should contain attribute name, description, maximum, minimum, mean, standard deviation, and histogram for numeric data, and mode and bar chart for nominal data.
1.2. Describe missing or error data with suggested handling methods for each attribute. Do not clean them at this stage.
Missing data should include all types such as null, blank, unknown, etc.
Errors should include any invalid or mismatching data.
________________________________________
## 2. Data Preparation
2.1. Write Python programs to remove variables with no inference to the target, with justifications, and keep comments for further processing.
2.2. Write Python programs to clean data and provide justifications.
2.3. Write Python programs to convert variables as per the following requirements. Provide screenshots of Python code with comments, as well as data before and after conversion.
2.4. Convert CUST_GENDER into binary (F = 0, M = 1).
2.5. Convert COUNTRY_NAME into ordinal numbers based on their frequency of occurrence in descending order.
2.6. Convert CUST_INCOME_LEVEL into three ordinal levels:
                •	1 = Low income
                •	2 = Middle income
                •	3 = High income
2.7. Convert EDUCATION into ordinal numbers based on USA education levels in ascending order.
2.8. Convert OCCUPATION into a series of binary columns using one-hot encoding.
________________________________________
## 3. Data Analysis
a) Convert variables (except comments) not included in the data preparation stage into numerical or binary format and write a Python program to show the correlation of all variables with the target.
b) Write a Python program to analyze comment sentiment and create a sentiment column with values:
•	1 = Positive
•	0 = Neutral
•	-1 = Negative
________________________________________
## 4. Data Exploration
Write a Python program that displays a histogram of one processed variable, allowing the user to select any variable at runtime. The program should continue running until the user chooses to exit.
________________________________________
## 5. Data Mining
•	Keep the first 100 customer records from the processed campaign data for testing and use the remaining records to build a logistic regression model using the top 10 relevant independent variables. Identify the intercept and coefficients for each independent variable.
•	Test the accuracy of the model using the first 100 customer records and explain the results with appropriate graphs.
•	Implement a predictive application based on the logistic regression model. The application should include a suitable user interface that allows users to input customer records via keyboard or file upload and receive predicted outputs.

<div align="center">
  
**[⬆ Back to Top](#top)**

</div>

