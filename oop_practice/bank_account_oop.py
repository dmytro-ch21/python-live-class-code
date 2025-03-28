class BankAccount:
    # This variable is declared outside of any methods
    # It will be accessible for all objects generated from BankAccount class
    # To access it we just call the Class.variable
    transaction_fee = 7.99
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    # methods 
    def deposit(self, amount):
        if amount <= 0:
            print(f"Deposit should be more than 0. Provided: {amount}")
            return False
        self.balance += amount
        print(f"{self.owner}'s new balance: ${self.balance}")
        return True
        
    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            print(f"Insufficient funds or improper amount provided")
            return False
        self.balance -= amount    
        print(f"{self.owner}'s new balance: ${self.balance}")
        return True
        
    def print_info(self):
        print(f"========= {self.owner}'s Account Overview ===========")
        print(f"Name: {self.owner}")
        print(f"Balance: ${self.balance}")
        
          
# ========================= Practice ======================
      
       
alice_account = BankAccount("Alice", 2000)
alice_account.print_info()
alice_account.deposit(2000)
alice_account.withdraw(500)

alice_account.print_info()

# modify the data/attributes of an object 
alice_account.owner = "Alice Baker"
alice_account.print_info()

# if no validation in deposit and withdraw 
# we can break the logic 
operation_success = alice_account.deposit(-5000)

operation_success = alice_account.deposit(5000)
alice_account.print_info()

if operation_success:
    print(f"Transaction Fee: ${BankAccount.transaction_fee}")
    alice_account.balance -= BankAccount.transaction_fee



alice_account.print_info()

alice_account.withdraw(-9000)
alice_account.print_info()
alice_account.print_info()


