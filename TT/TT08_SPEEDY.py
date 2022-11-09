import turtle

turtle.bgcolor("blue")

turtle.speed(0)

for i in range(300,-300,-10):
    turtle.penup()
    turtle.goto(-400,i)
    turtle.pendown()
    turtle.forward(600)
    
#y-axis
turtle.left(90)
for i in range(300,-300,-10):
    turtle.penup()
    turtle.goto(i-100,-290)
    turtle.pendown()
    turtle.forward(590)




