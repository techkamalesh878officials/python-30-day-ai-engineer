import pandas as pd
import numpy as np
df=pd.read_csv('/content/day18_students.csv')
r,c = df.shape
#/pd.set_option("display.float_format", "{:.2f}".format)
print('''================================================================
                 PANDAS STUDENT DATA ANALYZER
================================================================
''')
print(f'''DATASET SUMMARY
----------------------------------------------------------------
Dataset Shape       : {r} rows × {c} columns
Total Students      : {r}
Total Columns       : {c}
Columns : \n{list(df)}
''')#df.columns.tolist()

print(f'''
SUBJECT PERFORMANCE
----------------------------------------------------------------
Subject              Average       Highest       Lowest
----------------------------------------------------------------''')
print(f'''
Python               {np.mean(df['Python']):.2f}         {df['Python'].max()}           {df['Python'].min()}
Maths                {np.mean(df['Maths']):.2f}         {df['Maths'].max()}            {df['Maths'].min()}
AI                   {np.mean(df['AI']):.2f}         {df['AI'].max()}         {df['AI'].min()}
Data Structures      {np.mean(df['Data_Structures']):.2f}         {df['Data_Structures'].max()}           {df['Data_Structures'].min()}
Database             {np.mean(df['Database']):.2f}         {df['Database'].max()}         {df['Database'].min()}

''')

print(f'''
STUDENT PERFORMANCE
----------------------------------------------------------------''')

df['total_mark']=df['Python']+df['AI']+df['Data_Structures']+df['Maths']+df['Database']
df['average_mark']=df['total_mark']/5#
ts=df.loc[df['total_mark'].idxmax(), 'Name']
ta=df.loc[df['Attendance'].idxmax(), 'Name']
ps=np.all(df[['Python','AI','Maths','Data_Structures','Database']]>=40,axis=1)
psc=ps.sum()

print(f'''
Top Student          : {ts}
Highest Average      : {df['average_mark'].max()} %

Top Attendance       : {ta}
Attendance           : {np.max(df['Attendance'])} %

Passed Students      : {psc} / {r}

''')


print(f'''
FILTER ANALYSIS
----------------------------------------------------------------''')

a75=np.all(df[['Attendance']]>=75,axis=1)
avg70=np.all(df[['average_mark']]>=70,axis=1)
p3=np.all(df[['Projects']]>=3,axis=1)
sh20=np.all(df[['Study_Hours_Per_Week']]>=20,axis=1)

print(f'''
Attendance >= 75%   : {a75.sum()} students
Average Marks >= 70 : {avg70.sum()} students
Projects >= 3       : {np.sum(p3)} students
Study Hours >= 20   : {sh20.sum()} students''')


# DEPARTMENT ANALYSIS
d_c = df.groupby('Department').size()
d_a = df.groupby('Department')['average_mark'].mean()

b_d = d_a.idxmax()
b_d_a = d_a.max()

print('''
DEPARTMENT ANALYSIS
----------------------------------------------------------------
Department                  Students       Avg Marks
----------------------------------------------------------------''')

for i in d_c.index:
    print(f'{i:<28} {d_c[i]:<14} '
          f'{d_a[i]:.2f}')

print(f'''
Best Department       : {b_d}
Department Average    : {b_d_a:.2f}
''')

print('''================================================================
                    ANALYSIS COMPLETED
================================================================''')

#output:
#================================================================
#                 PANDAS STUDENT DATA ANALYZER
#================================================================
#
#DATASET SUMMARY
#----------------------------------------------------------------
#Dataset Shape       : 30 rows × 14 columns
#Total Students      : 30
#Total Columns       : 14
#Columns : 
#['Student_ID', 'Name', 'Gender', 'Department', 'Year', 'City', 'Python', 'Maths', 'AI', 'Data_Structures', 'Database', 'Attendance', 'Projects', 'Study_Hours_Per_Week']
#
#
#SUBJECT PERFORMANCE
#----------------------------------------------------------------
#Subject              Average       Highest       Lowest
#----------------------------------------------------------------
#
#Python               70.87         100           36
#Maths                70.80         99            35
#AI                   66.90         100.0         38.0
#Data Structures      73.20         100           37
#Database             72.72         100.0         35.0
#
#
#
#STUDENT PERFORMANCE
#----------------------------------------------------------------
#
#Top Student          : Rohit
#Highest Average      : 88.2 %
#
#Top Attendance       : Deepika
#Attendance           : 99.0 %
#
#Passed Students      : 19 / 30
#
#
#
#FILTER ANALYSIS
#----------------------------------------------------------------
#
#Attendance >= 75%   : 19 students
#Average Marks >= 70 : 16 students
#Projects >= 3       : 18 students
#Study Hours >= 20   : 12 students
#
#DEPARTMENT ANALYSIS
#----------------------------------------------------------------
#Department                  Students       Avg Marks
#----------------------------------------------------------------
#AI                           4              69.07
#Computer Science             9              67.18
#Data Science                 10             73.92
#Information Technology       7              74.90
#
#Best Department       : Information Technology
#Department Average    : 74.90
#
#================================================================
#                    ANALYSIS COMPLETED
#================================================================
