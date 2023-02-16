#Create demo code to demonstrate the ideas of: sequence, selection, repetition & variable.

#sequence
x=int(input("input a number: "))
x=x+2
y= int(input("what is two more than that number? "))

#variable
z = False

#repetition
while z==False:
    #selection
    if y != x:
        print("wrong")
        y= int(input("what is two more than that number? "))
        z=False
    else:
        print("correct")
        z=True

