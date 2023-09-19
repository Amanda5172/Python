i = input("List(eg. 1 2 3): ")
i = i.split()

l=[]

l.append(int(i[0]))
l.append(int(i[len(i)-1]))

print(l)
