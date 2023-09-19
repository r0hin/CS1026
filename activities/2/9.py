phone = input("Enter your phone number: ")

# Digits 0-9
if (str(phone).isdigit()):
  pass;
else:
  print("Not a number.")
  exit()

phone = int(phone)

if (phone > 999999999 and phone < 10000000000):
  pass;
else:
  print("Wrong # of digits.")
  exit()

if (str(phone).startswith("226")):
  pass;
else:
  print("Not start with 226.")
  exit()

formatted = str(phone)[0:3] + "-" + str(phone)[3:6] + "-" + str(phone)[6:10]

print("Valid phone number.")
print("Formatted: " + formatted)