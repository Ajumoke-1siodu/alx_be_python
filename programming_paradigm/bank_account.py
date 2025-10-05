class BankAccount:
        def __init__(self, initial_balance=0.0):
                    """Initialize the account with an optional initial balance."""
                            self.account_balance = initial_balance

                                def deposit(self, amount):
                                            """Add money to the account."""
                                                    if amount > 0:
                                                                    self.account_balance += amount
                                                                                print(f"Deposited: ₦{amount:.2f}")
                                                                                        else:
                                                                                                        print("Deposit amount must be positive.")

                                                                                                            def withdraw(self, amount):
                                                                                                                        """Withdraw money if sufficient funds exist."""
                                                                                                                                if amount <= 0:
                                                                                                                                                print("Withdrawal amount must be positive.")
                                                                                                                                                            return False
                                                                                                                                                                if amount > self.account_balance:
                                                                                                                                                                                print("Insufficient funds!")
                                                                                                                                                                                            return False
                                                                                                                                                                                                self.account_balance -= amount
                                                                                                                                                                                                        print(f"Withdrew: ₦{amount:.2f}")


