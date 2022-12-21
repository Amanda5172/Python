vm=["water","soft drink","chocolate bar", "sandwich","ice cream"]
vp=["3.00","5.15","4.50","6.00","8.75"]

for i in range(len(vm)):
    print(f"{i} {vm[i]:<15} {vp[i]}")

c=int(input("Number of the item you wish to purchase: "))

ch=-1
m=float(input("Money: "))
ch=m-float(vp[c])

while ch<0:
    print("Insufficient money.")
    m=m+float(input("Money: "))
    ch=m-float(vp[c])

d=round(ch,2)
t=str(d).find('.')
r=str(m).find('.')

if len(str(d)[t+1::])<2:
    d=str(d)+'0'
if len(str(m)[r+1::])<2:
    m=str(m)+'0'
    
print()
print("Total money received:",m)
if ch!=0:
    print("Change:",d)

print("Please collect your %s."%vm[c])
