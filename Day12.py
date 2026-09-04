#sales data analyzer
pq=int(input('Enter number of products : '))
quan={}
pname={}
price={}
rev={}
totq=0
totrev=0
high=0
low=0
tp=""
lp=""
avg=0
#input
for i in range(1,pq+1):
  pname[i]=input(f'\n{i} Enter product name : ')
  quan[i]=int(input(f'{i} Enter Quantity : '))
  price[i]=int(input(f'{i} Enter price per product : '))
  rev[i]=quan[i]*price[i]
  totq=totq+quan[i]
  totrev=totrev+rev[i]
  if high<=rev[i]:
    high=rev[i]
    tp=pname[i]
avg=totrev/pq
low = min(rev.values())
for key,value in rev.items():
  if value==low:
    lp=pname[key]
    break
  
print("=" * 70)
print("                    SALES DATA ANALYZER")
print("=" * 70)

print(f"{'S.No':<8}{'Product':<20}{'Quantity':<12}{'Price':<12}{'Revenue'}")
print("-" * 70)

for i in range(1, pq + 1):
    print(f"{i:<8}{pname[i]:<20}{quan[i]:<12}{price[i]:<12}{rev[i]}")

print("-" * 70)
print(f"Total Products    : {pq}")
print(f"Total Quantity    : {totq}")
print(f"Total Revenue     : ₹{totrev}")
print(f"Average Revenue   : ₹{avg:.2f}")
print(f"Highest Revenue   : ₹{high}")
print(f"Lowest Revenue    : ₹{low}")
print(f"Top Product       : {tp}")
print(f"Lowest Product    : {lp}")
print("=" * 70)
