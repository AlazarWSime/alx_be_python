class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0
    
    def withdraw(self, amount):
       try:
          if amount < self.account_balance:
             self.account_balance -= amount
             return True
          else: 
           return False
       except (ValueError, TypeError):
           print("Invalid withdaral amount.")
           return False

    def deposit(self, amount):
      try:
               
         self.account_balance += amount
         return True
             
      except (ValueError, TypeError):
         
         print("Invalid deposit amount.")
         return False
      
    def display_balance(self):
        print(f"your current Balance: ${self.account_balance}")
