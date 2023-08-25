import random

r = random.randint(1,111)
print(r)

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

if bs(l,100,0,r) == False:
    l.sort()
    if bs(l,100,0,r)==False:
        print("item not in")
    else:
        print("found")
else:
    print("found")
