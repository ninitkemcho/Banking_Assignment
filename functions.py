accounts = {}  
def add_account(name, amount, unique_IBAN):
    accounts[unique_IBAN]={'name': name, 'balance': amount}
import random
def generate_unique_IBAN():
    while True:
        iban = 'TB' 
        for i in range(4):
            iban+=random.choice('0123456789')
        if iban not in accounts:
            return iban     