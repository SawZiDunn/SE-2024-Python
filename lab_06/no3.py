import turtle

def draw_polygon(x, y, type=4, size=100):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    degree = 360 / type
    for _ in range(type):
        turtle.forward(size)
        turtle.left(degree)
    turtle.done()

draw_polygon(0, 0)
