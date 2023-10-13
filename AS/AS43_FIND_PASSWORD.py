j=[]
with open("cia_agent.txt","r") as ef:
    for i in ef:
        j.append(i)

k=[]
for i in j:
    for x in i:
        if x.isalpha()==True:
            k.append(x)

def top():
    d=0
    for p in range(len(k)):
        c=k.count(k[p])
        if c>d:
            d=c
            f=k[p]
            return f

def bottom():
    d=50
    for p in range(len(k)):
        c=k.count(k[p])
        if c<d:
            d=c
            f=k[p]
    return f

print("Top 3 letters: ")
for e in range(3):
    r=top()
    k.remove(r)
    print(e,r)

print("Bottom 3 letters:")
for w in range(3):
    r=bottom()
    k.remove(r)
    print(w,r)
