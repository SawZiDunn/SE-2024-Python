from abc import ABC, abstractmethod
import turtle

class Char(ABC):
    @abstractmethod
    def draw(self, x, y):
        pass

    @abstractmethod
    def getWidth(self):
        pass

class Char0(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(30)

    def getWidth(self):
        return 60

class Char1(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(60)
        turtle.backward(60)

    def getWidth(self):
        return 60

# Subclass Char2
class Char2(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.left(90)
        turtle.forward(60)
        turtle.right(90)
        turtle.pendown()

        
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)

    def getWidth(self):
        return 60

class Char3(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.left(90)
        turtle.forward(60)
        turtle.right(90)
        turtle.pendown()

        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.left(180)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)

    def getWidth(self):
        return 60

class Char4(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.left(90)
        turtle.forward(60)
        turtle.right(90)
        turtle.pendown()

        turtle.right(90)
        for _ in range(3):
            turtle.forward(30)
            turtle.left(90)
        turtle.left(90)
        turtle.forward(60)

    def getWidth(self):
        return 60

# Subclass Char5
class Char5(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)

    def getWidth(self):
        return 60

class Char6(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.left(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.pendown()

        for _ in range(4):
            turtle.forward(30)
            turtle.right(90)
        turtle.left(90)
        
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)

    def getWidth(self):
        return 60

class Char7(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.left(90)
        turtle.forward(60)
        turtle.right(90)
        turtle.pendown()

        turtle.forward(30)
        turtle.right(90)
        turtle.forward(60)
        

    def getWidth(self):
        return 60

class Char8(Char):
    def draw(self, x, y):
        x += 15
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        turtle.circle(15, 360)
        turtle.penup()
        turtle.goto(x, y + 30)
        turtle.pendown()
        turtle.circle(15, 360)
        turtle.right(90)
        turtle.forward(30)

    def getWidth(self):
        return 60

class Char9(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.left(90)
        turtle.forward(60)
        turtle.right(90)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(30)
            turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(30)

    def getWidth(self):
        return 60

# Function to draw a number
def drawNum(x):
    
    digits = {
        '0': Char0(),
        '1': Char1(),
        '2': Char2(),
        '3': Char3(),
        '4': Char4(),
        '5': Char5(),
        '6': Char6(),
        '7': Char7(),
        '8': Char8(),
        '9': Char9(),
    }

    if isinstance(x, int):
        x = str(x)

    x_pos = -100
    
    for digit in x:
        if digit in digits:
            
            digits[digit].draw(x_pos, 0)
            x_pos += 40
            turtle.setheading(0)

drawNum("789")
turtle.done()
