n = int(input("Enter number: "))

for i in range(1, n + 1):
  nums = [];
  for i in range(1, i + 1):
    nums.append(str(i))
  print(*nums, sep = " ")