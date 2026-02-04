##### MD FAHIM HOSSAIN | Data analyst

### Quetion - 1.1. Produce a meta data table to show characteristics of each attribute.

# Data Load & import essential packages

# In[ ]:


import pandas as pd
import numpy as np
df = pd.read_csv('/content/Marketing Campaign data.csv')
df.head(2)


# In[ ]:


df11 = pd.read_csv('/content/Marketing Campaign data.csv')
df12 = pd.read_csv('/content/Marketing Campaign data.csv')
df13 = pd.read_csv('/content/Marketing Campaign data.csv')


# Maximum, Minimum, Mean, Std. Deviation

# In[ ]:


# List of numerical variables
numerical_cols = ['AGE', 'HOUSEHOLD_SIZE', 'YRS_RESIDENCE']

# Convert columns to numeric (force errors to NaN)
df[numerical_cols] = df[numerical_cols].apply(pd.to_numeric, errors='coerce')

# Calculate metadata
numerical_metadata = pd.DataFrame({
    'Attribute Name': numerical_cols,
    'Min': df[numerical_cols].min().values,
    'Max': df[numerical_cols].max().values,
    'Mean': df[numerical_cols].mean().values,
    'Std. Deviation': df[numerical_cols].std().values
})

print("Numerical Metadata:")
print(numerical_metadata)


# Mode

# In[ ]:


# List of nominal variables
nominal_cols = [
    'CUST_ID', 'CUST_GENDER', 'CUST_MARITAL_STATUS', 'COUNTRY_NAME',
    'CUST_INCOME_LEVEL', 'EDUCATION', 'OCCUPATION', 'AFFINITY_CARD',
    'BULK_PACK_DISKETTES', 'FLAT_PANEL_MONITOR', 'HOME_THEATER_PACKAGE',
    'BOOKKEEPING_APPLICATION', 'PRINTER_SUPPLIES', 'Y_BOX_GAMES',
    'OS_DOC_SET_KANJI', 'COMMENTS'
]

# Prepare metadata with mode and mode count
mode_values = []
mode_counts = []

for col in nominal_cols:
    if not df[col].mode().empty:
        mode = df[col].mode().iloc[0]
        count = df[col].value_counts().loc[mode]
    else:
        mode = 'No mode'
        count = 0
    mode_values.append(mode)
    mode_counts.append(count)

# Create the dataframe
nominal_metadata = pd.DataFrame({
    'Attribute Name': nominal_cols,
    'Mode': mode_values,
    'Mode Count': mode_counts
})

print("\nNominal Metadata with Mode and Count:")
print(nominal_metadata)


# In[ ]:


# df['COLUMN_NAME'].unique()  -- unique values in a column

#df['CUST_ID '].value_counts()             -- unique values as well as their counts
#df['CUST_ID'].value_counts(ascending=True) -- +accending order by column vlaues


df['CUST_GENDER'].value_counts().sort_values(ascending=False)    #---  acceding order by MOde/ frequency or high count to low count
#df['COMMENTS'].value_counts().sort_values(ascending=False)
#df['CUST_ID'].value_counts().sort_values(ascending=False)


# Histogram

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns

# Plot histograms for numerical columns
for col in numerical_cols:
    plt.figure(figsize=(8, 6))
    sns.histplot(df[col], kde=True, bins=20, color='skyblue')
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()


# Bar chart

# In[ ]:


# Plot bar charts for nominal columns, excluding 'CUST_ID' and 'COMMENTS'
for col in nominal_cols:
    if col in ['CUST_ID', 'COMMENTS']:
        continue  # Skip excluded columns
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x=col, palette='Set2')
    plt.title(f'Bar Chart of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


# In[ ]:


# Plot top 10 most frequent comments (if COMMENTS is a free-text column)
top_comments = df['COMMENTS'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=top_comments.values, y=top_comments.index, palette='Set3')
plt.title('Frequency of Comments')
plt.xlabel('Frequency')
plt.ylabel('Comment')
plt.grid(True)
# Save the figure before showing
plt.tight_layout()  # Adjust layout to avoid clipping
plt.savefig('comments.png', dpi=300)  # Save as PNG with high resolution
plt.show()


# Saving Historgrap or bar chart image

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt



# List of numerical variables
numerical_cols = ['AGE', 'HOUSEHOLD_SIZE', 'YRS_RESIDENCE']

# Convert to numeric (force errors to NaN)
df[numerical_cols] = df[numerical_cols].apply(pd.to_numeric, errors='coerce')

# Generate histograms for each numerical column and save them as images
for col in numerical_cols:
    plt.figure(figsize=(8, 6))
    df[col].dropna().hist(bins=20, edgecolor='black')  # Drop NaN values for clean histograms
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)

    # Save the histogram as a .png file
    histogram_filename = f'{col}_histogram.png'
    plt.savefig(histogram_filename)
    plt.close()  # Close the plot to avoid display in Jupyter Notebook

    print(f"Saved {histogram_filename}")


# In[ ]:


# List of nominal variables
nominal_cols = [
    'CUST_ID', 'CUST_GENDER', 'CUST_MARITAL_STATUS', 'COUNTRY_NAME',
    'CUST_INCOME_LEVEL', 'EDUCATION', 'OCCUPATION', 'AFFINITY_CARD',
    'BULK_PACK_DISKETTES', 'FLAT_PANEL_MONITOR', 'HOME_THEATER_PACKAGE',
    'BOOKKEEPING_APPLICATION', 'PRINTER_SUPPLIES', 'Y_BOX_GAMES',
    'OS_DOC_SET_KANJI', 'COMMENTS'
]

