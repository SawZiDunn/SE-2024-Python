import math

class QuadraticEquation:
    def __init__(self, a, b, c) -> None:
        self._a = a
        self._b = b
        self._c = c
    
    def get_a(self):
        return self._a
    
    def get_b(self):
        return self._b
    
    def get_c(self):
        return self._c
    
    def getDiscriminant(self):
        return pow(self.get_b(), 2) - 4 * self.get_a() * self.get_c()
    

    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return 0
        return (-self.get_b() + math.sqrt(self.getDiscriminant())) / 2 * self.get_a()

    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return 0
        return (-self.get_b() - math.sqrt(self.getDiscriminant())) / 2 * self.get_a()
    
def main():
    quadraticEquation = QuadraticEquation(1, -8, 15)
    print(f"Root 1: {quadraticEquation.getRoot1()}")
    print(f"Root 2: {quadraticEquation.getRoot2()}")

main()
