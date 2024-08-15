import turtle

def draw_square(size, n):
    # turtle.speed(0)

    length = size / n

    for i in range(n):
        for j in range(n):

            x = i * length - size / 2
            y = j * length - size / 2

            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

            if (i + j) % 2 == 0:
                turtle.fillcolor("black")
            else:
                turtle.fillcolor("white")

            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(length)
                turtle.right(90)
            turtle.end_fill()

    turtle.done()

def main():
    size = 100
    n = int(input("N: "))
    draw_square(size, n)

if __name__ == "__main__":
    main()
