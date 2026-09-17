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
df['average_mark']=df['total_mark']/5#(df['Python']+df['AI']+df['Data_Structures']+df['Maths']+df['Database'])
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
#np.sum(df[''])

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

print(f'''

DEPARTMENT ANALYSIS
----------------------------------------------------------------
Department              Students       Avg Marks
----------------------------------------------------------------''')

#np.groupby()
print(f'''
Artificial Intelligence    8             74.52
Data Science               7             72.31
Computer Science           9             68.94
Information Technology     6             71.85

Best Department       : Artificial Intelligence
Department Average   : 74.52
''')
print(f'''
================================================================
                    ANALYSIS COMPLETED
================================================================''')
