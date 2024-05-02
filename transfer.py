accounts={"TB0016": {'name':"Nini", 'surname': 'Tkemaladze', 'amount': 0},
          "TB0008": {'name':"Nicolas", 'surname': 'Tsagareli', 'amount': 0}}

def transfer(sender, receiver, amount):
    if accounts[sender]['amount']-amount>=0:
        for iban in accounts:
            if iban==sender:
                accounts[sender]['amount']-=amount
            elif iban==receiver:
                accounts[receiver]['amount']+=amount
        tr=f'{sender} transferred {amount}₾ to {receiver}'
        add_transfer_history(sender, tr)
        add_transfer_history(receiver, tr)
        return accounts
    else:
        print('Not enough balance')
        

def add_balance_history(iban, history):
    balance_history[iban].append(history)
    return balance_history

def add_transfer_history(iban, history):
    transfer_history[iban].append(history)
    return transfer_history