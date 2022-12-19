p1=0
p2=0
c="y"

while c=="y":
    q1 = input("Enter your question for User 2: ")
    a1 = input("Enter your answer to that question: ")

    for i in range(50):
        print()

    q2 = input("Enter your question for User 1: ")
    a2 = input("Enter your answer to that question: ")


    print(q1)
    e1 = input("Enter your answer to that question: ")
    if e1==a1:
        print("Correct!")
        p2=p2+1

    for i in range(50):
        print()

    print(q2)
    e2 = input("Enter your answer to that question: ")
    if e2==a2:
        print("Correct!")
        p1=p1+1

    for i in range(50):
        print()

    c = input("Would you like to continue the game? y/n: ")

print("User 1 points:",p1)
print("User 2 points:",p2)
