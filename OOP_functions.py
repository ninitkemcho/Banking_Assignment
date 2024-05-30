import random
from datetime import datetime

class Account:
    def __init__(self, name, initial_balance, iban):
        self.name = name
        self.iban = iban
        self.balance = initial_balance
        self.transaction_history = []
        self.balance_history = [f"{iban} filled with {initial_balance}₾"]
        self.add_transaction("Deposit", initial_balance)
    
    def add_transaction(self, transaction_type, amount):
        self.transaction_history.append({"type": transaction_type, "amount": amount})
    
    def deposit_funds(self, amount):
        self.balance += amount
        self.add_transaction("Deposit", amount)
        print("Deposit successful")
    
    def transfer_funds(self, receiver_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            receiver_account.balance += amount
            self.add_transaction("Transfer", -amount)
            receiver_account.add_transaction("Transfer", amount)
            print(f"Successfully transferred {amount}₾ from {self.iban} to {receiver_account.iban}")
        else:
            print("Not enough balance")
    
    def get_details(self):
        return f"Account Holder: {self.name}\nCurrent Balance: {self.balance} GEL"
    
    def get_transaction_history(self, category="both"):
        if category == "both":
            return self.transaction_history + self.balance_history
        elif category == "balance":
            return self.balance_history
        elif category == "transfer":
            return self.transaction_history
    
    def save_to_file(self, filename="transactions.txt"):
        text = f"{self.name}, {self.iban}, {self.balance}\n"
        with open(filename, 'a') as file:
            file.write(text)
    
    def save_user_to_csv(self, filename="users.csv"):
        text = f"{self.iban}, {self.name}, {self.balance}\n"
        with open(filename, "a") as file:
            file.write(text)
    
    def save_transaction_to_csv(self, receiver_iban, amount, filename="transaction.csv"):
        text = f"From {self.iban}, to {receiver_iban}, {amount}, {datetime.now()}\n"
        with open(filename, 'a') as file:
            file.write(text)

class Loan:
    LOAN_INTEREST_RATE = 0.082  # Fixed loan interest rate (8.2%)

    def calculate_loan(account, loan_amount):
        total_payable = loan_amount * (1 + Loan.LOAN_INTEREST_RATE)
        term = int(input("Enter desired loan period in months: "))
        print(f"Total payable amount (including interest): {total_payable} GEL")
        Loan.loan_payment_plan(loan_amount, term)
        confirm_loan = input("Do you want to proceed with the loan? (yes/no) ")
        if confirm_loan.lower() == "yes":
            account.deposit_funds(loan_amount)
            print(f"{loan_amount} added to your account balance.")
            account.balance_history.append(f"{loan_amount} added to {account.iban}")
            account.save_to_file()
        else:
            print("Loan cancelled")

    def loan_payment_plan(loan_amount, term):
        interest_rate = Loan.LOAN_INTEREST_RATE
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
                file.write(f"{payment['Month']}, {payment['Total Payment']}, {payment['Principal Payment']}, {payment['Interest Payment']}, {payment['Remaining Balance']}\n")
        return payments

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, initial_balance):
        unique_IBAN = self.generate_unique_IBAN()
        account = Account(name, initial_balance, unique_IBAN)
        self.accounts[unique_IBAN] = account
        account.save_to_file()
        account.save_user_to_csv()
        print(f"Account added successfully with IBAN: {unique_IBAN}")
    
    def get_account(self, iban):
        return self.accounts.get(iban, None)
    
    def generate_unique_IBAN(self):
        while True:
            iban = 'TB'
            iban += ''.join(random.choices('0123456789', k=4))
            if iban not in self.accounts:
                return iban
    
    def clear_file(self, filename):
        with open(filename, "w"):
            pass
