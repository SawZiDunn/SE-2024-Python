class Calculator:
    def __init__(self, acc=0.0) -> None:
        self._acc = acc

    def set_accumulator(self, a: int):
        # if a is neither an int or a float
        if not isinstance(a, (int, float)): 
            raise ValueError("Has to be a number!")
        self._acc = a

    def get_accumulator(self):
        return self._acc
    
    def add(self, x):
        self._acc += x

    def substract(self, x):
        self._acc -= x

    def multiply(self, x):
        self._acc *= x

    def divide(self, x):
        if x == 0:
            raise ZeroDivisionError("Cannot be divided by zero!")
        self._acc /= x

    def print_result(self):
        print(f"Result: {self._acc}")

class Sci_calc(Calculator):
    def __init__(self, acc=0.0) -> None:
        super().__init__(acc)
    
    def square(self):
        return pow(self._acc, 2)
    
    def exp(self, x):
        return pow(self._acc, x)
    
    def factorial(self):
        temp = self._acc
        factorial = 1

        while temp >= 1:
            factorial *= temp
            temp -= 1
        return factorial
    
    def print_result(self):
        print(f"Result: {self._acc:.2e}")


def test_calculator():
    calculator = Calculator()
    calculator.print_result()

    calculator.set_accumulator(25)
    calculator.divide(0)
    calculator.print_result()


def test_sci_calc():
    sci_calc = Sci_calc()
    sci_calc.set_accumulator("hi")
    print(sci_calc.factorial())
    sci_calc.print_result()


# test_calculator()
test_sci_calc()

    