# Generate bar charts for each nominal column and save them as images
for col in nominal_cols:
    plt.figure(figsize=(8, 6))
    df[col].dropna().value_counts().plot(kind='bar', edgecolor='black')  # Drop NaN values for clean bars
    plt.title(f'Bar Chart of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)

    # Save the bar chart as a .png file
    bar_chart_filename = f'{col}_bar_chart.png'
    plt.savefig(bar_chart_filename)
    plt.close()  # Close the plot to avoid display in Jupyter Notebook

    print(f"Saved {bar_chart_filename}")


# In[ ]:





# In[ ]:





# ## Question - 1.2. Describe missing or error data with suggestion of handling methods of each attribute.

# In[ ]:


# df['COLUMN_NAME'].unique()  -- unique values in a column

#df['CUST_ID '].value_counts()             -- unique values as well as their counts
#df['CUST_ID'].value_counts(ascending=True) -- +accending order by column vlaues


df['CUST_GENDER'].value_counts().sort_values(ascending=False)    #---  acceding order by MOde/ frequency or high count to low count
#df['COMMENTS'].value_counts().sort_values(ascending=False)
#df['CUST_ID'].value_counts().sort_values(ascending=False)


# In[ ]:


df1 = pd.read_csv('/content/Marketing Campaign data.csv')


# In[ ]:


df1.columns


# In[ ]:


df1['HOUSEHOLD_SIZE'].value_counts()    # it has date & 9+ values


# In[ ]:


df1['OCCUPATION'].value_counts()        # it has ?


# In[ ]:


df1['COMMENTS'].isnull().sum()           # it has Null values


# ## Question 2.1. Write Python programs to remove variables with no inference to the target justifications and keep comments for further process.

# remove variables with no inference to the target justifications and keep comments

# In[ ]:


import pandas as pd

# Load the dataset

# Drop variables with no inference to the target
df1 = df1.drop(['CUST_ID'], axis=1)       # 'CUST_ID' is an identifier and has no predictive power
                                          # Keep 'COMMENTS' for future NLP/sentiment analysis
# Show the remaining columns
print("Remaining columns:\n", df1.columns.tolist())


# In[ ]:


df1.head(3)
#df1.shape


# In[ ]:


df.shape


# ## Question 2.2. Write Python programs to clean data and provide justifications.

# •	Write Python programs to clean data and provide justifications.

# In[ ]:


# fillna
# isna
# isnull


# 'HOUSEHOLD_SIZE'

# In[ ]:


# Remove leading/trailing whitespace
df1['HOUSEHOLD_SIZE'] = df1['HOUSEHOLD_SIZE'].astype(str).str.strip()

# Replace specific problematic values
df1['HOUSEHOLD_SIZE'] = df1['HOUSEHOLD_SIZE'].replace({
    '9+': 9,
    '5-Apr': np.nan,
    '8-Jun': np.nan
})
# Convert to numeric
df1['HOUSEHOLD_SIZE'] = pd.to_numeric(df1['HOUSEHOLD_SIZE'], errors='coerce')
df1['HOUSEHOLD_SIZE'] .unique()


# In[ ]:


# To see the total number of NaN values in a column
df1['HOUSEHOLD_SIZE'].isna().sum()


# In[ ]:


df1['HOUSEHOLD_SIZE'].shape


# ['OCCUPATION']

# In[ ]:


## Cleaning OCCUPATION
# Replace " ? " with NaN
df1['OCCUPATION'] = df1['OCCUPATION'].replace('?', np.nan)


# ['COMMENTS']

# In[ ]:


## Cleaning COMMENTS
# Replace null values with a default placeholder
df1['COMMENTS'] = df1['COMMENTS'].fillna('No Comment')


# In[ ]:


# Replace blank strings or 'Unknown' strings with NaN
#df1.replace(["", " ", "Unknown", "unknown"], np.nan, inplace=True)


# In[ ]:


df1.shape


# ########## Chechk by unique() function to see the nan/null value or all values + by exactly search by value of col by isna()

# In[ ]:


#df1['HOUSEHOLD_SIZE'].unique()
#df1['OCCUPATION'].unique()

#print((df1['COMMENTS'] == 'No Comment').sum())            #-- Null values are replace by 'No Comment'

#print(df1['OCCUPATION'].isna().sum())
#print(df1['HOUSEHOLD_SIZE'].isna().sum())    - # both the column fill as a null value as 'nan'


# #### Check the drop rows

# In[ ]:


# Drop all rows that contain any NaN values
df2 = df1.dropna()
df2.shape
# Optional: Reset index after dropping rows
#df_cleaned = df_cleaned.reset_index(drop=True)


# In[ ]:


# To see how many rows were deleted:
deleted_rows = df1.shape[0] - df2.shape[0]
print(f"Number of rows deleted: {deleted_rows}")


# In[ ]:


# To check only for specific columns
print("OCCUPATION null count:", df1['OCCUPATION'].isna().sum())
print("HOUSEHOLD_SIZE null count:", df1['HOUSEHOLD_SIZE'].isna().sum())


# In[ ]:


# Rows where BOTH columns are null
both_null = df1[df1['OCCUPATION'].isna() & df1['HOUSEHOLD_SIZE'].isna()]
print("Number of rows with both OCCUPATION and HOUSEHOLD_SIZE as null:", both_null.shape[0])


# In[ ]:


# Rows where either OCCUPATION or HOUSEHOLD_SIZE is null
total_nulls = df1[df1['OCCUPATION'].isna() | df1['HOUSEHOLD_SIZE'].isna()]
print("Total rows with null in OCCUPATION or HOUSEHOLD_SIZE:", total_nulls.shape[0])
# Rows with only OCCUPATION null
# Rows with only HOUSEHOLD_SIZE null
# Rows with both null


# In[ ]:


# To see which rows were deleted: in CSV file
deleted_rows_df = df1[df1.isna().any(axis=1)]
deleted_rows_df.to_csv("deleted_rows.csv", index=False)


# In[ ]:


print(deleted_rows_df)


# In[ ]:


df_cleaned = df2


# In[ ]:


# Show count of null values in each column
df_cleaned.isnull().sum()
#df1.isnull().sum()               # - check the comparison


# ## Question 2.3(a, b, c, d, e) or 2.3 to 2.7

# •	Write a Python program to convert variables as per the following requirements. You should provide screenshots of your Python code with comments as well as data before and after conversion.

# ###### First check unique values then convert

# In[ ]:


#df['EDUCATION'].nunique()        - unique number total
#df1['HOUSEHOLD_SIZE'].unique()
#df['CUST_ID '].value_counts()             -- unique values as well as their counts
#df['CUST_ID'].value_counts(ascending=True) -- +accending order by column vlaues

#print((df1['COMMENTS'] == 'No Comment').sum())            #-- Null values are replace by 'No Comment'
#print(df1['OCCUPATION'].isna().sum())


# ###### 2.3 or (a) Convert CUST_GENDER into binary (F → 0, M → 1)

# In[ ]:


# Convert CUST_GENDER into binary values
#df_cleaned['CUST_GENDER'].unique()

df_cleaned['CUST_GENDER'] = df_cleaned['CUST_GENDER'].map({'F': 0, 'M': 1})


# In[ ]:


df1['CUST_GENDER'].unique()


# In[ ]:


df_cleaned['CUST_GENDER'].unique()


# ###### 2.4 or (b) Convert COUNTRY_NAME to ordinal based on frequency (descending)

# In[ ]:


# Create ordinal mapping based on frequency
#df_cleaned['COUNTRY_NAME'].unique()

country_order = df_cleaned['COUNTRY_NAME'].value_counts().rank(method='first', ascending=False).astype(int)
df_cleaned['COUNTRY_NAME'] = df_cleaned['COUNTRY_NAME'].map(country_order)


# In[ ]:


print(country_order.sort_values())


# In[ ]:


df_cleaned['COUNTRY_NAME'].value_counts()


# ####### 2.5 or (c) Convert CUST_INCOME_LEVEL into 3 ordinal levels (1=Low, 2=Middle, 3=High)

# In[ ]:


# Display unique values of 'CUST_INCOME_LEVEL' in alphabetical order vertically
unique_values = df_cleaned['CUST_INCOME_LEVEL'].unique()
unique_values_sorted = sorted(unique_values)

# Display vertically
for value in unique_values_sorted:
    print(value)


# Convert CUST_INCOME_LEVEL into 3 ordinal levels (1=Low, 2=Middle, 3=High)

# In[ ]:


# Define the mapping for income levels into 3 ordinal levels (Low, Middle, High)
income_mapping = {
    'A: Below 30,000': 1,         # Low Income
    'B: 30,000 - 49,999': 1,     # Low Income
    'C: 50,000 - 69,999': 2,     # Middle Income
    'D: 70,000 - 89,999': 2,     # Middle Income
    'E: 90,000 - 109,999': 2,    # Middle Income
    'F: 110,000 - 129,999': 2,   # Middle Income
    'G: 130,000 - 149,999': 3,   # High Income
    'H: 150,000 - 169,999': 3,   # High Income
    'I: 170,000 - 189,999': 3,   # High Income
    'J: 190,000 - 249,999': 3,   # High Income
    'K: 250,000 - 299,999': 3,   # High Income
    'L: 300,000 and above': 3    # High Income
}

# Apply the mapping to the 'CUST_INCOME_LEVEL' column
df_cleaned['CUST_INCOME_LEVEL'] = df_cleaned['CUST_INCOME_LEVEL'].map(income_mapping)


# In[ ]:


df_cleaned['CUST_INCOME_LEVEL'].unique()
#df1['CUST_INCOME_LEVEL'].unique()


# ####### 2.6 or (d) Convert EDUCATION into ordinal levels based on USA education system

# In[ ]:


# Display unique values of 'CUST_INCOME_LEVEL' in alphabetical order vertically
unique_values = df_cleaned['EDUCATION'].unique()
unique_values_sorted1 = sorted(unique_values)

# Display vertically
for value in unique_values_sorted1:
    print(value)


# In[ ]:


df_cleaned['EDUCATION'].unique()


# In[ ]:


#df['EDUCATION'].value_counts()
df_cleaned['EDUCATION'].nunique()


# Convert EDUCATION into ordinal levels based on USA education system

# In[ ]:


# Define the mapping for education levels into ordinal numbers (corrected)
education_mapping = {
    'Presch.': 1,
    '1st-4th': 2,
    '5th-6th': 3,
    '7th-8th': 4,
    '9th': 5,
    '10th': 6,
    '11th': 7,
    '12th': 8,
    'HS-grad': 9,
    'Assoc-A': 10,
    'Assoc-V': 11,
    '< Bach.': 12,  # Added < Bach. before Bach.
    'Bach.': 13,
    'Masters': 14,
    'Profsc': 15,
    'PhD': 16
}

# Apply the mapping to the 'EDUCATION' column
df_cleaned['EDUCATION'] = df_cleaned['EDUCATION'].map(education_mapping)


# In[ ]:


for level, code in education_mapping.items():
    print(f"{code} : {level}")


# In[ ]:


print(df_cleaned['EDUCATION'].sort_values())


# In[ ]:


df_cleaned['EDUCATION']


# In[ ]:


df_cleaned.columns


# ####### 2.7 or (e) Convert OCCUPATION using One-Hot Encoding

# In[ ]:


# Display unique values of 'CUST_INCOME_LEVEL' in alphabetical order vertically
unique_values = df_cleaned['OCCUPATION'].unique()
unique_values_sorted1 = sorted(unique_values)

# Display vertically
for value in unique_values_sorted1:
    print(value)


# Convert OCCUPATION using One-Hot Encoding

# #### # switch off the code - for keep it one column for QUestion 3-5 otherwise it will be diffiuct to find correlation and ML model apply and for making comment

# In[ ]:


# Perform One-Hot Encoding on 'OCCUPATION' column
# df_cleaned = pd.get_dummies(df_cleaned, columns=['OCCUPATION'], prefix='OCCUPATION', dtype=int)   # switch of it for keep it one column for QUestion 3-5


# In[ ]:


df_cleaned.head(15)


# In[ ]:


# List of transformed columns (original or new ones created)
transformed_cols = ['CUST_GENDER', 'COUNTRY_NAME', 'CUST_INCOME_LEVEL', 'EDUCATION']
# Add all one-hot encoded columns for OCCUPATION
occupation_encoded_cols = [col for col in df_cleaned.columns if col.startswith('OCCUPATION')]

# Combine all transformed columns
final_transformed_cols = transformed_cols + occupation_encoded_cols

# Display only these columns
df_cleaned[final_transformed_cols].head(10)


# In[ ]:


df1[transformed_cols + ['OCCUPATION']]


# In[ ]:





# In[ ]:





# ## Question 3(a) or 3.1

# a)	Convert variables (except comments) not included in the data preparation process of Task 2 to numbers or binary and write a Python program to show the correlation of all variables with the target.

# #### convert 'CUST_MARITAL_STATUS' col

# In[ ]:


df_cleaned.columns


# In[ ]:


df_cleaned['CUST_MARITAL_STATUS'].unique()


# Convert marital_status

# In[ ]:


# Define the mapping for marital status into ordinal numbers
marital_status_mapping = {
    'NeverM': 1,
    'Married': 2,
    'Mabsent': 3,
    'Separ.': 4,
    'Divorc.': 5,
    'Widowed': 6
}

# Apply the mapping to the 'CUST_MARITAL_STATUS' column
df_cleaned['CUST_MARITAL_STATUS'] = df_cleaned['CUST_MARITAL_STATUS'].map(marital_status_mapping)


# In[ ]:


for code, status in marital_status_mapping.items():
    print(f"{status} : {code}")


# In[ ]:


df_cleaned.head(3)


# #### Convert  OCCUPATION - output in order

# In[ ]:


df_cleaned['OCCUPATION'].unique()


# In[ ]:


# Define the mapping for occupations into ordinal numbers based on assumed importance
occupation_mapping = {
    'House-s': 1,      # Housekeeping
    'Farming': 2,      # Farming and fishing
    'Handler': 3,      # Handlers, cleaners
    'Other': 4,        # Miscellaneous/Unspecified
    'Transp.': 5,      # Transport
    'Machine': 6,      # Machine operators
    'Crafts': 7,       # Craft workers
    'Cleric.': 8,      # Clerical work
    'Sales': 9,        # Sales jobs
    'TechSup': 10,     # Technicians and support
    'Protec.': 11,     # Protective services
    'Exec.': 12,       # Executive, managerial
    'Prof.': 13,       # Professional (Doctors, Engineers, etc.)
    'Armed-F': 14      # Armed forces (often considered a separate or top-tier category)
}

# Apply the mapping to the 'OCCUPATION' column
df_cleaned['OCCUPATION'] = df_cleaned['OCCUPATION'].map(occupation_mapping)


# In[ ]:


for name, rank in occupation_mapping.items():
    print(f"{rank} : {name}")


# In[ ]:


df_cleaned.head(3)


# In[ ]:


df_cleaned.shape


# ### Correlation

# In[ ]:


df_cleaned.columns


# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df_cleaned is your DataFrame and it already has all variables as numeric
# Define the target variable
target = 'AFFINITY_CARD'

# List of feature variables
features = [
    'CUST_GENDER', 'AGE', 'CUST_MARITAL_STATUS', 'COUNTRY_NAME', 'CUST_INCOME_LEVEL',
    'EDUCATION', 'OCCUPATION', 'HOUSEHOLD_SIZE', 'YRS_RESIDENCE', 'BULK_PACK_DISKETTES',
    'FLAT_PANEL_MONITOR', 'HOME_THEATER_PACKAGE', 'BOOKKEEPING_APPLICATION', 'PRINTER_SUPPLIES',
    'Y_BOX_GAMES', 'OS_DOC_SET_KANJI'  # remove "comments"
]
len(features)


# In[ ]:


# Calculate the correlation matrix
correlation_matrix = df_cleaned[features + [target]].corr()

# Get the correlation of all variables with the target variable
correlation_with_target = correlation_matrix[target]

# Display the correlation values
#print("Correlation of variables with target ('AFFINITY_CARD'):")
#print(correlation_with_target)
# Display the correlation values in an attractive format
# Display the correlation values in an attractive format
print("\n--- Correlation of variables with target ('AFFINITY_CARD') ---")
print(correlation_with_target.sort_values(ascending=False).round(2))


# In[ ]:


# Optional: Visualize the correlation matrix using a heatmap
plt.figure(figsize=(14, 10))  # Increase figure size for better visibility
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f",
            cbar_kws={'label': 'Correlation Coefficient'}, center=0,
            annot_kws={'size': 10, 'weight': 'bold', 'color': 'black'},  # Reduced font size here
            linecolor='white', linewidths=0.8, square=True)  # Adjust gridlines

