import turtle
import random
 
turtle.screensize(1000, 1000, "white") #Added to make this work on smaller screens
 
r1 = random.randint(20,700)
t1 = (800-r1)/2
 
r2 = random.randint(20,700)
t2 = (800-r2)/2
 
r3 = random.randint(20,700)
t3 = (800-r3)/2
 
r4 = random.randint(20,700)
t4 = (800-r4)/2
 
r5 = random.randint(20,700)
t5 = (800-r5)/2
 
r6 = random.randint(20,700)
t6 = (800-r6)/2
 
r7 = random.randint(20,700)
t7 = (800-r7)/2
 
r8 = random.randint(20,700)
t8 = (800-r8)/2
 
r9 = random.randint(20,700)
t9 = (800-r9)/2
 
randomr = [r1,r2,r3,r4,r5,r6,r7,r8]
randomt = [t1,t2,t3,t4,t5,t6,t7,t8]
 
turtle.speed(0)
turtle.up()
turtle.goto(-400,350)
turtle.down()
 
for i in range(7):
    turtle.forward(randomr[i])
    turtle.up()
    turtle.forward(randomt[i])
    turtle.down()
    turtle.forward(randomt[i])
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(randomr[i])
    turtle.up()
    turtle.forward(randomt[i])
    turtle.down()
    turtle.forward(randomt[i])
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
 
turtle.forward(r9)
turtle.up()
turtle.forward(t9)
turtle.down()
turtle.forward(t9)
turtle.left(90)
turtle.forward(800)
 
turtle.up()
turtle.goto(-400,350)
turtle.down()
turtle.back(600)
turtle.up()
turtle.color("red")
turtle.shape("turtle")
turtle.goto(-400,380)
turtle.right(90)
turtle.pendown()
 
# You simply have to beat the maze
# You are not allowed to change code above, go round the outside, teleport etc.
# This challenge was made by a year 9 girl!
# Start coding the solution below.
# You can use lists & variables above to help.


xsl=[-400+r1+(t1/2), -400+r2+(t2/2), -400+r3+(t3/2), -400+r4+t4/2, -400+r5+t5/2, -400+r6+t6/2, -400+r7+t7/2, -400+r8+t8/2, -400+r9+t9/2]
xsr=[400-r1-(t1/2), 400-r2-(t2/2), 400-r3-(t3/2), 400-r4-t4/2, 400-r5-t5/2, 400-r6-t6/2, 400-r7-t7/2, 400-r8-t8/2, 400-r9-t9/2]

y=360

turtle.color("blue")
turtle.pu()
turtle.goto(-400, 360)
turtle.setheading(0)
turtle.pd()
for f in range(7):
    turtle.goto(xsl[f],y)
    turtle.setheading(270)
    turtle.fd(40)
    y=y-40
    turtle.goto(xsr[f],y)
    turtle.setheading(270)
    turtle.fd(40)
    y=y-40
turtle.goto(xsl[8],y)
turtle.setheading(270)
turtle.fd(40)
turtle.fd(100)
