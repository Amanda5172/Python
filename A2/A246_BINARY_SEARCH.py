import random

r = random.randint(1,111)
#print(r)

def bs(top,bottom,find):
    global count
    count=0
    while bottom<=top:
        count=count+1
        middle = (top+bottom)//2
        if middle == find:
            return middle
        elif middle < find:
            bottom = middle + 1
        else:
            top = middle - 1
    return False


print(bs(111,1,r))
print(count)