# Enhance the title and axis labels
plt.title('Correlation Matrix of Features with Target (AFFINITY_CARD)', fontsize=18, fontweight='bold', color='black')  # Title in black
plt.xticks(rotation=45, ha='right', fontsize=10, color='darkred')  # Smaller font size for x-axis labels
plt.yticks(rotation=0, fontsize=10, color='darkred')  # Smaller font size for y-axis labels

# Adjust layout for better spacing and readability
plt.tight_layout()

# Show the plot
plt.show()


# ## 3(b) or 3.2

# b)	Write a Python program to analyse comments sentiment and create a sentiment column with values of 1 positive, 0 neutral, and -1 negative.

# analyse comments sentiment and create a sentiment column with values of 1 positive, 0 neutral, and -1

# In[ ]:


df_cleaned['COMMENTS'].nunique()


# In[ ]:


#df_cleaned['COMMENTS'].unique()  # see all the unique comment from the COMMENTS variable


# In[ ]:


# Install the necessary package
get_ipython().system('pip install -q textblob')


# In[ ]:





# In[ ]:


# Import necessary libraries
import pandas as pd
from textblob import TextBlob


# In[ ]:


# Sample data: replace this with your actual comments list or load from CSV
comments = [
    "A great idea.  Thank you!  Signed, happy in Texas",
    "A great program but I have to complain just a bit. Why do you need to know how many children I have, where I shop, etc.?  Give us a discount for shopping at your store, but don't ask too many personal questions.",
    "A lousy idea.  I threw your card away. If you want to know what I buy, I'll shop elsewhere.",
    "Affinity card is a great idea. But your store is still too expensive. I am tired of your lousy junk mail.",
    "Affinity card is great. I think it is a hassle to have to remember to bring it in every time though.",
    "Affinity card makese sense only for bulk purchases. For all others, driving so far is not worth the discount. Either offer free shipping or build a store close by.",
    "Can I apply my discount to a purchase I made last month? Excellent program.  Thanks",
    "Can I use my Affinity card to buy bulk purchases and ship them to my mother in Arizona?",
    "Could you send an Affinity Card to my mother in France?  Let me know and I'll send you here address.",
    "Dear store manager, please do not send me any more Affinity cards. I do not shop at your store very often and I feel that your new card imposes an invasion on my privacy.",
    "Does this discount work if you live in Australia?I've moved and I would like to purchase a few items as gifts but want the discount.  Have you ever considered offering free shipping?",
    "Don't send me any more promotions.  I get too much lousy junk mail already",
    "Even with the new 10% card, your prices are still too expensive. I am tired of your gimmicks.",
    "Forget it. I 'm not giving you all my personal information.  I wish you'd give up and respect a customer's privacy.",
    "Great program.  Love the discount. Signed happy customer.",
    "How much would it cost to upgrade my computer to the latest model you advertised this week?",
    "I am not going to waste my time filling up this three page form. Lousy idea.",
    "I am unhappy with the service at your store. Do not consider me a loyal customer just because I use your Affinity Card",
    "I don't like your new Affinity Card program.  Too little, too late.  I am very happy with your competitor's stores.",
    "I just purchased a computer from your store last month.  Why didn't you offer this discount then?",
    "I love it. Will never shop at other shops again!",
    "I love shopping with my Affinity Card! Thank you. I used it to purchase a new flat panel monitor. It is amazing. Thank you again!",
    "I love the discounts. But I mostly end upbuying  things I do not need.",
    "I love the new on-line documentation.",
    "I purchased a new computer from your store recently and then received the new discount membership card.  Could I speak with a store manager about getting discounts for my past purchases?",
    "I purchased a new computer recently, but the manuals weren't included.  Could you ship them to me directly?",
    "I purchased the new mouse pads and love them. I also purchased one for my sister and one for my brother.",
    "I run a small convenience store. Any chance that I would be eligible for larger discounts if I purchase a large quantity of items (bulk purchase)?",
    "I shop your store a lot.  I love your weekly specials.",
    "I used to shop at your store, but have stopped now. I tried to return some electronic items and your store manager was a pain to deal with.",
    "I wanted to write you to let you know that I've purchased several items at your store recently and have been very satisfied with my purchases. Keep up  the good work.",
    "If I forget my affinity card, can I still shop here and get the discount?",
    "It is a good way to attract new shoppers. After shopping at your store for more than a month, I am ready to move on though. Not enough variety",
    "My brother uses the affinity card a lot. I think the competitor has better prices without it.",
    "My sister told me about your store and I was impressed. Now I use it for all my shopping here.",
    "Shopping at your store is a hassle. I rarely shop there and usually forget to bring your new loyalty card and hence never get the items at the sale price.  Can a store manager look up my account on-line?",
    "Thank you! But I am very unhappy with all the junk mail you keep sending.",
    "Thank you, But please remove my name from your list.",
    "Thanks a lot for my new affinity card. I love the discounts and have since started shopping at your store for everything.",
    "Thanks but even with your discounts, your products are too expensive. Sorry.",
    "The more times that I shop at your store, the more times I am impressed.  Don't change anything",
    "The new affinity card is great. Thank you. I do  have to say that it is a hassle to remember to bring it  with me when I shop as I only shop at your store  for sale items. Could you keep my record in your computer?",
    "This Affinity Card is great.I am delighted that you sent me one as I 've only shopped at your store once. I was so pleased to be included in your program that I immediately purchased a new flat panel monitor.",
    "Why didn't you start a program like this before? Everyone else has been offering discounts like this for years.",
    "No comments"
]

