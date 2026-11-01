#day-24 classification project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.datasets import load_breast_cancer#dataset from online
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression#model 1
from sklearn.tree import DecisionTreeClassifier#model 2
from sklearn.ensemble import RandomForestClassifier#model 3
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
data = load_breast_cancer()
lbc = pd.DataFrame(data.data,columns=data.feature_names)
lbc['target'] = data.target
x=lbc.drop('target',axis=1)#independent variable
y=lbc['target']#dependent variable
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)#train_test_split process
target_counts = Counter(data.target)#for classes
clas=f"Classes : {data.target_names[0]}={0} ({target_counts[0]}), {data.target_names[1]}={1} ({target_counts[1]})"
print('Day24 ML-classification project')
print(f'''
Dataset
-------
Shape   : {data.data.shape}
{clas}''')
#standardization
ss=StandardScaler()
x_train_s=ss.fit_transform(x_train)
x_test_s=ss.transform(x_test)
#ML-LogisticRegression
lr_model=LogisticRegression()
lr_model.fit(x_train_s, y_train)
y_pred=lr_model.predict(x_test_s)
lr_accuracy=accuracy_score(y_test,y_pred)
cm=confusion_matrix(y_test,y_pred)
print()
print(f'''
1.Logistic Regression
---------------------
Accuracy : {lr_accuracy:.2%}
Confusion Matrix:
{cm}''')
print(f'''
1.Predictions (first 5)
-----------------------
Sample  Actual    Predicted''')
#to print actual vs predictions values
y_test_reset = y_test.reset_index(drop=True)
for i in range(5):
    print(f"{i+1:<8} {y_test_reset[i]:<10.1f} {y_pred[i]}")

report = classification_report(y_test, y_pred)
print(f'\n1.Classification Report:\n{'-'*24}\n{report}')
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Class 0', 'Class 1'])
disp.plot(cmap=plt.cm.Blues)
disp=plt.title("1.Logistic Regression's confussion matrix")
plt.show()
#DecisionTreeClassifier
dt_model=DecisionTreeClassifier(random_state=42)
dt_model.fit(x_train_s, y_train)
y_pred1=dt_model.predict(x_test_s)
dt_accuracy=accuracy_score(y_test,y_pred1)
cm=confusion_matrix(y_test,y_pred1)
print()
print(f'''
2.Decision Tree
---------------
Accuracy : {dt_accuracy:.2%}
Confusion Matrix:
{cm}''')
print(f'''
2.Predictions (first 5)
-----------------------
Sample  Actual    Predicted''')
#to print actual vs predictions values
y_test_reset = y_test.reset_index(drop=True)
for i in range(5):
    print(f"{i+1:<8} {y_test_reset[i]:<10.1f} {y_pred1[i]}")

report = classification_report(y_test, y_pred1)
print(f'\n2.Classification Report:\n{'-'*24}\n{report}')
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Class 0', 'Class 1'])
disp.plot(cmap=plt.cm.Greens)
disp=plt.title("2.Decision Tree's confussion matrix")
plt.show()
#randomforestclassifier
rft_model=RandomForestClassifier()
rft_model.fit(x_train_s,y_train)
y_pred2=rft_model.predict(x_test_s)
rft_accuracy=accuracy_score(y_test,y_pred2)
cm=confusion_matrix(y_test,y_pred2)
print()
print(f'''
3.Random Forest Tree
--------------------
Accuracy : {rft_accuracy:.2%}
Confusion Matrix:
{cm}''')
print(f'''
3.Predictions (first 5)
-----------------------
Sample  Actual    Predicted''')
#to print actual vs predictions values
y_test_reset = y_test.reset_index(drop=True)
for i in range(5):
    print(f"{i+1:<8} {y_test_reset[i]:<10.1f} {y_pred2[i]}")

report = classification_report(y_test, y_pred2)
print(f'\n3.Classification Report:\n{'-'*24}\n{report}')
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Class 0', 'Class 1'])
disp.plot(cmap=plt.cm.Grays)
disp=plt.title("3.Random Forest Tree's confussion matrix")
plt.show()
#model comparison
if lr_accuracy > dt_accuracy and lr_accuracy > rft_accuracy:
  win='Logistic Regression'
elif dt_accuracy > lr_accuracy and dt_accuracy > rft_accuracy:
  win='Decision Tree'
else:
  win='Random Forest Tree'
print(f'''
Model Comparison
----------------
Logistic Regression : {lr_accuracy:.2%}
Decision Tree       : {dt_accuracy:.2%}
Random Forest Tree  : {rft_accuracy:.2%}
Winner              : {win}''')
