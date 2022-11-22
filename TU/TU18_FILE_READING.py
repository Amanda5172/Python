#Exercise 1
with open("rudyard.txt","r") as whole_file:
    print("Press enter to read the next lines.")
    for line in whole_file:
        print(line,end="")
        n = input()
