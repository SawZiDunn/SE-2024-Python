import turtle

def nested_triangles(radius, gap):
    turtle.speed(0)

    while radius >= 20:
        turtle.circle(radius)
        radius -= gap
        turtle.penup()
        
        turtle.left(90)
        turtle.forward(gap)
        turtle.right(90)
        turtle.pendown()
    turtle.done()

nested_triangles(200, 20)
