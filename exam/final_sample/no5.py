from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, price, count):
        self.price = price
        self.count = count

    @abstractmethod
    def calculate_cost(self):
        pass


class Electronics(Product, ABC):
    def __init__(self, price, count, vat):
        super().__init__(price, count)
        self.vat = vat # percent

    @abstractmethod
    def calculate_cost(self):
        return self.price * ((100 + self.vat) / 100) * self.count
        

class Book(Product):
    def __init__(self, price, count, discount):
        super().__init__(price, count)
        self.discount = discount # in percent

    def calculate_cost(self):
        return self.price * ((100 - self.discount) / 100) * self.count

class TV(Electronics):
    def calculate_cost(self):
        return super().calculate_cost()
        

class Laptop(Electronics):
    def calculate_cost(self):
        return super().calculate_cost()

items = [
    Book(100, 2, 10),
    TV(8000, 1, 7),
    Laptop(20000, 1, 7)
]

total = 0
for i in items:
    total += i.calculate_cost()

print(f"Total Cost: {total} Baht")

