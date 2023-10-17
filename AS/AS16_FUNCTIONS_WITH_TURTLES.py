import turtle

wn = turtle.Screen()      
wn.bgcolor("lightgreen")
t = turtle.Turtle()
t.pencolor("pink")
t.width(5)
t.speed(-1)


#Exercise 1

def square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

for i in range(5):
    square(t, 25)
    t.pu()
    t.fd(40)
    t.pd()

    
#Exercise 2
t.goto(0,0)
t.setheading(0)
t.clear()

w = 20

for i in range(5):
    square(t,w)
    t.pu()
    t.goto(0-w/2,0-w/2)
    t.pd()
    w=w+20


#Exercise 3
t.goto(0,0)
t.setheading(0)
t.clear()


def poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

poly(t, 8, 50)


#Exercise 4
t.goto(0,0)
t.setheading(0)
t.clear()
t.width(2)

for i in range(20):
    square(t,30)
    t.lt(360/20)
    

#Exercise 5
t.goto(0,0)
t.setheading(0)
t.clear()
s=10

for i in range(20):
    s=s+10
    t.fd(s)
    t.lt(90)

t.goto(0,0)
t.setheading(0)
t.clear()
s=10

for i in range(50):
    s=s+5
    t.fd(s)
    t.lt(95)


#Exercise 6
t.goto(0,0)
t.setheading(0)
t.clear()

def equitriangle(t, sz):
    for i in range(3):
        t.forward(sz)
        t.left(120)

equitriangle(t,50)


#Exercise 7
def sum_to_n(n):
    t=0
    for i in range(1,n+1):
        t = t+i
    return t

print(sum_to_n(10))


#Exercise 8
import math

def area_of_circle(r):
    area = 2 * math.pi * (r**2)
    return area

print(area_of_circle(3))


#Exercise 9
t.goto(0,0)
t.setheading(0)
t.clear()

def star(s):
    for i in range(5):
        t.fd(s)
        t.rt(144)

star(100)


#Exercise 10
t.goto(0,0)
t.setheading(0)
t.clear()

for j in range(5):
    star(100)
    t.pu()
    t.fd(350)
    t.rt(144)
    t.pd()
