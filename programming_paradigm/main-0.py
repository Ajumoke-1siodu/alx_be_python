import sys
from bank_account import BankAccount

def main():
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <operation> [amount]")
        print("Operations: deposit, withdraw, balance")
        sys.exit(1)

    operation = sys.argv[1].lower()

    if operation == "deposit":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py deposit <amount>")
            sys.exit(1)
        amount = float(sys.argv[2])
        account.deposit(amount)
        account.display_balance()

    elif operation == "withdraw":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py withdraw <amount>")
            sys.exit(1)
        amount = float(sys.argv[2])
        account.withdraw(amount)
        account.display_balance()

    elif operation == "balance":
        account.display_balance()

    else:
        print("Invalid operation. Use: deposit, withdraw, or balance.")

if __name__ == "__main__":
    main()
