import random


r1 =" should elaborate more."

r2 = " needs to write more points."

r3 = " has made excellent progress."

r4 = " has shown improvement."

r5 = " should give more relevant points."

r6 = ", well done!"

r7 = ", keep up the good work!"

r8 = " has room for improvement in the quality of work."


r = [r1,r2,r3,r4,r5,r6,r7,r8]

n = random.randint(0,7)

name = str(input("Student name: "))

print(name+r[n])
           
