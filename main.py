from functions import *
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
            
                
                


if __name__ == "__main__":
    main()