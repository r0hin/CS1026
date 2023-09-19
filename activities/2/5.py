drink = input("Enter your drink: ")
if (drink == "coffee"):
  age = int(input("Enter your age: "))
  if (age > 9):
    print("Coffee is served.")
  else:
    print("You are not eligible to drink coffee.")
else:
  print(drink.capitalize(), "is served.")