# Create a DataFrame
df21 = pd.DataFrame({'COMMENTS': comments})

# Function to classify sentiment
def classify_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return 1   # Positive
    elif polarity < -0.1:
        return -1  # Negative
    else:
        return 0   # Neutral

# Apply sentiment classification
df21['SENTIMENT'] = df21['COMMENTS'].apply(classify_sentiment)

# Show result
df21.head()


# In[ ]:


df21['COMMENTS'].count()


# In[ ]:


df21['SENTIMENT'].value_counts()


# In[ ]:


# Merge df_cleaned with df21 on the 'COMMENTS' column
df_cleaned = df_cleaned.merge(df21[['COMMENTS', 'SENTIMENT']], on='COMMENTS', how='left')
df_cleaned.head(5)


# In[ ]:


df2.shape


# In[ ]:


print ('Assigment 1-3 Done, Congratulation!')


# # 4.

# Data exploration
# 
# Write a Python program that displays a histogram of one of the processed variables, allowing the user to select any one variable at run time. The program should continue running until the user chooses to exit.
# 

# In[ ]:


df2 = df_cleaned


# In[ ]:


df2.columns


# 4. Write a Python program that displays a histogram of one of the processed variables, allowing the user to select any one variable at run time. The program should continue running until the user chooses to exit.

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns

