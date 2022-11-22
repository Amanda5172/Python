#Exercise 1
with open("rudyard.txt","r") as whole_file:
    print("Press enter to read the next lines.")
    for line in whole_file:
        print(line,end="")
        n = input()
        
#Exercise 2
c = input("Which poem do you want to read? 'If' or 'ma'am' ")

if c == "If":
    with open("rudyard.txt","r") as whole_file:
        print("Press enter to read the next lines.")
        for line in whole_file:
            print(line,end="")
            n = input()

elif c == "ma'am":
    with open("mam.txt","r") as whole_file:
        print("Press enter to read the next lines.")
        for line in whole_file:
            print(line,end="")
            n = input()
