#Log analyzer
log=int(input("How many logs? "))
lname={}
lsta={}
lerr={}

su={}
fen={}
ec={}
sc=0
fc=0
scr=0
fcr=0
mcerr=''
tsu=''
#i/p
for i in range(1,log+1):
  lname[i]=input(f'\n{i})Enter user name : ')
  lsta[i]=int(input(f'{i})Enter Status (1.Success/2.Fail) in numbers : '))

  if lsta[i]==2:
    fc=fc+1
    lerr[i]=input(f'{i})Enter Error name : ')
    
    err=lerr[i]

    if err in ec:
            ec[err] = ec[err] + 1
    else:
            ec[err] = 1

  elif lsta[i]==1:
        sc = sc + 1
        user = lname[i]

        if user in su:
            su[user] = su[user] + 1
        else:
            su[user] = 1
  else:
    print('Please enter correctly')

if su:
    max_success = max(su.values())

    for user, count in su.items():
        if count == max_success:
            tsu = user
            break

if ec:
    max_error = max(ec.values())

    for err, count in ec.items():
        if count == max_error:
            mcerr = err
            break

scr=(sc/log)*100
fcr=(fc/log)*100
#o/p
print('='*50)
print('           LOG ANALYZER')
print('='*50)
print(f'Total Entries       : {log}')
print(f'Successful          : {sc}')
print(f'Failed              : {fc}')
print(f'Success Rate        : {scr}')
print(f'Failure Rate        : {fcr}')
print(f'Most Common Error   : {mcerr}')
print(f'Top Successful User : {tsu}')
print('='*50)
