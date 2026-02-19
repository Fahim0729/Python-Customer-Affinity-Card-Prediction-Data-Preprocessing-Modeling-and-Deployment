# 🎯 Marketing Campaign Data Analysis: Affinity-Card Prediction, Predictive Application, and User Interface

The dataset contains **1,500 customer records**, each consisting of **19 variables**, including socio-demographic and product ownership information. The target variable is:

- **🎯 AFFINITY_CARD (Variable 11):**  
  - `1 = High-value`  
  - `0 = Low-value`

The dataset is in **CSV format** with the following attributes:

1. 🆔 CUST_ID  
2. 👤 CUST_GENDER  
3. 📅 AGE  
4. 💍 CUST_MARITAL_STATUS  
5. 🌎 COUNTRY_NAME  
6. 💵 CUST_INCOME_LEVEL  
7. 🎓 EDUCATION  
8. 💼 OCCUPATION  
9. 🏠 HOUSEHOLD_SIZE  
10. 🏘️ YRS_RESIDENCE  
11. 🎯 AFFINITY_CARD  
12. 💽 BULK_PACK_DISKETTES  
13. 🖥️ FLAT_PANEL_MONITOR  
14. 🎬 HOME_THEATER_PACKAGE  
15. 📒 BOOKKEEPING_APPLICATION  
16. 🖨️ PRINTER_SUPPLIES  
17. 🎮 Y_BOX_GAMES  
18. 📚 OS_DOC_SET_KANJI  
19. 📝 COMMENTS  

---

## 📝 Requirement Specifications

### 1. Data Understanding

**1.1 🗂 Metadata Table**  
- Produce a table showing characteristics of each attribute.  
- Include for **numeric attributes**: max, min, mean, standard deviation, histogram.  
- Include for **nominal attributes**: mode and bar chart.  

🟩 The metadata table has been created according to the specified requirements, summarizing the characteristics of each attribute. For numeric attributes, the table includes maximum, minimum, mean, standard deviation, and corresponding histograms 📊 to visualize their distributions. For nominal attributes, the table presents the mode along with bar charts 📊 to illustrate category frequencies.

A portion of the metadata table, showing a few representative attributes, is presented below:

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/07c313677ad06b692d3106042931947352b686e9/MetaData_Table.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: Summary of Attribute Characteristics with Statistics and Charts</em>
</p>


**1.2 ⚠️ Missing or Error Data Analysis**  
- Describe all missing values (null, blank, unknown, etc.)  
- Describe any **invalid or mismatching data**   
> ⚠️ Do **not clean the data** at this stage.

🟩 Missing values and erroneous data were identified in the HOUSEHOLD_SIZE, OCCUPATION, and COMMENTS columns. The figure presents these columns along with the counts of missing and erroneous entries. Additionally, the grand total of missing and erroneous values across these columns is calculated.

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/473e8b07eec2c8a08b2d9caf8e6e52dfc3627821/Error.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: Missing and Erroneous Values in Selected Columns</em>
</p>

### 2. Data Preparation

**2.1 🧹 Remove Irrelevant Variables**  
- Write Python programs to remove variables with no inference to the target.

🟩 The data has 19 columns where CUST-ID is the unique identification for each customer. Thus, CUST-ID has been removed as it is not useful for inferring target variable. 

**2.2 🧼 Data Cleaning**  
- Provide **justifications** for each cleaning step (Missing or Error Data).

🟩 The cleaning process for HOUSEHOLD_SIZE, OCCUPATION, and COMMENTS columns are descrived below:
- **HOUSEHOLD_SIZE**
Error values such as “9+”, “5-Apr”, and “8-Jun” were identified. The value “9+” is replaced with 9, while invalid entries like “5-Apr” and “8-Jun” are removed.
- **OCCUPATION**
Entries marked as “?” indicate missing occupation data and are removed. This ensures the column contains only valid categorical values, maintaining dataset quality for analysis.
- **COMMENTS**
Null or blank entries are replaced with “No Comment”, explicitly marking missing feedback as a valid category.


The proposed suggestions for handling missing values and error values are presented in the following table 
<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/473e8b07eec2c8a08b2d9caf8e6e52dfc3627821/Handling.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: Suggestions for handling missing and error values</em>
</p>

