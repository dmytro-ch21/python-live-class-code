class BankAccount:
    def __init__(self, owner, account_number, balance = 0):
        self.owner = owner
        self._account_type = "Checking"
        self.__account_number = account_number
        self.__balance = balance
        
    def deposit(self, amount):
           if amount <= 0:
               return False
           self.__balance += amount
           return True
       
    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            return False
        self.__balance -= amount 
        return True
    
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def set_owner(self, new_owner):
        if not new_owner: # None, "", etc...
            print(f"The value {new_owner} is not valid!")
            return False
        self.owner = new_owner
        return True
    
       
# ================ Practice ===================
account = BankAccount("Alice Baker", 456_243_3244, 5000.0)
print(account.get_balance())
print(account.get_account_number())

# access variabes - not recommended
account.owner = "Alice M Baker"
print(account.owner)
# to avoid such situatians thatr a property gets assigned None or empty 
# we can create a setter method to update the field
# account.owner = None 
# print(account.owner)

account.set_owner("Alice Michelle Baker")
print(account.owner)

account.set_owner("")
print(account.owner)

account.set_owner(None)
print(account.owner)
