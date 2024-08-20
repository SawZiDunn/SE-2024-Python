import turtle

def draw_square(size, n):

    turtle.speed(0)
    turtle.penup()
    x, y = 0, 0 # define where the first row starts
    turtle.goto(x, y)
    turtle.pendown()

    length = size / n # for each mini-square

    for i in range(n):
        for j in range(n):

            if (i + j) % 2 == 0:
                turtle.fillcolor("black")
            else:
                turtle.fillcolor("white")

            turtle.begin_fill()
            for k in range(4):
                turtle.forward(length)
                turtle.right(90)
            turtle.end_fill()
            turtle.forward(length)
            

        turtle.backward(size)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)

    turtle.done()

def main():
    size = 100
    n = int(input("N: "))
    draw_square(size, n)

main()
