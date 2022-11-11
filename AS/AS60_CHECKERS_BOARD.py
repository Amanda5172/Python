n = int(input())
m = int(input())

b = []

for i in range(n):
    g=[]
    if i % 2 == 0:
        for j in range (m):
            if j % 2 == 0:
                l = "."
            else:
                l = "*"
            g.append(l)
    else:
        for j in range (m):
            if j % 2 == 0:
                l = "*"
            else:
                l = "."
            g.append(l)  
    b.append(g)
            
print(b)


#n rows, m columns
