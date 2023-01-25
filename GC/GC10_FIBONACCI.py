fi = []

a=0
n=int(input("How many numbers would you like? "))

for i in range(n):
    fi.append(a)
    if i<1:
        a=a+1
    else:
        b=fi[i-1]
        c=fi[i]
        a=b+c


print(fi)
