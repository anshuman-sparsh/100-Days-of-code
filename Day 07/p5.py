# 🔹 5. Mini ATM
# Build a function-based ATM simulator:
# check_balance(), deposit(amount), withdraw(amount)
# Start with balance = 1000
# Use a menu loop to let the user perform actions
# Print updated balance after each action
# (Use a while loop to solve it)




balance = 1000

def check_balance():
    print(f"Your current balance is ₹{balance}")

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ₹{amount},New balance: ₹{balance}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew ₹{amount}, New balance: ₹{balance}")
    else:
        print("Insufficient balance!")


while True:
    print("ATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        deposit(amount)
    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        withdraw(amount)
    elif choice == "4":
        print("Exited!")
        break
    else:
        print("Invalid option. Please choose again.")
