from OOP_functions import Bank, Loan

def main():
    bank = Bank()
    
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
            bank.add_account(name, amount)
            
        elif choice == 2:
            while True:
                iban = input("Please enter your IBAN: ")
                account = bank.get_account(iban)
                if not account:
                    print("Invalid IBAN")
                else:
                    break
            while True:
                amount = input("Please enter the amount to deposit: ")
                if not amount.replace('.','',1).isdigit():
                    print("Invalid Amount")
                else:
                    break
            account.deposit_funds(float(amount))
            account.save_to_file()
            account.balance_history.append(f'{iban} filled with {amount}₾')
            
        elif choice == 3:
            while True:
                sender_iban = input("Enter sender's IBAN: ")
                sender_account = bank.get_account(sender_iban)
                if not sender_account:
                    print('Invalid IBAN')
                else:
                    break

            while True:
                receiver_iban = input("Enter receiver's IBAN: ")
                receiver_account = bank.get_account(receiver_iban)
                if not receiver_account:
                    print('Invalid IBAN')
                else:
                    break

            while True:
                amount = input("Enter amount to transfer: ")
                if amount.replace('.','',1).isdigit():
                    amount = float(amount)
                else:
                    print('Enter valid number')
                    continue
                
                if sender_account.balance < amount:
                    print("Not enough balance")
                    continue
                else:
                    break
                
            sender_account.transfer_funds(receiver_account, amount)
            sender_account.save_to_file()
            receiver_account.save_to_file()
            sender_account.save_transaction_to_csv(receiver_iban, amount)
            
        elif choice == 4:
            while True:
                iban = input("Please enter your IBAN: ")
                account = bank.get_account(iban)
                if not account:
                    print("Invalid IBAN")
                else:
                    break
            print(account.get_details())
            
        elif choice == 5:
            while True:
                iban = input('Enter IBAN to check history: ')
                account = bank.get_account(iban)
                if not account:
                    print('Enter valid IBAN')
                else:
                    break
            
            category = input('Add filter type (balance/transfer/both): ')
            history = account.get_transaction_history(category)
            for record in history:
                print(record)
                
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
                account = bank.get_account(iban)
                if not account:
                    print("Invalid IBAN")
                else:
                    break
            Loan.calculate_loan(account, loan_amount)

        elif choice == 7:
            bank.clear_file("transactions.txt")
            exit("Goodbye")

if __name__ == "__main__":
    main()
