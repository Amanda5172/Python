#Use a 2d array to create a playlist system for 10 artists with 10 songs each. 

#Your algorithm will create a random order for the songs, 
#with the bands having a minimum distance of 2 songs. i.e. you can't play the same band again until 2 songs have passed. 
#(You do not have to play EVERY song in the system, just 20 is enough.)


import random

b = [["A1", 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']]

m = 1
for i in range(10):
    b.append(['S'+str(m),'S'+str(m),'S'+str(m),'S'+str(m),'S'+str(m),'S'+str(m),'S'+str(m),'S'+str(m),'S'+str(m),'S'+str(m)])
    m=m+1
print(b)


l = []
p = []

for j in range(20):
    a = random.randint(0,9)
    o = random.randint(1,9)
    
    if j<2:
        p.append(a)
        
    elif j<2:
        x = j - 1
        
        while a == p[x]:
            a = random.randint(1,5)
            
        p.append(a)
        
    else:
        x = j - 1
        y = j - 2
        
        while a == p[x] or a == p[y]:
            a = random.randint(1,5)
            
        p.append(a)

    l.append([b[0][a],b[o][a]])

print()
print("Playlist: ",l)


