# real world atm problem   User has balance = 10000
# ATM should:
# 1. Ask user to enter withdrawal amount
# 2. If amount > balance → "Insufficient balance"
# 3. If amount <= 0 → "Invalid amount"
# 4. If amount is valid → deduct and show remaining balance
# 5. Ask again and again until user enters 0 to exit


balance=10000
i=0
while True:
 amount=int(input("Enter your withdrawal amount="))
 if amount==0:
   print("Thanku And good bye ")
   break
 elif amount>balance:
    print("Insufficient Balance")
 elif amount<0:
   print("Invalid amount")
 else:
   remaining_balance=balance-amount
   print("remaining balance=",remaining_balance)  
   balance=remaining_balance
   print("new updated balance",balance)