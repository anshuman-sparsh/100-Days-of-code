INR_TO_USD_RATE = 83.0

def convert_inr_to_usd():
    try:
        inr = float(input("Enter amount in INR: ₹"))
        usd = inr / INR_TO_USD_RATE
        print(f"₹{inr:,.2f} is equal to ${usd:,.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def convert_usd_to_inr():
    try:
        usd = float(input("Enter amount in USD: $"))
        inr = usd * INR_TO_USD_RATE
        print(f"${usd:,.2f} is equal to ₹{inr:,.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\n--- Currency Converter ---")
        print("1. Convert INR to USD")
        print("2. Convert USD to INR")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            convert_inr_to_usd()
        elif choice == '2':
            convert_usd_to_inr()
        elif choice == '3':
            print("Exiting converter.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()