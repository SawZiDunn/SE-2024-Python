import turtle

def main():
    r = float(input("Radius: "))
    turtle.width(7)
    colours = ["blue", "black", "red", "yellow", "green"]

    # center for blue ring
    # values are adjustable
    x, y = -200, 0
    temp = (2 * r) + (r / 2)

    for (index, colour) in enumerate(colours):
        # for the yellow(4th) ring
        if index == 3:
            y -= r # move the position down by the radius value
            x -= temp * 3 # get the original x value
            x += temp / 2
            

        turtle.color(colour)
        turtle.penup()
        turtle.goto(x, y - r)
        turtle.pendown()
        turtle.circle(r)

        x += temp #move the ring to the right for every loop
    turtle.done()
    

if __name__ == "__main__":
    main()

