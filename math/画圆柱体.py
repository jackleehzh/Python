import turtle as w
import math


def gotoXY(x, y):
    w.penup()
    w.hideturtle()
    w.goto(x, y)
    w.pendown()
    w.showturtle()


def drawEllipse(x, y, a, b, degree1, degree2, isdotted):
    gotoXY(x + a * math.cos(degree1 / 180 * math.pi), y + b * math.sin(degree1 / 180 * math.pi))
    if isdotted == 0:
        for i in range(degree1, degree2, 1):
            w.goto(x + a * math.cos(i / 180 * math.pi), y + b * math.sin(i / 180 * math.pi))
    else:
        for i in range(degree1, degree2, 8):
            for j in range(5):
                w.goto(x + a * math.cos((i + j) / 180 * math.pi), y + b * math.sin((i + j) / 180 * math.pi))
            w.penup()
            for j in range(3):
                w.goto(x + a * math.cos((i + j + 5) / 180 * math.pi), y + b * math.sin((i + j + 5) / 180 * math.pi))
            w.pendown()


drawEllipse(0, 150, 100, 60, 0, 360, 0)
drawEllipse(0, -100, 100, 60, 0, 180, 1)
drawEllipse(0, -100, 100, 60, 181, 360, 0)
gotoXY(-100, 150)
w.right(90)
w.forward(250)

gotoXY(100, 150)
w.forward(250)

gotoXY(0, -200)
w.color('pink')
w.write('李明韬', font=('Lisu', 20))
w.hideturtle()
w.done()