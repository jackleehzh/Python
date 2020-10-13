import turtle as w
w.speed(0)
w.hideturtle()


def my_goto(x, y):
    w.pu()
    w.goto(x, y)
    w.pd()


def draw_line(x):
    my_goto(x, 0)
    w.goto(x, 200)


def draw_empty_rectangle(x, y, n):
    my_goto(x, y)
    w.fillcolor('white')
    w.begin_fill()
    w.pu()
    w.goto(x + 14 * (1 + n) + 2, y)
    w.goto(x + 14 * (1 + n) + 2, y + 10 + 2)
    w.goto(x, y + 10 + 2)
    w.goto(x, y)
    w.pd()
    w.end_fill()


def draw_rectangle(x, y, n):
    my_goto(x, y)
    w.goto(x + 14 * (1 + n), y)
    w.goto(x + 14 * (1 + n), y + 10)
    w.goto(x, y + 10)
    w.goto(x, y)


my_goto(-200, 0)
w.forward(100)
my_goto(-50, 0)
w.forward(100)
my_goto(100, 0)
w.forward(100)

draw_line(-150)
draw_line(0)
draw_line(150)

listA = []
listB = []
listC = []
a = -192
b = 2
m = 8
for i in range(m):
    draw_rectangle(-192 + (5 - m) * 7 + i * 7, 2 + i * 12, m - i)
    listA.append(m - i)


def move(la, x, lc, z):
    l = len(la)
    e = la.pop()
    draw_empty_rectangle(-193 + (5 - m) * 7 + x * 150 + (m - e) * 7, 1 + (l - 1) * 12, e)
    draw_line(-150 + x * 150)
    lc.append(e)
    l = len(lc)
    draw_rectangle(-192 + (5 - m) * 7 + z * 150 + (m - e) * 7, 2 + (l - 1) * 12, e)


def hanoi(n, la, x, lb, y,  lc, z):
    if n == 1:
        move(la, x, lc, z)
    else:
        hanoi(n - 1, la, x, lc, z, lb, y)
        move(la, x, lc, z)
        hanoi(n - 1, lb, y, la, x, lc, z)


hanoi(m, listA, 0, listB, 1,  listC, 2)

w.done()
