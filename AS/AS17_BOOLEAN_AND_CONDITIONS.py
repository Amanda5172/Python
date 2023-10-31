import turtle
import math

#Exercise 1

def day(n):
    days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    return days[n]

print(day(1))


#Exercise 2
print()
def countdays(n,add):
    tot = n + add%7
    if tot > 6:
        tot=tot-7
    return day(tot)


print(countdays(3,137))

        
#Exercise 3
print()

print("a<=b")
print("a<b")
print("a<b and day!=3")
print("a<b and day==18")

#Exercise 4
print()

print(3==3)
print(3!=3)
print(3>=4)
print(not(3<4))


#Exercise 5
print()

print(not(False and False) or False)
print(not(False and False) or True)
print(not(False and True) or False)
print(not(False and True) or True)
print(not(True and False) or False)
print(not(True and False) or True)
print(not(True and True) or False)
print(not(True and True) or True)


#Exercise 6
print()

def grade(mark):
    if mark>=75:
        return "First"
    elif mark>=70:
        return "Upper Second"
    elif mark>=60:
        return "Second"
    elif mark>=50:
        return "Third"
    elif mark>=45:
        return "F1 Supp"
    elif mark>=40:
        return "F2"
    else:
        return "F3"

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in xs:
    print(grade(i))

#Exercise 7
def draw_bar(t, height):  
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.pu()
    t.forward(10)
    t.pd()

tess = turtle.Turtle()    
tess.color("blue")
tess.speed(-1)
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess, a)


#Exercise 8

def draw_bar(t, height):
    t.begin_fill()        
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.pu()
    t.forward(10)
    t.pd()

tess.goto(0,0)
tess.setheading(0)
tess.clear()


for a in xs:
    if a>=200:
        tess.color("blue", "red")
    elif a>=100:
        tess.color("blue", "yellow")
    elif a<100:
        tess.color("blue", "green")
    draw_bar(tess, a)
    

#Exercise 9
def draw_bar(t, height):
    t.begin_fill()        
    t.left(90)
    t.forward(height)
    if height<0:
        t.pu()
        t.fd(-15)
        t.write("  "+ str(height))
        t.fd(15)
        t.pd()
    else:
        t.write("  "+ str(height))
    t.setheading(0)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.pu()
    t.forward(10)
    t.pd()

tess.goto(0,0)
tess.setheading(0)
tess.clear()
tess.color("blue")

xs = [-48,117,200,-240,160,260,220]

for a in xs:    
    draw_bar(tess, a)


#Exercise 10
print()
def find_hypot(l1,l2):
    l3 = math.sqrt(l1**2+l2**2)
    return l3
print(find_hypot(3,4))


#Exercise 11
print()
def is_rightangled(l1,l2,l3):
    y=math.sqrt(l1**2+l2**2)
    if  abs(l3-y) < 0.000001: 
        return True
    else:
        return False

print(is_rightangled(3,4,6))


#Exercise 12
print()
def is_rightangled2(l1,l2,l3):
    y=math.sqrt(l1**2+l2**2)
    
    longest=l1
    if l2>longest:
        longest=l2
        if l3>longest:
            longest=l3
    
    if  abs(longest-y) < 0.000001: 
        return True
    else:
        return False

print(is_rightangled2(3,4,5))



#Exercise 13
print()

a = math.sqrt(2.0)
print(a, a*a)
print(a*a == 2.0)

