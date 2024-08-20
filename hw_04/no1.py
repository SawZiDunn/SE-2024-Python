import turtle

def main():
    x0 = int(input("x0: "))
    y0 = int(input("y0: "))

    x1 = int(input("x1: "))
    y1 = int(input("y1: "))

    x2 = int(input("x2: "))
    y2 = int(input("y2: "))

    turtle.penup()
    turtle.goto(x0, y0)
    turtle.write("p0")
    turtle.pendown()

    turtle.goto(x1, y1)
    turtle.write("p1")
    turtle.penup()
    turtle.goto(x2, y2)
    turtle.pendown()
    turtle.write("p2")
    turtle.penup()
    turtle.goto(x2, y2 - 50)
    turtle.pendown()

    cross_product = (x2 - x0) * (y1 - y0) - (y2 - y0) * (x1 - x0)

    if cross_product > 0:
        turtle.write("p2 is on the right side of the line.")
    elif cross_product < 0:
        turtle.write("p2 is on the left side of the line.")
    else:
        turtle.write("p2 is on the line")
        
    turtle.hideturtle()
    turtle.done()

main()







