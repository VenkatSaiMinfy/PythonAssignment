class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print(rect.area())
print(rect.perimeter())


class Counter:
    def __init__(self):
        self.value = 0
    
    def increment(self):
        self.value += 1
    
    def decrement(self):
        self.value -= 1
    
    def reset(self):
        self.value = 0

counter = Counter()
counter.increment()
counter.increment()
print(counter.value)
counter.decrement()
print(counter.value)
counter.reset()
print(counter.value)


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, doors, fuel_type):
        super().__init__(make, model, year)
        self.doors = doors
        self.fuel_type = fuel_type

car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
print(car.make)
print(car.doors)


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
