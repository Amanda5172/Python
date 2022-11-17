import turtle

r = int(input("Number of sides: "))

for i in range(r):
  turtle.forward(50)
  turtle.right(360/r)
turtle.done()
