import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#data set impoting as a dataframe
file_path = r"C:\Users\HP\Downloads\Regulatory Affairs of Road Accident Data 2020 India.csv"  
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip().str.lower()
print("Standardized Columns:")
print(df.columns)# Display the standardized column names
print("\nDataset Preview:")
print(df.head())# Display initial 5 rows
print("\nMissing Values in Dataset:")
print(df.isnull().sum())# Check for missing values for data cleaning purpose
df_cleaned = df.dropna() # Remove rows with missing values
print("\nDataset After Cleaning (No Missing Values):")
print(df_cleaned.isnull().sum())
plt.figure(figsize=(12, 8))# Distribution of Accidents Across Cities
sns.countplot(y='million plus cities', data=df_cleaned, 
              order=df_cleaned['million plus cities'].value_counts().index)
plt.title('Distribution of Road Accidents in Million-Plus Cities')
plt.xlabel('Number of Accidents')
plt.ylabel('Cities')
plt.show()
plt.figure(figsize=(10, 6))# Analysis of Accident Causes (Category)
sns.countplot(y='cause category', data=df_cleaned, 
              order=df_cleaned['cause category'].value_counts().index)
plt.title('Distribution of Accident Causes (Category)')
plt.xlabel('Number of Accidents')
plt.ylabel('Cause Category')
plt.show()
plt.figure(figsize=(12, 8))# Analysis of Accident Causes (Subcategory)
sns.countplot(y='cause subcategory', data=df_cleaned, 
              order=df_cleaned['cause subcategory'].value_counts().index)
plt.title('Detailed Analysis of Accident Causes (Subcategory)')
plt.xlabel('Number of Accidents')
plt.ylabel('Cause Subcategory')
plt.show()
plt.figure(figsize=(8, 5))# Outcomes of Incidents
sns.countplot(x='outcome of incident', data=df_cleaned, 
              order=df_cleaned['outcome of incident'].value_counts().index)
plt.title('Outcomes of Road Accidents')
plt.xlabel('Outcome')
plt.ylabel('Number of Incidents')
plt.show()
outcome_vs_cause = df_cleaned.groupby(['cause category', 'outcome of incident'])['count'].sum().unstack()
outcome_vs_cause.plot(kind='bar', stacked=True, figsize=(14, 8))
plt.title('Accident Causes vs Outcomes')
plt.xlabel('Cause Category')
plt.ylabel('Number of Incidents')
plt.legend(title='Outcome')
plt.show()# Analyzing Accident Causes vs Outcomes


