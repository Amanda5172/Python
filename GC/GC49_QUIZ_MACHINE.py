import random
import time

digits = int(input("What is the maximum number of digits to work with? "))
tim = int(input("Seconds before answer is revealed: "))

op = [' + ',' - ',' * ',' / ']
num = []
ope = []
ran = random.randint(2,digits)

for i in range(ran):
    r = random.randint(1,100)
    num.append(r)
    o = random.randint(0,3)
    ope.append(o)

pri = ""

for k in range(len(num)):
    pri = pri + str(num[k])
    if k!=len(num)-1:
        pri = pri + str(op[ope[k]])

print()
print("Question:",pri)

time.sleep(tim)

print("Answer:",eval(pri))

