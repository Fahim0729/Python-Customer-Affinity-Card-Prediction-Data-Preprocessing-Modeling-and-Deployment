# 🎯 Marketing Campaign Data Analysis: Affinity-Card Prediction, Predictive Application and User Interface

## 📋 Project Overview
This project demonstrates an **end-to-end data analytics workflow** focused on predictive modeling and business insights. It combines **feature engineering, sentiment analysis, and logistic regression** to identify key drivers of customer behavior. A **user-friendly application** was developed to provide real-time predictions, showcasing practical skills in Python, data visualization, and applied machine learning.

<div align="center">

## 🛠 Key Libraries & Skills

**Data Manipulation & Analysis:** `pandas`, `numpy` — Data cleaning and transformation  

**Data Visualization:** `matplotlib`, `seaborn` — visualization  

**Machine Learning:** `scikit-learn` (`LogisticRegression`, `train_test_split`, `StandardScaler`, `accuracy_score`, `confusion_matrix`) — Model building, evaluation, and prediction  

**Natural Language Processing:** `TextBlob` — Sentiment analysis  

**Interactive Applications:** `ipywidgets`, `IPython.display` — User interface for the interactive prediction application  

**File Handling:** Core Python modules (`io`, `base64`) — Uploading and processing

</div>

---

## 📊 Dataset Overview

<div align="center">

| **Observation**                 | **Details** |
|:--------------------------------:|:-----------:|
| Total Records                   | 1,500       |
| Total Variables                 | 19          |
| Target Variable Name            | AFFINITY_CARD |
| Target Variable Categories      | 0 = Low-value, 1 = High-value |
| Missing Values Present?         | Yes (HOUSEHOLD_SIZE, OCCUPATION, COMMENTS), Variable Types: Numeric, Categorical |

</div>

---

## 📝 Project Insights & Explanation

### 1. Data Understanding

