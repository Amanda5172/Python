# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

nume = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
numb = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

I = 0
V = 0
X = 0
L = 0
C = 0
D = 0
M = 0

i = 12


num = input("Number: ")

if num.isdigit() == True:
    num = int(num)
    while num:
        div = num//numb[i]
        num = num%numb[i]

        while div:
            print(nume[i], end="")
            div = div - 1
        i = i-1
else:
    tot = 0
    while num:
        try:
            j = nume.index(num[0:2])
            num = num[2::]
        except ValueError:
            j = nume.index(num[0])
            num = num[1::]
        tot = tot + numb[j]
    print(tot)













