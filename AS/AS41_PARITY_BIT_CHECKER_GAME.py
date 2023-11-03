import random

one=0
p=""
for k in range(7):
    i = bool(random.getrandbits(1))
    if i==True:
        p=p+"1"
        one = one+1
    else:
        p=p+"0"

if one%2==0:
    cor = "even"
else: cor="odd"

k = random.randint(1,2)
if k ==1: #even
    if one%2==0:
        cor = 0
    else: cor=1
else:
    if one%2==0:cor = 1
    else: cor= 0
    
if k==1: print("Use even parity:", p)
else: print("Use odd parity:", p)
ans=int(input("Parity bit? "))

if ans == cor:
    print("Correct.")
else:
    print(f"Wrong. Correct answer is {cor}.")
