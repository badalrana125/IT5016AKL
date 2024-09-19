class Account:
 
    def __init__(self, owner, balance=0): 
       self.owner = owner # Public attribute 
       self._balance = balance # Private attribute 
  
    def deposit(self, amount): 
      if amount>0: 
       self.balance += amount
       print(F"${amount} deposited.")
      else: 
        print("Deposit amount must be positive.") 
    def withdraw(self, amount): 
       if 0<amount <= self.balance: 
        self._balance-= amount
        print(f"${self.amount} withdrawn.") 
        print("Insufficient balance or invalid amount.") 
    def get_balance(self): 
     return self.balance 

account = Account("James", 100) 


account.deposit(50) # Output: $50 deposited.
print(account.get_balance())# Output: 150 
account.withdraw(75) # Output: $75 withdrawn. 
print(account.get_balance())# Output: 75 
