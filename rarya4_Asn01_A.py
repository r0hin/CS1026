''''
  CS1026a 2023
  Assignment 01 Project 01 - Part A
  Rohin Arya
  251371185
  rarya4
  Sept 18, 2023
'''

# Starting message
print("Project One <01> - Part A : Fibonacci Sequence")

# Get the ending index integer
ending = int(input("Sequence ends at: "))

index = 0 # Counts index
a = 0 # Counts first number
b = 1 # Counts second number

while index <= ending:
  print(str(index) + ": " + str(a) + " " + str(format(a, ",d"))) # Print values
  c = a + b # Temporary variable to store sum of a and b
  a = b # Move b to a
  b = c # Set b to sum of previous a and b
  index += 1 # Increment index

# Ending Message
print("\nEND: Project One <01> - Part A")
print("Rohin Arya rarya4 251371185")