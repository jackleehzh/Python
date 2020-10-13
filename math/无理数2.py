import turtle
import math


c = []
c.append([0, 0])
c.append([20, 0])
turtle.forward(20)


def cal_point(x, y):
    x00 = 0
    y00 = 0
    for i in range(len(c) - 1):
        x1 = c[i][0]
        y1 = c[i][1]
        x2 = c[i + 1][0]
        y2 = c[i + 1][1]
        x0 = 0
        #解直线方程
        if x1 == x2 == 20:
            x0 = x1
        else:
            x0 = (y1 - x1 * ((y2 - y1) / (x2 - x1))) / (y / x - (y2 - y1) / (x2 - x1))
        y0 = x0 * y / x

        L0 = x ** 2 + y ** 2
        L2 = (x - x0) ** 2 + (y - y0) ** 2
        #判断线段交点，且距离小于该点到(0, 0)点的距离
        if ((x1 <= x0 <= x2 or x2 < x0 < x1) and (y1 < y0 < y2 or y2 < y0 < y1)) and L2 < L0:
             x00 = x0
             y00 = y0

    return x00, y00


for i in range(100):
    sinC = 1 / math.sqrt(i + 1)
    arcC = round(math.asin(sinC) * 180 / math.pi, 1)
    turtle.left(arcC)
    turtle.forward(20)
    x, y = turtle.pos()
    x0, y0 = cal_point(x, y)
    c.append([x, y])
    turtle.goto(x0, y0)
    turtle.goto(x, y)

print(c)
turtle.done()
