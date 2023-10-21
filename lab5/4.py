values = [1, 2, 3, 4, 5]
newValues = values[:]

for i in range(len(values)):
  newValues[i] += 1
  print("Old value at index {} is {}".format(i, values[i]))
  print("New value at index {} is {}".format(i, newValues[i]))