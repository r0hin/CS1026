fullname = input("Enter your full name: ")

# Check if contains a space
if (not " " in fullname):
  print("Invalid")

print("First letter: ", fullname[0])
print("Last letter: ", fullname[-1])