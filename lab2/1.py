age = int(input("Enter your age: "))
if age >= 9:
  height = float(input("Enter your height in cm: "))
  if height > 130:
    print("You may go on this ride!")
  else:
    print("You are too short.")
else:
  print("You are too young.")

