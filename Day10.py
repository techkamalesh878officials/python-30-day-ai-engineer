#python code for number analysis
num=int(input('enter a value between (1 to 1000) : '))
if(num%2==0):
    ty=("Type : Even ")
elif(num%2!=0):
    ty=("Type : Odd")
if(num>=0):
    st=("Status : Positive")
elif(num<0):
    st=("Status : Negative")
if(num%5==0):
    dv=("Divisble by 5 : Yes")
elif(num%5!=0):
    dv=("Divisble by 5 : No")
if(num>100):
    gr=("Greater than 100 : yes")
elif(num<=100):
    gr=('Greater than 100 : No')

if(num>=-5 and num<=1000):
  print(ty)
  print(st)
  print(dv)
  print(gr)
else:
 print("Re-enter the number!")
