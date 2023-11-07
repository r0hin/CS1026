lowerbound = int(input("Starting number in sequence: "))
upperbound = int(input("Ending number in sequence: "))

# Get number of numbers divisible by 2 and 3 in range
for i in range(lowerbound, upperbound + 1):
  if i % 2 == 0 and i % 3 == 0:
    print(i)
