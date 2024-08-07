import turtle

def main():
    x = float(input("Length of the star: "))
    turtle.penup()
    turtle.goto(-100, 60)
    turtle.pendown()
    for i in range(5):
        turtle.forward(x)
        turtle.right(144) # 36 Degree
    
    turtle.done()

main() 