import random

r=random.randint(1,12)
t=random.randint(1,12)
w=r*t

a=int(input("%d x %d: " %(r,t)))

if a==w:
    print("Correct!")
else:
    print("Wrong.")
