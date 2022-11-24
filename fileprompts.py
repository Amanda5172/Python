import random
c=0

with open("promptspal.txt","r") as ef:
    t = len(ef.readlines())
    print(t)
    i = random.randint(1,t)
    for line in ef:
        if c==i:
            print(line)
        c = c+1
