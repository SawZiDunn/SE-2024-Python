class EWallet:
    def __init__(self, owner, max_amt) -> None:
        self.owner = owner
        self.max_amt = max_amt
        self.cur_amt = 0

    def deposit(self, amt):
        if self.cur_amt + amt <= self.max_amt:
            self.cur_amt += amt
        else:
            print("Excedeed Max Limit")
    
    def withdraw(self, amt):
        if self.cur_amt - amt < 0:
            print("Insufficient Balance!")
        else:
            self.cur_amt -= amt

    def check_amt(self):
        return f"Your Balance is {self.cur_amt}"
    
class SmartEWallet(EWallet):
    def __init__(self, owner, max_amt) -> None:
        super().__init__(owner, max_amt)
        self.history = list()

    def deposit(self, amt):
        super().deposit(amt)
        self.history.append(f"- {amt} Deposited")

    def withdraw(self, amt):
        super().withdraw(amt)
        self.history.append(f"- {amt} Withdrawn")
    
    def view_history(self):
        for i in self.history:
            print(i)

myWallet = SmartEWallet("Jack", 10000)
myWallet.deposit(3500)
myWallet.withdraw(500)
myWallet.deposit(3800)
myWallet.deposit(3600)

print(myWallet.check_amt())
myWallet.view_history()

