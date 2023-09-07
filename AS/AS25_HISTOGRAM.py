his = input()

for i in his:
    if i.isdigit()==True:
        for j in range(int(i)):
            print('*',end='')
        print()
