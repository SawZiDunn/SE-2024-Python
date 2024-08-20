import turtle

def draw_rectangle(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(f"({x}, {y})")

    turtle.penup()
    turtle.goto(x - width / 2, y - height / 2) # bottom left point
    turtle.pendown()

    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(180)

def main():
    x1 = int(input("First Rectangle Center - x1: "))
    y1 = int(input("First Rectangle Center - y1: "))
    rectangle_width1 = float(input("First Rectangle Width: "))
    rectangle_height1 = float(input("First Rectangle Height: "))

    x2 = int(input("Second Rectangle Center - x2:"))
    y2 = int(input("Second Rectangle Center - y2: "))
    rectangle_width2 = float(input("Second Rectangle Width: "))
    rectangle_height2 = float(input("Second Rectangle Height: "))

    half_width1 = rectangle_width1 / 2
    half_height1 = rectangle_height1 / 2
    half_width2 = rectangle_width2 / 2
    half_height2 = rectangle_height2 / 2

    left1 = x1 - half_width1
    right1 = x1 + half_width1
    top1 = y1 + half_height1
    bottom1 = y1 - half_height1

    left2 = x2 - half_width2
    right2 = x2 + half_width2
    top2 = y2 + half_height2
    bottom2 = y2 - half_height2

    # print("left1", left1, "right1", right1, "top1", top1, "bottom1", bottom1)
    # print("left2", left2, "right2", right2, "top2", top2, "bottom2", bottom2)

    draw_rectangle(x1, y1, rectangle_width1, rectangle_height1)
    draw_rectangle(x2, y2, rectangle_width2, rectangle_height2)

    turtle.penup()
    turtle.goto(min(x1, x2), min(bottom1, bottom2) - 100)
    turtle.pendown()

    if left2 <= left1 and right2 >= right1 and top2 >= top1 and bottom2 <= bottom1:
        turtle.write("1st rectangle is inside 2nd rectangle.")
    elif left1 <= left2 and right1 >= right2 and top1 >= top2 and bottom1 <= bottom2:
        turtle.write("2nd rectangle is inside 1st rectangle.")
    elif left1 < right2 and right1 > left2 and top1 > bottom2 and bottom1 < top2:
        turtle.write("Two rectangles are overlapping with one another.")
    else:
        turtle.write("Two rectangles are neither overlapping nor inside one another.")
    turtle.done()

main()
