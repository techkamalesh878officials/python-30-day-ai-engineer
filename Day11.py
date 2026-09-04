name=input("Enter your name : ")
tamil=int(input("Enter your tamil marks : "))
english=int(input("Enter your english marks : "))
java=int(input("Enter your java marks : "))
datasys=int(input("Enter your data systems marks : "))
ora=int(input("Enter your Oracle marks : "))
total=tamil+english+java+datasys+ora
avg=total/5
high=max(tamil,english,java,datasys,ora)
low=min(tamil,english,java,datasys,ora)
#status
if(tamil >=40 and english >=40 and java >=40 and datasys >=40 and ora >=40):
  sta="Pass :) Take it easy!"
else:
  sta="Fail :( listen!Try!correct!"
#performance
if(avg>=80):
  per='Excellent'
elif(avg >= 60):
  per='Good'
elif(avg >= 40):
  per='Average'
else:
  per='Needs Improvement'
#grade
if(avg >=80):
  gra='A'
elif(avg>=60):
  gra='B'
elif(avg>=40):
  gra='C'
else:
  gra='D'
print('='*40)
print(f"===== STUDENT PERFORMANCE ANALYZER =====")
print("Name             : ",name)
print("Tamil            : ",tamil)
print("English          : ",english)
print("Java             : ",java)
print("Data Systems     : ",datasys)
print("Oracle           : ",ora)
print('='*40)
print(f"Total           : {total}")
print(f"Average         : {avg}")
print(f"Highest         : {high}")
print(f"Lowest          : {low}")
print(f'Status          : {sta}')
print(f'Performance     : {per}')
print(f'Grade           : {gra}')
