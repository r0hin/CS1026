while True:
  age = int(input("Enter your age: "))
  if age < 0:
    break
  if age < 18:
    print("Sorry, you can't drive.")
  else:
    print("You can drive.")