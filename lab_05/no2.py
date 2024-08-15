import turtle

def draw_square(size, n):
    turtle.penup()
    x, y = 0, 0
    turtle.goto(x, y)
    turtle.pendown()

    length = size / n # the side of each small square
    for i in range(n):
        for j in range(n):
            for _ in range(n - 1):
                turtle.forward(length)
                turtle.right(90)
            turtle.forward(length)
        
        
        turtle.backward(length * n)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)
        
    turtle.done()


def main():
    size = 100
    n = int(input("N: "))
    draw_square(size, n)

main()