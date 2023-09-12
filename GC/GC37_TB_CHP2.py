#Ex1
v = "All work and no play makes Jack a dull boy"

x = v.split()

for i in x:
    print(i,' ',end='')

#
print()
#Ex2
print()
print(6*(1-2))

#Ex3 - shows the error message 'invalid syntax'


#Ex4
print()
bruce=6
print(bruce + 4)


#Ex5
print()
P = 10000
n=12
r = 0.08
t = int(input("Number of years: "))

A = P*(1 + (r/n))**(n*t)
print(A)


#Ex6
print()
print(5%2) #1
print(9%5) #4
print(15%12) #3
print(12%15) #12
print(6%6) #0
print(0%7) #0
#print(7%0) #0 division error


#Ex7
print()
t = 14+51
c = 0
while t>12:
    t=t-12
    c=c+1

if c%2==0:
    print(t,"am")
else:
    print(t,"pm")
    
#Ex8
print()
curtim = int(input("Current time in hours: "))
waitim = int(input("Hours to wait: "))
t = curtim+waitim
c = 0
while t>12:
    t=t-12
    c=c+1

if c%2==0:
    print(t,"am")
else:
    print(t,"pm")
