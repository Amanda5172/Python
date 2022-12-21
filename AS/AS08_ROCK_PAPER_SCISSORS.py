import random
o=["rock","paper","scissors"]
p=int(input("Rock(1), paper(2), scissors(3): "))

c=random.randint(1,3)
print("Computer plays",o[c-1])

if p==3 and c==1:
    print("Computer wins!")
elif p==1 and c==3:
    print("You win!")
elif c>p:
    print("Computer wins!")
elif p>c:
    print("You win!")
elif p==c:
    print("It's a tie!")
    

