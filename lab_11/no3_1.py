class Name:
    def __init__(self, t, f, l) -> None:
        self.setName(t, f, l)

    def setName(self, t, f, l):
        self._title = t
        self._firstName = f
        self._lastName = l

    def getFullName(self):
        return self._title + self._firstName + self._lastName
    
class Date():
    def __init__(self, d, m, y) -> None:
        self.setDate(d, m , y)

    def setDate(self, d, m, y):
        self._day = d
        self._month = m
        self._year = y

    def getDate(self):
        return f"{self._day}/{self._month}/{self._year}"
    
    def getDateBC(self):
        return f"{self._day}/{self._month}/{self._year + 543}"
    
class Address:
    def __init__(self) -> None:
        pass

    def setAddress(self, houseNo, street, district, city, country, postcode):
        self._houseNo = houseNo
        self._street = street
        self._district = district
        self._city = city
        self._country = country
        self._postcode = postcode

    def getAddress(self):
        return f"{self._houseNo}, {self._street}, {self._district}, {self._city}, {self._country}, {self._postcode}"
    

