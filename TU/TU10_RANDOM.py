#Exercise 1
import random

mynumber = random.uniform(0.1, 9.9)
print(mynumber)

#Exercise 2
import random
Choose_Name = ["James","John","Mark","Rick","Matthew"]
for i in range(1,5):
    chosen = random.choice(Choose_Name)
    print("Do you want to keep", chosen, "in the list? y/n: ")
    r = input()
    if r =="n":
        Choose_Name.remove(chosen)
print(Choose_Name)

