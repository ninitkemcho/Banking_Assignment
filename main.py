from functions import *
from transfer import transfer
def main():
    while True:
        menu = ["1. Create bank account", "2. Add balance", "3. Transfer money", "4. Account details", "5. Account history", "6. Loan calculator", "7. Exit"]
        for i in menu:
            print(i)
        choice = int(input("Enter number: "))
        if choice == 1:
            name = input("To create account, enter your name: ")
            while True:
                amount = int(input("Enter initial balance (0 -> 100): "))
                if amount > 100:
                    print("Initial balance should not be more than 100 GEL")
                else:
                    break           
            unique_IBAN = generate_unique_IBAN()
            add_account(name, amount, unique_IBAN)
            transaction_history[unique_IBAN] = []
            balance_history[unique_IBAN] = []
            print(f"Account added successfully with IBAN: {unique_IBAN}")
        elif choice == 2:
            while True:
                iban = input("Please enter your IBAN: ")
                if iban not in accounts:
                    print("Invalid IBAN")
                else:
                    break
            while True:
                amount = input("Please enter the amount to deposit: ")
                if not amount.replace('.','',1).isdigit():
                    print("Invalid Amount")
                else:
                    break
            deposit_funds(iban,float(amount))
        elif choice==3:
            while True:
                sender=input("Enter sender's IBAN: ")
                if sender not in accounts:
                    print('Invalid IBAN')
                else:
                    break

            while True:
                receiver=input("Enter receiver's IBAN: ")
                if receiver not in accounts:
                    print('Invalid IBAN')
                else:
                    break

            while True:
                amount=input("Enter amount to transfer: ")
                if amount.replace('.','',1).isdigit():
                    amount=float(amount)
                else:
                    print('Enter valid number')
                    continue
                
                if accounts[sender]['amount']<amount:
                    print("Not enough balance")
                    continue
                else:
                    break

            transfer(sender, receiver, amount)
            print(f'Succesfully transfered {amount}₾ from {sender} to {receiver}')
        elif choice == 4:
            while True:
                iban = input("Please enter your IBAN: ")
                if iban not in accounts:
                    print("Invalid IBAN")
                else:
                    break
            for i,v in accounts.items():
                if i == iban:
                    print(f"{v['name']},Your Balance Is {v['balance']}")
        elif choice==5:
            while True:
                iban=input('Enter IBAN to check history: ')
                if iban not in accounts:
                    print('Enter valid IBAN')
                else:
                    break
            
            category=input('Add filter type (balance/transfer/both): ')

            if category=="both":
                if iban in transaction_history:
                    for transaction in transaction_history[iban]:
                        print(transaction)
                if iban in balance_history:
                    for balance in balance_history[iban]:
                        print(balance)
            elif category=='balance':
                if iban in balance_history:
                    for balance in balance_history[iban]:
                        print(balance)
            else:
                if iban in transaction_history:
                    for transaction in transaction_history[iban]:
                        print(transaction)
        elif choice == 6:
            while True:
                loan_amount = input("Please enter the Loan Amount: ")
                
                if not loan_amount.replace('.','',1).isdigit():
                    print("Invalid Amount!")
                else:
                    loan_amount = float(loan_amount)
                    break
            while True:
                iban = input("Please enter your IBAN: ")
                if iban not in accounts:
                    print("Invalid IBAN")
                else:
                    break
            calculate_loan(iban,loan_amount)
            print(accounts)


        
        elif choice == 7:
            exit("Goodbye")
if __name__ == "__main__":
    main()