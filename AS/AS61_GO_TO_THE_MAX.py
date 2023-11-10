l = input()
l=l.split()

k=input()
t=k.split()
largest = int(t[0])
row=0
col=0

for j in range(len(t)):
    if int(t[j])>largest:
        largest=int(t[j])
        col=j
        row=0


for i in range(int(l[0])-1):
    k=input()
    t=k.split()
    
    for j in range(len(t)):
        if int(t[j])>largest:
            largest=int(t[j])
            col=j
            row=i+1
        elif int(t[j])==largest:
            if j==col and i<row:
                row=i
            elif row==i and j<col:
                    col=j


print(row, col)
