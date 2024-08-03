import turtle

def main():
    r = float(input("Radius: "))
    turtle.width(7)
    colours = ["blue", "black", "red", "yellow", "green"]

    # blue ring center
    # values are adjustable
    x, y = -220, 100

    for (index, colour) in enumerate(colours):
        # for the yellow(4th) ring
        if index == 3:
            y -= 110 # move the position down by 110
            x -= (220 * 3) # get the original x value
            x = x / 2 if x < 0 else x * 2

        turtle.color(colour)
        turtle.penup()
        turtle.goto(x, y - r)
        turtle.pendown()
        turtle.circle(r)

        x += 220 #move the ring to the right by 220
    turtle.done()
    

if __name__ == "__main__":
    main()

