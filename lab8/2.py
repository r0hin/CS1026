sentence ="I had such a horrible day It was awful so bad sigh It could not have been worse but actually though it was such a terrible horrible awful bad day"
makeItHappy = {"horrible": "amazing", "bad": "good", "awful": "awesome", "worse" :"better",
"terrible" : "great"}
spsentence = sentence.split()

for index in range(0, len(spsentence)) :
  if spsentence[index] in makeItHappy:
    spsentence[index] = makeItHappy[spsentence[index]]
    
newString = ""
for word in spsentence:
  newString = newString + word + " "

print(newString)