#day25-model evaluation project
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression#model 1
from sklearn.tree import DecisionTreeClassifier#model 2
from sklearn.ensemble import RandomForestClassifier#model 3
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, auc
from sklearn.pipeline import make_pipeline
data = load_breast_cancer()
lbc = pd.DataFrame(data.data,columns=data.feature_names)
lbc['target'] = data.target
x=lbc.drop('target',axis=1)#independent variable
y=lbc['target']#dependent variable
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)#train_test_split process
models = {
    "Logistic Regression": LogisticRegression(random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),}
rows=[]
fitted={}
for name,model in models.items():
  pl=make_pipeline(StandardScaler(),model)
  pl.fit(x_train,y_train)
  y_pred=pl.predict(x_test)
  acc=accuracy_score(y_test,y_pred)
  cm=confusion_matrix(y_test,y_pred)
  scores=cross_val_score(pl,x,y,cv=5,scoring="accuracy")
  fitted[name] = pl
  rows.append({"Model":name,"CV Mean":round(scores.mean(),4),"CV Std":round(scores.std(),4),"Test Accuracy":f"{acc:.2%}"})
  print(f"Model   : {name}")
  print(f"Accuracy: {acc:.4f}")
  print(f"Mean CV : {scores.mean():.4f}")
  print(f"Std CV  : {scores.std():.4f}")
  print(f"Confusion Matrix:\n{cm}")
  print(f"Cross-Validation Scores:{scores}")
  print("-" * 80)
lr=fitted["Logistic Regression"]#ROC AUC (LR)
probs=lr.predict_proba(x_test)[:,1]
fpr,tpr,_=roc_curve(y_test,probs)
roc_auc=auc(fpr,tpr)
print(f"\nROC AUC [Logistic Regression]:{roc_auc:.4f}\n")
r_c=plt.figure(figsize=(6, 5))
r_c=plt.plot(fpr,tpr,label=f"AUC = {roc_auc:.4f}")
r_c=plt.plot([0,1],[0,1],'r--',label="Random guess")
r_c=plt.title("ROC curve - Logistic Regression")
r_c=plt.xlabel("False positive Rate")
r_c=plt.ylabel("True positive Rate")
r_c=plt.legend()
r_c=plt.tight_layout()
r_c=plt.savefig('/tmp/day25roc_curve.png')
r_c=plt.show()
rf=fitted["Random Forest"].named_steps['randomforestclassifier']# Feature importance(RF)
imp=pd.Series(rf.feature_importances_,index=x.columns).sort_values(ascending=False)
print("\nTop 5 feature importances(Random Forest)")
print("-----------------------------------------")
for f,v in imp.head(5).items():
    print(f"{f:<25}: {v:.4f}")
fibc=plt.figure(figsize=(8, 5))#bar chart
fibc=imp.head(10)[::-1].plot(kind='barh', color='red')
fibc=plt.title("Top 10 feature importances[Random Forest]")
fibc=plt.xlabel("Importance")
fibc=plt.tight_layout()
fibc=plt.savefig('/tmp/day25feature_importance.png')
fibc=plt.show()
print("\nFinal Comparison")# Final table
print("----------------")
print(pd.DataFrame(rows).to_string(index=False))
y_pred_lr=lr.predict(x_test)# Predictions from Logistic Regression(first 5)
y_test_reset=y_test.reset_index(drop=True)
print("\nPredictions (first 5) - Logistic Regression")
print("Sample  Actual  Predicted  Probability(benign)")
for i in range(5):
    print(f"{i+1:<8}{y_test_reset[i]:<8}{y_pred_lr[i]:<11}{probs[i]:.3f}")
print('Model evaluation concluded...')
