import math, turtle

class Circle:
    def __init__(self, x, y, radius) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    def getArea(self):
        return math.pi * pow(self.radius, 2)
    
    def getPerimeter(self):
        return 2 * math.pi * self.radius
    
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
        turtle.reset()
        self.draw()

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y - self.radius)
        turtle.pendown()

        turtle.circle(self.radius)

circle1 = Circle(100, 100, 100)
print(f"Circle 1 Area: {circle1.getArea():.2f}")
print(f"Circle 1 Parameter: {circle1.getPerimeter():.2f}")
circle1.draw()

circle1.move(0, 0)

turtle.done()