accounts = {}  
def add_account(name, amount, unique_IBAN):
    accounts[unique_IBAN]={'name': name, 'balance': amount}