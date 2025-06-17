# 🔹 3. BankAccount
# Create a class with owner and balance.
# Add a method show_balance() and instantiate it with your name.



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: ₹{self.balance}")

my_account = BankAccount("Anshuman Sparsh", 5000)
my_account.show_balance()