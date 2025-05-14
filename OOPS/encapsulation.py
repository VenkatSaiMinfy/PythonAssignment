class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid withdrawal amount.")
    
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number

account = BankAccount("123456", 1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(200)
print(account.get_balance())
print(account.get_account_number())

try:
    account.__balance = 2000
except AttributeError:
    print("Cannot directly access private attribute")
