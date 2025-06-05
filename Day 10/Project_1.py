# Project 1: Personal Expense Tracker
# 🔹 Project Goal
# Build a console-based expense tracker where users can add expenses, see their total, and check their balance.



print("=== Expense Tracker ===")

initial_balance = float(input("Add your starting balance: ₹"))
expenses=[]



def add_expense():
    amount = float(input("\n Enter expense: ₹"))
    expenses.append(amount)
    print(f"\n Added ₹{amount:.2f} to expenses!")

def show_expenses():
    print("\n All Expenses: ")
    for i, expense in enumerate(expenses, 1):  # Added numbering(LNT)
        print(f"{i}. ₹{expense:.2f}")  # Better formatting(LNT)


def show_total():
    print(f"\nTotal Spent: ₹{sum(expenses):.2f}")

def show_remaining():
    get_balance = initial_balance-sum(expenses)
    print(f"\n Remaining balance: ₹{get_balance:.2f}")

while True:
    print("\n Main Menu")
    print("1. Add Expense")
    print("2. Show All Expenses")
    print("3. Show Total Spent")
    print("4. Show Remaining Balance")
    print("5. Exit")

    choice = int(input("Enter your choice(1-5): "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        show_expenses()
    elif choice == 3:
        show_total()
    elif choice == 4:
        show_remaining()
    elif choice == 5:
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice! Please choose between 1-5.")
    