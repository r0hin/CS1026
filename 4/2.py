num = int(input("Enter number that is zero or higher: "))

factorial = 0;
while num > 0:
  factorial += num
  num -= 1

print(factorial)