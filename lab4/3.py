def countVowels(word):
  numVowels = 0
  for letter in word:
    if letter in 'aeiouAEIOU':
      numVowels += 1
  
  return numVowels

print(countVowels("AEIOu"))