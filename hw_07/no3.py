class LinearEquation:
    def __init__(self, a, b, c, d, e, f) -> None:
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
    
    def get_c(self):
        return self.__c
    
    def get_d(self):
        return self.__d
    
    def get_e(self):
        return self.__e
    
    def get_f(self):
        return self.__f
    
    def isSolvable(self):
        return self.__a * self.__d - self.__b * self.__c != 0
         

    def getX(self):
        numerator = self.__e * self.__d - self.__b * self.__f
        denominator = self.__a * self.__d - self.__b * self.__c
        return "%.2f" % (numerator / denominator) # two decimal places
    
    def getY(self):
        numerator = self.__a * self.__f - self.__e * self.__c
        denominator = self.__a * self.__d - self.__b * self.__c
        return "%.2f" % (numerator / denominator)

def main():
    eq = LinearEquation(2, 3, 2, 6, 4, 10)
    
    print(f"isSolvable: {eq.isSolvable()}")
    print("x:", eq.getX())
    print("y:", eq.getY())
    
    eq2 = LinearEquation(1, 1, 1, 1, 1, 1)
    
    print(f"isSolvable: {eq2.isSolvable()}")

main()