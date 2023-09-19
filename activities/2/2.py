balance = int(input("Enter your balance: "))
withdrawal = int(input("Enter the amount to withdraw: "))

if (withdrawal > balance):
  print("Insufficient balance")
else:
  print("Transaction successful")
  print("Remaining balance: ", balance - withdrawal)