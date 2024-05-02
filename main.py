import random
from functions import add_account, accounts
def generate_unique_IBAN():
    while True:
        iban = 'TB' 
        for i in range(4):
            iban+=random.choice('0123456789')
        if iban not in accounts:
            return iban       
def main():
    while True:
        menu = ["1. Create bank account", "2. Control balance", "3. Transfer money", "4. Account details", "5. Account history", "6. Loan calculator", "7. Exit"]
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
            print(f"Account added successfully with IBAN: {unique_IBAN}")
if __name__ == "__main__":
    main()