Use a 2d array to create a playlist system for 10 artists with 10 songs each. 

Your algorithm will create a random order for the songs, 
with the bands having a minimum distance of 2 songs. i.e. you can't play the same band again until 2 songs have passed. 
(You do not have to play EVERY song in the system, just 20 is enough.)





import random

b = [["A1", 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']]

m = 1
for i in range(10):
    b.append([m,m,m,m,m,m,m,m,m,m])
    m=m+1
print(b)



#have to choose from[0][n]
#then choose [m][n]

l = []
#playlist

p = []
#p to make sure the artist does not repeat

for x in range(20):
    a = random.randint(0,9)
    o = random.randint(0,9)
    
    p.append(a)
    while a == p[x-1] or p[x-2]:
        a = random.randint(0,9)
    
    l.append([b[0][a],b[o][a]])

#for the different artist, use another list?, p, append, check if a == p[n-1] or p[n-2]


print(l)
