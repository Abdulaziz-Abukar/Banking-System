# We're importing the 'random' module to generate random account numbers.
import random

# Define a SingleAccount class that represents either a Checking or Savings account.


class SingleAccount:
    # Constructor method to initialize the account with type (Checking or Savings), balance, and transactions.
    def __init__(self, account_type):
        self.account_type = account_type  # Either "Checking" or "Savings"
        self.balance = 0.0  # Initial balance is set to 0.0
        self.transactions = []  # A list to store transactions

    # Method to deposit a specific amount to the account.
    def deposit(self, amount):
        self.balance += amount  # Increases the balance
        # Append the transaction details to the transaction list.
        self.transactions.append(
            f"Deposited ${format(amount, ',')} to {self.account_type}. Balance: ${format(self.balance, ',')}")
        # Inform the user about the deposited amount and the new balance.
        print(
            f"Deposited ${format(amount, ',')} to {self.account_type}. New balance: ${format(self.balance, ',')}")

    # Method to withdraw a specific amount from the account.
    def withdraw(self, amount):
        # Check if there's enough balance to withdraw.
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount  # Decrease the balance
        # Append the transaction details to the transactions list.
        self.transactions.append(
            f"Withdrew ${format(amount, ',')} from {self.account_type}. Balance: ${format(self.balance, ',')}")
        # Inform the user about the withdrawal and the new balance.
        print(
            f"Withdrew ${format(amount, ',')} from {self.account_type}. New balance: ${format(self.balance, ',')}")

    # Method to display the account's balance.
    def display_balance(self):
        print(f"{self.account_type} balance: ${format(self.balance, ',')}")

# Define a class for an Account which will have both Checking and Savings.


class Account:
    # Constructor method to initialize an account with an account number, holder's name, and associated SingleAccounts.
    def __init__(self, account_holder_name):
        # Randomly generate a 4-digit account number
        self.account_number = random.randint(1000, 9999)
        self.account_holder_name = account_holder_name
        # Create Checking and Savings accounts for this Account.
        self.checking = SingleAccount('Checking')
        self.savings = SingleAccount('Savings')

 # Method to show transactions for both Checking and Savings accounts.
    def show_transactions(self):
        # Check if there are no transactions.
        if not self.checking.transactions and not self.savings.transactions:
            print("No transactions available.")
            return
        print("Transaction History:")
        # Display Checking transactions.
        for transaction in self.checking.transactions:
            print(transaction)
        # Display Savings transactions.
        for transaction in self.savings.transactions:
            print(transaction)


# List to store all the created accounts.
accounts = []

# Function to create a new account.


def create_account():
    name = input("Enter your name: ")
    new_account = Account(name)
    accounts.append(new_account)  # Add the new account to the accounts list.
    print(
        f"Account created successfully! Your account number is {new_account.account_number}")

# Function to search for an account based on its account number.


def find_account(account_number):
    for acc in accounts:
        if acc.account_number == account_number:
            return acc
    return None

# Function for various banking operations after accessing an account.


def bank_operations(account):
    # The loop ensures that the banking operations continue until the user decides to exit.
    while True:
        # Present the user with options related to their bank operations.
        choice = input(
            "\n1. Deposit\n2. Withdraw\n3. Check Balances\n4. Transfer Funds\n5. View Transactions\n6. Exit\nChoose an option: ")

        # Deposit funds to either Checking or Savings based on the user's choice.
        if choice == "1":
            # Ask the user to specify the account type for deposit (Checking or Savings).
            acc_type = input("Deposit to Checking or Savings? ").capitalize()

            # A loop to ensure the user provides a valid deposit amount.
            while True:
                try:
                    # Ask the user for the deposit amount.
                    amount = float(input("Enter deposit amount: "))

                    # If the user provides a negative or zero amount, raise an error.
                    if amount <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid amount. Please enter a positive number.")

            # Deposit the provided amount to the selected account.
            if acc_type == "Checking":
                account.checking.deposit(amount)
            elif acc_type == "Savings":
                account.savings.deposit(amount)
            else:
                # If user does not select Checking or Savings.
                print("Invalid choice.")

        # Withdraw funds from either Checking or Savings based on the user's choice.
        elif choice == "2":
            acc_type = input(
                "Withdraw from Checking or Savings? ").capitalize()

            # A loop to ensure the user provides a valid withdrawal amount.
            while True:
                try:
                    # Ask the user for the withdrawal amount.
                    amount = float(input("Enter withdrawal amount: "))

                    # If the user provides a negative or zero amount, raise an error.
                    if amount <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid amount. Please enter a positive number.")

            # Withdraw the provided amount from the selected account.
            if acc_type == "Checking":
                account.checking.withdraw(amount)
            elif acc_type == "Savings":
                account.savings.withdraw(amount)
            else:
                # If user does not select Checking or Savings.
                print("Invalid choice.")

        # Display the balances of both the Checking and Savings accounts.
        elif choice == "3":
            account.checking.display_balance()
            account.savings.display_balance()

        # Transfer funds between Checking and Savings accounts.
        elif choice == "4":
            # Ask the user for the source and destination accounts for the transfer.
            source = input("Transfer from (Checking/Savings): ").capitalize()
            destination = input(
                "Transfer to (Checking/Savings): ").capitalize()

            # Ask the user for the transfer amount.
            amount = float(input("Enter transfer amount: "))

            # Transfer from Checking to Savings.
            if source == "Checking" and destination == "Savings":
                if amount <= account.checking.balance:
                    account.checking.withdraw(amount)
                    account.savings.deposit(amount)
                else:
                    print("Insufficient funds in Checking.")

            # Transfer from Savings to Checking.
            elif source == "Savings" and destination == "Checking":
                if amount <= account.savings.balance:
                    account.savings.withdraw(amount)
                    account.checking.deposit(amount)
                else:
                    print("Insufficient funds in Savings.")

            else:
                # If user does not select valid source/destination combination.
                print("Invalid transfer option.")

        # Display all the transactions for the account.
        elif choice == "5":
            account.show_transactions()

        # Exit the banking operations and return to the main menu.
        elif choice == "6":
            print("Exiting account operations.")
            break


# The main function that drives the banking system's interface.
def main():
    # This loop keeps the banking system running until the user decides to exit.
    while True:
        # Present the user with the main options of the banking system.
        print("\nEnhanced Banking System")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")

        # Capture the user's choice.
        option = input("Choose an option: ")

        # If the user chooses to create a new account.
        if option == "1":
            create_account()  # This function handles account creation.

        # If the user chooses to access an existing account.
        elif option == "2":
            # Ask the user to provide their account number.
            acc_number = int(input("Enter your account number: "))

            # Find the account using the provided account number.
            account = find_account(acc_number)

            # If the account is found, allow the user to perform bank operations on that account.
            if account:
                bank_operations(account)
            else:
                # Inform the user if the account number is not recognized.
                print("Account not found.")

        # If the user chooses to exit the banking system.
        elif option == "3":
            print("Thank you for using the Enhanced Banking System!")
            break  # Break out of the loop, effectively ending the program.


# Ensure the script only runs the main function if executed as the main module.
if __name__ == "__main__":
    main()
