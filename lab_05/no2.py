import turtle

def draw_square(size, n):
    turtle.speed(0)
    turtle.penup()
    x, y = 0, 0 # define where the first row starts
    turtle.goto(x, y)
    turtle.pendown()

    length = size / n # the length of each small square
    for i in range(n):
        for j in range(n):
            for k in range(4):
                turtle.forward(length)
                turtle.right(90)
            turtle.forward(length)

        # turtle.backward(size)
        # turtle.right(90)
        # turtle.forward(length)
        # turtle.left(90)

        turtle.penup()
        turtle.goto(x, y - length * (i + 1))
        turtle.pendown()

        
    turtle.done()


def main():
    size = 100
    n = int(input("N: "))
    draw_square(size, n)

main()