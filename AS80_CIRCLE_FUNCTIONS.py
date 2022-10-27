import #pi number place


def area(radius):
    a = radius * radius# * pi
    print("Area =", a)

def circumference(radius):
    c = 2 * radius# * pi
    print("Circumference =", c)

r = int(input())
area(r)
circumference(r)

