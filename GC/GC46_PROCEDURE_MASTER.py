def DefaultLine():
    Line(60)

def Line(Size):
    for Length in range(0, Size):
        print('-', end='')

MySize = int(input("Input a length: "))


if MySize == -1:
    DefaultLine()
else:
    Line(MySize)

            
