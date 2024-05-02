accounts={"TB0016": {'name':"Nini", 'surname': 'Tkemaladze', 'amount': 0},
          "TB0008": {'name':"Nicolas", 'surname': 'Tsagareli', 'amount': 0}}


def transfer(sender, receiver, amount):
    enough_balance
    sender_exists
    if accounts[sender]['amount']-amount>=0:
        for iban in accounts:
            if iban==sender:
                accounts[sender]['amount']-=amount
            elif iban==receiver:
                accounts[receiver]['amount']+=amount
        tr=f'{sender} transferred {amount}₾ to {receiver}'
        history['sender'].append(tr)
        
        return accounts
    else:
        print('Not enough balance')
        return 
        
print(accounts['TB0016']['amount'])

history={}
history={:{balance:[],transfer:[],}}
tr=f'{sender} transferred {amount}₾ to {receiver}'

history['TB0008']={}
history['TB0008']['transfer']=[tr]
