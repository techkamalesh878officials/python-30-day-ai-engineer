print('='*40)
print("Ai Engineer Entry")
print('='*40)
#user
name=input("Enter your name : ")
py=int(input("Enter your python level(1/2/3) : "))
studyh=int(input("Enter study hours (1 to 10): "))
exp=int(input("Enter your years of exp in company : "))
print('='*40)
#logic
if(py==1):
  lve="Beginner"
elif(py==2):
  lve="Intermediate"
elif(py==3):
  lve="Advanced"
else:
  print("invalid !")
if(studyh>=5):
  sty="Great dedication! 🔥"
else:
  sty="Keep improving your consistency!"
#o/p
print()
print('='*40)
print(f"===== AI ENGINEER PROFILE =====")
print("Name: ",name)
print("Level: ",lve)
print("Study Hours: ",studyh,"hours/day")
print(f"Experience: {exp} years")
print(f"\nreview : {sty}\n")
print("Keep learning! 🚀")
print('='*40)
