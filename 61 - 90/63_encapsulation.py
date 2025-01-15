class BankAccount:
    def __init__(self):
        self._balance = 0
    
    def get_balance(self):
        return self._balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount

account = BankAccount()
account.set_balance(100)
print(account.get_balance())