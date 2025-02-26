class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def get_customer(self, customer_id):
        return self.customers.get(customer_id, None)

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def get_accounts(self):
        return self.accounts

class BankAccount:
    def __init__(self, account_number, customer, balance=0.0):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def display_details(self):
        print(f"Account Number: {self.account_number}, Owner: {self.customer.name}, Balance: ${self.balance:.2f}")

# Example usage
bank = Bank("ABC Bank")

# Creating customers
customer1 = Customer(101, "Krunal")
customer2 = Customer(102, "Aditya")

bank.add_customer(customer1)
bank.add_customer(customer2)

# Creating bank accounts
account1 = BankAccount("A101", customer1, 5000.0)
account2 = BankAccount("A102", customer2, 1000.0)

customer1.open_account(account1)
customer2.open_account(account2)

# Transactions
account1.deposit(200)
account1.withdraw(100)
account1.display_details()
print(" ")
account2.deposit(500)
account2.withdraw(1600)  
account2.display_details()
