#DAY 21 — Student Data Visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ds=pd.read_csv('/content/day19_cleaned_students.csv')#<-- input: day19_cleaned_students.csv
ds['total_mark']=ds['Python']+ds['AI']+ds['Data_Structures']+ds['Maths']+ds['Database']
ds['average_mark']=ds['total_mark']/5

#1.Bar chart — Average marks per department
b1=plt.figure(figsize=(8, 5))
dept_marks = ds.groupby('Department')['average_mark'].mean()
b1=plt.bar(dept_marks.index,dept_marks.values,color=['blue','orange','green','red'])
b1=plt.title('Average_marks per department')
b1=plt.xlabel('Departments')
b1=plt.ylabel('Average_marks')
b1=plt.tight_layout()
b1=plt.savefig('/tmp/day21_dept_marks.png')
b1=plt.show()

#2.Bar chart — Student count per department
b2=plt.figure(figsize=(8, 5))
dept_count = ds.groupby('Department').size()
b2=plt.bar(dept_count.index,dept_count.values,color=['blue','orange','green','red'])
b2=plt.title('Student count per department')
b2=plt.xlabel('Departments')
b2=plt.ylabel('Student_count')
b2=plt.tight_layout()
b2=plt.savefig('/tmp/day21_dept_count.png')
b2=plt.show()

#3.Histogram — Distribution of average marks (how many students fall in each marks range)
h3=plt.figure(figsize=(8,5))
plt.hist(ds['average_mark'], bins=8, color='blue', edgecolor='black')
h3=plt.title('Distribution of Average marks')
h3=plt.xlabel('Average Marks')
h3=plt.ylabel('Number of Students')
h3=plt.tight_layout()
h3=plt.savefig('/tmp/day21_marks_distribution.png')
h3=plt.show()

#4.Bar chart — Average attendance per department
b4=plt.figure(figsize=(8,5))
dept_atten=ds.groupby('Department')['Attendance'].mean()
b4=plt.bar(dept_atten.index,dept_atten.values,color=['red','green','blue','yellow'],edgecolor='black')
b4=plt.title('Average Attendance Per Department')
b4=plt.xlabel('Department')
b4=plt.ylabel('Attendance %')
b4=plt.tight_layout()
b4=plt.savefig('/tmp/day21_dept_attendance.png')
b4=plt.show()

#5.Scatter plot — Study hours vs average marks (one dot per student)
sp5=plt.figure(figsize=(8,5))
sp5=plt.scatter(ds['Study_Hours_Per_Week'],ds['average_mark'],color='blue',label='Per Student')
sp5=plt.axhline(ds['average_mark'].mean(), color='red', linestyle='--', linewidth=2, label=f'Class Average : {ds['average_mark'].mean():.2f}')
sp5=plt.title('Study hours vs average marks')
sp5=plt.xlabel('Study hours per week')
sp5=plt.ylabel('Average marks')
sp5=plt.legend()
sp5=plt.tight_layout()
sp5=plt.savefig('/tmp/day21_study_vs_marks.png')
sp5=plt.show()

#6.Bar chart — Average marks by gender
b6=plt.figure(figsize=(8,5))
avg_g=ds.groupby('Gender')['average_mark'].mean()
b6=plt.bar(avg_g.index,avg_g.values,color=['blue','green'])
b6=plt.title('Average Marks by Gender')
b6=plt.xlabel('Gender')
b6=plt.ylabel('Average mark')
b6=plt.tight_layout()
b6=plt.savefig('/tmp/day21_gender_marks.png')
b6=plt.show()
