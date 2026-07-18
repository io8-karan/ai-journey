
class BankAccount:
       def __init__(self,account_holder,balance=0):
           self.account_holder=account_holder
           self.balance=balance
       def deposit(self,amount):
           self.balance +=amount
          
       def withdraw(self,detect_amount):
           self.balance -= detect_amount
          
       def show_balance(self):
           return self.balance
class Account(BankAccount):
       def __init__(self,account_holder,balance):
           super(). __init__(account_holder,balance)
       def __str__(self):
           return f"Name:{self.account_holder}\nBalance:{self.balance}"
class SavingAccount(Account):
        def __init__(self,account_holder,balance,rate,time):
            super().__init__(account_holder,balance)
            self.rate=rate
            self.time=time
        def interestt(self):
             self.interest=(self.rate * self.time * self.balance) / 100
             self.balance += self.interest
             print("after adding interest balance is:",self.balance)
          
        def withdraw(self,amount):
            if self.balance - amount >= 1500:
                self.balance -= amount
                return self.balance
            else:
                print("no wothdraw of minimum balance")
                return self.balance
        def show(self):
            print(f"Rate of Interest is {self.interest}") 
          
        def __str__(self):
           return f"Name:{self.account_holder}\nBalance:{self.balance}\nRate:{self.rate}\nTime:{self.time}"   
o=Account("KAran",25000)
o.deposit(25000)
print(o)