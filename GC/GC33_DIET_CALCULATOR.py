cap = 2500
total = 0

food=0
print("Calories to consume: ", cap-total)
print()

food = input("Name of food: ")

while food!="stop":
    r=False
    while r==False:
        try:
            cal = float(input("Amount of calories: "))
            r=True
            total = total + cal
        except ValueError:
            r=False
    print("Calories to consume: ", cap-total)
    print()
    food = input("Name of food: ")
    if food == "end day":
        total=0
        print()
        print("Calories to consume: ", cap-total)
        print()
        food = input("Name of food: ")
    
