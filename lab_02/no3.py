import turtle

def main():
    x = turtle.Turtle()
    size = 100

    for i in range(6):
        x.forward(size)
        x.left(60)
   
    x.penup()
    x.goto(20, -20)
    x.pendown()
    x.write(f"Size {size}")
    x.done()

main()



    
    