# DataFrame: df_cleaned
allowed_columns = ['CUST_GENDER', 'CUST_MARITAL_STATUS', 'COUNTRY_NAME',
                   'CUST_INCOME_LEVEL', 'EDUCATION', 'OCCUPATION',
                   'sentiment_score', 'sentiment']

print("📊 Available columns to plot a histogram:")
print(", ".join(allowed_columns))
print("Type 'exit' to quit.\n")

while True:
    selected_column = input("🔹 Enter a column name to plot a histogram (or type 'exit' to quit): ")

    if selected_column.lower() == 'exit':
        print("✅ Exiting program. Thank you!")
        break
    elif selected_column in allowed_columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df2, x=selected_column, bins=10, kde=True, color='skyblue', edgecolor='black')

        plt.title(f'Histogram of {selected_column}', fontsize=16, fontweight='bold')
        plt.xlabel(selected_column, fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    else:
        print("❌ Invalid column name. Please choose from the list above.\n")


# In[ ]:





# ## 5. Data Mining

# In[ ]:


df2.columns


# In[ ]:


df3 = df2.iloc[:, :-3]
df3.columns


# In[ ]:


df3.shape


# In[ ]:


df3.head(3)


# ### Question 5.1

# •	Keep the first 100 customer records from processed campaign data for testing and keep the rest to build a logistic regression ML model using the top 10 relevant independent variables with Python program. Find intercept and coefficients for each independent variable.

# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


# In[ ]:


# Clean column names (remove extra spaces if any)
df3.columns = df3.columns.str.strip()

# Check if target variable exists
if 'AFFINITY_CARD' not in df3.columns:
    raise KeyError("Target column 'AFFINITY_CARD' not found in the DataFrame")

# Compute the full correlation matrix
correlation_matrix = df3.corr()

# Get correlation of all variables with the target variable
correlation_with_target = correlation_matrix['AFFINITY_CARD'].sort_values(ascending=False)

# Display correlation values
print("Correlation of each variable with 'AFFINITY_CARD':\n")
print(correlation_with_target)


# Keep the first 100 customer records from processed campaign data for testing and keep the rest to build a logistic regression ML model using the top 10 relevant independent variables with Python program. Find intercept and coefficients for each independent variable.

# In[ ]:


from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# STEP 1: Select top 10 features (excluding the target itself)
top_10_features = correlation_with_target[1:11].index.tolist()
print("Top 10 features based on correlation:\n")#, top_10_features)

# STEP 2: Split the dataset
test_data = df3.head(100)
train_data = df3.tail(df3.shape[0] - 100)

# STEP 3: Define features and target
X_train = train_data[top_10_features]
y_train = train_data['AFFINITY_CARD']
X_test = test_data[top_10_features]
y_test = test_data['AFFINITY_CARD']

# STEP 4: Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# STEP 5: Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)             # train model by train data

# STEP 6: Get intercept and coefficients
intercept = model.intercept_[0]
coefficients = model.coef_[0]

# STEP 7: Create DataFrame for feature coefficients
coef_df = pd.DataFrame({
    'Feature': top_10_features,
    'Coefficient': coefficients
})

# Display the results
print("\nIntercept:", intercept)
print("\nCoefficients for each feature:\n")
print(coef_df)


# In[ ]:





# ### Question 5.2 - Test the accuracy of the model using the first 100 customer records and explain the results with graphs.

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Make predictions on the test data (first 100 customer records)
y_pred = model.predict(X_test_scaled)

# 2. Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of the logistic regression model: {:.2f}%".format(accuracy * 100))

# 3. Confusion Matrix to understand model performance
conf_matrix = confusion_matrix(y_test, y_pred)

# 4. Enhanced Confusion Matrix with custom color palette and annotations (without percentages)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='magma', linewidths=1.5, linecolor='black',
            xticklabels=['Not Purchased', 'Purchased'], yticklabels=['Not Purchased', 'Purchased'],
            cbar_kws={'label': 'Frequency'}, annot_kws={'size': 14, 'weight': 'bold', 'color': 'red'})  # Changed color to red

