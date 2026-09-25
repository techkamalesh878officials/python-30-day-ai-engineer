import pandas as pd
import numpy as np
df2=pd.read_csv('/content/day19_cleaned_students.csv')#here paste the address link of day19th dataset
r,c=df2.shape
df2['total_mark']=df2['Python']+df2['AI']+df2['Data_Structures']+df2['Maths']+df2['Database']
df2['average_mark']=df2['total_mark']/5#
print(f'''Student Performance EDA
Dataset
-------
Rows: {r}
Columns: {c}''')
#perfomance
cam=df2['average_mark'].mean()
t5s = df2.sort_values(by="average_mark", ascending=False).head(5)
print(f'''
Performance
-----------
Class average marks  : {cam:.2f}
Highest average      : {np.max(df2['average_mark'])}
Lowest average       : {np.min(df2['average_mark'])}
Top 5 students:
{t5s[['Student_ID' , "Name", "average_mark",]]}''')
#attendance
sb75 = df2[df2["Attendance"] < 75].sort_values(by="Attendance",ascending=False)
print(f'''
Attendance
----------
Average attendance   : {np.mean(df2['Attendance']):.2f}
Highest attendance   : {np.max(df2['Attendance']):.2f}%
Lowest attendance    : {np.min(df2['Attendance']):.2f}%
Students below 75%   :
{sb75[["Name","Attendance"]]}''')
# DEPARTMENT ANALYSIS
d_c = df2.groupby('Department').size()
d_a = df2.groupby('Department')['average_mark'].mean()
d_att=df2.groupby('Department')['Attendance'].mean()
b_d = d_a.idxmax()
b_d_a = d_a.max()
print('''
Department
-----------
Department                   Students      Avg Marks    Attendance
---------------------------------------------------------------------''')
for i in d_c.index:
    print(f'{i:<25} : {d_c[i]:<2}students |'
          f' marks {d_a[i]:.2f} | '
          f'attendance {d_att[i]:.2f}')
print(f'''Best Department       : {b_d}
Department Average    : {b_d_a:.2f}''')
#study habits
ashw=df2['Study_Hours_Per_Week'].mean()
print(f'''
Study Habits
------------
Average study hours/week        : {ashw:.2f}
Students studying >=20 hrs/week : {np.all(df2[['Study_Hours_Per_Week']]>=20,axis=1).sum()}
Avg marks (>=20 hrs)            : {df2[df2["Study_Hours_Per_Week"] >= 20]['average_mark'].mean()}
Avg marks (<20 hrs)             : {df2[df2["Study_Hours_Per_Week"] < 20]['average_mark'].mean()}''')
print(f'''
Projects
--------
Average projects completed : {df2['Projects'].mean():.2f}
Most projects              : {df2.loc[df2['Projects'].idxmax(), 'Name']} ({df2['Projects'].max()} projects)''')
print(f'''
Bonus
---------
Correlation (study hours vs avg marks) : {df2['Study_Hours_Per_Week'].corr(df2['average_mark'])}''')
#Interpretation: Weak positive — barely any link between study hours and marks here
#Key Findings
#------------
#- 9 of 30 students (30%) are below 75% attendance — at-risk group
#- Information Technology has the highest avg marks; AI has the lowest
#- Students studying >=20 hrs score 9.3 marks higher on average
#- Top scorer (Rohit) and most-projects student (Arun) are different people
#- Rohit leads the class with 88.20 avg marks
