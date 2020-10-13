import turtle
import math

# 尺规作图，此题关键是确定第三个顶点的位置

turtle.forward(100)
turtle.pu()
turtle.goto(0, -100)
turtle.pd()
turtle.circle(100)
turtle.pu()
turtle.goto(100, -100)
turtle.pd()
turtle.circle(100)

# 两圆的其中一个交点
x = 100 / 2
y = math.sqrt(100 ** 2 - 50 ** 2)

turtle.pu()
turtle.goto(0, 0)
turtle.pd()
turtle.goto(x, y)

turtle.pu()
turtle.goto(100, 0)
turtle.pd()
turtle.goto(x, y)

turtle.done()
