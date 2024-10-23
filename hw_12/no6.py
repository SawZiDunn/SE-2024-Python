from abc import ABC, abstractmethod

class StationaryGood(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_cost(self):
        pass # no need to return price here, subclasses will implement their own get_cost()

class Magazine(StationaryGood):
    def __init__(self, name, price):
        super().__init__(name, price)
    
    def get_cost(self):
        return self.price

class Book(StationaryGood):
    def __init__(self, name, price):
        super().__init__(name, price)
    
    def get_cost(self):
        return self.price * 0.9

class Ribbon(StationaryGood):
    def __init__(self, name, price_per_meter, length):
        super().__init__(name, price_per_meter)
        self.length = length
    
    def get_cost(self):
        return self.price * self.length

def getTotalCost(basket):
    total_cost = 0
    for item in basket:
        total_cost += item.get_cost()
    return total_cost

basket = [
    Magazine("Computer World", 70),
    Magazine("Computer World", 70),
    Magazine("Computer World", 70),
    Book("Windows 7 for Beginners", 200),
    Book("Windows 7 for Beginners", 200),
    Ribbon("Blue Ribbon", 5, 10)
]


total_cost = getTotalCost(basket)
print(f"Total cost of the goods: {total_cost} Bahts")
