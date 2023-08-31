#try = 5 pts
#conversion = 2pts
#penalty = 3pts

t1=input("Team 1: ")
t2=input("Team 2: ")
print()

try1=0
try2=0
con1=0
con2=0
pen1=0
pen2=0

tgoal=0

while tgoal!="end":
    tgoal=input("Team name: ")
    if tgoal=="end":
        break
    tpoint=int(input("Points: "))
    print()
    if tgoal==t1:
        match tpoint:
            case 2:
                con1+=1
            case 3:
                pen1+=1
            case 5:
                try1+=1
    elif tgoal==t2:
        match tpoint:
            case 2:
                con2+=1
            case 3:
                pen2+=1
            case 5:
                try2+=1


score1=try1*5 + con1*2 + pen1*3
score2=try2*5 + con2*2 + pen2*3

print()
print(f"{'team':<10} {'score':<15} {'try':<20} {'conversion':<25} {'penalty':<30}")
print(f"{t1:<10} {score1:<15} {try1:<20} {con1:<25} {pen1:<30}")
print(f"{t2:<10} {score2:<15} {try2:<20} {con2:<25} {pen2:<30}")
