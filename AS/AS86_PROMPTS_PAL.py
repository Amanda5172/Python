import random

with open("promptspal.txt","r") as ef:
    t = ef.readlines()
    i = random.randint(0,len(t)-1)
    print(t[i])
