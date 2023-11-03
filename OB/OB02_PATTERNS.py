import turtle

class pattern():
    def __init__(self, angle: int, times: int):
        self.__angle = angle # Integer
        self.__times = times # Integer

    def draw_pattern(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.setup(800, 600)  
        turtle.bgcolor('black')
        turtle.speed(-1)
        for x in range(self.__times):
            turtle.pencolor(colors[x % 6])
            turtle.width(x / 100 + 1)
            turtle.forward(x)
            turtle.left(self.__angle)
        #turtle.done()

pat=[]
with open("patterns.txt","r") as ef:
    for line in ef:
        pat.append(int(line.strip("\n")))

for i in range(0,len(pat),2):
    mypattern=pattern(pat[i],pat[i+1])
    mypattern.draw_pattern()
    turtle.clear()
