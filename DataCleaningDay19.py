#Student Dataset Data Cleaning System
import pandas as pd
import numpy as np
df1=pd.read_csv('/content/day18_students.csv')#use old dataset of day18
print(f'''Student Dataset Data Cleaning
''')
r,c = df1.shape
dr=df1.duplicated()
print(f'''
Before cleaning
----------------
Rows          : {r}
Columns       : {c}
Missing Values: {np.sum(df1.isnull().sum())}
Duplicate Rows: {dr.sum()}''')
#data cleaning
df1['AI']=df1['AI'].fillna(df1['AI'].mean())
df1['Database']=df1['Database'].fillna(df1['Database'].mean())
df1['Attendance']=df1['Attendance'].fillna(df1['Attendance'].mean())
# Text standardization
df1['Name'] = df1['Name'].str.strip()
df1['Gender'] = df1['Gender'].str.strip()
df1['Department'] = df1['Department'].str.strip()
df1['City'] = df1['City'].str.strip()
print(f'''
Cleaning
--------
Missing Values Handled    : {np.sum(df1.isnull().sum())}
Duplicates Removed        : {df1.duplicated().sum()}
Invalid Values Handled    : 0
Text Values Standardized  : Yes''')
print(f'''
After cleaning
---------------
Rows              : {r}
Columns           : {c}
Missing values    : {np.sum(df1.isnull().sum())}
Duplicate rows    : {df1.duplicated().sum()}''')
#for save the dataset:
df1.to_csv('/content/day19_cleaned_students.csv', index=False)
print(f'''
Clean dataset saved as: day19_cleaned_students.csv''')
dl=input('\nYou want to Download the cleaned dataset ? (y/n) : ')
if dl=='y' or dl=='Y':
  from google.colab import files
  files.download('day19_cleaned_students.csv')
else:
  print('Data cleaning completed...')
