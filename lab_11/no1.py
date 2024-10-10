import math

class Point:
    def __init__(self, x=0.00, y=0.00) -> None:
        self._x = x
        self._y = y
    
    def printInfo(self):
        print(f"Position: {self._x}, {self._y}")
    
class Circle(Point):
    def __init__(self, x=0.00, y=0.00, radius=0.00) -> None:
        super().__init__(x, y)
        self.radius = radius
        '''
        Everytime we try to assign a value to self.radius, radius is validated
        because of setter property.
        '''

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
  
        self.__radius = value

    def area(self):
        return math.pi * pow(self.__radius, 2)
    
    def printInfo(self):
        super().printInfo()
        print(f"Radius: {self.__radius}")
        print(f"Area: {self.area():.2f}")

point = Point(5, 6)
point.printInfo()

try:
    circle = Circle(1, 2, -10)
    circle.printInfo()
except ValueError as e:
    print(e)

circle1 = Circle(1, 2, 10)
circle1.printInfo()
circle1.__radius = -9 # .__radius is not accessible, so the value won't be assigned
circle1.printInfo()

