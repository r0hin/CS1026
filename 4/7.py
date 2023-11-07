password = input("Enter your password: ")

acceptable = True;

if len(password) < 10:
  acceptable = False

hasDigit = False
hasSpecial = False
hasUpper = False

for char in password:
  if char.isdigit():
    hasDigit = True
  elif char.isupper():
    hasUpper = True
  elif not char.isalnum():
    hasSpecial = True

if not hasDigit or not hasSpecial or not hasUpper:
  acceptable = False

if (acceptable):
  print("Your password is acceptable.")
else:
  print("Your password is not acceptable.")