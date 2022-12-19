t=input("Enter the time(eg,05:30, 14:06): ")

m = int(t[0:2])

a = m+51
k=0

while a>24:
    a=a-24
    k=k+1

if a<10:
    l=str("0"+str(a)+t[2:5])
elif a==24:
    l=str("00"+t[2:5])
else:
    l=str(str(a)+t[2:5])

print("Set alarm for",k,"days later at", l)
