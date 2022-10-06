import random, sys, string

data = ['integer', 'real','character','string','boolean','date']


def integer():
    b= random.randint(0,sys.maxsize)

def real():
    b = random.expovariate(1)

def char():
    return chr(random.randint(48,126))


    
print(data)
u = int(input("Select a data type from the list(from 0 to 5): "))

if u==0:
    integer()
elif u == 1:
    real()
elif u ==2:
    character()
elif u == 3:
    string()
elif u == 4:
    boolean()
else:
    date()





