import turtle
import statistics

def get_point(point_name):
    x = float(input("x coordinate for " + point_name + ": "))
    y = float(input("y coordinate for " + point_name + ": "))
    return x, y

def main():
    x1, y1 = get_point("p1")
    x2, y2 = get_point("p2")
    x3, y3 = get_point("p3")

    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    turtle.penup()

    x_value = statistics.median([x1, x2, x3])
    y_value = min(y1, y2, y3) - 20
    turtle.goto(x_value, y_value)
    turtle.pendown()
    turtle.write(f"Area = {area:.2f}")

    turtle.done()

main() 