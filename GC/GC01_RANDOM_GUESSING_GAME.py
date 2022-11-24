import random
n = random.randint(1,100)

g=False
t = input("Guess an integer number from 1 to 100: ")

while g == False:
    if isinstance(t, str):
        x = t.isnumeric()
        
        if x==True and 0<int(t)<101 :
            
            if int(t) > n:
                t=input(("Guess lower: "))
            elif int(t) < n:
                t=input(("Guess higher: "))
            else:
                print("You got it!")
                g=True
                break
            
        else:
            print("Invalid guess.")
            t = input("An integer number from 1 to 100: ") 

    else:
        print("Invalid guess.")
        t = input("An integer number from 1 to 100: ")

    
