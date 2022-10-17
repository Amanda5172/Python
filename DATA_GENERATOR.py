import random, sys, string, datetime

data = ['integer', 'real','character','string','boolean','date']


def inte():
    b = random.randint(0,sys.maxsize)
    return b

def real():
    b = random.expovariate(1)
    return b

def char():
    b = chr(random.randint(48,126))
    return b

def stri():
    n = random.randint(5,20)
    b = ''.join(random.choice(string.ascii_letters) for i in range(n))
    return b

def bool():
    b = random.randint(1,2)
    return b==1

def date():
    y = random.randint(1600,2022)
    m = random.randint(0,12)
    d = random.randint(0,28)
    b = datetime.datetime(y, m, d)
    return b

    
print(data)
u = int(input("Select a data type from the list(from 0 to 5): "))

if u==0:
    print(inte())
elif u == 1:
    print(real())
elif u ==2:
    print(char())
elif u == 3:
    print(stri())
elif u == 4:
    print(bool())
else:
    print(date())




