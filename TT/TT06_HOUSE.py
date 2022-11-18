import turtle

turtle.speed(0)

def shape(n,s):
    for i in range(n):
      turtle.forward(s)
      turtle.left(360/n)

#house outline
turtle.pu()
turtle.goto(-150,-100)
turtle.pd()
shape(4,200)
turtle.pu()
turtle.goto(-170,100)
turtle.pd()
shape(3,240)

#window1
turtle.pu()
turtle.goto(-120,30)
turtle.pd()
shape(4,50)

turtle.pu()
turtle.goto(-115,35)
turtle.pd()
shape(4,17)

turtle.pu()
turtle.goto(-92,35)
turtle.pd()
shape(4,17)

turtle.pu()
turtle.goto(-115,57)
turtle.pd()
shape(4,17)

turtle.pu()
turtle.goto(-92,57)
turtle.pd()
shape(4,17)





#window2
turtle.pu()
turtle.goto(-30,30)
turtle.pd()
shape(4,50)

turtle.pu()
turtle.goto(-25,35)
turtle.pd()
shape(4,17)

turtle.pu()
turtle.goto(-2,35)
turtle.pd()
shape(4,17)

turtle.pu()
turtle.goto(-25,57)
turtle.pd()
shape(4,17)

turtle.pu()
turtle.goto(-2,57)
turtle.pd()
shape(4,17)

#door
turtle.pu()
turtle.goto(-75,-100)
turtle.pd()
turtle.lt(90)
turtle.fd(100)
turtle.rt(90)
turtle.fd(50)
turtle.rt(90)
turtle.fd(100)

turtle.pu()
turtle.goto(-70, -50)
turtle.pd()
turtle.circle(6)
