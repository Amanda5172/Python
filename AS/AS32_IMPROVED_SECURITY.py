import random

number = []
floor = int(input("Number of floors: "))

for i in range(floor):
    k = random.randint(1, floor)
    while k in number:
        k = random.randint(1, floor)
    print("Floor",k)
    number.append(k)
