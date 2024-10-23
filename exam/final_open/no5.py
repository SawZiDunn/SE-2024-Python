from abc import ABC, abstractmethod

class Sale_item(ABC):
    def __init__(self, name, unit_price) -> None:
        self.name = name
        self.unit_price = unit_price

    @abstractmethod
    def calculate_total(self):
        pass


class Food(Sale_item, ABC):
    def __init__(self, name, unit_price) -> None:
        super().__init__(name, unit_price)

    @abstractmethod
    def calculate_total(self):
        pass

class Itemized_food(Food):
    def __init__(self, name, unit_price, count) -> None:
        super().__init__(name, unit_price)
        self.count = count

    def calculate_total(self):
        return self.count * self.unit_price
    
class Measured_food(Food):
    def __init__(self, name, unit_price, kg) -> None:
        super().__init__(name, unit_price)
        self.kg = kg

    def calculate_total(self):
        return self.kg * self.unit_price
    
class Book(Sale_item):
    def __init__(self, name, unit_price, count, discount) -> None:
        super().__init__(name, unit_price)
        self.discount = discount # in percentage
        self.count = count

    def calculate_total(self):
        return self.unit_price * ((100 - self.discount) / 100) * self.count
    
class Appliance(Sale_item):
    def __init__(self, name, unit_price, count, vat) -> None:
        super().__init__(name, unit_price)
        self.vat = vat # in percent

    def calculate_total(self):
        return self.unit_price * ((100 + self.vat) / 100)
    
    
purchased_items = [
    Itemized_food("Vegetable Oil", 40, 2),
    Measured_food("Mange", 70, 1.8),
    Book("Python Book", 200, 1, 15),
    Appliance("Rice Cooker", 1200, 1, 7)
]

total_cost = 0
for i in purchased_items:
    total_cost += i.calculate_total()
print(f"Total Cost: {total_cost} Baht")
    
    
        