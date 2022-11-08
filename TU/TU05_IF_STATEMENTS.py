#Exercise 1: Paste in the following code. What happens if you:

test = input("Is it raining? y/n ")
if test == "y":
    print("Oh dear, no football today!")
   
#a. Remove the indent - will not run
test = input("Is it raining? y/n ")
if test == "y":
print("Oh dear, no football today!")

#b. Type in a capital Y - does not return anything
test = input("Is it raining? y/n ")
if test == "y":
    print("Oh dear, no football today!")
    
#c. Change the "y" to "Y" - will only work if the user types in Y
test = input("Is it raining? y/n ")
if test == "Y":
    print("Oh dear, no football today!")


#Exercise 2
test = input("Is it raining? y/n ")
if test in ["y", "Y", "yes"]:
    print("Oh dear, no football today!")


#Exercise 3 - needs indentation
else:
print("Great we can play!")

#Corrected version:
test = input("Is it raining? y/n ")
if test in ["y", "Y", "yes"]:
    print("Oh dear, no football today!")
else:
    print("Great we can play!")


