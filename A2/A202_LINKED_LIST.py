#2 1d arrays, one for element, one for pointers
#null pointer points to -1

ele=["a","b","c","d"]
point=[1,3,-1,2]
start=0

def printlist(ele, point,i):
    while i!=-1:
        print(ele[i],end="")
        i = point[i]
    print()

def find(ele,point,i,fin):
    try: 
        while ele[i]!=fin:
            i=i+1
    except:
        i=-1
        
    return i

#print(find(ele,point,start,"c"))

def dell(ele,point,i,fin):
    index = find(ele,point,i,fin)
    
    try:
        before = point.index(index)
        if point[index]==-1:
            point[before]=-1
        else:
            point[before]=point[index]
    except:
        i=point[index]

    return ele, point,i


def add(ele,point,i,fin,ind):
    length = len(ele)
    ele.append(fin)
    s=i


    if ind<length:
        num=1
        while num!=ind:
            s = point[s]
            num=num+1
        point.append(point[s])
        point[s]=length
        
    elif ind==0:
        i=length
        point.append(0)
    else:
        last=point.index(-1)
        point[last]=length
        point.append(-1)
        
    return ele, point, i
        


printlist(ele,point,start)

l1=dell(ele,point,start,"b")
printlist(l1[0],l1[1],l1[2])

l2=add(ele,point,start,"b",1)
printlist(l2[0],l2[1],l2[2])


