from math import cos, radians, pi, sin
import random
import turtle


def draw(a, angle):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    if a > 5 and a * cos(angle * pi / 180) > 5 and a * sin(angle * pi / 180) > 5:
        turtle.pendown()
        turtle.color((r, g, b))
        turtle.begin_fill()
        for i in range(5):
            turtle.fd(a)
            turtle.right(90)
        turtle.end_fill()

        turtle.penup()
        turtle.left(90 + angle)
        draw(a * cos(radians(angle)), angle)
        turtle.right(90)
        turtle.fd(a * cos(radians(angle)))
        draw(a * cos(radians(90 - angle)), angle)
        turtle.right(90)
        turtle.fd(a * cos(radians(90 - angle)))
        turtle.right(angle)
        turtle.fd(a)
        turtle.right(90)
        turtle.fd(a)
        turtle.right(90)


if __name__ == '__main__':
    turtle.mode('logo')
    turtle.speed(0)
    turtle.colormode(255)
    turtle.seth(0)
    turtle.penup()
    turtle.goto(50, -200)
    side_lenght = random.randint(30, 100)
    angle = random.randint(10, 80)
    #draw(side_lenght, angle)
    draw(100, 30)

    turtle.done()
