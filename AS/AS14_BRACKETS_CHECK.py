w=input()
c=0
t=0

for i in w:
    if i == "(":
        c=c+1
    if i ==")":
        t=t+1

r=t-c
e=c-t

if c==t:
    print("No missing brackets!")
elif c>t:
    print("Missing %d ')'s" %e)
elif t>c:
    print("Missing %d '('s" %r)
