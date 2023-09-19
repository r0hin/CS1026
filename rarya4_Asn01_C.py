''''
  CS1026a 2023
  Assignment 01 Project 0B - Part C
  Rohin Arya
  251371185
  rarya4
  Sept 18, 2023
'''

# Get starting number
start_num = input("The starting number of transistors: ") or "17"
# Get starting year
start_year = input("The year to start calculations from: ") or "1957"
# Get number of years
num_years = input("The number of years to calculate for: ") or "30"

# Print the table header
print("YEAR : TRANSISTORS : FLOPS")

# Variable to decide whether to skip current year or not
skip_year = False # Skip every second year

# Loop through the years
for year in range(int(start_year), int(start_year) + int(num_years) + 1):
  if skip_year: # Skip every second year
    skip_year = False
    continue
  else:
    skip_year = True

  # Calculate the exponent (number of doublings)
  exponent = (((year - int(start_year) + 1) / 2) - 0.5)

  # Transistors = start_num * 2 ^ exponent (expontent = number of doublings)
  transistors = int(start_num) * (2 ** int(exponent))

  # Calculate the number of flops
  flops = transistors * 50

  label = "" # The label for the number
  # Use copied variable number to preserve original number
  num = flops
  # Get kilo, mega, giga, tera, peta, exa, etc
  if flops > 1000:
    label = "kiloFLOPS"
    num = flops / 1000
  if flops > 1000000:
    label = "megaFLOPS"
    num = flops / 1000000
  if flops > 1000000000:
    label = "gigaFLOPS"
    num = flops / 1000000000
  if flops > 1000000000000:
    label = "teraFLOPS"
    num = flops / 1000000000000
  if flops > 1000000000000000:
    label = "petaFLOPS"
    num = flops / 1000000000000000
  if flops > 1000000000000000000:
    label = "exaFLOPS"
    num = flops / 1000000000000000000
  
  # Format the number to 2 decimal places
  num = format(num, ".2f")

  # Add commas to the number in new variable
  commad_number = format(flops, ",d")

  # Print the table row
  print(str(year) + " : " + str(format(transistors, ",d")) + " : " + str(num) + " " + label + " " + str(commad_number))

# END: Assignment 01 Project 0B - Part C
print("Rohin Arya rarya4 251371185")