
mylist = [1,4,6,2]

i = 0

while i<len(mylist):
    if mylist[i]>mylist[i+1]:
        t=mylist[i]
        mylist[i]=mylist[i+1]
        mylist[i+1]=t
    i=i+1

print(list)
