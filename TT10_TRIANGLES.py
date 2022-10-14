import turtle

def triangle(x,y,sz):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(3):
        turtle.forward(sz)
        turtle.left(120)
        
for y in range (-100,100,20):
    for x in range (-100,100,20):
        triangle(x,y,10)

