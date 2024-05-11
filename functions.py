import random
from datetime import datetime

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
    LOAN_INTEREST_RATE = 0.082  # Fixed loan interest rate (8.2%)
    total_payable = loan_amount * (1 + LOAN_INTEREST_RATE)
    term=input("Enter desired loan period in months: ")
    print(f"Total payable amount (including interest): {total_payable} GEL")
    loan_payment_plan(loan_amount=loan_amount, term=term)
    confirm_loan = input("Do you want to proceed with the loan? (yes/no) ")
    if confirm_loan.lower() == "yes":
        accounts[iban]['balance'] += loan_amount
        add_transaction(iban, "Loan", loan_amount)
        print(f"{loan_amount} added to your account balance.")
        bal=f'{loan_amount} added to {iban}'
        add_balance_history(iban,bal)
        append_history_to_txt(iban)
    else:
        print("Loan cancelled")

def loan_payment_plan(loan_amount, term):
    interest_rate = 0.082
    loan_amount = int(loan_amount)
    term = int(term)
    total_payment = loan_amount * (1 + interest_rate)
    monthly_payment = total_payment / term
    monthly_interest_payment = (loan_amount * interest_rate) / term
    remaining_balance = loan_amount
    payments = []
    for month in range(1, term + 1):
        principal_payment = monthly_payment - monthly_interest_payment
        remaining_balance -= principal_payment
        payments.append({
            "Month": month,
            "Total Payment": round(monthly_payment, 2),
            "Principal Payment": round(principal_payment, 2),
            "Interest Payment": round(monthly_interest_payment, 2),
            "Remaining Balance": round(max(remaining_balance, 0), 2)
        })
    with open('loan_payment_plan.csv', 'w') as file:
        file.write("Month, Total Payment, Principal Payment, Interest Payment, Remaining Balance\n")
        for payment in payments:
            if "Month" in payment: 
                file.write(f"{payment['Month']}, {payment['Total Payment']}, {payment['Principal Payment']}, {payment['Interest Payment']}, {payment['Remaining Balance']}\n")
    return payments

def transfer(sender, receiver, amount):
    if accounts[sender]['balance']-amount>=0:
        for iban in accounts:
            if iban==sender:
                accounts[sender]['balance']-=amount
            elif iban==receiver:
                accounts[receiver]['balance']+=amount
        tr=f'{sender} transferred {amount}₾ to {receiver}'
        add_transaction_history(sender, tr)
        add_transaction_history(receiver, tr)
        return accounts
    else:
        print('Not enough balance')
        
def add_balance_history(iban, history):
    balance_history[iban].append(history)
    return balance_history

def add_transaction_history(iban, history):
    transaction_history[iban].append(history)
    return transaction_history

def append_history_to_txt(iban):
    text = f"{accounts[iban]['name']}, {iban}, {accounts[iban]['balance']}\n"
    with open("transactions.txt", 'a') as file:
        file.write(text)
def add_user_to_csv(name,iban,balance):
    text = f"{iban}, {name}, {balance}\n"
    with open("users.csv", "a") as file:
        file.write(text)
def add_transaction_to_transactioncsv(sender,receiver,amount):
    text = f"From {sender}, to {receiver}, {amount}, {datetime.now()}\n"
    with open("transaction.csv", 'a') as file:
        file.write(text)

def clear_file(filename):
    with open(filename, "w"):
        pass

