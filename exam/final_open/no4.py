class SavingAccount:
    def __init__(self, bank_name, acc_name, acc_id, balance):
        self.bank_name = bank_name
        self.acc_name = acc_name
        self.acc_id = acc_id
        self.balance = balance
        self.transaction_history = list()

    def deposit(self, money, person, date):
        self.balance += money
        self.transaction_history.append(f"{money} Deposited by {person} on {date}")
    
    def withdraw(self, money, person, date):
        if self.balance - money >= 0:
            self.balance -= money
            self.transaction_history.append(f"{money} Withdrawn by {person} on {date}")
        else:
            print("Insufficient Balance!")
            self.transaction_history.append(f"{money} withdrawl failed by {person} on {date}!")

    def get_balance(self):
        return self.balance
    
    def print_statement(self):
        for i in self.transaction_history:
            print(i)
    
class OverDrawnAccount(SavingAccount):
    def __init__(self, bank_name, acc_name, acc_id, balance, overdrawn_limit) -> None:
        super().__init__(bank_name, acc_name, acc_id, balance)
        self.overdrawn_limit = overdrawn_limit

    def withdraw(self, money, person, date):
        # if the amount after withdrawal, let's say => -2000 is is less than - overdrawn_limit
        if self.balance - money < (- self.overdrawn_limit):
            print("Overdrawn limit exceeded!")
            self.transaction_history.append(f"{money} Withdrawal failed by {person} on {date} due to exceeding overdrawn limit!")
        else:
            self.balance -= money
            self.transaction_history.append(f"{money} Withdrawn by {person} on {date}")

mgmg = OverDrawnAccount("SCB", "Mg Mg", "123", 0, 1000)

print("Initial balance:", mgmg.get_balance())
mgmg.withdraw(200, "Mg Mg", "30/05/2001")
print("Balance after withdrawal:", mgmg.get_balance())
mgmg.print_statement()

mgmg.withdraw(1500, "Mg Mg", "01/06/2001")
print("Balance after attempting to overdraw:", mgmg.get_balance())
mgmg.print_statement()

