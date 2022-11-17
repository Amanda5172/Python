running = ["Alice", "Bob", "Charlie"]

ballot = []
choice1 = []
choice2 = []
choice3 = []

print("./runoff Alice, Bob, Charlie")
n = int(input("Number of voters: "))

for r in range(n):
    print("")
    c1 = str(input("Rank 1: "))
    choice1.append(c1)
    c2 = str(input("Rank 2: "))
    choice2.append(c2)
    c3 = str(input("Rank 3: "))
    choice3.append(c3)

ballot.append(choice1)
ballot.append(choice2)
ballot.append(choice3)

print("")

#runoff code
vote1 = 0

for v in range(len(ballot)):
    running = ["Alice", "Bob", "Charlie"]
    acount = ballot[vote1].count('Alice')#needed to use '' here instead of "" because the array input was with ''
    bcount = ballot[vote1].count('Bob')
    ccount = ballot[vote1].count('Charlie')

    counts = []
    counts.append(acount)
    counts.append(bcount)
    counts.append(ccount)

    if acount > len(ballot[vote1])/2:
        print("Alice")
        break

    elif bcount > len(ballot[vote1])/2:
        print("Bob")
        break

    elif ccount > len(ballot[vote1])/2:
        print("Charlie")
        break

    else:
        elim=[]
        for i in range(len(counts)):
            if counts[i] == min(counts):
                elim.append(i)
        if 0 in elim :
            #print("Alice is eliminated")
            running.remove("Alice")
            for r in range(len(ballot[vote1])):
                if ballot[vote1][r] == "Alice":
                    ballot[vote1][r] = ballot[v+1][r]
        if 1 in elim:
            #print("Bob is eliminated")
            running.remove("Bob")
            for r in range(len(ballot[vote1])):
                if ballot[vote1][r] == "Bob":
                    ballot[vote1][r] = ballot[v+1][r]
        if 2 in elim:
            #print("Charlie is eliminated")
            running.remove("Charlie")
            for r in range(len(ballot[vote1])):
                if ballot[vote1][r] == "Charlie":
                    ballot[vote1][r] = ballot[v+1][r]

    if len(running)==1:
        print(running[0])
        break
    elif len(running)==0 and v==len(ballot):
        print("Tie")
        break
        
