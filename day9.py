#AI skill analyser
name1=input("Enter your Name : ")
py=int(input("Enter your python level (1/2/3): "))
studyh1=int(input("Enter study hour (1 to 10) : "))
exp1=int(input("Enter your Experience in years: "))
#logic
if(py==1):
  py1=("Beginner")
  if(studyh1<=5):
    rc="Focus on Python fundamentals."
  else:
    rc=' Great! Continue Python and start problem solving.'
elif(py==2):
  py1=("Intermediate")
  rc='Start NumPy, Pandas and basic ML.'
elif(py==3):
  py1=("Advanced")
  rc='Start machine learning projects.'
else:
  py1=("Invalid please Enter appropirate options in python level !")
if(studyh1>=1 and studyh1<=5):
  re=("Keep improving your consistency!")
elif(studyh1>=6 and studyh1<=10):
  re=(" Great dedication! 🔥")
else:
  re=("Invalid please Enter appropirate options in study hours !")

#output:
print()
print('='*40)
print(f"===== AI SKILL ANALYZER =====")
print("Name: ",name1)
print("Level: ",py1)
print("Study Hours: ",studyh1)
print(f"Experience: {exp1} years")
print('='*40)
print('\t===== RECOMMENDATION =====')
print('='*40)
print(f"\n\n{rc}\n\n")

print('='*40)
print(f"\nReview : {re}\n")
print("Keep learning! 🚀")
print('='*40)
