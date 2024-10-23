import turtle

def draw_triangle(size):
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

def nested_triangles(size, gap):
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()

    while size >= 20:
        draw_triangle(size)
        size -= gap * 2
        turtle.penup()
        
        turtle.left(30)
        turtle.forward(gap)
        turtle.right(30)
        turtle.pendown()
    turtle.done()

nested_triangles(200, 20)
