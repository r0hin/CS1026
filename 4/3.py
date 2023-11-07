string = input("Enter a string: ")

counta = 0
counte = 0
counti = 0
counto = 0
countu = 0

for char in string:
  if char == "a":
    counta += 1
  elif char == "e":
    counte += 1
  elif char == "i":
    counti += 1
  elif char == "o":
    counto += 1
  elif char == "u":
    countu += 1

print("a: " + str(counta))
print("e: " + str(counte))
print("i: " + str(counti))
print("o: " + str(counto))
print("u: " + str(countu))