plt.title('Confusion Matrix', fontsize=18, weight='bold')
plt.xlabel('Predicted', fontsize=14)
plt.ylabel('Actual', fontsize=14)
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.show()

# 5. Enhanced Predicted Probability Histogram with cumulative distribution
y_prob = model.predict_proba(X_test_scaled)[:, 1]  # Probability for the positive class

# Plotting the histogram with KDE and cumulative plot
plt.figure(figsize=(10, 6))
sns.histplot(y_prob, bins=20, kde=True, color='skyblue', edgecolor='black', linewidth=1.5, stat='density')

# Adding the cumulative distribution
sns.kdeplot(y_prob, color='darkorange', shade=True, linewidth=2, cumulative=True)

plt.title('Predicted Probabilities of Affinity Card Purchase with Cumulative Distribution', fontsize=18, weight='bold')
plt.xlabel('Predicted Probability', fontsize=14)
plt.ylabel('Density', fontsize=14)
plt.xticks(rotation=0)
plt.grid(True, linestyle='--', alpha=0.6)

# Show legend for KDE
plt.legend(['Histogram', 'Cumulative Density'], loc='upper left', fontsize=12)
plt.show()

# 6. Additional: Bar Plot for Accuracy Comparison (optional, for visual comparison with baseline)
# This can be useful if comparing multiple models
plt.figure(figsize=(6, 5))
plt.bar(['Logistic Regression'], [accuracy], color='salmon', edgecolor='black')
plt.title('Model Accuracy Comparison', fontsize=16, weight='bold')
plt.xlabel('Model', fontsize=14)
plt.ylabel('Accuracy (%)', fontsize=14)
plt.ylim(0, 1)
plt.show()


