# I = 1
# V = 5
# X = 10
# L = 50
# C = 100

# divide by 100, 90, 50, 40, 10, 9, 5, 4, 1

nume = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C"]
numb = [1, 4, 5, 9, 10, 40, 50, 90, 100]

I = 0
V = 0
X = 0
L = 0
C = 0


for j in range(101):
    i = 8
    
    while j:
        div = j // numb[i]
        j = j % numb[i]
     
        while div:
            print(nume[i], end = "")
            div = div - 1
        i = i - 1

    print()
