import turtle
import math

def main():
    center_x = int(input("Center x-coordinate: "))
    center_y = int(input("Center y-coordinate: "))
    radius = float(input("Radius: "))
    area = math.pi * radius * radius
    circle = turtle.Turtle()
    circle.penup()
    circle.goto(center_x, center_y - radius)
    circle.pendown()
    circle.circle(radius, 360)

    circle.penup()
    circle.goto(center_x, center_y)
    circle.pendown()
    circle.write(area, align="center")
    circle.done()
    
main()
    