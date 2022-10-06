import random, sys

data = ['integer', 'real','character','string','boolean','date']
n = int(input("Input a number from 0 to 5: "))


if n==0:
    b= random.randint(0,sys.maxsize)

elif n==1:
    b = random.expovariate(1)

elif n==2:
    r = [string.ascii_uppercase, string.ascii_lowercase]
    s = random.randint(0,1)
    if s = 0:
        b = string.ascii_uppercase
    b = r[s]


print(data[n])
print(b)
