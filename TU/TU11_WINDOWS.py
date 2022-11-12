import tkinter
import random

window = tkinter.Tk()

Names = ["James","John","Mark","Rick","Matthew","Luke"]

def AssignedName():
     MyRandom = random.randint(0,5)
     
     name.configure(text="Name: " + str(Names[MyRandom]))

MyTitle = tkinter.Label(window, text="Random Name Picker",font="Georgia 16 bold")
MyTitle.pack()

MyButton = tkinter.Button(window, text="OK", command=AssignedName)
MyButton.pack()

name = tkinter.Label(window, font="Georgia 16 bold")
name.pack()

window.mainloop()

