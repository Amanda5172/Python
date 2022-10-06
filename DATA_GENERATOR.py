import random, sys

data = ['integer', 'real','character','string','boolean','date']
n = int(input("Input a number from 0 to 5: "))


if n==0:
    b= random.randint(0,sys.maxsize)

elif n==1:
    b = random.expovariate(1)

print(data[n])
print(b)
