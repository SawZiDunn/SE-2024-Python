
# referenced
import turtle

turtle.speed(0)

def cross(width, times):
    if times == 0:
        turtle.dot(6)
        return
    else:
        for _ in range(4):
            turtle.forward(width)
            cross(width / 2, times - 1)
            turtle.right(180)
            turtle.forward(width)
            turtle.left(90)

cross(100, 4)
turtle.done()