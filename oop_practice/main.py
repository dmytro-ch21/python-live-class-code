# You can import other classes with import statement
# In python you can import thisng in different ways
# import module - imoprting a specif module/file in python
# -- this requires you to use the module name moving forward to access anything from it
# e.g bank_account_oop.BankAccount()

# Another apprach is to use the specific import with from and import
# from module import a_specific_thing

from bank_account_oop import BankAccount
# import bank_account_oop

alice_account = BankAccount("Alice", 2000)
print(alice_account.owner)
print(alice_account.balance)