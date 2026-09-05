#EXPENSE TRACKER

nex=int(input('Enter no.of Expense : '))
ename={}
tot=0
hex=0
lex=0
eavg=0
te=''
le=''
eamou={}
plel=''
#input
if(nex>=3 and nex<=10):
 for i in range(1,nex+1):
   ename[i]=input(f'\n{i}) Enter Name: ')
   eamou[i]=int(input(f"{i}) Enter Amount: "))
   tot=tot+eamou[i]
   if(hex<=eamou[i]):
     hex=eamou[i]
     te=ename[i]
   eavg=tot/nex
   
 lex=min(eamou.values())
 for key,value in eamou.items():
   if value==lex:
     le=ename[key]
     break


 if(tot>=2000):
   plel='High Spending'
 elif(tot>=1000):
   plel='Moderate Spending'
 elif(tot>=500):
   plel='Normal Spending'
 else:
   plel='Low Spending'
#output
 print('========================================')
 print('             EXPENSE TRACKER')
 print('========================================')

 print(f"{'S.No':<8}{'Expanse Name':<16}{'Amount':<12}")
 for i in range(1,nex+1):
     print(f"{i:<8}{ename[i]:<12}:   {eamou[i]:<12}")
 print()
 print('-'*40)
 print(f'Total Spending   : ₹{tot}')
 print(f'Average Expense  : ₹{eavg}')
 print(f'Highest Expense  : ₹{hex}')
 print(f'Lowest Expense   : ₹{lex}')
 print(f'No. of Expenses  : {nex}')
 print(f"Highest Item     : {te}")
 print(f"Lowest Item      : {le} ")#
 print(f"Spending Level   : {plel}")
 print('='*40)
else:
  print('Invalid!, No.of Expense is must between 3 to 10')
