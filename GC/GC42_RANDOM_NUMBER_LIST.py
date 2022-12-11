import random
a=[]
t=0

for i in range(50):
    n=random.randint(1,100)
    a.append(n)
    t=t+n

mi=min(a)
ma=max(a)
ave=t/50

print("Min:",mi)
print("Max:",ma)
print("Average:",ave)
