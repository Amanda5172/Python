import turtle

turtle.bgcolor("blue")

turtle.speed(0)

for i in range(300,-300,-10):
    turtle.penup()
    turtle.goto(-400,i)
    turtle.pendown()
    turtle.forward(600)
    
#y-axis
for i in range(300,-300,-10):
    turtle.penup()
    turtle.left(90)
    turtle.goto(i,-400)
    turtle.pendown()
    turtle.forward(600)



