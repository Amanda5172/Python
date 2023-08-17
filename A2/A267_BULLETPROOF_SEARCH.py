#not done
import random

r = random.randint(1,111)

l=[]

for i in range(1,100):
    l.append(i)

def bs(listname,top,bottom,find):
    while bottom<=top:
        middle = (top+bottom)//2
        if middle == find:
            return middle
        elif middle < find:
            bottom = middle + 1
        else:
            top = middle - 1
    return False

def sort(listname):
    pass
    #idk what sort

if bs(l,0,100,r) == False:
    sort(l)
    if bs(l,0,100,r)==False:
        print("item not in")
