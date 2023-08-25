import random

l = []
for i in range(9):
    r = random.randint(1,100)
    l.append(r)

print("initial list:",l)
ls=l
ls.sort()
print("check:",ls)

for cpointer in range(1,9):
    temp = l[cpointer]
    pointer = cpointer - 1
    t=False
    while l[pointer] > temp and pointer>=0:
        #print(l[pointer],temp)
        l[pointer+1]=l[pointer] 
        pointer=pointer-1
        t=True
    if t==True:
        l[pointer+1]=temp
    #print(l)

print("sorted list:",l)




