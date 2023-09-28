# Simple ATM program

# Initialize account balance
balance = 1000

# Function to display account balance
def display_balance():
    print(f"Your account balance is ${balance:.2f}")

# Function to deposit funds
def deposit():
    global balance
    amount = float(input("Enter the amount to deposit: $"))
    if amount > 0:
        balance += amount
        print(f"${amount:.2f} has been deposited.")
    else:
        print("Invalid amount. Please enter a positive value.")

# Function to withdraw funds
def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"${amount:.2f} has been withdrawn.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        print("Invalid amount. Please enter a positive value.")

# Main program loop
while True:
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        display_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
