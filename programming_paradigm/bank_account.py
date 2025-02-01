class BankAccount:
    """Initialize the bank account with an optional starting balance (default is 0)."""
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
        
        
    def deposit(self, amount):
       """"Add money to the account.""" 
       self.account_balance += amount
       
       
    def withdraw(self, amount):
        """"Withdraw money if there are sufficient funds."""
        if amount > self.account_balance:
            return False   # Not enough money
        self.account_balance -= amount
        return True  # Successful withdrawal
    
    def display_balance(self):
        """"Print the current balance."""
        print(f"Current Balance: ${self.account_balance}")
         