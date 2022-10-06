import random, sys, string

data = ['integer', 'real','character','string','boolean','date']


def integer():
    b = random.randint(0,sys.maxsize)
    return b

def real():
    b = random.expovariate(1)
    return b

def char():
    b = chr(random.randint(48,126))
    return b

def string():
    n = random.randint(0,10)
    b = 



    
print(data)
u = int(input("Select a data type from the list(from 0 to 5): "))

if u==0:
    print(integer())
elif u == 1:
    print(real())
elif u ==2:
    print(char())
elif u == 3:
    print(string())
elif u == 4:
    print(boolean())
else:
    print(date())




