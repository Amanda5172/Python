item = int(input())
position = 0
found = False
myarray=[5,2,8,4]

while position < len(myarray) and found == False:
    if myarray[position] == item:
        found = True
        print("Found it at position", position)
    else:
        position = position + 1

if found == False:
    print("Can't find it!")
