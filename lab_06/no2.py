import turtle

def draw_square(n):
    for _ in range(4):
        turtle.forward(n)
        turtle.left(90)

def draw_nested_squares(x):
    for _ in range(4):
        for j in range(1, 5):
            draw_square(x * j)
        turtle.right(90)
    turtle.done()

draw_nested_squares(50)