**1.1 🗂 Metadata Table**  
🟩 The [metadata table](https://github.com/Fahim-Hossain-Data/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/9e7fdd72f4de9e8744f3ebf71edc78e3f616bfe6/2.%20Meta_Data_Table.pdf) summarizes the characteristics of each attribute. For numeric variables, it includes statistical measures such as maximum, minimum, mean, and standard deviation, along with histograms to visualize distributions. For categorical variables, the table highlights the mode and bar charts to show category frequencies.

A portion of the metadata table, showing a few representative attributes, is presented below:

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/07c313677ad06b692d3106042931947352b686e9/MetaData_Table.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: Summary of Attribute Characteristics with Statistics and Charts</em>
</p>


**1.2 ⚠️ Missing or Error Data Analysis**   
> ⚠️ **not clean the data** at this stage.

🟩 Missing values and erroneous data were identified in the HOUSEHOLD_SIZE, OCCUPATION, and COMMENTS columns. The figure presents these columns along with the counts of missing and erroneous entries. Additionally, the grand total of missing and erroneous values across these columns is calculated.

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/473e8b07eec2c8a08b2d9caf8e6e52dfc3627821/Error.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: Missing and Erroneous Values in Selected Columns</em>
</p>

---

### 2. Data Preparation

**2.1 🧹 Remove Irrelevant Variables**  

🟩 The data has 19 columns where CUST-ID is the unique identification for each customer. Thus, CUST-ID has been removed as it is not useful for inferring target variable. 

**2.2 🧼 Data Cleaning:** Justification for each cleaning step (handling missing and erroneous data)

🟩 The cleaning process for HOUSEHOLD_SIZE, OCCUPATION, and COMMENTS columns are descrived below:
- **HOUSEHOLD_SIZE:**
Error values such as “9+”, “5-Apr”, and “8-Jun” were identified. The value “9+” was replaced with 9, while invalid entries like “5-Apr” and “8-Jun” were removed.
- **OCCUPATION:**
Entries marked as “?” indicated missing occupation data and were removed. This ensures the column contains only valid categorical values, maintaining dataset quality for analysis.
- **COMMENTS:**
Null or blank entries were replaced with “No Comment”, explicitly marking missing feedback as a valid category.


The proposed suggestions for handling missing values and error values are presented in the following table 
<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/473e8b07eec2c8a08b2d9caf8e6e52dfc3627821/Handling.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: Suggestions for handling missing and error values</em>
</p>

After cleaning, the dataset contains **1312** valid rows, with **188** rows removed due to errors or missing values.

<div align="center">

### 🔄 Variable Conversion

</div>
  
- Python programs for the following conversions:  

  - **2.3 👤 CUST_GENDER → binary:** converted into a binary variable using a **mapping** approach to simplify analysis: F → 0, M → 1.
    
  - **2.4 🌎 COUNTRY_NAME → ordinal numbers:** Encoded as ordinal values based on frequency, where more frequent countries received lower numeric ranks.

  - **2.5 💵 CUST_INCOME_LEVEL → ordinal levels:**  Grouped into ordinal income tiers (1 = Low income, 2 = Middle income, 3 = High income) to preserve income                                                             hierarchy while reducing category complexity.
  
  - **2.6 🎓 EDUCATION → ordinal numbers:** Mapped to ordinal levels based on the U.S. education hierarchy, ranging from preschool to PhD.
    
  - **2.7 💼 OCCUPATION → one-hot encoding:** Applied one-hot encoding to transform categorical occupations into binary indicator variables using get_dummies.

---

### 3. Data Analysis

**3.1 📊 Correlation Analysis**  

🟩 Correlation of independent variables with target variable is shown in the following figure. Based on the correlation values, the variable YRS_RESIDENCE has the highest correlation with the target variable AFFINITY_CARD, followed by EDUCATION and OCCUPATION.   

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/14776f5f8b9e75ccbcfdfd054fca0399a545c159/Corr_ALL.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: correlation of variables</em>
</p>

  
**3.2 📝 Sentiment Analysis**  

🟩 The COMMENTS column was analyzed for sentiment using the TextBlob package. A function, classify_sentiment, computes the polarity of each comment and classifies it as positive (1), neutral (0), or negative (-1). The results are stored in a new column, SENTIMENT.

The number of comments classified under the SENTIMENT column and the levels (-1, 0, +1) are shown in the following figure. 

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/4a4340fa8026d1ab1fe1cd55886a2598e3724753/Senti.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: SENTIMENT and its count</em>
</p>

---

### 4. Data Exploration
A Python program has been developed to display histograms of any processed variable, allowing users to select the variable at runtime. The program runs continuously, providing visual insights until the user chooses to exit.

🟩 The Python program has been developed to visualize the distribution of processed variables ('CUST_GENDER', 'CUST_MARITAL_STATUS', 'COUNTRY_NAME', 'CUST_INCOME_LEVEL', 'EDUCATION', 'OCCUPATION', and 'sentiment') using histograms. In this program, users are allowed to select any one variable at runtime, and its corresponding histogram will be displayed. The program is designed to run continuously in a loop until an explicit exit command is given by the user. This interactive functionality has been implemented to support exploratory data analysis (EDA), where the distribution, spread, and potential outliers of variables can be observed. Such visual analysis is considered essential for understanding the underlying structure of the data during preprocessing and model development stages. 
The user is presented with the interface shown in the following figure, where they can enter a variable name or exit the program.

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/3e62e8245f75e9389adab96786cfbfb02a2e2e3c/Hist_prog.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: user input interface</em>
</p>

---

### 5. Data Mining

**5.1 🏗 Model Building**  
- Kept the **first 100 customer records** as a test set.  
- Used the remaining records to **build a logistic regression model** using the **top 10 relevant independent variables**.  
- Identify the **intercept and coefficients** for each independent variable.

🟩 For this analysis, the first 100 customer records from the processed campaign dataset were set aside for testing, while the remaining data were used to build a logistic regression model. The correlation between each independent variable and the target was calculated, and the top 10 features were selected as predictors. After training, the model’s intercept and coefficients were obtained to assess the direction and magnitude of each feature’s influence.

The intercept value of -1.730 served as the baseline. Among the top predictors, CUST_GENDER (1.035) had the strongest positive impact, followed by EDUCATION (0.645), OCCUPATION (0.469), YRS_RESIDENCE (0.468), and HOME_THEATER_PACKAGE (0.401). Most features positively influence the outcome, while OS_DOC_SET_KANJI (-0.203) showed a slight negative effect.

The next figure illustrates the intercept and coefficients of the top 10 features.

<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/0fb70468b38feb38e7c94a95a23f8a8dd90a45c7/Intercept_Top10-CorrL.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: intercept and top 10 variable’s coefficien</em>
</p>


**5.2 🧪 Model Testing**  
- Test the model on the **first 100 records**.  
- Explain results with **appropriate graphs** and performance metrics.

🟩 The logistic regression model was evaluated using the first 100 customer records reserved for testing. Predictions were compared with actual outcomes, and performance was assessed using accuracy and a confusion matrix.

The model achieved 79% accuracy, correctly predicting 65 non-purchases (true negatives) and 14 purchases (true positives), while misclassifying 16 purchases (false negatives) and 5 non-purchases (false positives). Overall, the model demonstrates good predictive performance.

 The model’s accuracy and confusion matrix are shown in the next figure.
 
<p align="center">
  <img src="https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/a8a90c5f86988bf0ea9056647d2e273c523833a5/Performance_Mat.png" alt="Histogram" width="600"/>
  <br>
  <em>Figure: Model accuracy and Confusion Matrix of the logistic regression</em>
</p>



**5.3 💻 Predictive Application**  
An application was implemented using the logistic regression model, featuring a user interface that allows input of customer records via keyboard or file upload, and provides predicted Affinity Card results to the user.

🟩 A predictive application was developed based on the logistic regression model, featuring a user-friendly interface for real-time predictions of affinity card purchases (Figure-5.3.1). Users can enter customer data manually or upload a CSV file.

When entering data manually, the levels of the top 10 independent variables are displayed for selection. After selecting the input values and clicking the ‘Predict’ button, the predicted outcome is displayed (Figure-5.3.2). 
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

--- 


### 📎 Deliverables

- Python scripts (.py or Jupyter Notebook) for:  
  - Data cleaning 🧼  
  - Conversion 🔄  
  - Correlation & Sentiment analysis 📊📝  
  - Histogram plotting 📊  
  - Logistic regression model & testing 🏗🧪  
  - Predictive application 💻
  - Processed dataset with new **binary and ordinal variables**, **sentiment column**, and **logistic regression results** ✅

---

## 🌐 I’d Love to Connect!

- **LinkedIn:** [Md Fahim Hossain](https://www.linkedin.com/in/md-fahim-hossain-b51258227/)  
- **Email:** [fahimhossain0729@gmail.com](mailto:fahimhossain0729@gmail.com)


<div align="center">
  
**[⬆ Back to Top](#top)**

</div>

