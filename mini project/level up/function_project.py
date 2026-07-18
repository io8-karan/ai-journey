# Create a menu-driven program using functions
# 1 . Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit
balance=10000
while True:
    print("A T M")
    print("choice == 1 → |Deposit")
    print("choice == 2 → check balance & show balance")
    print("choice == 3 → Withdraw Money")
    print("choice == 4 → exit")
    choice=int(input("Enter a choice:"))
    if choice==1:
     print("deposit")
     
     def deposit(amount):
        num=int(input("Enter a amount you want to add"))
        amount+=num
        return amount     
     balance=deposit(balance)
    elif choice==2:
       print("check balance")
       def check(amount):
          return amount
       print(check(balance))
    elif choice==3:
       print("Withdraw |Money")
       def withdraw(amount):
         num=int(input("Enter a amount you want to add"))
         amount-=num
         return amount 
       balance=withdraw(balance)
    elif choice==4:
       print("exit")
       break
print("Total Balance is:",balance)