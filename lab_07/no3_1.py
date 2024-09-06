import turtle

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def getArea(self):
        return self.width * self.height
    
    def getPerimeter(self):
        return 2 * self.width + 2 * self.height
    
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
    
    def intersect(self, rec):
        x1 = max(self.x, rec.x)
        y1 = max(self.y, rec.y)
        x2 = min(self.x + self.width, rec.x + rec.width)
        y2 = min(self.y + self.height, rec.y + rec.height)
        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2 - x1, y2 - y1)
        else:
            return None
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)

def main():
    r1 = Rectangle(0, 0, 200, 200)
    r1.draw()
    r2 = Rectangle(50, 50, 200, 200)
    r2.draw()

    r3 = r1.intersect(r2)
    turtle.fillcolor("Green") 
    turtle.begin_fill()
    r3.draw()
    turtle.end_fill()
    r3.getArea()

main()
turtle.done()