def deposit(self, amount):
    """Deposit money into the account."""
    if amount > 0:
        self.__account_balance += amount
        print(f"Deposited: ${amount:.1f}")
    else:
        print("Deposit amount must be positive.")

def withdraw(self, amount):
    """Withdraw money from the account if sufficient balance exists."""
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return False
    elif amount > self.__account_balance:
        print("Insufficient funds.")
        return False
    else:
        self.__account_balance -= amount
        print(f"Withdrew: ${amount:.1f}")
        return True

def display_balance(self):
    """Display the current account balance."""
    print(f"Current Balance: ${self.__account_balance:.1f}")

