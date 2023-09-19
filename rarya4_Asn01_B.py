''''
  CS1026a 2023
  Assignment 01 Project 01 - Part B
  Rohin Arya
  251371185
  rarya4
  Sept 18, 2023
'''

# Find all prime numbers within a range
# Get the lower bound
lower_bound = int(input("Enter lower bound: "))
# Get the upper bound
upper_bound = int(input("Enter upper bound: "))

if (lower_bound > upper_bound):
  # Swap the bounds if lower_bound is greater than upper_bound
  temp = lower_bound # Temporary variable to store lower_bound
  lower_bound = upper_bound
  upper_bound = temp
  print("Swapped bounds")
 
for num in range(lower_bound, upper_bound + 1):
  prime_found = True # Variable that assume num is prime
  for i in range(2, num): # Numbers ranging from 2 to num - 1
    if num % i == 0: # If num is divisible by i (% means remainer, and it must be 0)
      prime_found = False # num is not prime
      break # Break out of the loop
  if prime_found and num > 1:
    print(str(num) + " is prime")

# END: Assignment 01 Project 01 - Part B
print("Rohin Arya rarya4 251371185")