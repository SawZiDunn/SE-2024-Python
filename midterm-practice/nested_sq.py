import turtle

def draw_square(n):
    for _ in range(4):
        turtle.forward(n)
        turtle.right(90)

def draw_nested_squares(size, gap):
    turtle.speed(0)
    while size >= 20:
        draw_square(size)
        size -= (gap * 2)
        turtle.penup()
        turtle.forward(gap)
        turtle.right(90)
        turtle.forward(gap)
        turtle.left(90)
        turtle.pendown()
    turtle.done()

draw_nested_squares(200, 20)