After cleaning, the dataset contains **1312** valid rows, with **188** rows removed due to errors or missing values.

**🔄 Variable Conversion**  
- Write Python programs for the following conversions:  

  - **2.3 👤 CUST_GENDER → binary:** F = 0, M = 1

    🟩  The CUST_GENDER column was converted into a binary variable using a **mapping** approach to simplify analysis: F → 0, M → 1
    
  - **2.4 🌎 COUNTRY_NAME → ordinal numbers** based on frequency (descending order)

    🟩  The COUNTRY_NAME column was converted into ordinal numbers based on frequency. Countries that appear more frequently were assigned lower ordinal numbers,           and less frequent countries were assigned higher numbers. This was done using a **mapping** approach with descending order of frequency                            **(ascending=False)**.
    
  - **2.5 💵 CUST_INCOME_LEVEL → ordinal levels:**  
    - 1 = Low income  
    - 2 = Middle income  
    - 3 = High income

    🟩 The CUST_INCOME_LEVEL column was converted into ordinal levels using a **mapping** approach:
          - 1 = Low Income → “Below 30,000” and “30,000–49,999”
          - 2 = Middle Income → “50,000–129,999”
          - 3 = High Income → “130,000 and above”
      This mapping reduces the number of categories while preserving the ordinal relationship of income, making the variable suitable for statistical and machine        learning analyses.
      
  - **2.6 🎓 EDUCATION → ordinal numbers** based on USA education levels (ascending order)

    🟩 The EDUCATION column was converted into ordinal numbers based on the U.S. education system using a **mapping** approach. Each educational level was assigned a          numeric value reflecting its order in the education hierarchy (**ascending** order), from preschool to PhD
    
  - **2.7 💼 OCCUPATION → one-hot encoding** (binary columns for each occupation)

    🟩 The OCCUPATION column was converted using one-hot encoding, creating binary columns for each occupation. This was implemented using **get_dummies**, which          transforms each categorical value into a separate column with 0/1 indicators.


### 3. Data Analysis

**3.1 📊 Correlation Analysis**  
- Write a Python program to show **correlation of all variables with the target**.

🟩 CORRELATION:  Correlation of independent variables with target variable is shown in the following figure. Based on the correlation values, the variable YRS_RESIDENCE has the highest correlation with the target variable AFFINITY_CARD, followed by EDUCATION and OCCUPATION.   

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/14776f5f8b9e75ccbcfdfd054fca0399a545c159/Corr_ALL.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: correlation of variables</em>
</p>

  
**3.2 📝 Sentiment Analysis**  
- Analyze the COMMENTS column using Python.  
- Create a new **Sentiment column** with values:  
  - 1 = Positive ✅  
  - 0 = Neutral ⚪  
  - -1 = Negative ❌
 
🟩 The COMMENTS column was analyzed for sentiment using the TextBlob package. A function classify_sentiment computes the polarity of each comment and classifies it as positive (1), neutral (0), or negative (-1). The results are stored in a new column, SENTIMENT.

The number of comments classified under the SENTIMENT column and the levels (-1, 0, +1) are shown in the following figure 

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/4a4340fa8026d1ab1fe1cd55886a2598e3724753/Senti.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: SENTIMENT and its count</em>
</p>

---

### 4. Data Exploration

- Write a Python program to **display a histogram** of any processed variable 📊.  
- The program should **allow runtime selection** of variables.  
- Continue running until the **user chooses to exit** 🔁.

🟩 A Python program will be developed to visualize the distribution of processed variables ('CUST_GENDER', 'CUST_MARITAL_STATUS', 'COUNTRY_NAME', 'CUST_INCOME_LEVEL', 'EDUCATION', 'OCCUPATION', and 'sentiment') using histograms. In this program, users are allowed to select any one variable at runtime, and its corresponding histogram will be displayed. The program is designed to run continuously in a loop until an explicit exit command is given by the user. This interactive functionality has been implemented to support exploratory data analysis (EDA), where the distribution, spread, and potential outliers of variables can be observed. Such visual analysis is considered essential for understanding the underlying structure of the data during preprocessing and model development stages. 
The user is presented with the interface shown in the following figure, where they can enter a variable name or exit the program.

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/3e62e8245f75e9389adab96786cfbfb02a2e2e3c/Hist_prog.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: user input interface</em>
</p>


