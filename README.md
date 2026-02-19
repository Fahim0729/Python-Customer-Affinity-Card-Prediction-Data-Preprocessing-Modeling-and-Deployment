# 🎯 Marketing Campaign Data Analysis: Affinity-Card Prediction, Predictive Application, and User Interface

The dataset contains **1,500 customer records**, each consisting of **19 variables**, including socio-demographic and product ownership information. The target variable is:

- **🎯 AFFINITY_CARD (Variable 11):**  
  - `1 = High-value`  
  - `0 = Low-value`

All datasets are in **CSV format** with the following attributes:

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
- Include for **numeric attributes**: max, min, mean, standard deviation, histogram 📊.  
- Include for **nominal attributes**: mode and bar chart 📊.  

![MetaData](https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/07c313677ad06b692d3106042931947352b686e9/MetaData_Table.png)


**1.2 ⚠️ Missing or Error Data Analysis**  
- Describe all missing values (null, blank, unknown, etc.)  
- Describe any **invalid or mismatching data**  
- Suggest handling methods for each attribute.  
> ⚠️ Do **not clean the data** at this stage.

![Error](https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/473e8b07eec2c8a08b2d9caf8e6e52dfc3627821/Error.png)

########################################################  add 1 tables error data handling & say we will delete them ....................................
---

### 2. Data Preparation

**2.1 🧹 Remove Irrelevant Variables**  
- Write Python programs to remove variables with no inference to the target.  
- Provide justifications and keep **comments** for further processing.  

 ###################################################################### remove cast id ..........................................
**2.2 🧼 Data Cleaning**  
- Write Python programs to clean the data.  
- Provide **justifications** for each cleaning step.  

![Handling](https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/473e8b07eec2c8a08b2d9caf8e6e52dfc3627821/Handling.png)

#########################################################  mention as null - delete those data  + final data Dimension ........................................

**2.3 🔄 Variable Conversion**  
- Write Python programs for the following conversions and include **screenshots**:  

  - **2.4 👤 CUST_GENDER → binary:** F = 0, M = 1  
  - **2.5 🌎 COUNTRY_NAME → ordinal numbers** based on frequency (descending order)  
  - **2.6 💵 CUST_INCOME_LEVEL → ordinal levels:**  
    - 1 = Low income  
    - 2 = Middle income  
    - 3 = High income  
  - **2.7 🎓 EDUCATION → ordinal numbers** based on USA education levels (ascending order)  
  - **2.8 💼 OCCUPATION → one-hot encoding** (binary columns for each occupation)
    
#######################################################################  just mention that only which function is used to for encoding in each question ...................
---

### 3. Data Analysis

**3.1 📊 Correlation Analysis**  
- Convert variables (except COMMENTS) not included in preparation into **numerical or binary format**.  
- Write a Python program to show **correlation of all variables with the target**.  

![Corr_ALL](https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/14776f5f8b9e75ccbcfdfd054fca0399a545c159/Corr_ALL.png)
#############################  CUST_MARITAL_STATUS + which function ,,,   Add correlation figure ..... 
  
**3.2 📝 Sentiment Analysis**  
- Analyze the COMMENTS column using Python.  
- Create a new **Sentiment column** with values:  
  - 1 = Positive ✅  
  - 0 = Neutral ⚪  
  - -1 = Negative ❌  

![Senti](https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/4a4340fa8026d1ab1fe1cd55886a2598e3724753/Senti.png)w 

##########################################  add figure 3.2.3 sentiment and its count ...........................................................
---

### 4. Data Exploration

- Write a Python program to **display a histogram** of any processed variable 📊.  
- The program should **allow runtime selection** of variables.  
- Continue running until the **user chooses to exit** 🔁.

![Hist_Prog](https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/3e62e8245f75e9389adab96786cfbfb02a2e2e3c/Hist_prog.png)

################################################################# just add 4.1 picture ................................................
---

### 5. Data Mining

**5.1 🏗 Model Building**  
- Keep the **first 100 customer records** as a test set.  
- Use the remaining records to **build a logistic regression model** using the **top 10 relevant independent variables**.  
- Identify the **intercept and coefficients** for each independent variable.  
![Intercept-Top10_Corr](https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/0fb70468b38feb38e7c94a95a23f8a8dd90a45c7/Intercept_Top10-CorrL.png)

**5.2 🧪 Model Testing**  
- Test the model on the **first 100 records**.  
- Explain results with **appropriate graphs** 📈 and performance metrics.  

![Performance](https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/a8a90c5f86988bf0ea9056647d2e273c523833a5/Performance_Mat.png)

**5.3 💻 Predictive Application**  
- Implement an application using the **logistic regression model**.  
- Include a **user interface** to input customer records via **keyboard or file upload** ⌨️📁.  
- Output **predicted Affinity Card results** to the user 🎯.

![Optiom](https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/ee6af59ff566c8d25c09f5f18cdb8bf2635a7176/Option.png)

![keyboard_Input](https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/ee6af59ff566c8d25c09f5f18cdb8bf2635a7176/Keyboard_input.png)

![File_Input](https://github.com/Fahim0729/Python-Customer-Affinity-Card-Prediction-Data-Preprocessing-Modeling-and-Deployment/blob/ee6af59ff566c8d25c09f5f18cdb8bf2635a7176/File_Input.png)


####################################################################  Add 10 correlation value picture, model resutls, 5.3.1, 5.3.9, 5.9.10 ( how the program will work)
---

### 📎 Deliverables

- Python scripts (.py or Jupyter Notebook) for:  
  - Data cleaning 🧼  
  - Conversion 🔄  
  - Correlation & Sentiment analysis 📊📝  
  - Histogram plotting 📊  
  - Logistic regression model & testing 🏗🧪  
  - Predictive application 💻  

- Screenshots and charts for each step 📸  

- Processed dataset with new **binary and ordinal variables**, **sentiment column**, and **logistic regression results** ✅


<div align="center">
  
**[⬆ Back to Top](#top)**

</div>

