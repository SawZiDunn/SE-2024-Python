class Department:

    def __str__(self) -> str:
        return f"{self._description}"
    
    def __init__(self, description, manager="", employeeList=None) -> None:
        self._description = description
        self._manager = manager
        self._employeeList: list = [] if employeeList is None else employeeList

    def addEmployee(self, employee):
        self._employeeList.append(employee)
        employee._department = self

    def deleteEmployee(self, employee):
        self._employeeList.remove(employee)
        employee._department = None


    def setManager(self, employee):
        if employee in self._employeeList and isinstance(employee, PermEmployee):
            self._manager = employee

    def printInfo(self):
        print(f"Description: {self._description}, Manager: {self._manager}")
        print("Employees: ")
        for e in self._employeeList:
            e.printInfo()

class Person:
    def __init__(self, name, birthdate, address) -> None:
        self._name = name
        self._birthdate = birthdate
        self._address = address

    def printInfo(self):
        print(f"Name: {self._name}, DOB: {self._birthdate}, Address: {self._address}")

class Employee(Person):
    def __init__(self, name, birthdate, address, startDate, department=None) -> None:
        super().__init__(name, birthdate, address)
        self._department = department
        self._startDate = startDate

    def printInfo(self):
        super().printInfo()
        print(f"Department: {self._department}, StartDate: {self._startDate}")

class TempEmployee(Employee):
    def __init__(self, name, birthdate, address, startDate, department, wage) -> None:
        super().__init__(name, birthdate, address, startDate, department)
        self._wage = wage

    def printInfo(self):
        super().printInfo()
        print(f"Wage: {self._wage}")

class PermEmployee(Employee):
    def __str__(self) -> str:
        return f"{self._name}"
    
    def __init__(self, name, birthdate, address, startDate, department, salary) -> None:
        super().__init__(name, birthdate, address, startDate, department)
        self._salary = salary

    def printInfo(self):
        super().printInfo()
        print(f"Salary: {self._salary}")


eng = Department("Engineering", "No Manager")

emp1 = PermEmployee("Visit", "1990-01-01", "123 Main St", "2020-01-01", None, 50000)
emp2 = TempEmployee("Sun", "1992-05-15", "456 Elm St", "2021-05-10", None, 25)

eng.printInfo()  # Before adding employees
eng.addEmployee(emp1)
eng.addEmployee(emp2)
eng.printInfo()  # After adding employees

eng.deleteEmployee(emp2)  # Removing employee
eng.printInfo()

eng.setManager(emp1)  # Set manager
print("==============")
eng.printInfo()

