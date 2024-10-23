import turtle, math

def diamond(s):
    length = s * math.sqrt(2)
    turtle.penup()
    turtle.backward(s)
    turtle.left(45)
    turtle.pendown()

    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)
    turtle.right(45)
    turtle.penup()
    turtle.forward(s)
    turtle.pendown()

def cross(s):
    for _ in range(4):
        turtle.forward(s)
        turtle.backward(s)
        turtle.right(90)

def pile(s):
    cross(s / 2)
    diamond(s / 2)
    diamond(s)
    turtle.done()



pile(100)