### 5. Data Mining

**5.1 🏗 Model Building**  
- Keep the **first 100 customer records** as a test set.  
- Use the remaining records to **build a logistic regression model** using the **top 10 relevant independent variables**.  
- Identify the **intercept and coefficients** for each independent variable.

🟩 For this analysis, the first 100 customer records from the processed campaign dataset were set aside for testing, while the remaining data were used to build a logistic regression model. The correlation between each independent variable and the target was calculated, and the top 10 features were selected as predictors. After training, the model’s intercept and coefficients were obtained to assess the direction and magnitude of each feature’s influence.

The intercept value of -1.730 serves as the baseline. Among the top predictors, CUST_GENDER (1.035) has the strongest positive impact, followed by EDUCATION (0.645), OCCUPATION (0.469), YRS_RESIDENCE (0.468), and HOME_THEATER_PACKAGE (0.401). Most features positively influence the outcome, while OS_DOC_SET_KANJI (-0.203) shows a slight negative effect.

The next figure illustrates the intercept and coefficients of the top 10 features.

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/0fb70468b38feb38e7c94a95a23f8a8dd90a45c7/Intercept_Top10-CorrL.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: intercept and top 10 variable’s coefficien</em>
</p>


**5.2 🧪 Model Testing**  
- Test the model on the **first 100 records**.  
- Explain results with **appropriate graphs** 📈 and performance metrics.

🟩 The logistic regression model was evaluated using the first 100 customer records reserved for testing. Predictions were compared with actual outcomes, and performance was assessed using accuracy and a confusion matrix.

The model achieved 79% accuracy, correctly predicting 65 non-purchases (true negatives) and 14 purchases (true positives), while misclassifying 16 purchases (false negatives) and 5 non-purchases (false positives). Overall, the model demonstrates good predictive performance.

 The model’s accuracy and confusion matrix are shown in the next figure.
 
<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/a8a90c5f86988bf0ea9056647d2e273c523833a5/Performance_Mat.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: Model accuracy and Confusion Matrix of the logistic regression</em>
</p>



**5.3 💻 Predictive Application**  
- Implement an application using the **logistic regression model**.  
- Include a **user interface** to input customer records via **keyboard or file upload** ⌨️📁.  
- Output **predicted Affinity Card results** to the user 🎯.

🟩 A predictive application was developed based on the logistic regression model, featuring a user-friendly interface for real-time predictions of affinity card purchases (Figure-5.3.1). Users can enter customer data manually or upload a CSV file.

When entering data manually, the levels of the top 10 independent variables are displayed for selection. After selecting the input values and clicking the ‘Predict’ button, the predicted outcome is displaye (Figure-5.3.2). 
Alternatively, users can upload a CSV file, as illustrated in Figure-5.3.3.

The following figures illustrate the interfaces of the workflow:

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/ee6af59ff566c8d25c09f5f18cdb8bf2635a7176/Option.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure-5.3.1: User interface for importing data manually or uploading a CSV file</em>
</p>

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/ee6af59ff566c8d25c09f5f18cdb8bf2635a7176/Keyboard_input.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure-5.3.2: interface of Enter customer data manually </em>
</p>

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/ee6af59ff566c8d25c09f5f18cdb8bf2635a7176/File_Input.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure-5.3.3: interface for upload csv file</em>
</p>

**🛠 Key functions implemented**: _init_, show_model_summary, create_widgets, manual_entry, predict, display_prediction




### 📎 Deliverables

- Python scripts (.py or Jupyter Notebook) for:  
  - Data cleaning 🧼  
  - Conversion 🔄  
  - Correlation & Sentiment analysis 📊📝  
  - Histogram plotting 📊  
  - Logistic regression model & testing 🏗🧪  
  - Predictive application 💻
  - - Processed dataset with new **binary and ordinal variables**, **sentiment column**, and **logistic regression results** ✅


<div align="center">
  
**[⬆ Back to Top](#top)**

</div>

