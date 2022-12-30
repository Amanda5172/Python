
def addo(wp):
    wp=str(wp+'o'+wp)
    return wp

def encode(w):
    j=[]
    nw=''
    for i in range(len(w)):
        if w[i] in ['a','e','i','o','u',' ']:
            j.append(i)

    for i in range(len(w)):
        if i in j:
            if j.index(i)==0:
                k=addo(w[0:i])
                nw=nw+k
                nw=nw+w[i]
            if j.index(i)<len(j)-1:
                if i+1<j[j.index(i)+1]:
                    k=addo(w[i+1:j[j.index(i)+1]])
                    nw=nw+k
                    nw=nw+w[j[j.index(i)+1]]
                else:
                    nw=nw+w[j[j.index(i)+1]]
            if j.index(i)==len(j)-1 and i!=len(w)-1:
                k=addo(w[i+1::])
                nw=nw+k
        
    return nw
