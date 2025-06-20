# Project 4: Class-Based ATM System
# 🎯 Goal: Build a fully functional ATM simulator using OOP with classes and methods.



class Account:

    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin 

    def check_balance(self):
        print(f"\nBalance: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn.")
        else:
            print("Insufficient balance.")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed.")
        else:
            print("Incorrect old PIN.")

print("Terminal ATM\n")
user = Account("Anshuman", 10000, "8965")

entered_pin = input("Enter your PIN: ")
if entered_pin == user.pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user.check_balance()
        elif choice == "2":
            try:
                amt = float(input("Enter amount to deposit: "))
                user.deposit(amt)
            except:
                print("Invalid amount.")
        elif choice == "3":
            try:
                amt = float(input("Enter amount to withdraw: "))
                user.withdraw(amt)
            except:
                print("Invalid amount.")
        elif choice == "4":
            old_pin = input("Enter current PIN: ")
            new_pin = input("Enter new PIN: ")
            user.change_pin(old_pin, new_pin)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
else:
    print("Incorrect PIN.")
 