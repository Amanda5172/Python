import random

mylist = []

for t in range(1,9):
    z = random.randint(1,30)
    mylist.append(z)

j = 1

while j <len(mylist):
    i=0
    while i < len(mylist)-1:
        if mylist[i] > mylist[i+1]:
            t= mylist[i]
            mylist[i]= mylist[i+1]
            mylist[i+1] = t
        i=i+1
    j=j+1
     
print(mylist)

#Extension = len(mylist) - 1
