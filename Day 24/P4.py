# 🔹 4. Account → SavingsAccount
# Base class has balance and deposit() method.
# Child class adds interest_rate and add_interest().




class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Added interest ₹{interest}. New balance: ₹{self.balance}")

acc = SavingsAccount(1000, 5)
acc.deposit(500)
acc.add_interest()
