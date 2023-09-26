
while True:
  num = int(input("Enter number: "))
  if (num < 0):
    break

  for i in range(1, num + 1):
    if (i % 2 != 0):
      print(i)
      