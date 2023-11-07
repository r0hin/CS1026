age = input("Enter your age: ")
account = input("Do you have an account? (y/n): ")

if (account == "y"):
  if (age >= 18):
    print("You have access to all features.")
  else:
    print("You have limited access to some features.")
else:
  if (age >= 18):
    print("You can create an account to have all features.")
  else:
    print("You can create an account to have limited access to some features.")
    