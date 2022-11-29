import turtle

t=turtle
t.speed(0)

classwidth=2

frequency=[5,2,8,6]

#axes
t.lt(90)
t.fd(100)
t.write("y-axis")
t.fd(-100)

t.rt(90)
t.fd(100)
t.write("x-axis")
t.fd(-100)

#data
for i in range(len(frequency)):
    t.lt(90)
    t.fd(frequency[i] * 10)
    t.rt(90)
    t.fd(classwidth * 10)
    t.rt(90)
    t.fd(frequency[i]*10)
    t.lt(90)


