import random

number = []
floor = int(input("Number of floors: "))
k = random.randint(1, floor)

for i in range(floor):
    while k in number:
        k = random.randint(1, floor)
    print("Floor",k)
    number.append(k)
