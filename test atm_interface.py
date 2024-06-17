class ATM:
    def __init__(self, accounts):
        self.accounts = accounts

    def authenticate_user(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number]['pin'] == pin:
            self.current_account = self.accounts[account_number]
            return True
        return False

    def get_balance(self):
        return self.current_account['balance']

    def deposit(self, amount):
        self.current_account['balance'] += amount

    def withdraw(self, amount):
        if amount <= self.current_account['balance']:
            self.current_account['balance'] -= amount
            return True
        return False

def main():
    accounts = {
        '123456': {'pin': '1234', 'balance': 1000},
        '654321': {'pin': '4321', 'balance': 500}
    }

    atm = ATM(accounts)

    print("Welcome to the ATM")

    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    if atm.authenticate_user(account_number, pin):
        while True:
            print("\nMenu:")
            print("1. Balance Inquiry")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                print(f"Your balance is: ${atm.get_balance()}")
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
                print(f"${amount} deposited. Your new balance is: ${atm.get_balance()}")
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                if atm.withdraw(amount):
                    print(f"${amount} withdrawn. Your new balance is: ${atm.get_balance()}")
                else:
                    print("Insufficient balance!")
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Authentication failed. Please check your account number and PIN.")

if __name__ == "__main__":
    main()
