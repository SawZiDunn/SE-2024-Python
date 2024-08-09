import turtle

x0 = int(input("x1: "))
y0 = int(input("y1: "))

x1 = int(input("x1: "))
y1 = int(input("y1: "))

x2 = int(input("x1: "))
y2 = int(input("y1: "))

turtle.penup()
turtle.goto(x0, y0)
turtle.write("p0")
turtle.pendown()
turtle.goto(x2, y2)
turtle.write("p3")
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("p2")
turtle.done()







