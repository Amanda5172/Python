w = input()
nw=''

#ordinary word to code
def addo(wp):
    wp=str(wp+'o'+wp)
    print(wp)
    return wp

for i in range(len(w)-1):
    if w[i] not in ['a','e','i','o','u']:
        if w[i+1] not in ['a','e','i','o','u']:
            p=str(w[i]+w[i+1])
            r=addo(p)
            nw=str(nw+str(r))
        elif w[i-1] not in ['a','e','i','o','u'] and i!=0:

        else:
            p=str(w[i])
            print(p)
            r=addo(p)
            nw=str(nw+str(r))
    else:
        nw=str(nw+w[i])


print(nw)
