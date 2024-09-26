import turtle

def command_line_turtle():
    print("Hello, welcome to Turtle World!")
    while True:
        x = input("turtle|> ").strip()
        if x == "fd":
            turtle.forward(float(input("Forward Unit: ")))
        elif x == "back":
            turtle.backward(float(input("Backward Unit: ")))
        elif x == "lt":
            turtle.left(float(input("Left Turn Unit: ")))
        elif x == "rt":
            turtle.right(float(input("Right Turn Unit: ")))
        elif x == "pu":
            turtle.penup()
        elif x == "pd":
            turtle.pendown()
        elif x == "reset":
            turtle.clearscreen()
        elif x == "quit":
            turtle.done()
            break
        else:
            print("Wrong command, please try again.")

command_line_turtle()