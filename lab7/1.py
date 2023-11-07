values = [1, 2, 3, 4, 5, "hello", 6, 7, 8, 9, "10"]

try:
  for cur in values:
    print(cur)
    if type(values[cur] == str):
      raise ValueError("String found in list")
except ValueError as e:
  print(e)
finally:
  print("Done")