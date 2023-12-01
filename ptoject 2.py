class BankingApp:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def view_balance(self):
        print(f"Your balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: +${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew: -${amount}")
        else:
            print("Insufficient funds")

    def view_transactions(self):
        if not self.transactions:
            print("No transaction history")
        else:
            print("Previous transactions:")
            for transaction in self.transactions:
                print(transaction)

# Example usage of the BankingApp class
def main():
    bank = BankingApp()

    while True:
        print("\n1. View Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. See Previous Transactions")
        print("5. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            bank.view_balance()
        elif choice == '2':
            amount = float(input("Enter deposit amount: $"))
            bank.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: $"))
            bank.withdraw(amount)
        elif choice == '4':
            bank.view_transactions()
        elif choice == '5':
            print("Thank you for using the banking app.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
