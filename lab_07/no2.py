class BankAccount:
    def __init__(self, bank_name, owner, acc_num, balance) -> None:
        self.bank_name = bank_name
        self.owner = owner
        self._acc_num = acc_num
        self._balance = balance
    
    def get_balance(self):
        print(f"Your current balance is {self._balance} Dollars.")

    def deposit(self, amount):
        self._balance += amount
        print(f"You deposited {amount} Dollars.")
        self.get_balance()

    def withdraw(self, amount):
        if amount > self._balance:
            print("Not enough balance!")
            return
        self._balance -= amount
        print(f"You withdrew {amount} Dollars.")
        self.get_balance()

def main():
    bank_acc1 = BankAccount("K Bank", "John", "123", 10000)
    bank_acc1.deposit(5000)

    bank_acc1.withdraw(7000)
    

main()