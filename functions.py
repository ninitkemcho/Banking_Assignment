import random

accounts = {}
transaction_history = {}
balance_history = {}

def add_account(name, amount, unique_IBAN):
    accounts[unique_IBAN] = {'name': name, 'balance': amount}
    transaction_history[unique_IBAN] = []
    add_transaction(unique_IBAN, "Deposit", amount)

def add_transaction(iban, transaction_type, amount):
    if iban in transaction_history:
        transaction_history[iban].append({"type": transaction_type, "amount": amount})

def generate_unique_IBAN():
    while True:
        iban = 'TB'
        for i in range(4):
            iban += random.choice('0123456789')
        if iban not in accounts:
            return iban

def deposit_funds(iban, amount):
    if iban in accounts:
        accounts[iban]['balance'] += amount
        add_transaction(iban, "Deposit", amount)
        print("Deposit successful")
    else:
        print("Invalid IBAN")

def get_account_details(iban):
    if iban in accounts:
        print(f"Account Holder: {accounts[iban]['name']}")
        print(f"Current Balance: {accounts[iban]['balance']} GEL")
    else:
        print("Invalid IBAN")

def calculate_loan(iban, loan_amount):
    if iban in accounts:
        LOAN_INTEREST_RATE = 0.082  # Fixed loan interest rate (8.2%)
        total_payable = loan_amount * (1 + LOAN_INTEREST_RATE)
        print(f"Total payable amount (including interest): {total_payable} GEL")
        confirm_loan = input("Do you want to proceed with the loan? (y/n) ")
        if confirm_loan.lower() == "y":
            accounts[iban]['balance'] += loan_amount
            add_transaction(iban, "Loan", loan_amount)
            print("Loan amount added to your account balance.")
    else:
        print("Invalid IBAN")