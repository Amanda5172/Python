import random

a = input("Confess or stay silent(c/s): ")
b = random.randint(0,1)
#0 is c, 1 is s



if a=='c' and b==0:
    print("Both chose to confess. 5 years in jail for both.")
elif a=='c' and b==1:
    print("Prisoner A confessed, while Prisoner B stayed silent. Prisoner A is released, but Prisoner B will remain  20 years in jail")
elif a=='s' and b==0:
    print("Prisoner B confessed, while Prisoner A stayed silent. Prisoner B is released, but Prisoner A will remain  20 years in jail")
elif a=='s' and b==1:
    print("Both chose to stay silent. 1 year in jail each.")
