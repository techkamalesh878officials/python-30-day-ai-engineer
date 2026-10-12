#Day 22 ML
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer #for dataset from online
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
data=load_breast_cancer()
bc=pd.DataFrame(data.data, columns=data.feature_names)
bc['target']=data.target
x=bc.drop('target',axis=1)
y=bc['target']
print(f'''Dataset
-------
Shape          : {bc.shape}
Features       : {data.data.shape[1]}
\t{y.value_counts().to_string()}\t
Missing values : {bc.isnull().sum().sum()}
Duplicates     : {bc.duplicated().sum()}
''')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(f'''Split
-----
X_train        :{x_train.shape}
X_test         :{x_test.shape}
Y_train        :{y_train.shape}
Y_test         :{y_test.shape}
''')
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)
corr=bc.corr()['target'].abs().sort_values(ascending=False)
corr=corr.drop('target').head(5)
print(f"Before scaling - mean of feature 0 : {x_train.iloc[:, 0].mean():.2f}")
print(f"After scaling  - mean of feature 0 : {x_train_scaled[:, 0].mean():.2f}")
print(f'''\nCorrelation for target column : 
-------------------------------
{corr.to_string()}''')
