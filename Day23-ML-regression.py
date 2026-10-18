#day 23 regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
data = load_diabetes()
rds = pd.DataFrame(data.data,columns=data.feature_names)
rds['target'] = data.target
x=rds.drop('target',axis=1)#independent variable
y=rds['target']#dependent variable
print(f'''
Dataset
-------
Shape    : {data.data.shape}
Target   : \n{y.describe().to_string()}''')
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
print(f'''
Split
-----
X_train  : {x_train.shape}
X_test   : {x_test.shape}
Y_train  : {y_train.shape}
Y_test   : {y_test.shape}''')
#standardization
ss=StandardScaler()
x_train_s=ss.fit_transform(x_train)
x_test_s=ss.transform(x_test)
#ML-regression
model=LinearRegression()
model.fit(x_train_s, y_train)
y_pred = model.predict(x_test_s)
#ml-metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'''
Model Results
-------------
MAE      : {mae:.2f}
MSE      : {mse:.2f}
RMSE     : {rmse:.2f}
R² Score : {r2:.2f}''')
print(f'''
Predictions (first 5)
---------------------
Sample  Actual    Predicted''')
#to print actual vs predictions values
y_test_reset = y_test.reset_index(drop=True)
for i in range(5):
    print(f"{i+1:<8} {y_test_reset[i]:<10.1f} {y_pred[i]:.2f}")
print()
#to scatter plot actual vs pred
plt.scatter(y_test,y_pred)
mn = y_test.min()
mx = y_test.max()
plt.plot([mn, mx], [mn, mx], color='red', linestyle='--')
plt.title('Actual vs Predicted')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.tight_layout()
plt.savefig('/tmp/day23_actual_vs_pred.png')
plt.show()