# In[ ]:





# ### Question 5.3

# Implement a predictive application based on the created logistic regression ML model. The application should have an appropriate user interface to allow users to input customer records from keyboard and file to receive predicted answers.

# In[ ]:


from google.colab import files
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import io
import base64

class ColabAffinityCardPredictor:
    def __init__(self, df3):
        # Store reference to dataframe
        self.df3 = df3

        # STEP 1: Feature selection
        correlation_matrix = self.df3.corr()
        correlation_with_target = correlation_matrix['AFFINITY_CARD'].sort_values(ascending=False)
        self.top_10_features = correlation_with_target[1:11].index.tolist()

        # STEP 2: Data splitting
        self.test_data = self.df3.head(100)
        self.train_data = self.df3.tail(self.df3.shape[0] - 100)

        # STEP 3: Prepare training data
        X_train = self.train_data[self.top_10_features]
        y_train = self.train_data['AFFINITY_CARD']

        # STEP 4: Feature scaling
        self.scaler = StandardScaler()
        self.X_train_scaled = self.scaler.fit_transform(X_train)

        # STEP 5: Model training
        self.model = LogisticRegression()
        self.model.fit(self.X_train_scaled, y_train)

        # STEP 6: Store coefficients
        self.intercept = self.model.intercept_[0]
        self.coefficients = self.model.coef_[0]

        # Feature configuration with descriptive labels
        self.features = self.top_10_features
        self.category_mappings = {
            'OCCUPATION': {
                'options': ['1 : House-s', '2 : Farming', '3 : Handler', '4 : Other',
                           '5 : Transp.', '6 : Machine', '7 : Crafts', '8 : Cleric.',
                           '9 : Sales', '10 : TechSup', '11 : Protec.', '12 : Exec.',
                           '13 : Prof.', '14 : Armed-F'],
                'values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            },
            'EDUCATION': {
                'options': ['1 : Presch.', '2 : 1st-4th', '3 : 5th-6th', '4 : 7th-8th',
                           '5 : 9th', '6 : 10th', '7 : 11th', '8 : 12th', '9 : HS-grad',
                           '10 : Assoc-A', '11 : Assoc-V', '12 : < Bach.', '13 : Bach.',
                           '14 : Masters', '15 : Profsc', '16 : PhD'],
                'values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
            },
            'CUST_GENDER': {
                'options': ['1 : M', '0 : F'],
                'values': [1, 0]
            },
            'COUNTRY_NAME': {
                'options': ['1 : United States of America', '2 : Argentina', '3 : Italy', '4 : Brazil',
                            '5 : Poland', '6 : Germany', '7 : United Kingdom', '8 : Canada',
                            '9 : Singapore', '10 : Saudi Arabia', '11 : Denmark', '12 : New Zealand',
                            '13 : Japan', '14 : China', '15 : Australia', '16 : France', '17 : Turkey', '18 : Spain'],

                'values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
            },
            'BULK_PACK_DISKETTES': {
                'options': ['0 : No', '1 : Yes'],
                'values': [0, 1]
            },
            'HOME_THEATER_PACKAGE': {
                'options': ['0 : No', '1 : Yes'],
                'values': [0, 1]
            },
            'BOOKKEEPING_APPLICATION': {
                'options': ['0 : No', '1 : Yes'],
                'values': [0, 1]
            },
            'OS_DOC_SET_KANJI': {
                'options': ['0 : No', '1 : Yes'],
                'values': [0, 1]
            }
        }

        self.create_widgets()
        self.show_model_summary()

    def show_model_summary(self):
        print("Model Training Summary:")
        print(f"Top 10 features: {', '.join(self.top_10_features)}")
        print(f"Intercept: {self.intercept:.4f}")
        print("\nFeature Coefficients:")
        coef_df = pd.DataFrame({
            'Feature': self.top_10_features,
            'Coefficient': self.coefficients
        })
        display(coef_df)
        print("\n" + "-"*50 + "\n")

    def create_widgets(self):
        self.menu_button1 = widgets.Button(description="1. Enter customer data manually")
        self.menu_button1.on_click(self.manual_entry)
        self.menu_button2 = widgets.Button(description="2. Upload customer data file")
        self.menu_button2.on_click(self.file_upload)
        self.output = widgets.Output()

        display(widgets.VBox([
            widgets.Label("AFFINITY CARD PREDICTION SYSTEM"),
            widgets.Label("Select an option:"),
            self.menu_button1,
            self.menu_button2,
            self.output
        ]))

    def manual_entry(self, b):
        with self.output:
            clear_output()
            input_widgets = {}
            for feature in self.features:
                if feature in self.category_mappings:
                    # Create dropdown with descriptive labels
                    input_widgets[feature] = widgets.Dropdown(
                        options=list(zip(
                            self.category_mappings[feature]['options'],
                            self.category_mappings[feature]['values']
                        )),
                        description=feature + ':',
                        style={'description_width': 'initial'}
                    )
                else:
                    input_widgets[feature] = widgets.FloatText(
                        description=feature + ':',
                        style={'description_width': 'initial'}
                    )

            submit_button = widgets.Button(description="Predict", layout={'width': '200px'})
            submit_button.on_click(lambda b: self.make_prediction(input_widgets))
            display(widgets.VBox(list(input_widgets.values()) + [submit_button]))

    def file_upload(self, b):
        with self.output:
            clear_output()
            print("Please upload a CSV file with customer data")
            upload = widgets.FileUpload(accept='.csv', multiple=False)
            display(upload)

            def on_upload_change(change):
                if upload.value:
                    name = list(upload.value.keys())[0]
                    self.process_uploaded_file(upload.value[name])

            upload.observe(on_upload_change, names='value')

    def process_uploaded_file(self, file_content):
        with self.output:
            clear_output()
            try:
                df = pd.read_csv(io.BytesIO(file_content['content']))
                missing_cols = set(self.features) - set(df.columns)
                if missing_cols:
                    print(f"Error: Missing columns in file: {', '.join(missing_cols)}")
                    return

                # Scale the features before prediction
                X = df[self.features]
                X_scaled = self.scaler.transform(X)

                results = []
                for idx, row in enumerate(X_scaled):
                    input_array = row.reshape(1, -1)
                    prediction = self.model.predict(input_array)[0]
                    probability = self.model.predict_proba(input_array)[0][1]

                    results.append({
                        'Customer': idx+1,
                        'Prediction': 'YES' if prediction == 1 else 'NO',
                        'Probability': f"{probability:.2%}"
                    })
                    print(f"\nCustomer {idx+1}:")
                    self.display_prediction(prediction, probability)

                print("\nProcessing complete!")
                results_df = pd.DataFrame(results)
                csv = results_df.to_csv(index=False)
                b64 = base64.b64encode(csv.encode()).decode()
                href = f'<a href="data:file/csv;base64,{b64}" download="affinity_predictions.csv">Download Predictions</a>'
                display(HTML(href))
            except Exception as e:
                print(f"Error processing file: {str(e)}")

    def make_prediction(self, input_widgets):
        with self.output:
            clear_output()
            input_data = {feature: widget.value for feature, widget in input_widgets.items()}
            prediction, probability = self.predict(input_data)
            self.display_prediction(prediction, probability)

    def predict(self, input_data):
        try:
            processed_data = []
            for feature in self.features:
                value = input_data.get(feature, 0)

                if value in [None, '']:
                    processed_data.append(0)
                else:
                    processed_data.append(float(value))

            input_array = np.array(processed_data).reshape(1, -1)
            input_scaled = self.scaler.transform(input_array)
            prediction = self.model.predict(input_scaled)
            probability = self.model.predict_proba(input_scaled)
            return prediction[0], probability[0][1]
        except Exception as e:
            print(f"Error making prediction: {str(e)}")
            return None, None

    def display_prediction(self, prediction, probability):
        if prediction is not None:
            print("\nPrediction Result:")
            print(f"Affinity Card Prediction: {'YES' if prediction == 1 else 'NO'}")
            print(f"Probability of acceptance: {probability:.2%}")
            print("\nInterpretation:")
            if prediction == 1:
                print("This customer is likely to accept an affinity card offer.")
            else:
                print("This customer is unlikely to accept an affinity card offer.")

# Initialize with your dataframe
# df3 must be defined in your environment with 'AFFINITY_CARD' column
# predictor = ColabAffinityCardPredictor(df3)
predictor = ColabAffinityCardPredictor(df3)


# 6.	Information

# In[ ]:


print("CourseWork of 'CC7182 Programming for Analytics Spring Semester 2024-2025' - Completed by 'MD FAHIM HOSSAIN' ")


# ## The End of Project
# 

# In[ ]:




